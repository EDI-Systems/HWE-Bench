# 综述

# 特性

LTH7R是一款完整的单节锂离子电池采用恒定电流/恒定电压线性充电器。其SOT-23-5L封装与较少的外部元件数量使得LTH7R成为便携式应用的理想选择。

LTH7R可以适合USB电源和适配器电源工作。由于采用了内部PMOSFET架构，加上防倒充电路，所以不需要外部检测电阻和隔离二极管。热反馈可对充电电流进行调节，以便在大功率操作或高环境温度条件下对芯片温度加以限制。

充电电压固定于4.2V，而充电电流可通过一个电阻进行外部设置。当充电电流在达到最终浮充电压之后降至设定值1/10时，LTH7R将自动终止充电循环。

当输入电压（交流适配器或USB电源）被拿掉时，LTH7R自动进入一个低电流状态，将电池漏电流降至2μA以下。也可将 LTH7R 置于停机模式，从而将供电电流降至55μA。LTH7R 的其它特点包括充电电流监控器、欠压闭锁、自动再充电和一个用于指示充电结束和输入电压接入的状态引脚。

LTH7R 采用绿色环保的SOT-23-5L封装以及最少3个外围器件可有效减小电路PCB布板空间。LTH7R 可工作于-40°C to +85°C。

 高达500mA的可编程充电电流  
 无需MOSFET、检测电阻或隔离二极管  
 恒定电流/恒定电压操作，并具有可在无过热危险的情况下实现充电速率最大化的热调节功能  
 直接从USB 端口给单节锂离子电池充电  
 精度达到1%的4.2V预设充电终止电压  
 用于电池电量检测的充电电流监控器输出  
 自动再充电  
 充电状态输出引脚  
 C/10充电终止  
 停机模式下的供电电流为 55μA  
 2.85V涓流充电  
 软启动限制浪涌电流  
 SOT23-5L封装

# 应用范围

 移动电话，PDAs，MP3播放器  
 USB 数据卡  
 TWS 耳机充电仓  
 电池充电电路  
 其它手持设备

# 典型应用

![](images/80fc75553d50913cafa7b9dbc65c473f238b44789cceb84752bbaed58396606f.jpg)  
1. 典型应用电路

# 封装信息（顶视图）

![](images/2d71e99eb96565814df8492b4110f75e871ff80aa3ca406516533afe576ce017.jpg)

# 引脚信息

表1. 引脚描述  

<table><tr><td rowspan=1 colspan=1>引脚</td><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>引脚功能描述</td></tr><tr><td rowspan=1 colspan=1>1id</td><td rowspan=1 colspan=1>CHRG</td><td rowspan=1 colspan=1>开漏输出的充电状态指示端</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>地</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>BAT</td><td rowspan=1 colspan=1>充电电流输出引腳</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>电源输入引脚</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>PROG</td><td rowspan=1 colspan=1>恆流充电电流设置和充电电流监测端</td></tr></table>

绝对最大额定范围和封装热特性  

<table><tr><td rowspan=1 colspan=2>描述</td><td rowspan=1 colspan=1>范围</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=2>VCC电压引脚</td><td rowspan=1 colspan=1>-0.3~6.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=2>BAT电压引腳</td><td rowspan=1 colspan=1>-4.2~5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=2>其它引脚</td><td rowspan=1 colspan=1>-0.3~5.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=2>存储温度范围</td><td rowspan=1 colspan=1>-65~+150</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=2>结温</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=2>焊接温度(10s)</td><td rowspan=1 colspan=1>260</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=2 colspan=1>ESD</td><td rowspan=1 colspan=1>HBM</td><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>CDM</td><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>封装热阻(θA)</td><td rowspan=1 colspan=1>SOT-23-5L</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>°C/W</td></tr><tr><td rowspan=1 colspan=1>功耗，PD@TA=25°℃</td><td rowspan=1 colspan=1>SOT-23-5L</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>W</td></tr></table>

注：超出上述绝对最大额定值不一定使器件产生永久性损伤，但长期在（或超出）绝对最大额定值条件下工作会影响器件的可靠性。

# 推荐工作条件

<table><tr><td rowspan=1 colspan=1>描述</td><td rowspan=1 colspan=1>范围</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>工作结温(T)</td><td rowspan=1 colspan=1>-40~125</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>工作环境温度(TA)</td><td rowspan=1 colspan=1>-40~85</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>电源电压(VCC)</td><td rowspan=1 colspan=1>+4.0~+6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>充电连续输出电流(SOT23-5)</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>A</td></tr></table>

# ESD 警告

因为集成电路可能会在不注意时被ESD损伤，所以建议妥善且安全地操作和保存。同时ESD损伤有时会造成集成电路完全毁坏，但有时仅会造成某些参数的变化，这将导致其与说明书标称的规格存在差异，并且越精密的集成电路越容易受此影响。

# 免责声明

本公司保留不预先通知而对此产品的设计、规格和其它相关事宜做出合理调整的权利。请从公司网站或从公司销售部门获取最新有效的说明书版本。

# 典型应用电路

![](images/e59cd47dd38957b3660d068a7fe2406a893dd7b235bd3f669023466b19f9daaf.jpg)  
图 2. 典型应用电路

![](images/717c8abf965d28ea970d3f3992e349b7617c4309a2b946b57555224e7040750c.jpg)  
图3. 双指标灯应用电路

# 电气特性

除非特殊说明，否则条件均为VCC=5V，VBAT = 3.6V，TJ = 25°C。   

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>测试条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>输入电源电压</td><td rowspan=1 colspan=1>Vcc</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=3 colspan=1>静态电流</td><td rowspan=3 colspan=1>la</td><td rowspan=1 colspan=1>充电模式，RpROG=10k</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>待机模式(充电终止)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>停机模式(RpROG 未连接,Vcc&lt;VBAT, Or Vcc&lt;Vuv)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>稳定输出（浮充）电压</td><td rowspan=1 colspan=1>VFLOAT</td><td rowspan=1 colspan=1>0°C≤TA≤85°C, RpROG = 2k</td><td rowspan=1 colspan=1>4.158</td><td rowspan=1 colspan=1>4.200</td><td rowspan=1 colspan=1>4.242</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=6 colspan=1>BAT引脚电流</td><td rowspan=6 colspan=1>IBAT</td><td rowspan=1 colspan=1>RpROG = 10k，电流模式</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>110</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>RpROG = 2.5k， 电流模式</td><td rowspan=1 colspan=1>360</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>440</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>RpROG = 2k，电流模式</td><td rowspan=1 colspan=1>450</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>待机模式,VBAT = 4.2V</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2.5</td><td rowspan=1 colspan=1>-6</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>停机模式 (RpROG 未连接)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1</td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>睡眠模式,Vcc= 0V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>涓流充电电流</td><td rowspan=1 colspan=1>ITRIKL</td><td rowspan=1 colspan=1>VBAT&lt;VTRIKL, RpROG = 2K</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>涓流充电门限电压</td><td rowspan=1 colspan=1>VTRIKL</td><td rowspan=1 colspan=1>RpROG = 2k, VBAT上升</td><td rowspan=1 colspan=1>2.75</td><td rowspan=1 colspan=1>2.85</td><td rowspan=1 colspan=1>2.95</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>涓流充电迟滞电压</td><td rowspan=1 colspan=1>VTRHYS</td><td rowspan=1 colspan=1>RPROG = 2k</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>VCC欠压闭锁门限电压</td><td rowspan=1 colspan=1>Vuv</td><td rowspan=1 colspan=1>Vcc从低到高</td><td rowspan=1 colspan=1>3.40</td><td rowspan=1 colspan=1>3.55</td><td rowspan=1 colspan=1>3.70</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VCC欠压闭锁迟滞电压</td><td rowspan=1 colspan=1>VUVHYS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=2 colspan=1>VCC-VBAT闭锁门限电压</td><td rowspan=1 colspan=1>VASD</td><td rowspan=1 colspan=1>Vcc从低到高</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>mv</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Vcc从高到低</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=2 colspan=1>C/10终止电流门限</td><td rowspan=1 colspan=1>ITERM</td><td rowspan=1 colspan=1>RpROG = 10k</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RPROG = 2.0k</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>PROG引腳电压</td><td rowspan=1 colspan=1>VPROG</td><td rowspan=1 colspan=1>RpROG = 2k，电流模式</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>CHRG引脚输出低电压</td><td rowspan=1 colspan=1>VCHRG</td><td rowspan=1 colspan=1>ICHRG = 5mA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>再充电电池门限电压</td><td rowspan=1 colspan=1>∆VRECHRG</td><td rowspan=1 colspan=1>VFLOAT - VRECHRG</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>限定温度模式中的结温</td><td rowspan=1 colspan=1>TuM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>145</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>功率FET导通电阻</td><td rowspan=1 colspan=1>RoN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>600</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mΩ</td></tr><tr><td rowspan=1 colspan=1>软启动时间</td><td rowspan=1 colspan=1>tss</td><td rowspan=1 colspan=1>IBAT = 0 to IBAT =1000V/RpROG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μs</td></tr><tr><td rowspan=1 colspan=1>再充电比较器滤波时间</td><td rowspan=1 colspan=1>tRECHARGE</td><td rowspan=1 colspan=1>VBAT高至低</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>终止比较器滤波时间</td><td rowspan=1 colspan=1>tTERM</td><td rowspan=1 colspan=1>1BAT降至 ICHG/10</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>PROG引腳上拉电流</td><td rowspan=1 colspan=1>IPROG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=2 colspan=1>手动停机门限电压</td><td rowspan=2 colspan=1>VMSD</td><td rowspan=1 colspan=1>PROG引腳电平上升</td><td rowspan=1 colspan=1>3.40</td><td rowspan=1 colspan=1>3.50</td><td rowspan=1 colspan=1>3.60</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>PROG引腳电平下降</td><td rowspan=1 colspan=1>1.90</td><td rowspan=1 colspan=1>2.00</td><td rowspan=1 colspan=1>2.10</td><td rowspan=1 colspan=1>V</td></tr></table>

# 结构框图

![](images/7d735d5b4e4bbbfd22e4ba3aba77f88241a2299095a5220ebb32ceedf26a0169.jpg)  
图 4．内部结构

# 典型特性曲线

除非特殊说明，否则条件均为VCC=5V，VBAT = 3.6V，TJ = 25°C。

![](images/e30b9861818334c3a4fb3ae2f79c4aee09039a7bba5d830fa8720da7e3b9bfbb.jpg)  
ROG 引脚电压 vs 电源电压（恒流模式）

![](images/706cac699f58b2d76f6ef96a0b582279060ec3431bb6e52756c5811f0189fe12.jpg)  
PROG 引脚电压 vs 温度

![](images/1912442175b0b86ed3cdb59d2cfdd49f6b7529e45eb10221c125ce92d0027878.jpg)  
充电电流 vsPROG 引脚电压

![](images/275034c442fdcc888297894c32645565f39fe703091c6dbb76d7e8fe9e0197ab.jpg)  
浮充电压 vs 充电电流

![](images/906f119dbce6604cd6d84d91485e77339097d0b667495881fb9ce0de8558d41d.jpg)  
浮充电压 vs 温度

![](images/d7bc6aaf1f4d44d53808898281e65cd952dbb757917ae992b9439a4dbb08b416.jpg)  
浮充电压 vs 电源电压

![](images/9619dfe8b43d48bc7ce5aefc97c060cdd7f4581aae05b57fe5cc1610b8867118.jpg)  
涓流充阈值 vs 温度

![](images/a6b4fc70480119ae15ab4a86e10db6b2ef314c86dace7a2354bb6c0180818eac.jpg)  
充电电流 vs 电池电压

![](images/7e9b544e4f092fc3f72b8960f2433c230f27c49721cf3318a494da6b453bf3b7.jpg)  
充电电流 vs 电源电压

# 典型特性曲线（续）

除非特殊说明，否则条件均为VCC=5V，VBAT = 3.6V，TJ = 25°C。

![](images/75b284ef91903c66005052524e638898a34bfd626bffeb4b814a756184b119f1.jpg)  
充电电流 vs 环境温度

![](images/b330ba6b041f82c2c78b39ccbe244e2c2623bb7e3c30d71686c71dc412b15aba.jpg)  
再充电电压阈值 vs 温度

![](images/5301ce4b35cebaf297839d0ab400fbcfece3126f0ddde2f93b22dc0380831fea.jpg)  
功率 MOS 开态电阻 vs 温度

# 功能描述

LTH7R是一款完整的单节锂离子电池采用恒定电流/恒定电压线性充电器。它能够提供高达500mA的充电电流（借助一个热设计良好的PCB布局）和±1%精度的浮充电 压。LTH7R集成了一个内部P沟道功率MOSFET及热调 节电路，无需隔离二极管或外部电流检测电阻。因此，基本充电器电路仅需两个外部元件。不仅如此，LTH7R还可以接USB电源工作。

# 正常充电循环

当VCC引脚电压升至UVLO门限电平以上且在PROG引脚与 地之间连接了一个精度为1%的设定电阻或当一个电池与 充电器输出端相连时，一个充电循环开始。如果BAT引脚 电平低于2.85V，则充电器进入涓流充电模式。在该模式 中，LTH7R提供约1/10的设定充电电流，以便将电池 电压提升到一个安全电平，从而实现满电流充电。

当BAT引脚电压升至2.85V以上时，充电器进入恒流模式，此时向电池提供恒定的充电电流。当BAT引脚电压达到最终浮充电压（4.2V）时，LTH7R进入恒压充电模式，且充电电流开始减小。当充电电流降至设定值的1/10，充电循环结束。

# 充电电流设置

充电电流是采用一个连接在PROG引脚与地之间的电阻来 设定的。电池充电电流是PROG引脚输出电流的1000倍。 设定电阻和充电电流采用下列公式来计算：

![](images/f333e907782a0866d4cb941773315c3f55d1bf46ffaafe75ea9e522559700c08.jpg)

从BAT引脚输出的充电电流可通过监视PROG引脚电压随 时确定，公式如下：

![](images/76a6bb6aaae0c0dd8f59909b4d49d45dddc592bd1434a2b08db3633735323788.jpg)

RPROG选择推荐表  

<table><tr><td rowspan=1 colspan=1>RPROG (KQ)</td><td rowspan=1 colspan=1>ICHG(mA)</td></tr><tr><td rowspan=1 colspan=1>1.66</td><td rowspan=1 colspan=1>600</td></tr><tr><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>500</td></tr><tr><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>400</td></tr><tr><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>300</td></tr><tr><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>200</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>100</td></tr></table>

# 终止充电

当充电电流在达到最终浮充电压后降至设定值的1/10时，充电循环被终止。该条件是通过采用一个内部滤波比较器对PROG引脚进行监控来检测的。当PROG引脚电压降至100mV以下的时间超过tTERM（一般为1.8ms）时，充电被终止。充电电流被关断，LTH7R进入待机模式，此时输入电源电流降至55μA。（注：C/10终止在涓流充电和热限制模式中失效）。

充电时，BAT引脚上的瞬变负载会使PROG引脚电压在DC充电电流降至设定值的1/10之间短暂地降至100mV以下。 终止比较器上的1.8ms滤波时间（tTERM）确保这种性质的瞬变负载不会导致充电循环过早终止。一旦平均充电电流降至设定值的1/10以下，LTH7R即终止充电循环并停止通过BAT引脚提供任何电流。在这种状态下，BAT引脚上的所有负载都必须由电池来供电。

在待机模式中，LTH7R对BAT引脚电压进行连续监控。

如果该引脚电压降到4.05V的再充电电压门限（VRECHRG）以下，则另一个充电循环开始并再次向电池供应电流。当在待机模式中进行充电循环的手动再启动时，必须先断开输入电压然后再重新接入输入电压，或者通过控制PROG引脚来关断充电器然后再启动。图5示出了一个典型充电循环的状态图。

![](images/06d87c7ba6d43a083f1ea666dfbd9a01fabebe6f90c122fb9ba51fed449fc69f.jpg)  
图5 典型充电循环的状态图

# 充电状态指标

LTH7R集成一个开漏输出的状态指示引脚CHRG。当LTH7R处于充电状态时，CHRG输出下拉，其它状态CHRG输出高阻态。

如果BAT引脚接一个10μF电容并且电池不连接，红色LED 将

<table><tr><td rowspan=1 colspan=1>以1-4s的周期闪烁。充电器状态</td><td rowspan=1 colspan=1>红色LED CHRG</td></tr><tr><td rowspan=1 colspan=1>充电</td><td rowspan=1 colspan=1>亮</td></tr><tr><td rowspan=1 colspan=1>充电终止</td><td rowspan=1 colspan=1>灭</td></tr><tr><td rowspan=1 colspan=1>欠压闭锁、电池反接或电池未连接</td><td rowspan=1 colspan=1>灭</td></tr><tr><td rowspan=1 colspan=1>BAT引脚接10uF电容且电池未连接</td><td rowspan=1 colspan=1>LED将以1-4s的周期闪烁</td></tr></table>

# 热限制

如果芯片温度升高到预设值145℃，内部热反馈环路将减小充电电流。该功能可防止 LTH7R过热，并允许用户提高给定电路板功率处理能力的上限而没有损坏LTH7R的风险。在保证充电器将在最坏情况下自动减小电流的前提下，可根据典型（而不是最坏情况）环境温度来设定充电电流。

# 欠压闭锁（UVLO）

一个内部欠压闭锁电路对输入电压进行监控，并在VCC升至欠压闭锁门限以上之前使充电器保持在停机模式。UVLO电路将使充电器保持在停机模式。如果UVLO比较器发生跳变，则在VCC升至比电池电压高100mV之前充电器将不会退出停机模式。

# 自动再充电

一旦充电循环被终止，LTH7R立即采用一个具有1.8ms滤波时间的比较器来对BAT引脚上的电压进行连续监控。当电池电压降至4.05V（大致对应于电池容量的80%至90%） 以下时，充电循环重新开始。这确保了电池被维持在（或接近）一个充满电状态，并免除了进行周期性充电循环启动的需要。在再充电循环过程中，CHRG引脚输出进入一 个强下拉状态。

# 稳定性考虑

只要电池与充电器的输出端相连，恒定电压模式反馈环 路就能够在未采用一个外部电容的情况下保持稳定。在 没有接电池时，为了减小纹波电压，建议采用一个输出电 容。当采用大数值的低ESR陶瓷电容时，建议增加一个与 电容串联的1Ω电阻。如果使用钽电容，则不需要串联电 阻。

在恒定电流模式中，位于反馈环路中的是PROG引脚，而 不是电池。恒定电流模式的稳定性受PROG引脚阻抗的影 响。当PROG引脚上没有附加电容，RPROG选择高达20k时充电器可以稳定。然而PROG节点的额外电容会减小设定电 阻的最大容许阻值。PROG引脚上的极点频率应保持在100kHz以上。因此，如果PROG引脚存在一个容性负载， CPROG，则可采用下式来计算RPROG的最大电阻值：

![](images/07b9d73cfb19d181b51e2fe7eadadc37eeced69d16c26cf8d41cb7bf46d51e08.jpg)

用户更感兴趣的是充电电流而不是瞬态电流。例如，如果 一个运行在低电流模式的开关电源与电池并联，则从BAT 引脚流出的平均电流通常比瞬态电流脉冲更加重要。在 这种场合，可在PROG引脚上采用一个简单的RC滤波器来 测量平均的电池电流（如图6所示）。在PROG引脚和滤波 电容之间增设了一个10k的电阻以确保稳定性。

![](images/3b3cf77fbfc3d354a8d6a24c2dd18364f95bfedcad20b82433fb080b97626f9d.jpg)  
图6 隔离PROG引脚上的容性负载和滤波器。

# 功耗考虑

芯片结温依赖于环境温度、PCB布局、负载和封装类型等多种因素。功耗与芯片结温可根据以下公式计算：

根据P 结温可由以下公式求得：

![](images/16745b664305c07eac2abb5d03e7e0f2485cdc464a558f129c5469347c1c6505.jpg)

其中

TJ 是芯片结温TA 是环境温度θJA是封装热阻

# 封装规格

![](images/ccb15a77a81bf5c20bb241fc3ee661daf149e4f64bcf47f5cb8c32bb210abaaf.jpg)  
SOT-23-5L package mechanical drawing

<table><tr><td rowspan=3 colspan=1>symbol</td><td rowspan=1 colspan=4>dimensions</td></tr><tr><td rowspan=1 colspan=2>millimeters</td><td rowspan=1 colspan=2>inches</td></tr><tr><td rowspan=1 colspan=1>min</td><td rowspan=1 colspan=1>max</td><td rowspan=1 colspan=1>min</td><td rowspan=1 colspan=1>max</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>2.7</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>0.1063</td><td rowspan=1 colspan=1>0.1181</td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>0.0591</td><td rowspan=1 colspan=1>0.0669</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>3.1</td><td rowspan=1 colspan=1>0.1102</td><td rowspan=1 colspan=1>0.1220</td></tr><tr><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=2>1.9</td><td rowspan=1 colspan=2>0.0748</td></tr><tr><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>0.0118</td><td rowspan=1 colspan=1>0.0197</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3MAX</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.0512MAX</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>0.0004</td><td rowspan=1 colspan=1>0.0039</td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.0118</td><td rowspan=1 colspan=1>0.0236</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.0039</td><td rowspan=1 colspan=1>0.0059</td></tr><tr><td rowspan=1 colspan=1>θ</td><td rowspan=1 colspan=1>0°</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>0°</td><td rowspan=1 colspan=1>8°</td></tr></table>

# Attention

■ Any and all HUA XUAN YANG ELECTRONICS products described or contained herein do not have specifications that can handle applications that require extremely high levels of reliability, such as life-support systems, aircraft's control systems, or other applications whose failure can be reasonably expected to result in serious physical and/or material damage. Consult with your HUA XUAN YANG ELECTRONICS representative nearest you before using any HUA XUAN YANG ELECTRONICS products described or contained herein in such applications.

■ HUA XUAN YANG ELECTRONICS assumes no responsibility for equipment failures that result from using products at values that exceed, even momentarily, rated values (such as maximum ratings, operating condition ranges, or other parameters) listed in products specifications of any and all HUA XUAN YANG ELECTRONICS products described or contained herein.

■ Specifications of any and all HUA XUAN YANG ELECTRONICS products described or contained herein stipulate the performance, characteristics, and functions of the described products in the independent state, and are not guarantees of the performance, characteristics, and functions of the described products as mounted in the customer’s products or equipment. To verify symptoms and states that cannot be evaluated in an independent device, the customer should always evaluate and test devices mounted in the customer’s products or equipment.

■ HUA XUAN YANG ELECTRONICS CO.,LTD. strives to supply high-quality high-reliability products. However, any and all semiconductor products fail with some probability. It is possible that these probabilistic failures could give rise to accidents or events that could endanger human lives, that could give rise to smoke or fire, or that could cause damage to other property. When designing equipment, adopt safety measures so that these kinds of accidents or events cannot occur. Such measures include but are not limited to protective circuits and error prevention circuits for safe design, redundant design, and structural design.

■ In the event that any or all HUA XUAN YANG ELECTRONICS products(including technical data, services) described or contained herein are controlled under any of applicable local export control laws and regulations, such products must not be exported without obtaining the export license from the authorities concerned in accordance with the above law.

■ No part of this publication may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopying and recording, or any information storage or retrieval system, or otherwise, without the prior written permission of HUA XUAN YANG ELECTRONICS CO.,LTD.

■ Information (including circuit diagrams and circuit parameters) herein is for example only ; it is not guaranteed for volume production. HUA XUAN YANG ELECTRONICS believes information herein is accurate and reliable, but no guarantees are made or implied regarding its use or any infringements of intellectual property rights or other rights of third parties.

■ Any and all information described or contained herein are subject to change without notice due to product/technology improvement, etc.   
When designing equipment, refer to the "Delivery Specification" for the HUA XUAN YANG ELECTRONICS product that you intend to use.