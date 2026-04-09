import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_Multiplexer.json")
CIR_FILE = os.path.join(BASE_DIR, "ppmux_final.net")
LOG_FILE = os.path.join(BASE_DIR, "ppmux_final.log")
REPORT_FILE = os.path.join(BASE_DIR, "ppmux_verification_report.txt") # 新增输出文件

# ================= 2. 判定指标与阈值 =================
TEST_CRITERIA = {
    "v_out_stage_a":   {"name": "初始电池供电电压", "min": 3.4, "max": 3.8, "unit": "V"},
    "v_dip_plug":      {"name": "插入瞬态最小电压", "min": 3.2, "max": 5.5, "unit": "V"},
    "i_peak_usb":      {"name": "USB 插入冲击电流", "min": -2.5, "max": 0.5, "unit": "A"},
    "v_out_stage_c":   {"name": "USB 稳态输出电压", "min": 4.3, "max": 5.0, "unit": "V"},
    "v_drop_d9":       {"name": "二极管正向压降",   "min": 0.1, "max": 0.6, "unit": "V"},
    "v_dip_unplug":    {"name": "拔出瞬态跌落电压", "min": 2.8, "max": 4.5, "unit": "V"},
    "v_out_stage_e":   {"name": "切回电池后电压",   "min": 3.4, "max": 3.8, "unit": "V"}
}

def build_perfect_netlist():
    """生成优化后的网表内容"""
    netlist = [
        "* Final Optimized PPMUX Circuit",
        ".model D_SCHOTTKY D(Is=1e-5 Rs=0.05 N=1.1)",
        ".model P_MOS VDMOS(pchan Vto=-1.0 Rs=0.05 Kp=2.0)", 
        ".tran 0 50m 0 10u",
        "V_BAT VBAT 0 3.7",
        "V_USB VBUS 0 PULSE(0 5 10m 100u 100u 20m 50m)",
        "D9 VBUS VOUT D_SCHOTTKY",
        "M1 VOUT VBUS VBAT VBAT P_MOS", 
        "C_FILTER VOUT 0 22uF",  # 关键修复：防止电压跌落
        "R_PULLDOWN VBUS 0 100k", # 关键修复：确保USB拔出后门极泄放
        "R_LOAD VOUT 0 100",
        ".meas TRAN v_out_stage_a AVG V(VOUT) FROM 5m TO 9m",
        ".meas TRAN v_dip_plug MIN V(VOUT) FROM 9.5m TO 15m",
        ".meas TRAN i_peak_usb MIN I(V_USB) FROM 9.5m TO 15m",
        ".meas TRAN v_out_stage_c AVG V(VOUT) FROM 18m TO 25m",
        ".meas TRAN v_drop_d9 AVG (V(VBUS)-V(VOUT)) FROM 18m TO 25m",
        ".meas TRAN i_leak_bat AVG I(V_BAT) FROM 18m TO 25m",
        ".meas TRAN v_dip_unplug MIN V(VOUT) FROM 29.5m TO 35m",
        ".meas TRAN v_out_stage_e AVG V(VOUT) FROM 40m TO 48m",
        ".end"
    ]
    return "\n".join(netlist)

def run_and_export():
    # 1. 执行仿真
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_perfect_netlist())
    
    print(">>> 正在启动仿真并生成报告...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE):
        print("错误：未找到仿真日志。")
        return

    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_data = f.read()

    # 2. 构建报告内容
    report_lines = []
    report_lines.append("=" * 85)
    report_lines.append(f"PPMUX 模块仿真验证报告 - 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 85)
    report_lines.append(f"{'监控指标':<25} | {'实测值':<15} | {'标准范围':<15} | {'结果'}")
    report_lines.append("-" * 85)

    passed_count = 0
    total_count = len(TEST_CRITERIA)

    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_data, re.I)
        if match:
            val = float(match.group(1))
            is_ok = spec["min"] <= val <= spec["max"]
            res_str = "PASS" if is_ok else "FAIL"
            if is_ok: passed_count += 1
            
            line = f"{spec['name']:<21} | {val:>12.4f}{spec['unit']} | {spec['min']}~{spec['max']} | {res_str}"
            report_lines.append(line)
        else:
            report_lines.append(f"{spec['name']:<21} | {'MISSING':<15} | - | ERROR")

    pass_rate = (passed_count / total_count) * 100
    report_lines.append("-" * 85)
    report_lines.append(f"统计摘要: 总计 {total_count} 项 | 通过 {passed_count} 项 | 失败 {total_count - passed_count} 项")
    report_lines.append(f"最终通过率 (Pass Rate): {pass_rate:.2f}%")
    report_lines.append("=" * 85)

    # 3. 输出到控制台
    final_report = "\n".join(report_lines)
    print(final_report)

    # 4. 写入 TXT 文件
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_report)
    
    print(f"\n>>> 报告已成功导出至: {REPORT_FILE}")

if __name__ == "__main__":
    try:
        run_and_export()
    except Exception as e:
        print(f"脚本运行出错: {e}")