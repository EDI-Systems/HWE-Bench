# ESP32­WROOM­32E ESP32­WROOM­32UE

技术规格书

2.4 GHz Wi­Fi + 蓝牙 ® + 低功耗蓝牙模组  
内置 ESP32 系列芯片，Xtensa® 双核 32 位 LX6 处理器  
可选 4/8/16 MB flash  
26 个 GPIO，外设丰富  
板上 PCB 天线或外部天线连接器

# 模组概述

# 说明：

点击链接或扫描二维码确保您使用的是最新版本的文档：  
https://espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_  
datasheet_cn.pdf

# 1.1 特性

# CPU 和片上存储器

• 内置 ESP32-D0WD-V3 芯片，Xtensa 双核 32 位LX6 微处理器，支持高达 240 MHz 的时钟频率  
• 448 KB ROM  
• 520 KB SRAM  
• 16 KB RTC SRAM

# Wi­Fi

• 802.11b/g/n  
• 802.11n 模式下数据速率高达 150 Mbps  
• 支持 A-MPDU 和 A-MSDU 聚合  
• 0.4 µs 保护间隔  
• 工作信道中心频率范围：2412 \~ 2484 MHz

# 蓝牙

# 模组集成元件

• 40 MHz 晶振• 4/8/16 MB SPI flash（可选）

# 天线选型

• ESP32-WROOM-32E：板载 PCB 天线• ESP32-WROOM-32UE：通过连接器连接外部天线

• 蓝牙 V4.2 BR/EDR 和蓝牙 LE 标准• Class-1、class-2 和 class-3 发射器• AFH  
• CVSD 和 SBC

# 工作条件

• 工作电压/供电电压：3.0 \~ 3.6 V  
• 工作环境温度：– 85°C 版：–40 \~ 85 °C– 105°C 版：–40 \~ 105 °C。注意，仅有内置4/8 MB flash 的模组支持 105 °C 版，内置16 MB flash 的模组尚不支持 105 °C 版。

# 外设

• SD 卡、UART、SPI、SDIO、I2C、LED PWM、电机PWM、I2S、IR、脉冲计数器、GPIO、电容式触摸传感器、ADC、DAC、TWAI®（兼容 ISO 11898-1，即 CAN 规范 2.0）

# 认证

• 蓝牙认证：BQB• RF 认证：FCC/CE-RED/SRRC• 环保认证：REACH/RoHS

# 可靠性测试

• HTOL/HTSL/uHAST/TCT/ESD

# 1.2 描述

ESP32-WROOM-32E 和 ESP32-WROOM-32UE 是两款通用型 Wi-Fi + Bluetooth + Bluetooth LE MCU 模组，功能强大，用途广泛，可以用于低功耗传感器网络和要求极高的任务，例如语音编码、音频流和 MP3 解码等。

ESP32-WROOM-32E 采用 PCB 板载天线，ESP32-WROOM-32UE 采用连接器连接外部天线。本文档提供的信

# 息适用于这两款模组。

模组的订购信息请见下表。

表 1: 模组订购信息  

<table><tr><td rowspan=1 colspan=1>模组</td><td rowspan=1 colspan=1>集成芯片</td><td rowspan=1 colspan=1>Flash</td><td rowspan=1 colspan=1>模组尺寸 (mm)</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROOM-32E（85°C版）</td><td rowspan=1 colspan=1>ESP32-D0WD-V3</td><td rowspan=1 colspan=1>4/8/16MB</td><td rowspan=1 colspan=1>18.0×25.5×3.1</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROOM-32E（105C版)</td><td rowspan=1 colspan=1>ESP32-D0WD-V3</td><td rowspan=1 colspan=1>4/8 MB</td><td rowspan=1 colspan=1>18.0×25.5×3.1</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROOM-32UE（85°C版）</td><td rowspan=1 colspan=1>ESP32-D0WD-V3</td><td rowspan=1 colspan=1>4/8/16 MB</td><td rowspan=1 colspan=1>18.0×19.2×3.2</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROOM-32UE （105°C版）</td><td rowspan=1 colspan=1>ESP32-D0WD-V3</td><td rowspan=1 colspan=1>4/8MB</td><td rowspan=1 colspan=1>18.0×19.2×3.2</td></tr></table>

# 说明：

1. 具体订购信息请参考文档《乐鑫产品选型工具》。  
2. 天线连接器尺寸详见章节 7.3。

ESP32-WROOM-32E 和 ESP32-WROOM-32UE 采用的芯片是 ESP32 系列的 ESP32-D0WD-V3\*。ESP32-D0WD-V3 芯片具有可扩展、自适应的特点。两个 CPU 核可以被单独控制。CPU 时钟频率的调节范围为 80 MHz 到 240MHz。用户可以关闭CPU的电源，利用低功耗协处理器监测外设的状态变化或某些模拟量是否超出阈值。ESP32还集成了丰富的外设，包括电容式触摸传感器、霍尔传感器、SD 卡接口、以太网接口、高速 SPI、UART、I2S和 I2C 等。

# 说明：

\* 关于 ESP32-D0WD-V3 的更多信息请参考 《ESP32 系列芯片技术规格书》模组集成了传统蓝牙、低功耗蓝牙和 Wi-Fi，具有广泛的用途：Wi-Fi 支持极大范围的通信连接，也支持通过路由器直接连接互联网；而蓝牙可以让用户连接手机或者广播 BLE Beacon 以便于信号检测。ESP32 芯片的睡眠电流小于 5 µA，使其适用于电池供电的可穿戴电子设备。模组支持的数据传输速率高达 150 Mbps，天线输出功率达到 20 dBm，可实现最大范围的无线通信。因此，这款模组具有行业领先的技术规格，在高集成度、无线传输距离、功耗以及网络联通等方面性能极佳。

ESP32 的操作系统是带有 LwIP 的 freeRTOS，还内置了带有硬件加速功能的 TLS 1.2。芯片同时支持 OTA 加密升级，方便用户在产品发布之后继续升级。

# 1.3 应用

• 通用低功耗 IoT 传感器集线器  
• 通用低功耗 IoT 数据记录器  
• 摄像头视频流传输  
• OTT 电视盒/机顶盒设备  
• 语音识别  
• 图像识别  
• Mesh 网络  
• 家庭自动化  
• 智慧楼宇  
• 工业自动化  
• 智慧农业  
• 音频设备  
• 健康/医疗/看护  
• Wi-Fi 玩具  
• 可穿戴电子产品  
• 零售 & 餐饮  
• 智能家居控制板  
• 智能 POS 应用

目录

# 目录

# 模组概述 2

1.1 特性  
1.2 描述  
1.3 应用

# 3

2 功能框图 8

3 管脚定义 9

3.1 管脚布局 9 管脚宁义 o

3.3 Strapping 管脚 11

4 电气特性 13

4.1 绝对最大额定值 13

4.2 建议工作条件 13

4.3 直流电气特性 (3.3 V, 25 °C) 13

4.4 功耗特性 14

4.5 Wi-Fi 射频特性

4.5.1 Wi-Fi 射频标准 14

4.5.2 发射器性能规格 15

4.5.3 接收器性能规格

15  
4.6 蓝牙射频 17  
4.6.1 接收器 - 基础数据率 (BR) 17  
4.6.2 发射器 - 基础数据率 (BR) 17  
4.6.3 接收器 - 增强数据率 (EDR) 18  
4.6.4 发射器 - 增强数据率 (EDR) 18

4.7 低功耗蓝牙射频

19

4.7.1 接收器

4.7.2 发射器 19

5 模组原理图 20

6 外围设计原理图 22

# 模组尺寸和 PCB 封装图形 23

7.1 模组尺寸 23   
7.2 推荐 PCB 封装图 24   
7.3 外部天线连接器尺寸 26

8 产品处理 27

8.1 存储条件 27  
8.2 静电放电 (ESD) 27  
8.3 回流焊温度曲线 27

乐鑫信息科技 4 ESP32-WROOM-32E & WROOM-32UE 技术规格书 v1.3反馈文档意见

28

# 9 相关文档和资源修订历史

# 表格

# 1 模组订购信息 3

2 管脚定义 10

3 Strapping 管脚 12

5 建议工作条件 13

6 直流电气特性 (3.3 V, 25 °C) 13

7 射频功耗 14

8 Wi-Fi 射频标准 15

9 发射器功率规格 15

13 接收器特性 - 基础数据率 (BR) 17

14 发射器特性 - 基础数据率 (BR) 17

15 接收器特性 - 增强数据率 (EDR) 18

16 发射器特性 - 增强数据率 (EDR) 18

7 低功耗蓝牙接收器特性 19

低功耗蓝牙发射器特性 19

# 插图

ESP32-WROOM-32E 功能框图 8

2 ESP32-WROOM-32UE 功能框图 8

3 管脚布局（顶视图） 9

4 ESP32-WROOM-32E 原理图 20

5 ESP32-WROOM-32UE 原理图 21

ESP32-WROOM-32E 模组尺寸 23

8 ESP32-WROOM-32UE 模组尺寸 23

9 ESP32-WROOM-32E 推荐 PCB 封装图 24

10 ESP32-WROOM-32UE 推荐 PCB 封装图 25

11 外部天线连接器尺寸图 26

12 回流焊温度曲线 27

# 2 功能框图

![](images/d635ee88149b8e3621b421b090f388bf38632007513dc77445f4c1d377dbcd4f.jpg)  
图 1: ESP32­WROOM­32E 功能框图

![](images/eb9c2705c99307ff39ed5ad236eb1627c779b8e21f6f57bc4ba740d602a5ae75.jpg)  
图 2: ESP32­WROOM­32UE 功能框图

# 3 管脚定义

# 3.1 管脚布局

管脚布局图显示了模组上管脚的大致位置。按比例绘制的实际布局请参考图 7.1 模组尺寸。ESP32-WROOM-32UE 没有禁止布线区 (keepout zone)，管脚布局和 ESP32-WROOM-32E 一样。

![](images/644c1c8eb4f566dca3c2de032ca3294fc23a5317b3736dea2cb6c305663047ee.jpg)  
图 3: 管脚布局（顶视图）

# 3.2 管脚定义

模组共有 38 个管脚，具体描述参见表 2。  
外设管脚分配请参考 《ESP32 系列芯片技术规格书》。

# 表 2: 管脚定义

见下页  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>类型1</td><td rowspan=1 colspan=1>功能</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>接地</td></tr><tr><td rowspan=1 colspan=1>3V3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>供电</td></tr><tr><td rowspan=1 colspan=1>EN</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>高电平：芯片使能；低电平：芯片关闭；注意：不能让 EN 管脚浮空。</td></tr><tr><td rowspan=1 colspan=1>SENSOR_VP</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>|</td><td rowspan=1 colspan=1>GPIO36, ADC1_CHO, RTC_GPIO0</td></tr><tr><td rowspan=1 colspan=1>SENSOR_VN</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>GPIO39, ADC1_CH3, RTC_GPIO3</td></tr><tr><td rowspan=1 colspan=1>1034</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>GPIO34, ADC1_CH6, RTC_GPIO4</td></tr><tr><td rowspan=1 colspan=1>1035</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>GPIO35, ADC1__CH7, RTC_GPIO5</td></tr><tr><td rowspan=1 colspan=1>1032</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Vo</td><td rowspan=1 colspan=1>GPIO32, XTAL_32K_P (32.768 kHz 晶振输人), ADC1_CH4,TOUCH9,RTC_GPIO9</td></tr><tr><td rowspan=1 colspan=1>1033</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO33, XTAL_32K_N (32.768 kHz 晶振输出)，ADC1_CH5, TOUCH8,RTC_GPIO8</td></tr><tr><td rowspan=1 colspan=1>1025</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO25, DAC_1, ADC2_CH8, RTC_GPIO6, EMAC_RXD0</td></tr><tr><td rowspan=1 colspan=1>1026</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO26, DAC_2, ADC2_CH9, RTC_GPIO7, EMAC_RXD1</td></tr><tr><td rowspan=1 colspan=1>1027</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO27, ADC2_CH7, TOUCH7, RTC_GPIO17, EMAC_RX_DV</td></tr><tr><td rowspan=1 colspan=1>1014</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>Vo</td><td rowspan=1 colspan=1>GPIO14, ADC2_CH6, TOUCH6, RTC_GPIO16, MTMS, HSPICLK,HS2_CLK, SD_CLK, EMAC_TXD2</td></tr><tr><td rowspan=1 colspan=1>1012</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO12, ADC2_CH5, TOUCH5, RTC_GPIO15, MTDI, HSPIQ,HS2_DATA2, SD_DATA2, EMAC_TXD3</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>接地</td></tr><tr><td rowspan=1 colspan=1>1013</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO13, ADC2_CH4, TOUCH4, RTC_GPIO14, MTCK, HSPID,HS2_DATA3, SD_DATA3, EMAC_RX_ER</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>请见表格下方说明²</td></tr><tr><td rowspan=1 colspan=1>1015</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO15, ADC2_CH3, TOUCH3, MTDO, HSPICS0, RTC_GPIO13,HS2_CMD, SD_CMD, EMAC_RXD3</td></tr><tr><td rowspan=1 colspan=1>102</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO2, ADC2_CH2, TOUCH2, RTC_GPIO12, HSPIWP, HS2_DATAO,SD_DATAO</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO0, ADC2_CH1, TOUCH1, RTC_GPIO11, CLK_OUT1,EMAC_TX_CLK</td></tr><tr><td rowspan=1 colspan=1>104</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO4, ADC2_CHO, TOUCHO, RTC_GPIO10, HSPIHD, HS2_DATA1,SD_DATA1, EMAC_TX_ER</td></tr><tr><td rowspan=1 colspan=1>1016</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO16, HS1_DATA4, U2RXD, EMAC_CLK_OUT</td></tr><tr><td rowspan=1 colspan=1>1017</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO17, HS1_DATA5, U2TXD, EMAC_CLK_OUT_180</td></tr><tr><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>1O</td><td rowspan=1 colspan=1>GPIO5, VSPICS0, HS1_DATA6, EMAC_RX_CLK</td></tr><tr><td rowspan=1 colspan=1>1018</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO18, VSPICLK, HS1_DATA7</td></tr></table>

表 2 – 接上页  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>类型1</td><td rowspan=1 colspan=1>功能</td></tr><tr><td rowspan=1 colspan=1>1019</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO19, VSPIQ, U0CTS, EMAC_TXD0</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>1021</td><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO21, VSPIHD, EMAC_TX_EN</td></tr><tr><td rowspan=1 colspan=1>RXDO</td><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO3, UORXD, CLK_OUT2</td></tr><tr><td rowspan=1 colspan=1>TXDO</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO1, U0TXD, CLK_OUT3, EMAC_RXD2</td></tr><tr><td rowspan=1 colspan=1>1022</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>VO</td><td rowspan=1 colspan=1>GPIO22, VSPIWP, U0RTS, EMAC_TXD1</td></tr><tr><td rowspan=1 colspan=1>1023</td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>1VO</td><td rowspan=1 colspan=1>GPIO23, VSPID, HS1_STROBE</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>接地</td></tr></table>

1 P：电源；I：输入；O：输出。2 ESP32-D0WD-V3 芯片上的 GPIO6 至 GPIO11 用于连接模组上集成的 SPI flash，不再拉出至模组管脚。

# 3.3 Strapping 管脚

# 说明：

以下内容摘自 《ESP32 系列芯片技术规格书》的 Strapping 管脚章节。芯片的 Strapping 管脚与模组管脚的对应关系，可参考章节 5 模组原理图。

ESP32-D0WD-V3 共有 5 个 Strapping 管脚。

• MTDI • GPIO0 • GPIO2 • MTDO • GPIO5

软件可以读取寄存器“GPIO_STRAPPING”中这 5 个管脚 strapping 的值。

在芯片的系统复位（上电复位、RTC 看门狗复位、欠压复位）放开的过程中，Strapping 管脚对电平采样并存储到锁存器中，锁存为“0”或“1”，并一直保持到芯片掉电或关闭。

每一个 Strapping 管脚都会连接内部上拉/下拉。如果一个 Strapping 管脚没有外部连接或者连接的外部线路处于高阻抗状态，内部弱上拉/下拉将决定 Strapping 管脚输入电平的默认值。

为改变 Strapping 的值，用户可以应用外部下拉/上拉电阻，或者应用主机 MCU 的 GPIO 控制 ESP32-D0WD-V3上电复位放开时的 Strapping 管脚电平。

复位放开后，Strapping 管脚和普通管脚功能相同。

配置 Strapping 管脚的详细启动模式请参阅表 3 。

表 3: Strapping 管脚  

<table><tr><td rowspan=1 colspan=6>内置 LDO (VDD_SDIO) 电压</td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=2>3.3V</td><td rowspan=1 colspan=2>1.8V</td></tr><tr><td rowspan=1 colspan=1>MTDI</td><td rowspan=1 colspan=1>下拉</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=2>1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>系统启动模式</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=2>SPI启动模式</td><td rowspan=1 colspan=2>下载启动模式</td></tr><tr><td rowspan=1 colspan=1>GPIOO</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=1>GPIO2</td><td rowspan=1 colspan=1>下拉</td><td rowspan=1 colspan=2>无关项</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=5>系统启动过程中，控制 UOTXD 打印</td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=2>UOTXD 正常打印</td><td rowspan=1 colspan=2>UOTXD上电不打印</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4>SDIO 从机信号输入输出时序</td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=1>下降沿采样下降沿输出</td><td rowspan=1 colspan=1>下降沿采样上升沿输出</td><td rowspan=1 colspan=1>上升沿采样下降沿输出</td><td rowspan=1 colspan=1>上升沿采样上升沿输出</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>GPIO5</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td></tr></table>

\* 固件可以通过配置一些寄存器比特位，在启动后改变“内置 LDO (VDD_SDIO) 电压”和“SDIO 从机信号输入输出时序”的设定。\* 由于模组内置了 3.3 V SPI flash，所以上电时不能将 MTDI 置 1。

# 4 电气特性

# 4.1 绝对最大额定值

超出绝对最大额定值可能导致器件永久性损坏。这只是强调的额定值，不涉及器件在这些或其它条件下超出本技术规格指标的功能性操作。建议工作条件请参考表 5 建议工作条件。长时间暴露在绝对最大额定条件下可能会影响模组的可靠性。

表 4: 绝对最大额定值  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=1>供电电压</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>TsTORE</td><td rowspan=1 colspan=1>存储温度</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>℃</td></tr></table>

\* 关于电源域请参考 《ESP32 系列芯片技术规格书》 附录中表 IO MUX。

# 4.2 建议工作条件

表 5: 建议工作条件  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=2>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=2>电源管脚电压</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IVDD</td><td rowspan=1 colspan=2>外部电源的供电电流</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=2 colspan=1>T</td><td rowspan=2 colspan=1>工作环境温度</td><td rowspan=1 colspan=1>85℃版</td><td rowspan=2 colspan=1>-40</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>85105</td><td rowspan=2 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>105℃版</td></tr></table>

# 4.3 直流电气特性 (3.3 V, 25 °C)

表 6: 直流电气特性 (3.3 V, 25 °C)  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>CIN</td><td rowspan=1 colspan=1>管脚电容</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>pF</td></tr><tr><td rowspan=1 colspan=1>$VIH</td><td rowspan=1 colspan=1>高电平输入电压</td><td rowspan=1 colspan=1>0.75 × VDD1</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>VDD&#x27;+ 0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=1>低电平输入电压</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.25 × VDD1</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IIH</td><td rowspan=1 colspan=1>高电平输入电流</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>nA</td></tr><tr><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>低电平输入电流</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>nA</td></tr><tr><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>高电平输出电压</td><td rowspan=1 colspan=1>0.8 × VDD1</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOL</td><td rowspan=1 colspan=1>低电平输出电压</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>0.1 × VDD1</td><td rowspan=1 colspan=1>V</td></tr></table>

见下页

表 6 – 接上页  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=2>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=3 colspan=1>IOH</td><td rowspan=3 colspan=1>高电平拉电流VDD1 = 3.3 V,VOH &gt;= 2.64 V,管脚输出强度设为最大值)</td><td rowspan=1 colspan=1>VDD3P3_CPU电源域1.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>VDD3P3_RTC电源域1.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>VDD_SDIO电源域1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>lOL</td><td rowspan=1 colspan=2>低电平灌电流WDD1= 3.3 V, VoL = 0.495 V,管脚输出强度设为最大值)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>RpU</td><td rowspan=1 colspan=2>上拉电阻</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>kΩ</td></tr><tr><td rowspan=1 colspan=1>RPD</td><td rowspan=1 colspan=2>下拉电阻</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>kΩ</td></tr><tr><td rowspan=1 colspan=1>VIL_nRST</td><td rowspan=1 colspan=2>CHIP_PU关闭芯片的低电平输入电压</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr></table>

1 VDD 是 I/O 的供电电源。关于电源域请参考 《ESP32 系列芯片技术规格书》 附录中表 IO MUX。2 VDD3P3_CPU 和 VDD3P3_RTC 电源域管脚的单个管脚的拉电流随管脚数量增加而减小，从约 40 mA减小到约 29 mA。3 VDD_SDIO 电源域的管脚不包括连接 flash 和/或 PSRAM 的管脚。

# 4.4 功耗特性

模组使用了先进的电源管理技术，可以在不同的功耗模式之间切换。关于不同功耗模式的描述，详见《ESP32 系列芯片技术规格书》 的 RTC 和低功耗管理章节。

表 7: 射频功耗  

<table><tr><td rowspan=1 colspan=1>工作模式</td><td rowspan=1 colspan=2>描述</td><td rowspan=1 colspan=1>平均值 (mA)</td><td rowspan=1 colspan=1>峰值 (mA)</td></tr><tr><td rowspan=6 colspan=1>Active（射频工作)</td><td rowspan=4 colspan=1>TX</td><td rowspan=1 colspan=1>802.11b, 20 MHz, 1 Mbps, @19.5 dBm</td><td rowspan=1 colspan=1>239</td><td rowspan=1 colspan=1>379</td></tr><tr><td rowspan=1 colspan=1>802.11g, 20 MHz, 54 Mbps, @15 dBm</td><td rowspan=1 colspan=1>190</td><td rowspan=1 colspan=1>276</td></tr><tr><td rowspan=1 colspan=1>802.11n, 20 MHz, MCS7, @13 dBm</td><td rowspan=1 colspan=1>183</td><td rowspan=1 colspan=1>258</td></tr><tr><td rowspan=1 colspan=1>802.11n, 40 MHz, MCS7, @13 dBm</td><td rowspan=1 colspan=1>165</td><td rowspan=1 colspan=1>211</td></tr><tr><td rowspan=2 colspan=1>RX</td><td rowspan=1 colspan=1>802.11b/g/n, 20 MHz</td><td rowspan=1 colspan=1>112</td><td rowspan=1 colspan=1>112</td></tr><tr><td rowspan=1 colspan=1>802.11n, 40 MHz</td><td rowspan=1 colspan=1>118</td><td rowspan=1 colspan=1>118</td></tr></table>

1 功耗数据是基于 3.3 V 电源、25 °C 环境温度，在 RF 接口处完成的测试结果。所有发射数据均基于50% 的占空比测得。2 测量 RX 功耗数据时，外设处于关闭状态，CPU 处于 idle 状态。

# 4.5 Wi­Fi 射频特性

# 4.5.1 Wi­Fi 射频标准

表 8: Wi­Fi 射频标准  

<table><tr><td rowspan=1 colspan=2>名称</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=2>工作信道中心频率范围1</td><td rowspan=1 colspan=1>2412~2484 MHz</td></tr><tr><td rowspan=1 colspan=2>Wi-Fi 协议</td><td rowspan=1 colspan=1>IEEE 802.11b/g/n</td></tr><tr><td rowspan=2 colspan=1>数据速率</td><td rowspan=1 colspan=1>20MHz</td><td rowspan=1 colspan=1>11b: 1, 2, 5.5, 11 Mbps11g: 6, 9, 12, 18, 24, 36, 48, 54 Mbps11n: MCS0-7, 72.2 Mbps (Max)</td></tr><tr><td rowspan=1 colspan=1>40 MHz</td><td rowspan=1 colspan=1>11n: MCS0-7, 150 Mbps (Max)</td></tr><tr><td rowspan=1 colspan=2>天线类型</td><td rowspan=1 colspan=1>PCB天线，外部天线2</td></tr></table>

1 工作信道中心频率范围应符合国家或地区的规范标准。软件可以配置工作信道中心频率范围。2 使用外部天线的模组输出阻抗为 50 Ω，不使用外部天线的模组可无需关注输出阻抗。

# 4.5.2 发射器性能规格

根据产品或认证的要求，您可以配置发射器目标功率。默认功率详见表 9。

表 9: 发射器功率规格  

<table><tr><td rowspan=1 colspan=1>速率</td><td rowspan=1 colspan=1>典型值 (dBm)</td></tr><tr><td rowspan=1 colspan=1>11b,1 Mbps</td><td rowspan=1 colspan=1>19.5</td></tr><tr><td rowspan=1 colspan=1>11b, 11 Mbps</td><td rowspan=1 colspan=1>19.5</td></tr><tr><td rowspan=1 colspan=1>11g,6 Mbps</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>11g,54 Mbps</td><td rowspan=1 colspan=1>14</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCSO</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>11n, HT20,MCS7</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>11n, HT40,MCSO</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>13</td></tr></table>

# 4.5.3 接收器性能规格

表 10: 接收灵敏度  

<table><tr><td rowspan=1 colspan=1>速率</td><td rowspan=1 colspan=1>典型值 (dBm)</td></tr><tr><td rowspan=1 colspan=1>1 Mbps</td><td rowspan=1 colspan=1>-97</td></tr><tr><td rowspan=1 colspan=1>2 Mbps</td><td rowspan=1 colspan=1>-94</td></tr><tr><td rowspan=1 colspan=1>5.5 Mbps</td><td rowspan=1 colspan=1>-92</td></tr><tr><td rowspan=1 colspan=1>11 Mbps</td><td rowspan=1 colspan=1>-88</td></tr><tr><td rowspan=1 colspan=1>6 Mbps</td><td rowspan=1 colspan=1>-93</td></tr><tr><td rowspan=1 colspan=1>9 Mbps</td><td rowspan=1 colspan=1>-91</td></tr><tr><td rowspan=1 colspan=1>12 Mbps</td><td rowspan=1 colspan=1>-89</td></tr><tr><td rowspan=1 colspan=1>18 Mbps</td><td rowspan=1 colspan=1>-87</td></tr><tr><td rowspan=1 colspan=1>24 Mbps</td><td rowspan=1 colspan=1>-84</td></tr><tr><td rowspan=1 colspan=1>36 Mbps</td><td rowspan=1 colspan=1>-80</td></tr><tr><td rowspan=1 colspan=1>48 Mbps</td><td rowspan=1 colspan=1>-77</td></tr></table>

见下页

表 10 – 接上页  

<table><tr><td rowspan=1 colspan=1>速率</td><td rowspan=1 colspan=1>典型值 (dBm)</td></tr><tr><td rowspan=1 colspan=1>54 Mbps</td><td rowspan=1 colspan=1>-75</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>-92</td></tr><tr><td rowspan=1 colspan=1>11n, HT20,NMCS1</td><td rowspan=1 colspan=1>-88</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS2</td><td rowspan=1 colspan=1>-86</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, 1MCS3</td><td rowspan=1 colspan=1>-83</td></tr><tr><td rowspan=1 colspan=1>11n, HT20,MCS4</td><td rowspan=1 colspan=1>-80</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS5</td><td rowspan=1 colspan=1>-76</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, NMCS6</td><td rowspan=1 colspan=1>-74</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-72</td></tr><tr><td rowspan=1 colspan=1>11n, HT40,IMCSO</td><td rowspan=1 colspan=1>-89</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS1</td><td rowspan=1 colspan=1>-85</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS2</td><td rowspan=1 colspan=1>-83</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS3</td><td rowspan=1 colspan=1>-80</td></tr><tr><td rowspan=1 colspan=1>11n, HT40,MCS4</td><td rowspan=1 colspan=1>-76</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS5</td><td rowspan=1 colspan=1>-72</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS6</td><td rowspan=1 colspan=1>-71</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>-69</td></tr></table>

表 11: 最大接收电平  

<table><tr><td rowspan=1 colspan=1>速率</td><td rowspan=1 colspan=1>典型值 (dBm)</td></tr><tr><td rowspan=1 colspan=1>11b, 1 Mbps</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>11b, 11 Mbps</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1>-8</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-8</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>-8</td></tr></table>

表 12: 邻道抑制  

<table><tr><td rowspan=1 colspan=1>速率</td><td rowspan=1 colspan=1>典型值 (dB)</td></tr><tr><td rowspan=1 colspan=1>11b, 11 Mbps</td><td rowspan=1 colspan=1>35</td></tr><tr><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>27</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>27</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS0</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>7</td></tr></table>

# 4.6 蓝牙射频

# 4.6.1 接收器 ­ 基础数据率 (BR)

表 13: 接收器特性 ­ 基础数据率 (BR)  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>灵敏度 @0.1% BER</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-90</td><td rowspan=1 colspan=1>-89</td><td rowspan=1 colspan=1>-88</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>最大接收信号 @0.1% BER</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>共信道抑制比C/</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>邻道选择性抑制比 C/I</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-6</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -1 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-6</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO -2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-33</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 −3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>-45</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=4 colspan=1>带外阻塞</td><td rowspan=1 colspan=1>30 MHz~2000 MHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2000 MHz~2400 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2500 MHz~3000 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>3000 MHz ~12.5 GHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>互调</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-36</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>dBm</td></tr></table>

# 4.6.2 发射器 ­ 基础数据率 (BR)

表 14: 发射器特性 ­ 基础数据率 (BR)  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>射频发射功率*</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>增益控制步长</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>射频功率控制范围</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-12</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+9</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>20dB带宽</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=3 colspan=1>邻道发射功率</td><td rowspan=1 colspan=1>F = FO ± 2 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = FO ± 3 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = FO ± &gt; 3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-59</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>∆ f 1avg</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>155</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2max</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>127</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2avg/∆ f 1avg</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.92</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td></tr><tr><td rowspan=1 colspan=1>ICFT</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-7</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>漂移速率</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>KHz/50μS</td></tr><tr><td rowspan=1 colspan=1>偏移 (DH1)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>偏移 (DH5)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>kHz</td></tr></table>

从 0 到 7，共有 8 个功率级别，发射功率范围从–12 dBm 到 9 dBm。功率电平每增加 1 时，发射功率增加 3 dB。默认情况下使用功率级别 4，相应的发射功率为 0 dBm。

# 4.6.3 接收器 ­ 增强数据率 (EDR)

表 15: 接收器特性 ­ 增强数据率 (EDR)  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=6>π/4 DQPSK</td></tr><tr><td rowspan=1 colspan=1>灵敏度 @0.01% BER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-90</td><td rowspan=1 colspan=1>-89</td><td rowspan=1 colspan=1>-88</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>最大接收信号 @0.01% BER</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>共信道抑制比C/</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>邻道选择性抑制比C/I</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0-1 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO −2 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-35</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -3 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8DPSK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>灵敏度 @0.01% BER</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>-84</td><td rowspan=1 colspan=1>-83</td><td rowspan=1 colspan=1>-82</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>最大接收信号 @0.01% BER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>共信道抑制比C/I</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>邻道抑制比C/</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -1 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>/</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -2 MHz</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0-3 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-38</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr></table>

# 4.6.4 发射器 ­ 增强数据率 (EDR)

表 16: 发射器特性 ­ 增强数据率 (EDR)  

<table><tr><td colspan="1" rowspan="1">参数</td><td colspan="1" rowspan="1">条件</td><td colspan="1" rowspan="1">最小值</td><td colspan="1" rowspan="1">典型值</td><td colspan="1" rowspan="1">最大值</td><td colspan="1" rowspan="1">单位</td></tr><tr><td colspan="1" rowspan="1">射频发射功率（见表14下方说明）</td><td colspan="1" rowspan="1">/</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">增益控制步长</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">dB</td></tr><tr><td colspan="1" rowspan="1">射频功率控制范围</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">-12</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">+9</td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">π/4 DQPSK max w0</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">-0.72</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="1">π/4 DQPSK max wi</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-6</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="1">π/4 DQPSK max Iwi + w0I</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">-7.42</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="1">8DPSK max w0</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0.7</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="1">8DPSK max wi</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">-9.6</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="1">8DPSK max Iwi + w0l</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-10</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">kHz</td></tr><tr><td colspan="1" rowspan="3">π/4 DQPSK调制精度</td><td colspan="1" rowspan="1">RMS DEVM</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">4.28</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="1">99% DEVM</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="1">Peak DEVM</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">13.3</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="3">8 DPSK调制精度</td><td colspan="1" rowspan="1">RMS DEVM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">5.8</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="1">99% DEVM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="1">Peak DEVM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">%</td></tr><tr><td colspan="1" rowspan="4">带内杂散发射</td><td colspan="1" rowspan="1">F = FO ± 1 MHz</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-46</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">F = FO ± 2 MHz</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-44</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">F = FO ± 3 MHz</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-49</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">F = FO +/-&gt; 3 MHz</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">-53</td><td colspan="1" rowspan="1">dBm</td></tr><tr><td colspan="1" rowspan="1">EDR 差分相位编码</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">%</td></tr></table>

# 4.7 低功耗蓝牙射频

# 4.7.1 接收器

表 17: 低功耗蓝牙接收器特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>灵敏度 @30.8% PER</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-94</td><td rowspan=1 colspan=1>-93</td><td rowspan=1 colspan=1>-92</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>最大接收信号 @30.8% PER</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>共信道抑制比 C/I</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+10</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>邻道抑制比C/</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -1 MHz</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-35</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO -3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=4 colspan=1>带外阻塞</td><td rowspan=1 colspan=1>30 MHz~2000 MHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2000 MHz~2400 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2500 MHz~3000MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>3000 MHz ~12.5 GHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>互调</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>-36</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr></table>

# 4.7.2 发射器

表 18: 低功耗蓝牙发射器特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>射频发射功率（见表14下方说明)</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>增益控制步长</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>射频功率控制范围</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-12</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+9</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=3 colspan=1>邻道发射功率</td><td rowspan=1 colspan=1>F = FO ± 2 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = F0 ± 3 MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-57</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F=FO±&gt;3MHz</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-59</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>∆ f 1avg</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>265</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2max</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>210</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2avg/∆ f 1avg</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+0.92</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td></tr><tr><td rowspan=1 colspan=1>ICFT</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>漂移速率</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>KHz/50μS</td></tr><tr><td rowspan=1 colspan=1>偏移</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>kHz</td></tr></table>

# 5 模组原理图

模组内部元件的电路图 。

![](images/dd103b67acfbe91f344b97b3009ae706e6d5ff6aea5d956293de5ec9287720ac.jpg)  
4: ESP32­WROOM­32E 原理图

![](images/ba5d4a9bb8400253b1b7752b6b62f2f3ecd8f46c9c531135466cac4d81ea6c5e.jpg)  
5: ESP32­WROOM­32U E 原理图

# 6 外围设计原理图

模组与外围器件（如电源、天线、复位按钮、JTAG 接口、UART 接口等）连接的应用电路图。

![](images/5a16c1406211c7b63385ab0cea232f65ef59aee924bd18f9c098ec659a147652.jpg)  
图 6: 外围设计原理图

• EPAD 管脚 39 可以不焊接到底板，但是焊接到底板的 GND 可以获得更好的散热特性。如果您想将 EPAD焊接到底板，请确保焊膏使用量正确。

• 为确保 ESP32 芯片上电时的供电正常，EN 管脚处需要增加 RC 延迟电路。RC 通常建议为 R = 10 kΩ，C= 1 µF，但具体数值仍需根据模组电源的上电时序和芯片的上电复位时序进行调整。ESP32 芯片的上电复位时序图可参考 《ESP32 系列芯片技术规格书》的电源管理章节。

# 7 模组尺寸和 PCB 封装图形

# 7.1 模组尺寸

![](images/54bdfc6363dea1d8b5f356c845bce44b73e0b73107616306abb27f04312d7c76.jpg)  
图 7: ESP32­WROOM­32E 模组尺寸

![](images/f9b53e955c1702325a245d0b877bfd807bfa360a2cf8da8596496d2c7c9ccc97.jpg)  
图 8: ESP32­WROOM­32UE 模组尺寸

# 说明：

有关卷带、载盘和产品标签的信息，请参阅 《乐鑫模组包装信息》。

# 7.2 推荐 PCB 封装图ESP

![](images/25cb2e0a65fa5fcefcec1c5eab66dc9bc05926ccb50304dc7656e3340a0e2862.jpg)  
图 9: ESP32­WROOM­32E 推荐 PCB 封装图

![](images/e98ca3da60324b85422411bc9805c960b6999a483b1d714ff343e2a13f7cc896.jpg)  
图 10: ESP32­WROOM­32UE 推荐 PCB 封装图

# 7.3 外部天线连接器尺寸

ESP32-WROOM-32UE 采用图 11 所示的第一代外部天线连接器，该连接器兼容：

• 广濑 (Hirose) 的 U.FL 系列连接器• I-PEX 的 MHF I 连接器• 安费诺 (Amphenol) 的 AMC 连接器

![](images/30ae99aadb415ae6190649fef6f8bf64068936b6c43ec928845496ec317ab1c8.jpg)  
图 11: 外部天线连接器尺寸图

<table><tr><td rowspan=1 colspan=1>③</td><td rowspan=1 colspan=1>SHELL</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>COPPERALLOY/AuPLATEDOVER Ni</td></tr><tr><td rowspan=1 colspan=1>②</td><td rowspan=1 colspan=1>CONTACT</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>COPPERALLOY/AuPLATEDOVER Ni</td></tr><tr><td rowspan=1 colspan=1>①</td><td rowspan=1 colspan=1>HOUSING</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>HIGHTTEMP. PLASTICUL94V-0/WHITE</td></tr><tr><td rowspan=1 colspan=1>ITEM</td><td rowspan=1 colspan=1>PARTNAME</td><td rowspan=1 colspan=1>QTY</td><td rowspan=1 colspan=1>MATERIAL/FINISH</td></tr></table>

# 8 产品处理

# 8.1 存储条件

密封在防潮袋 (MBB) 中的产品应储存在 < 40 °C/90%RH 的非冷凝大气环境中。  
模组的潮湿敏感度等级 MSL 为 3 级。  
真空袋拆封后，在 25±5 °C、60%RH 下，必须在 168 小时内使用完毕，否则就需要烘烤后才能二次上线。

# 8.2 静电放电 (ESD)

• 人体放电模式 (HBM)：±2000 V• 充电器件模式 (CDM)：±500 V• 空气放电：±6000 V  
• 接触放电：±4000 V

# 8.3 回流焊温度曲线

建议模组只过一次回流焊。

![](images/34a8a93f4a3b166d3488ac87ce0aa00aea33fffe807800fed088a0a1e05d442e.jpg)  
܋Ⴥ܄ — Ⴥଶғ25 \~ 150 ℃ ෸ᳵғ60 \~ 90 s ܋Ⴥෑሲғ1 \~ 3 ℃/s ᶼᅾ௤Ⴥ܄ — Ⴥଶғ150 \~ 200 ℃ ෸ᳵғ60 \~ 120 s ࢧၞᆄള܄ — Ⴥଶғ> 217 ℃ ෸ᳵғ60 \~ 90 sҔશ꧊Ⴥଶғ235 \~ 250 ℃ ෸ᳵғ30 \~ 70 s ܄ܩٯ — Ⴥଶғશ꧊Ⴥଶ \~ 180 ℃ ᴳჅෑሲ–1 \~ –5 ℃/s ᆄා — Ჟᱷᱞݳᰂ෫᱌ᆄා (SAC305)   
图 12: 回流焊温度曲线

# 9 相关文档和资源

# 相关文档

《ESP32 技术规格书》 – 提供 ESP32 芯片的硬件技术规格。《ESP32 技术参考手册》 – 提供 ESP32 芯片的存储器和外设的详细使用说明。《ESP32 硬件设计指南》 – 提供基于 ESP32 芯片的产品设计规范。《ESP32 勘误表及解决办法》 – 提供关于 ESP32 芯片的设计问题的说明和解决方案。  
• 证书http://espressif.com/zh-hans/support/documents/certificates  
• ESP32 产品/工艺变更通知 (PCN)http://espressif.com/zh-hans/support/documents/pcns  
• ESP32 公告 – 提供有关安全、bug、兼容性、器件可靠性的信息http://espressif.com/zh-hans/support/documents/advisories  
• 文档更新和订阅通知http://espressif.com/zh-hans/support/download/documents

# 开发者社区

• 《ESP32 ESP-IDF 编程指南》 – ESP-IDF 开发框架的文档中心。  
• ESP-IDF 及 GitHub 上的其它开发框架http://github.com/espressif  
• ESP32 论坛 – 工程师对工程师 (E2E) 的社区，您可以在这里提出问题、解决问题、分享知识、探索观点。http://esp32.com/  
• The ESP Journal – 分享乐鑫工程师的最佳实践、技术文章和工作随笔。http://blog.espressif.com/  
• SDK 和演示、App、工具、AT 等下载资源http://espressif.com/zh-hans/support/download/sdks-demos

# 产品

• ESP32 系列芯片 – ESP32 全系列芯片。http://espressif.com/zh-hans/products/socs?id=ESP32  
• ESP32 系列模组 – ESP32 全系列模组。http://espressif.com/zh-hans/products/modules?id=ESP32  
• ESP32 系列开发板 – ESP32 全系列开发板。http://espressif.com/zh-hans/products/devkits?id=ESP32  
• ESP Product Selector（乐鑫产品选型工具）– 通过筛选性能参数、进行产品对比快速定位您所需要的产品。http://products.espressif.com/#/product-selector?language=zh

# 联系我们

• 商务问题、技术支持、电路原理图 & PCB 设计审阅、购买样品（线上商店）、成为供应商、意见与建议http://espressif.com/zh-hans/contact-us/sales-questions

# 修订历史

<table><tr><td rowspan=1 colspan=1>日期</td><td rowspan=1 colspan=1>版本</td><td rowspan=1 colspan=1>发布说明</td></tr><tr><td rowspan=1 colspan=1>2021-11-08</td><td rowspan=1 colspan=1>v1.3</td><td rowspan=1 colspan=1>新增105°C版模组更新表4：绝对最大额定值更新表5：建议工作条件替换《乐鑫产品订购信息》为乐鑫产品选型工具更新章节1.1：特性中对TWAI的描述在图8：ESP32-WROOM-32UE模组尺寸下方新增一条说明更新图片格式升级文档格式</td></tr><tr><td rowspan=1 colspan=1>2021-02-09</td><td rowspan=1 colspan=1>v1.2</td><td rowspan=1 colspan=1>更新图9：ESP32-WROOM-32E推荐 PCB 封裝图、图10：ESP32-WROOM-32UE推荐 PCB封装图、图7:ESP32-WROOM-32E模组尺寸和图8：ESP32-WROOM-32UE 模组尺寸更新图12：回流焊温度曲线下方的说明更新 TWAITM为TWAI®</td></tr><tr><td rowspan=1 colspan=1>2020-11-02</td><td rowspan=1 colspan=1>v1.1</td><td rowspan=1 colspan=1>更新表7；在章节7.2 推荐PCB 封装图添加对 EPAD的说明；更新章节6 外围设计原理图中关于RC电路的说明。</td></tr><tr><td rowspan=1 colspan=1>2020-05-29</td><td rowspan=1 colspan=1>v1.0</td><td rowspan=1 colspan=1>正式发布</td></tr><tr><td rowspan=1 colspan=1>2020-05-18</td><td rowspan=1 colspan=1>v0.5</td><td rowspan=1 colspan=1>预发布</td></tr></table>

# 免责声明和版权公告

本文档中的信息，包括供参考的 URL 地址，如有变更，恕不另行通知。

本文档可能引用了第三方的信息，所有引用的信息均为“按现状”提供，乐鑫不对信息的准确性、真实性做任何保证。

乐鑫不对本文档的内容做任何保证，包括内容的适销性、是否适用于特定用途，也不提供任何其他乐鑫提案、规格书或样品在他处提到的任何保证。

乐鑫不对本文档是否侵犯第三方权利做任何保证，也不对使用本文档内信息导致的任何侵犯知识产权的行为负责。本文档在此未以禁止反言或其他方式授予任何知识产权许可，不管是明示许可还是暗示许可。

Wi-Fi 联盟成员标志归 Wi-Fi 联盟所有。蓝牙标志是 Bluetooth SIG 的注册商标。  
文档中提到的所有商标名称、商标和注册商标均属其各自所有者的财产，特此声明。  
版权归 © 2021 乐鑫信息科技（上海）股份有限公司。保留所有权利。