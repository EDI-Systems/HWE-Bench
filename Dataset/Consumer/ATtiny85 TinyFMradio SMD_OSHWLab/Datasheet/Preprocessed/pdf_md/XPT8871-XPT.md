# XPT8871 用户手册

2012 年 03 月

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# XPT8871

# 芯片功能说明

 XPT8871 是一款无FM干扰，AB/D 类可选式功率放大器。5V工作电压时，最大驱动功率为 5W（2Ω，BTL 负载，THD<10%），音频范围内总谐波失真噪声小于 1％。

 XPT8871的应用电路简单，只需极少数外围器件，集成反馈电阻；输出不需要外接耦合电容或上举电容和缓冲网络。

 XPT8871 采用 MSOP/SOP/ ESOP/DFN 封装，特别适合用于小音量、小体重的便携系统中。可以通过控制进入休眠模式，从而减少功耗。

XPT8871 内部具有过热自动关断保护机制；工作稳定，增益带宽积高达 2.5MHz，并且单位增益稳定。反馈电阻内置，通过配置外围参数可以调整放大器的电压增益及最佳音质效果，方便应用。完美的 USB低音炮及扩音器解决方案。

# 芯片功能主要特性

 对 FM 无干扰，高效率，音质优

 输出功率高（THD＋N<10%，1KHz 频率)：

 ESOP 封装的为 5W（2Ω负载）和 3.5W（3Ω负载），3W（4Ω负载）

 掉电模式漏电流小

 采用 MSOP/SOP/ ESOP/DFN 封装

 外部增益可调，集成反馈

 宽工作电压范围 2.0V—5.5V

 不需驱动输出耦合电容、自举电容和缓冲网络

 单位增益稳定

 兼容 LM4871

# 实物图：

![](images/c383c6489fb468684213fbd71ba2f352af26d6a862bcd616d1285e33798b1f9c.jpg)

#

 手提电脑

 台式电脑

 低压音响系统、USB、2.1/2.0 多媒体音响

# XPT8871 原理框图

![](images/3775d2a1c990459e21a34c487212f28f358fcb3836cf815f5791acf02d80d204.jpg)

# 芯片定购信息

<table><tr><td rowspan=1 colspan=1>芯片型号</td><td rowspan=1 colspan=1>封装类型</td><td rowspan=1 colspan=1>包装类型</td><td rowspan=1 colspan=1>最小包装数量（PCS)</td><td rowspan=1 colspan=1>备注</td></tr><tr><td rowspan=1 colspan=1>XPT8871MS</td><td rowspan=1 colspan=1>MSOP8</td><td rowspan=1 colspan=1>编带</td><td rowspan=1 colspan=1>3000/管</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>XPT8871SO</td><td rowspan=1 colspan=1>SOP8</td><td rowspan=1 colspan=1>管装</td><td rowspan=1 colspan=1>100/管</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>XPT8871ES</td><td rowspan=1 colspan=1>ESOP8</td><td rowspan=1 colspan=1>管装</td><td rowspan=1 colspan=1>100/管</td><td rowspan=1 colspan=1>带散热片</td></tr><tr><td rowspan=1 colspan=1>XPT8871DF</td><td rowspan=1 colspan=1>DFN</td><td rowspan=1 colspan=1>编带</td><td rowspan=1 colspan=1>3000/盘</td><td rowspan=1 colspan=1>带散热片</td></tr></table>

# 典型应用电路

![](images/91c19993cf662bd809248f5dcbe939df7ce2b4a4a1eb8f8d9c52a263c20a29c4.jpg)

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# 引脚分布图

![](images/85a88182c5b1a722ce95acac8f4cc84c2bd1817b7679e26786285febf5c69106.jpg)

XPT8871 SOP8、ESOP8、MSOP8.封装的管脚分布图

![](images/986061dacecc7ee0b0bf7558acf81911a031a4be3564073416db1a3661cb41e4.jpg)  
XPT8871 DFN 封装的管脚分布图

# XPT8871 管脚描述

XPT8871 管脚描述  

<table><tr><td rowspan=1 colspan=1>管脚号</td><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SD</td><td rowspan=1 colspan=1>掉电控制管脚，高电平有效，</td></tr><tr><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>BYP</td><td rowspan=1 colspan=1>内部共模电压旁路电容</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>MODE</td><td rowspan=1 colspan=1>AB类/D类模式选择</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-IN</td><td rowspan=1 colspan=1>模拟输入端，反相</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VON</td><td rowspan=1 colspan=1>模拟输出端负极</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>电源正</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>电源地</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>VOP</td><td rowspan=1 colspan=1>模拟输出端正极</td></tr></table>

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# 芯片特性说明

# 芯片最大极限值

芯片最大物理极限值  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>电源电压</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>储存温度</td><td rowspan=1 colspan=1>-65</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>℃</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>输入电压</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功耗</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>内部限制</td></tr><tr><td rowspan=1 colspan=1>耐ESD电压1</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>v</td><td rowspan=1 colspan=1>HBM</td></tr><tr><td rowspan=1 colspan=1>耐ESD电压2</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>MM     </td></tr><tr><td rowspan=1 colspan=1>节温</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>℃    </td><td rowspan=1 colspan=1>典型值150</td></tr><tr><td rowspan=1 colspan=1>推荐工作温度</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>℃</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>推荐工作电压</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4>热阻</td></tr><tr><td rowspan=1 colspan=1>JC(SOP)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>C/W</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>JA(SOP)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>140</td><td rowspan=1 colspan=1>C/W</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>JC(LLP)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.3</td><td rowspan=1 colspan=1>C/W</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>JA(LLP)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>56</td><td rowspan=1 colspan=1>C/W</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>焊接温度</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>220</td><td rowspan=1 colspan=1>℃</td><td rowspan=1 colspan=1>15秒内</td></tr></table>

# 芯片数字逻辑特性

关断信号数字逻辑特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=6>电源电压为5V</td></tr><tr><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=6>电源电压为3V</td></tr><tr><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=6>福                                    电源电压为2.6V</td></tr><tr><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr></table>

# 芯片性能指标特性

芯片性能指标 1（VDD＝5.0V，TA＝25o C）  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>测试条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>标准值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>电源电压</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IDD</td><td rowspan=1 colspan=1>电源静态电流</td><td rowspan=1 colspan=1>VIN=0V， IO=0A,</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>ISD</td><td rowspan=1 colspan=1>关断漏电流</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>μA</td></tr></table>

AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>测试条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>标准值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>Vos</td><td rowspan=1 colspan=1>输出失调电压</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.7</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>Ro</td><td rowspan=1 colspan=1>输出电阻</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8.5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>K</td></tr><tr><td rowspan=2 colspan=1>Po</td><td rowspan=2 colspan=1>输出功率</td><td rowspan=1 colspan=1>THD=1%,f=1KHz, RL=4 Ω</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>THD+N=10%,f=1KHz， RL=4Ω</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>THD+N</td><td rowspan=1 colspan=1>总失真度+噪声</td><td rowspan=1 colspan=1>AVD=2，20Hz≤f≤20KHzRL=4Ω， PO=0.5W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>PSRR</td><td rowspan=1 colspan=1>电源抑制比</td><td rowspan=1 colspan=1>VDD=4.9V 到 5.1V</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr></table>

# XPT8871 的典型参考特性

总谐波失真（THD），失真＋噪声（THD+N），信噪比（S/N）

![](images/9db76687d9710005d276912474024ed02a93e6d541b1e2513173726a1f3e72f8.jpg)

![](images/5e21605ff363acb2e6fa310a3a10185ca36399a6b1081890a33f300306d1edaa.jpg)

![](images/15fdebfc2737f843f317b91c26d6f7d1c63a97070b6f7833f3ae5aa0ae11a5f9.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）  
电源电压抑制比（PSRR）

![](images/b5f88f0f301f397bdbef036883751f1e7beb50cccae2a081fa8cfd49bf0c94a4.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

![](images/b405f08cf9a8478021beeb02f1570f16cfc463a3e6a65f1539257f1bd1a8ca1a.jpg)

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# 芯片功耗（Power Dissipation）

![](images/09234389bbd3404b9848b3a8ac87cd2afab1f7d8fd52867e75ca0d4f2923d6af.jpg)

![](images/e67521b1ca95cfb5fb7ad05d447e72847b1fbc144214ccd9ab56788042a534d8.jpg)  
Power Dissipaton vs Output Power,VDD=2.5V

# 关断滞回（Shut Down Hysteresis）

![](images/481c0640bac64f9f2cc8c371dca32ec93028c415099795c096a4c9d1c3770053.jpg)

![](images/b8bad2c274029de7649d78989ba018adf0eed891b0289d757bdd9c81d440376b.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

#

![](images/0b577e04c0aca0fd9c2f42ec54db89f82ca0865ecb9990ad74a3be37e336c852.jpg)

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

![](images/0229256618c675244ad8634de44a8c911c5f86543364b50a56b634b6eb490c14.jpg)

# 测试连接示意图

![](images/4478b0d1d7a4ba9ce0348ebf7ab9128f1e84319656fed6ffa18181f95533b902.jpg)  
XPT8871 测试连接示意图

注：

1. 在测试仪器与 XPT8871 之间必需加一个低通滤波器。

2. 测量功放的输出功率时，最好在喇叭前串个 22μH 电感。

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# XPT8871 应用说明

XPT8871 是一款 AB 类/D类可选的音频功率放大器，D类输入，输出都采用差分结构的差分放大器，可以应用在单端输入模式。

# 外部器件选择

 外部器件  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>尺寸</td><td rowspan=1 colspan=1>品牌</td><td rowspan=1 colspan=1>封装型号</td></tr><tr><td rowspan=1 colspan=1>Ri</td><td rowspan=1 colspan=1>150KΩ（±0.5%）</td><td rowspan=1 colspan=1>0603</td><td rowspan=1 colspan=1>Panasonic</td><td rowspan=1 colspan=1>ERJ2RHD154V</td></tr><tr><td rowspan=1 colspan=1>Cs</td><td rowspan=1 colspan=1>1μf（±22%，-80%)</td><td rowspan=1 colspan=1>0603</td><td rowspan=1 colspan=1>Murata</td><td rowspan=1 colspan=1>GRP155F50J105Z</td></tr><tr><td rowspan=1 colspan=1>Ci</td><td rowspan=1 colspan=1>3.3nF（±10%)</td><td rowspan=1 colspan=1>0603</td><td rowspan=1 colspan=1>Murata</td><td rowspan=1 colspan=1>GRP033B10J332K</td></tr></table>

# MODE功能

XPT8871 是一款 AB 类/D类可选的音频功率放大器，通过 MODE 功能键可对功放进行AB类D类的选择。

<table><tr><td rowspan=1 colspan=1>MODE</td><td rowspan=1 colspan=1>芯片功能模式</td></tr><tr><td rowspan=1 colspan=1>高电平</td><td rowspan=1 colspan=1>D类功率放大器</td></tr><tr><td rowspan=1 colspan=1>低电平</td><td rowspan=1 colspan=1>AB 类功率放大器</td></tr></table>

XPT8871设有Mode引脚，该管脚是用来对XPT8871的模式进行选择的管脚，该脚处于高电平时，进入D类工作模式；低电平时，选择AB类工作模式；默认为D类。

XPT8871可以在AB类和D类这两种工作模式之间进行自由切换，以下是采用AB类与D类优缺点分析比较：

AB 类音频放大器的效率只有 25%左右，能耗大；D 类具有高达 90%的效率。D 类技术的效率会被更加重视 应用场合多，如在日愈丰富的多媒体数码内容更多是 MP3 音乐、影音片段和数字电视

AB 类技术的音频性能好，THD+N低，PSRR 的绝对数值高。此外，AB 类的应用中没有噼啪声和咔嗒声，噪声很小，而且开启时间和关闭时间都很短，亦可实现节能的方案。D 类的工作模式完全不同于 AB 类，会产生某些高频谐波--- EMI 干扰。

在小功率音频驱动中，比如音频耳机功放对效率和功率的要求不高，或者 Hi-Fi 耳机放大器对失真率有较高的要求，此时 AB 类功放的超低失真率就体现出了优势，如今在耳机放大器的设计中 AB 类仍是唯一的选择；AB 类技术的音频性能好，THD+N 低，PSRR 的绝对数值高。

小型化趋势对降低 D类音频放大器的噪声带来了限制。

D类音频放大器的成本一般是 AB 类的 2 至3倍，尽管 D类提供较佳的功效及散热能力。

与简单的 D类取代 AB类不同，矽普特公司采用了兼容方案，在没有射频发射/传输的时候，运行 D类模式；  
在射频发射/传输的时候，运行 AB类模式，充分利用 D类和 AB 类的优点，弥补各自缺点。

# 芯片功耗

功耗对于放大器来讲是一个关键指标之一，差分输出的放大器的最大自功耗为：

PDMAX＝4×（VDD）2 /（2×∏2 ×RL）

必须注意，自功耗是输出功率的函数。

在进行电路设计时，不能够使得芯片内部的节温高于 TJMAX（150o C），根据芯片的热阻JA来设计，可以通过自己散热铜铂来增加散热性能。

如果芯片仍然达不到要求，则需要增大负载电阻、降低电源电压或降低环境温度来解决。

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# 退耦电容Cs

XPT8871 是一款高性能的音频功率放大器，需要适当的电源退耦以确保它的高效率和低谐波失真。退耦电容采用低阻抗陶瓷电容，容值为 1μF，尽量靠近芯片电源 供电度引脚，因为电路中任何电阻，电容和电感都可能影响到功率转换的效率。一个 10μF 或更大的电容放置在放大器的附近会得到更好的滤波效果，但在具有高电源电压抑制系数的放大器应用中是不需要这样一个电容的。

# 输入电容Ci

如果设计中的差分输入信号在 0.5V到 VCC-0.8V的范围内，如果输入信号幅度不在这个范围内，输入端是个高通滤波器或者 XPT8871 用在单端输入系统中，输入电容是必须的。输入端作为高通滤波器时，滤波器中心频率的计算公式如下：

![](images/050476282d2c3cf9015327ed42156ba1d6e5db1df84694ab1426d5161b1c673a.jpg)

输入电阻和输入电容的参数直接影响到滤波器的下限频率，从而影响放大器的性能。输入电容的计算公式如下：

![](images/13bee82658dd46cfad5fd8b39932d5209095deab137a32ae95cbe41865d32ab7.jpg)

如果信号的输入频率在音频范围内，输入电容的精度可以是±10％或者更高，因为电容不匹配会影响的滤波器的性能。采用大电容（1μF）可以很好的重现低频信号。但在 GSM 电话中，地面信号在 217Hz上下摆动，但在多媒体数字信号偏解码器的信号却没有这样的摆动。

XPT8871 内部集成两个运算放大器，第一个放大器的增益可以调整反馈电阻来设置，后一个为电压反相跟随，从而形成增益可以配置的差分输出的放大驱动电路。

# 芯片功耗

功耗对于放大器来讲是一个关键指标之一，差分输出的放大器的最大自功耗为：

PDMAX＝4×（VDD）2 /（2×∏2 ×RL）

必须注意，自功耗是输出功率的函数。

在进行电路设计时，不能够使得芯片内部的节温高于 TJMAX（150o C），根据芯片的热阻JA来设计，可以通过自己散热铜铂来增加散热性能。

如果芯片仍然达不到要求，则需要增大负载电阻、降低电源电压或降低环境温度来解决。

# 电源旁路

在放大器的应用中，电源的旁路设计很重要，特别是对应用方案的噪声性能及电源电压抑制性能。设计中要求旁路电容尽量靠近芯片、电源脚。典型的电容为 10μF的电解电容并上 0.1μF的陶瓷电容。

在 XPT8871应用电路中，另一电容 CB（接 BYP管脚）也是非常关键，影响 PSRR、开关/切换噪声性能。一般选择 0.1μF～1μF的陶瓷电容。

# SD脚工作模式选择

为了节电，在不使用放大器时，可以关闭放大器，XPT8871 有掉电控制管脚 SD，可以控制放大器是否工作。

该控制管脚的电平必须要接满足接口要求的控制信号，否则芯片可能进入不定状态。 暨 SD脚通过施加以

下三种不同电平状态，芯片则分别进入三种不同工作模式：

高电平：芯片进入掉电工作模式，关闭放大器，无输出信号，工作电流小于 0.6μA，通过选择进入此状态，能有效减少能耗，达到省电目的。

低电平：芯片处于正常工作模式。因此，在 使用过程中，务必让此引脚保持低电平。

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

空 置：芯片 处于 不定状态，不仅不能够进入掉电模式，其自功耗没有降低，达不到节电目的；而且易对芯片造成 不良影响，因此，在芯片长期 工作时，切忌勿让其处于悬空状态。

# 外围元件的选择

正确选择外围元器件才能够确保芯片的性能，尽管 XPT8871能够有很大的余量保证性能，但为了确保整个性能，也要求正确选择外围元器件。

XPT8871 在单位增益稳定，因此使用的范围广。通常应用单位增益放大来降低 THD＋N，是信噪比最大化。但这要求输入的电压最大化，通常的音频解码器能够有 1Vrms的电压输出。

另外，闭环带宽必须保证，输入耦合电容 Ci（形成一阶高通）决定了低频响应，

# XTP8871D类模式和传统D类放大器对比分析

# 传统D类功放调制方案

在没有信号输出（平均电压为 0V的时候），差分输出的两个输出端为占空比都为 50％，幅度为 VCC和-VCC而相位差 180 度的方波。负载出现幅度从-VCC 到 VCC 的方波。负载平均电压为 0V，但 通过负载的电流很高，耗费的了电源的很大的功率，对提高功放的效率不利。

![](images/6d3590955375b69aadafa7a0fb803c66ba753b3b6ce5a953f5f362c716ff5300.jpg)  
传统 D类功放调制方案没有信号时的输出波形

# XPT8871 调制方案

在 没有信号输出（平均电压为0V的时候），差分输出的两个输出端为占空比都为50％，幅度为VCC和-VCC而相位相差一点点的方波。从而负载出现幅度仍然从-VCC 到 VCC 但具有很小脉宽的脉冲信号。负载平均电压为 0V，但通过负载的平均电流低了很多，耗费电源的功率大大降低了，对提高功放的效率有利。

当输出正电压的时候，VoP输出占空比要比VoN要大，负载得到幅度为正的脉冲信号。当输出负电压的时候，VoP输出占空比要比VoN要小，负载得到幅度为负的脉冲信号。最终负载得到的波形与输入信号相对应。传统的D类放大器要输出滤波器的原因。

假如输出不加滤波器，传统 D类放大器输出的高频脉冲分量能量很大。将会在负载上耗费很大无用的功率，降低放大器的效率。加了 LC 滤波器以后虽然了 LC 上也消耗一定的功率，但会改善很多，因为 LC的内阻很小。

而在 XPT8871 的调制方案中，没有滤波器的情况下在负载上消耗的无用功率是很小的。因为脉冲的脉宽很小，并且幅度也比传统 D类功放小。所以在 XPT8871 的放大器应用中不需要输出滤波器。

![](images/5244bc86a9a464c308aeca8829d0faa7a9ce4cf4c49fd40ef936d7bf6ece2912.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）  
XPT8871 调制方案没有信号时的输出波形

# XPT8871 输出滤波器

在不加输出滤波器的情况下使用 XPT8871，放大器到扬声器的连线的长度一般在 100mm 以下。在手机等便携式通信设备，PAD 都可以不用输出滤波器。在一些环境等条件不允许和一些特殊的情况下，要加入输出滤波器，加入低通滤波器，比如 LC 滤波器

![](images/0ad0e259f381407d68b302f9ef777f06ef13e736e4fb1da628e642e69f295ee4.jpg)  
输出加贴片铁氧体磁珠滤波器典型应用电路

![](images/763fa673dc8c3cfbc5e37a275348cf82521eab408a7126e137a8fb903a96bde7.jpg)  
输出加 LC 滤波器典型应用电路（截止频率为 27KHz）

# 保护功能模式概述

XPT8871 是一款无破音D类音频功率放大器。且内置了这流保护，过热保护及欠压保护等功能。有效地保护芯片在异常工作状况下不被损坏。

# AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

# 过流保护功能

XPT8871 内置了过流保护功能模式，当检测到 VDD与 VSS之间有大电流或者是差分输出端出现短路现像。IC 就会把输出端置为高阻状态。XPT8871 就会进入过流保护模式。重新开关电源后即可取消该模式。

# XPT8871AB类设计参考实例

# 设计规格

输出功率 3Wrms  
 负载阻抗 4 欧姆  
 输入电平 1Vrms  
 输入电阻 20K  
 带宽 100Hz～20KHz+/-0.25dB

# 首先确定最小工作电压

根据 XPT8871 的输出功率与电源电压的关系图，可以确定电源电压应选择 5.0V。电源电压的裕量可以保证输出可以高于 1W 的功率而不失真。

选择电压后，然后考虑功耗的问题。

# 最后根据带宽要求来确定输入电容

输入低频的－3dB 带宽为 100Hz，1/5 低频点低于－3dB 约 0.17dB 及 5 倍高频点，在规格要求以内，取 fL＝20Hz，fH=100KHz，

因此可得 Ci 约 0.39μF。

高频点 fH由放大器的 GBW 决定，至少要求 GBW 大于 AVD×fH＝300KHz，远小于 XPT8871 的 2.5MHz。

# 其它注意事项

XPT8871 单位增益稳定，但如果增益超过 10 倍（20dB）时，额外的反馈电容 C 需要并联在电阻 R 上，避免高频的振荡现象。但必须要求与 Rf组成的极点频率高于 fH（在实例中为 300KHz），如本例中选择 Cf为 5pF时，转折频率为 320KHz。可以满足要求。

# 封装尺寸图

1、 MSOP8

![](images/4cf1affd26a29fabc587934519af8cc2a1c8878f4649582b8d5888f15804f892.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

2、 SOP8

![](images/96adb018957e73ae3b98405be03a5f61107ead8489d4cc46d205ba6a3a0ad299.jpg)

# 3、 DFN3×3

![](images/1d66a1b123d4b704bd5f38c96c76b44afc860e356f8c4f8c3b4f3f4a41610bb9.jpg)  
AB/D类切换、过热&欠压&过流保护、无FM 干扰+5W（2Ω）

注：ESOP8 封装尺寸与 SOP8 封装 完全一致，仅增加散热片。

当本手册内容改动及版本更新将不再另行通知，深圳市矽普特科技限公司保留所有权利