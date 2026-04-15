# ESP32­WROVER­E & ESP32­WROVER­IE

技术规格书

# 关于本文档

本文档为用户提供 ESP32-WROVER-E 和 ESP32-WROVER-IE 模组的技术规格。

# 文档版本

请至乐鑫官网 https://www.espressif.com/zh-hans/support/download/documents 下载最新版本文档。

# 修订历史

请至文档最后页查看修订历史。

# 文档变更通知

用户可以通过乐鑫官网订阅页面 www.espressif.com/zh-hans/subscribe 订阅技术文档变更的电子邮件通知。您需要更新订阅以接收有关新产品的文档通知。

# 证书下载

用户可以通过乐鑫官网证书下载页面 www.espressif.com/zh-hans/certificates 下载产品证书。

# 目录

1 概述

2 功能块图 3

3 管脚定义 4

3.3 Strapping 管脚 6

# 4 功能描述 8

# 4.2 外部 Flash 和 SRAM 8

4.4 RTC 和低功耗管理 8

# 5 外设接口和传感器 9

5.1 外设接口和传感器 9

6 电气特性 10

6.1 绝对最大额定值 10

6.2 建议工作条件 10

6.3 直流电气特性 (3.3 V, 25 °C) 10

6.4 Wi-Fi 射频 11

6.5 低功耗蓝牙射频 12

6.5.1 接收器 12

6.5.2 发射器

6.6 回流焊温度曲线 13

7 电路原理图 14

8 外围原理图 16

9 模组尺寸 17

10 PCB 封装图形 18

11 外部天线连接器尺寸 19

12 学习资源 20

12.2 必备资源 20

修订历史 21

表格

1 模组订购信息 1

2 模组产品规格 1

5

4 Strapping 管脚 6

5 绝对最大额定值 10

6 建议工作条件 10

7 直流电气特性 (3.3 V, 25 °C) 10

8 Wi-Fi 射频特性 11

9 低功耗蓝牙接收器特性 12

10 低功耗蓝牙发射器特性 12

# 插图

ESP32-WROVER-E 模组功能块图 3

2 ESP32-WROVER-IE 模组功能块图 3

3 管脚布局（顶视图） 4

4 回流焊温度曲线 13

5 ESP32-WROVER-E 电路原理图 14

6 ESP32-WROVER-IE 电路原理图 15

外围原理图 16

9 PCB 封装图形 18

10 外部天线连接器尺寸图 19

# 1 概述

ESP32-WROVER-E 和 ESP32-WROVER-IE 是两款通用型 Wi-Fi + Bluetooth + Bluetooth LE MCU 模组，功能强大，用途广泛，可以用于低功耗传感器网络和要求极高的任务，例如语音编码、音频流和 MP3 解码等。

ESP32-WROVER-E 采用 PCB 板载天线，ESP32-WROVER-IE 采用连接器连接外部天线。两款模组均配置了 4MB SPI flash 和 8 MB SPI PSRAM。本文档提供的信息适用于这两款模组。

模组的订购信息请见下表。

表 1: 模组订购信息  

<table><tr><td rowspan=1 colspan=1>模组</td><td rowspan=1 colspan=1>集成芯片</td><td rowspan=1 colspan=1>Flash</td><td rowspan=1 colspan=1>PSRAM</td><td rowspan=1 colspan=1>模组尺寸 (mm)</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROVER-E</td><td rowspan=2 colspan=1>ESP32-D0WD-V3</td><td rowspan=2 colspan=1>4MB1</td><td rowspan=2 colspan=1>8MB</td><td rowspan=2 colspan=1>18.0×31.4×3.3</td></tr><tr><td rowspan=1 colspan=1>ESP32-WROVER-IE</td></tr></table>

# 说明：

ESP32-WROVER-E 和 ESP32-WROVER-IE 采用的芯片是 ESP32 系列的 ESP32-D0WD-V3 \*。

ESP32-D0WD-V3 芯片具有可扩展、自适应的特点。两个 CPU 核可以被单独控制。CPU 时钟频率的调节范围为 80 MHz 到 240 MHz。用户可以关闭 CPU 的电源，利用低功耗协处理器监测外设的状态变化或某些模拟量是否超出阈值。ESP32 还集成了丰富的外设，包括电容式触摸传感器、霍尔传感器、SD 卡接口、以太网接口、高速 SPI、UART、I2S 和 I2C 等。

# 说明：

\* 关于 ESP32 系列芯片的产品型号说明请参照文档 《ESP32 技术规格书》模组集成了传统蓝牙、低功耗蓝牙和 Wi-Fi，具有广泛的用途：Wi-Fi 支持极大范围的通信连接，也支持通过路由器直接连接互联网；而蓝牙可以让用户连接手机或者广播 BLE Beacon 以便于信号检测。ESP32 芯片的睡眠电流小于 5 µA，使其适用于电池供电的可穿戴电子设备。模组支持的数据传输速率高达 150 Mbps，天线输出功率达到 20 dBm，可实现最大范围的无线通信。因此，这款模组具有行业领先的技术规格，在高集成度、无线传输距离、功耗以及网络联通等方面性能极佳。

ESP32 的操作系统是带有 LwIP 的 freeRTOS，还内置了带有硬件加速功能的 TLS 1.2。芯片同时支持 OTA 加密升级，方便用户在产品发布之后继续升级。

表 2 列出了模组的产品规格。

表 2: 模组产品规格  

<table><tr><td colspan="1" rowspan="1">类别</td><td colspan="1" rowspan="1">项目</td><td colspan="1" rowspan="1">产品规格</td></tr><tr><td colspan="1" rowspan="1">认证</td><td colspan="1" rowspan="1">RF认证</td><td colspan="1" rowspan="1">见ESP32-WROOM-32D 证书和ESP32-WROOM-32U证书</td></tr><tr><td colspan="1" rowspan="1">测试</td><td colspan="1" rowspan="1">可靠性</td><td colspan="1" rowspan="1">HTOL/HTSL/uHAST/TCT/ESD</td></tr><tr><td colspan="1" rowspan="3">Wi-Fi</td><td colspan="1" rowspan="2">协议</td><td colspan="1" rowspan="1">802.11 b/g/n (802.11n，速度高达 150 Mbps)</td></tr><tr><td colspan="1" rowspan="1">A-MPDU和A-MSDU 聚合，支持0.4μS保护间隔</td></tr><tr><td colspan="1" rowspan="1">工作中心频率范围</td><td colspan="1" rowspan="1">2412~2484 MHz</td></tr><tr><td colspan="1" rowspan="5">蓝牙</td><td colspan="1" rowspan="1">协议</td><td colspan="1" rowspan="1">符合蓝牙V4.2 BR/EDR和低功耗蓝牙标准</td></tr><tr><td colspan="1" rowspan="3">射频</td><td colspan="1" rowspan="1">具有-97 dBm 灵敏度的NZIF 接收器</td></tr><tr><td colspan="1" rowspan="1">Class-1, Class-2和 Class-3 发射器</td></tr><tr><td colspan="1" rowspan="1">AFH</td></tr><tr><td colspan="1" rowspan="1">音频</td><td colspan="1" rowspan="1">CVSD 和SBC音频</td></tr><tr><td colspan="1" rowspan="10">硬件</td><td colspan="1" rowspan="1">模组接口</td><td colspan="1" rowspan="1">SD 卡、UART、SPI、SDIO、I2C、LED PWM、电机 PWM、I2S、IR、脉冲计数器、GPIO、电容式触摸传感器、ADC、DAC、双线汽车接口(TWAI@)，兼容 ISO11898-1 协议 (CAN Specification 2.0)</td></tr><tr><td colspan="1" rowspan="1">片上传感器</td><td colspan="1" rowspan="1">霍尔传感器</td></tr><tr><td colspan="1" rowspan="1">集成晶振</td><td colspan="1" rowspan="1">40MHz晶振</td></tr><tr><td colspan="1" rowspan="1">集成SPI flash</td><td colspan="1" rowspan="1">4MB</td></tr><tr><td colspan="1" rowspan="1">集成PSRAM</td><td colspan="1" rowspan="1">8MB</td></tr><tr><td colspan="1" rowspan="1">工作电压/供电电压</td><td colspan="1" rowspan="1">3.0V~3.6 V</td></tr><tr><td colspan="1" rowspan="1">最小供电电流</td><td colspan="1" rowspan="1">500mA</td></tr><tr><td colspan="1" rowspan="1">建议工作温度范围</td><td colspan="1" rowspan="1">-40℃~85℃</td></tr><tr><td colspan="1" rowspan="1">封装尺寸</td><td colspan="1" rowspan="1">(18.00±0.15) mm × (31.40±0.15) mm × (3.30±0.15) mm</td></tr><tr><td colspan="1" rowspan="1">潮湿敏感度等级(MSL)</td><td colspan="1" rowspan="1">等级3</td></tr></table>

# 2 功能块图

![](images/f7ba6cbba35f7520955065c000b5ec8ab7ac7a92afc700aa7e54e1765a71129e.jpg)  
图 1: ESP32­WROVER­E 模组功能块图

![](images/5ab8f41f3822d237154a0ac098c1149ee882fd10d3e45dc5c513fc4ea63c20ae.jpg)  
图 2: ESP32­WROVER­IE 模组功能块图

# 3 管脚定义

# 3.1 管脚布局

![](images/2edd5f2a889ba701a9127c971db0f0a28c78bec7656cd8288ab73f4bcdf5f5bd.jpg)  
图 3: 管脚布局（顶视图）

# 3.2 管脚描述

模组共有 38 个管脚，具体描述参见表 3.

# 表 3: 管脚定义

<table><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">类型</td><td colspan="1" rowspan="1">功能</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">接地</td></tr><tr><td colspan="1" rowspan="1">3V3</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">供电</td></tr><tr><td colspan="1" rowspan="1">EN</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">使能模组，高电平有效。</td></tr><tr><td colspan="1" rowspan="1">SENSOR_VP</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">I</td><td colspan="1" rowspan="1">GPIO36, ADC1_CH0, RTC_GPIO0</td></tr><tr><td colspan="1" rowspan="1">SENSOR_VN</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">|</td><td colspan="1" rowspan="1">GPIO39, ADC1_CH3, RTC_GPIO3</td></tr><tr><td colspan="1" rowspan="1">1034</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GPIO34, ADC1_CH6, RTC_GPIO4</td></tr><tr><td colspan="1" rowspan="1">1035</td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">GPIO35, ADC1_CH7, RTC_GPIO5</td></tr><tr><td colspan="1" rowspan="1">1032</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO32，XTAL_32K_P (32.768 kHz 晶振输入)，ADC1_CH4，TOUCH9,RTC_GPIO9</td></tr><tr><td colspan="1" rowspan="1">1033</td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO33，XTAL_32K_N (32.768 kHz 晶振输出)，ADC1_CH5，TOUCH8,RTC_GPIO8</td></tr><tr><td colspan="1" rowspan="1">1025</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO25, DAC_1, ADC2_CH8, RTC_GPIO6, EMAC_RXD0</td></tr><tr><td colspan="1" rowspan="1">1026</td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO26, DAC_2, ADC2_CH9, RTC_GPIO7, EMAC_RXD1</td></tr><tr><td colspan="1" rowspan="1">1027</td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO27, ADC2_CH7, TOUCH7, RTC_GPIO17, EMAC_RX_DV</td></tr><tr><td colspan="1" rowspan="1">1014</td><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO14,ADC2_CH6， TOUCH6， RTC_GPIO16， MTMS， HSPICLK,HS2_CLK, SD_CLK, EMAC_TXD2</td></tr><tr><td colspan="1" rowspan="1">1012</td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO12, ADC2_CH5, TOUCH5, RTC_GPIO15, MTDI,HSPIQ,HS2_DATA2, SD_DATA2, EMAC_TXD3</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">接地</td></tr><tr><td colspan="1" rowspan="1">1013</td><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO13,ADC2_CH4,TOUCH4,RTC_GPIO14, MTCK,HSPID,HS2_DATA3, SD_DATA3, EMAC_RX_ER</td></tr><tr><td colspan="1" rowspan="1">SHD/SD2*</td><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO9, SD_DATA2, SPIHD, HS1_DATA2, U1RXD</td></tr><tr><td colspan="1" rowspan="1">SWP/SD3*</td><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO10, SD_DATA3, SPIWP, HS1_DATA3, U1TXD</td></tr><tr><td colspan="1" rowspan="1">SCS/CMD*</td><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO11, SD_CMD, SPICS0, HS1_CMD, U1RTS</td></tr><tr><td colspan="1" rowspan="1">SCK/CLK*</td><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO6, SD_CLK, SPICLK, HS1_CLK, U1CTS</td></tr><tr><td colspan="1" rowspan="1">SDO/SDO*</td><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO7, SD_DATAO, SPIQ, HS1_DATAO, U2RTS</td></tr><tr><td colspan="1" rowspan="1">SDI/SD1*</td><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO8, SD_DATA1, SPID, HS1_DATA1, U2CTS</td></tr><tr><td colspan="1" rowspan="1">1015</td><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">Vo</td><td colspan="1" rowspan="1">GPIO15, ADC2_CH3, TOUCH3, MTDO, HSPICS0, RTC_GPIO13,HS2_CMD, SD_CMD, EMAC_RXD3</td></tr><tr><td colspan="1" rowspan="1">102</td><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO2, ADC2_CH2, TOUCH2, RTC_GPIO12, HSPIWP, HS2_DATAO,SD_DATAO</td></tr><tr><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIOO,  ADC2_CH1,  TOUCH1,  RTC_GPIO11,  CLK_OUT1,EMAC_TX_CLK</td></tr><tr><td colspan="1" rowspan="1">104</td><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO4， ADC2_CHO, TOUCHO, RTC_GPIO10, HSPIHD, HS2_DATA1,SD_DATA1, EMAC_TX_ER</td></tr><tr><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">-</td><td></td></tr><tr><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1">-</td><td></td></tr><tr><td colspan="1" rowspan="1">105</td><td colspan="1" rowspan="1">29</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO5, VSPICS0, HS1_DATA6, EMAC_RX_CLK</td></tr><tr><td colspan="1" rowspan="1">1018</td><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO18, VSPICLK, HS1_DATA7</td></tr><tr><td colspan="1" rowspan="1">1019</td><td colspan="1" rowspan="1">31</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO19, VSPIQ, U0CTS, EMAC_TXD0</td></tr><tr><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">1021</td><td colspan="1" rowspan="1">33</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO21, VSPIHD, EMAC_TX_EN</td></tr><tr><td colspan="1" rowspan="1">RXDO</td><td colspan="1" rowspan="1">34</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO3, UORXD, CLK_OUT2</td></tr><tr><td colspan="1" rowspan="1">TXDO</td><td colspan="1" rowspan="1">35</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO1, U0TXD, CLK_OUT3, EMAC_RXD2</td></tr><tr><td colspan="1" rowspan="1">1022</td><td colspan="1" rowspan="1">36</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO22, VSPIWP, U0RTS, EMAC_TXD1</td></tr><tr><td colspan="1" rowspan="1">1023</td><td colspan="1" rowspan="1">37</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO23, VSPID, HS1_STROBE</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">接地</td></tr></table>

# 注意：

\* ESP32-D0WD-V3 芯片上的 GPIO6 至 GPIO11 用于连接模组上集成的 SPI flash，不再拉出至模组管脚。

# 3.3 Strapping 管脚

ESP32 共有 5 个 Strapping 管脚，可参考章节 7 电路原理图：

• MTDI • GPIO0 • GPIO2 • MTDO • GPIO5

软件可以读取寄存器“GPIO_STRAPPING”中这 5 个管脚 strapping 的值。

在芯片的系统复位（上电复位、RTC 看门狗复位、欠压复位）放开的过程中，Strapping 管脚对电平采样并存储到锁存器中，锁存为“0”或“1”，并一直保持到芯片掉电或关闭。

每一个 Strapping 管脚都会连接内部上拉/下拉。如果一个 Strapping 管脚没有外部连接或者连接的外部线路处于高阻抗状态，内部弱上拉/下拉将决定 Strapping 管脚输入电平的默认值。

为改变 Strapping 的值，用户可以应用外部下拉/上拉电阻，或者应用主机 MCU 的 GPIO 控制 ESP32 上电复位放开时的 Strapping 管脚电平。

复位放开后，Strapping 管脚和普通管脚功能相同。

配置 Strapping 管脚的详细启动模式请参阅表 4 。

表 4: Strapping 管脚  

<table><tr><td rowspan=1 colspan=4>内置 LDO (VDD_SDIO)电压</td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=1>3.3V</td><td rowspan=1 colspan=1>1.8V</td></tr><tr><td rowspan=1 colspan=1>MTDI</td><td rowspan=1 colspan=1>下拉</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=3>系统启动模式</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=1>SPI启动模式</td><td rowspan=1 colspan=1>下载启动模式</td></tr><tr><td rowspan=1 colspan=1>GPIO0</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>GPIO2</td><td rowspan=1 colspan=1>下拉</td><td rowspan=1 colspan=1>无关项</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=3>系统启动过程中，控制 UOTXD 打印</td></tr><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=1>UOTXD 正常打印</td><td rowspan=1 colspan=1>UOTXD上电不打印</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=4>SDIO 从机信号输入输出时序</td></tr></table>

<table><tr><td rowspan=1 colspan=1>管脚</td><td rowspan=1 colspan=1>默认</td><td rowspan=1 colspan=1>下降沿采样下降沿输出</td><td rowspan=1 colspan=1>下降沿采样上升沿输出</td><td rowspan=1 colspan=1>上升沿采样下降沿输出</td><td rowspan=1 colspan=1>上升沿采样上升沿输出</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>GPIO5</td><td rowspan=1 colspan=1>上拉</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td></tr></table>

# 说明：

• 固件可以通过配置一些寄存器比特位，在启动后改变“内置 LDO (VDD_SDIO) 电压”和“SDIO 从机信号输入输出时序”的设定。

• 由于模组的 flash 及 SRAM 的工作电压仅支持 3.3 V（VDD_SDIO 输出），所以模组内部 MTDI 的上拉电阻 R9 默认不上件。

# 4 功能描述

本章描述了 ESP32-WROVER-E 和 ESP32-WROVER-IE 的各个模块和功能。

# 4.1 CPU 和内存

ESP32-D0WD-V3 内置两个低功耗 Xtensa® 32-bit LX6 MCU。片上存储包括：

• 448 KB 的 ROM，用于程序启动和内核功能调用  
• 用于数据和指令存储的 520 KB 片上 SRAM  
• RTC 快速存储器，为 8 KB 的 SRAM，可以在 Deep-sleep 模式下 RTC 启动时用于数据存储以及被主CPU 访问  
• RTC 慢速存储器，为 8 KB 的 SRAM，可以在 Deep-sleep 模式下被协处理器访问  
• 1 Kbit 的 eFuse，其中 256 bit 为系统专用（MAC 地址和芯片设置）; 其余 768 bit 保留给用户程序, 这些程序包括 flash 加密和芯片 ID

# 4.2 外部 Flash 和 SRAM

ESP32 支持多个外部 QSPI flash 和静态随机存储器 (SRAM)。详情可参考《ESP32 技术参考手册》 中的 SPI 章节。ESP32 还支持基于 AES 的硬件加解密功能，从而保护开发者 flash 中的程序和数据。

ESP32 可通过高速缓存访问外部 QSPI flash 和 SRAM：

• 外部 flash 可以同时映射到 CPU 指令和只读数据空间。

– 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB，则 cache 性能可能由于 CPU 的推测性读取而降低。– 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。

• 外部 SRAM 可映射到 CPU 数据空间。一次最多可映射 4 MB。支持 8-bit、16-bit 和 32-bit 访问。

ESP32-WROVER-E 和 ESP32-WROVER-IE 集成了 4 MB SPI flash 和 8 MB PSRAM。

# 4.3 晶振

模组使用 40 MHz 晶振。

# 4.4 RTC 和低功耗管理

ESP32 采用了先进的电源管理技术，可以在不同的功耗模式之间切换。

关于 ESP32 在不同的功耗模式下的电流消耗，详见《ESP32 技术规格书》中章节“RTC 和低功耗管理”。

# 5 外设接口和传感器

# 5.1 外设接口和传感器

详见《ESP32 技术规格书》中外设接口和传感器章节。

# 说明：

GPIO6-11 已用于连接模组上集成的 SPI flash，GPIO16-17 已用于连接模组上集成的 PSRAM，其它外设可以使用其它任一 GPIO，详见章节 7 原理图。

# 6 电气特性

# 6.1 绝对最大额定值

超出绝对最大额定值表可能导致器件永久性损坏。这只是强调的额定值，不涉及器件在这些或其它条件下超出本技术规格指标的功能性操作。建议工作条件请参考表 6。

表 5: 绝对最大额定值  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=1>供电电压</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>loutput1</td><td rowspan=1 colspan=1>IO 输出总电流</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1,100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Tstore</td><td rowspan=1 colspan=1>存储温度</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>℃</td></tr></table>

1. 模组的 IO 输出总电流的测试条件为 25 °C 环境温度，VDD3P3_RTC, VDD3P3_CPU, VDD_SDIO 三个电源域的管脚输出高电平且直接接地。此时模组在保持工作状态 24 小时后，仍能正常工作。其中 VDD_SDIO 电源域的管脚不包括连接 flash 和/或 PSRAM 的管脚。

2. 关于电源域请参考《ESP32 技术规格书》 附录中表 IO_MUX。

# 6.2 建议工作条件

表 6: 建议工作条件  

<table><tr><td rowspan=1 colspan=1>符号</td><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=1>供电电压</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IVDD</td><td rowspan=1 colspan=1>外部电源的供电电流</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>工作温度</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>C</td></tr></table>

# 6.3 直流电气特性 (3.3 V, 25 °C)

表 7: 直流电气特性 (3.3 V, 25 °C)  

<table><tr><td colspan="1" rowspan="1">符号</td><td colspan="2" rowspan="1">参数</td><td colspan="1" rowspan="1">最小值</td><td colspan="1" rowspan="1">典型值</td><td colspan="1" rowspan="1">最大值</td><td colspan="1" rowspan="1">单位</td></tr><tr><td colspan="1" rowspan="1">CIN</td><td colspan="2" rowspan="1">管脚电容</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">pF</td></tr><tr><td colspan="1" rowspan="1">VIH</td><td colspan="2" rowspan="1">高电平输入电压</td><td colspan="1" rowspan="1">0.75×VDD1</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">VDD1+0.3</td><td colspan="1" rowspan="1">V</td></tr><tr><td colspan="1" rowspan="1">VIL</td><td colspan="2" rowspan="1">低电平输入电压</td><td colspan="1" rowspan="1">-0.3</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">0.25×VDD1</td><td colspan="1" rowspan="1">V</td></tr><tr><td colspan="1" rowspan="1">IH</td><td colspan="2" rowspan="1">高电平输入电流</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">50</td><td colspan="1" rowspan="1">nA</td></tr><tr><td colspan="1" rowspan="1">|</td><td colspan="2" rowspan="1">低电平输入电流</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">50</td><td colspan="1" rowspan="1">nA</td></tr><tr><td colspan="1" rowspan="1">VOH</td><td colspan="2" rowspan="1">高电平输出电压</td><td colspan="1" rowspan="1">0.8×VDD1</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">V</td></tr><tr><td colspan="1" rowspan="1">VOL</td><td colspan="2" rowspan="1">低电平输出电压</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">0.1×VDD1</td><td colspan="1" rowspan="1">V</td></tr><tr><td colspan="1" rowspan="1">符号</td><td colspan="2" rowspan="1">参数</td><td colspan="1" rowspan="1">最小值</td><td colspan="1" rowspan="1">典型值</td><td colspan="1" rowspan="1">最大值</td><td colspan="1" rowspan="1">单位</td></tr><tr><td colspan="1" rowspan="3">loH</td><td colspan="1" rowspan="3">高电平拉电流NDD1 = 3.3 V,VOH &gt;= 2.64 V,管脚输出强度设为最大值)</td><td colspan="1" rowspan="1">VDD3P3_CPU电源域1，2</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">40</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">mA</td></tr><tr><td colspan="1" rowspan="1">VDD3P3_RTC电源域1，2</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">40</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">mA</td></tr><tr><td colspan="1" rowspan="1">VDD_SDIO电源域1,3</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">mA</td></tr><tr><td colspan="1" rowspan="1">lOL</td><td colspan="2" rowspan="1">低电平灌电流WDD1 = 3.3 V, VoL = 0.495 V,管脚输出强度设为最大值)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">mA</td></tr><tr><td colspan="1" rowspan="1">RpU</td><td colspan="2" rowspan="1">上拉电阻</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">45</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">kΩ2</td></tr><tr><td colspan="1" rowspan="1">RPD</td><td colspan="2" rowspan="1">下拉电阻</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">45</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">kΩ</td></tr><tr><td colspan="1" rowspan="1">VIL_nRST</td><td colspan="2" rowspan="1">CHIP_PU 关闭芯片的低电平输入电压</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">0.6</td><td colspan="1" rowspan="1">V</td></tr></table>

# 说明：

1. VDD 是 I/O 的供电电源。关于电源域请参考《ESP32 技术规格书》 附录中表 IO_MUX。  
2. VDD3P3_CPU 和 VDD3P3_RTC 电源域管脚的单个管脚的拉电流随管脚数量增加而减小，从约 40 mA 减小到约 29mA。  
3. VDD_SDIO 电源域的管脚不包括连接 flash 和/或 PSRAM 的管脚。

# 6.4 Wi­Fi 射频

表 8: Wi­Fi 射频特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>工作中心频率范围1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2412</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2484</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>输出阻抗²</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>见说明2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=2 colspan=1>输出功率3</td><td rowspan=1 colspan=1>11n, MCS7</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11b模式</td><td rowspan=1 colspan=1>18.5</td><td rowspan=1 colspan=1>19.5</td><td rowspan=1 colspan=1>20.5</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=8 colspan=1>灵敏度</td><td rowspan=1 colspan=1>11b, 1 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-97</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11b, 11 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-88</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-92</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-75</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-92</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-72</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-89</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-69</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=4 colspan=1>邻道抑制</td><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr></table>

1. 工作中心频率范围应符合国家或地区的规范标准。软件可以配置工作频率范围。2. 使用外部天线的模组输出阻抗为 50 Ω，不使用外部天线的模组可无需关注输出阻抗。3. 根据产品或认证的要求，用户可以配置目标功率。

# 6.5 低功耗蓝牙射频

# 6.5.1 接收器

表 9: 低功耗蓝牙接收器特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>灵敏度 @30.8% PER</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-94</td><td rowspan=1 colspan=1>-93</td><td rowspan=1 colspan=1>-92</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>最大接收信号 @30.8% PER</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>共信道抑制比C/I</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>+10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>邻道抑制比C/</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 −1 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-35</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = F0 -3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-45</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=4 colspan=1>带外阻塞</td><td rowspan=1 colspan=1>30MHz~2000 MHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2000 MHz~2400 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2500MHz~3000 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>3000 MHz~12.5 GHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>互调</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-36</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr></table>

# 6.5.2 发射器

表 10: 低功耗蓝牙发射器特性  

<table><tr><td rowspan=1 colspan=1>参数</td><td rowspan=1 colspan=1>条件</td><td rowspan=1 colspan=1>最小值</td><td rowspan=1 colspan=1>典型值</td><td rowspan=1 colspan=1>最大值</td><td rowspan=1 colspan=1>单位</td></tr><tr><td rowspan=1 colspan=1>射频发射功率</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>增益控制步长</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>射频功率控制范围</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-12</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>+9</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=3 colspan=1>邻道发射功率</td><td rowspan=1 colspan=1>F = F0 ± 2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-52</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = F0 ± 3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-58</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = F0 ± &gt;3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-60</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>∆ f 1avg</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>265</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2max</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>247</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f 2avg/∆ f1avg</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>+0.92</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>ICFT</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>漂移速率</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>KHz/50S</td></tr><tr><td rowspan=1 colspan=1>偏移</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr></table>

# 6.6 回流焊温度曲线

![](images/28eeecd2ec91036345e3ae892c62431c81c1b4c2c5ed5e16397a40d2a1b9a8ac.jpg)  
܋Ⴥ܄ — Ⴥଶғ25 \~ 150 ℃ ෸ᳵғ60 \~ 90 s ܋Ⴥෑሲғ1 \~ 3 ℃/s ᶼᅾ௤Ⴥ܄ — Ⴥଶғ150 \~ 200 ℃ ෸ᳵғ60 \~ 120 s ࢧၞᆄള܄ — Ⴥଶғ>217 ℃ ෸ᳵғ60 \~ 90 sҔશ꧊Ⴥଶғ235 \~ 250 ℃ ෸ᳵғ30 \~ 70 s ܄ܩٯ — Ⴥଶғશ꧊Ⴥଶ \~ 180 ℃ ᴳჅෑሲ–1 \~ –5 ℃/s ᆄා — Ჟᱷᱞݳᰂ෫᱌ᆄා (SAC305)   
图 4: 回流焊温度曲线

# 说明：

建议模组只过一次回流焊。

# 电路原理图

模组内部元件的电路图 。

![](images/77a260d72fc69978be837254e772048cb2d328ed7807766396e6c07b382b9ff0.jpg)  
5: ESP32­WROVER­E 电路原理图

![](images/f6657e3c5be783be00cc88feb442c5ce407c6c4b502efc2e3623fd9fc7f0c565.jpg)  
6: ESP32­WROVER­I E 电路原理图

# 8 外围原理图

模组与外围器件（如电源、天线、复位按钮、JTAG 接口、UART 接口等）连接的应用电路图。

![](images/4e92d14be027e037b22593115132a77e0e58fc532cbac12172e16aff0ae2d970.jpg)  
图 7: 外围原理图

# 说明：

• 管脚 39 可以不焊接到底板。若用户将该管脚焊接到底板，请确保使用适量的焊锡膏。

• 为确保芯片上电时的供电正常，EN 管脚处需要增加 RC 延迟电路。RC 通常建议为 R = 10 kΩ，C = 1 µF，但具体数值仍需根据模组电源的上电时序和芯片的上电复位时序进行调整。芯片的上电复位时序图可参考《ESP32技术规格书》中的电源管理章节。

![](images/dff5046cebca6c6e077fa3482c056deccb4c43a67efa21bf96984344a7eaf7dd.jpg)  
8: 模组尺寸图

# 10 PCB 封装图形

![](images/9af35e76af28232c64127264a2708838b997daf0563f2f1a8b5a2dbd8f01f5a8.jpg)  
图 9: PCB 封装图形

# 11 外部天线连接器尺寸

![](images/ad986f80ee54a7dd33e60b7749c489d191cb4bc2ccbd6adb9721e4181b02e483.jpg)  
图 10: 外部天线连接器尺寸图

<table><tr><td rowspan=1 colspan=1>③</td><td rowspan=1 colspan=1>SHELL</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>COPPERALLOY/AuPLATEDOVER Ni</td></tr><tr><td rowspan=1 colspan=1>②</td><td rowspan=1 colspan=1>CONTACT</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>COPPERALLOY/AuPLATEDOVER Ni</td></tr><tr><td rowspan=1 colspan=1>①</td><td rowspan=1 colspan=1>HOUSING</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>HIGHTTEMP. PLASTICUL94V-0/WHITE</td></tr><tr><td rowspan=1 colspan=1>ITEM</td><td rowspan=1 colspan=1>PARTNAME</td><td rowspan=1 colspan=1>Q&#x27;TY</td><td rowspan=1 colspan=1>MATERIAL/FINISH</td></tr></table>

# 12 学习资源

# 12.1 必读资料

访问以下链接可下载有关 ESP32 的文档资料。

《ESP32 技术规格书》本文档为用户提供 ESP32 硬件技术规格简介，包括概述、管脚定义、功能描述、外设接口、电气特性等。

《ESP32 ECO V3 使用指南》本文介绍 ESP32 ECO V3 较之前硅片的主要变化。

《ESP32 勘误表及解决办法》本文收录了 ESP32 芯片的硬件问题并给出解决方法。

《ESP-IDF 编程指南》ESP32 相关开发文档的汇总平台，包含硬件手册，软件 API 介绍等。

# 《ESP32 技术参考手册》

该手册提供了关于 ESP32 的具体信息，包括各个功能模块的内部架构、功能描述和寄存器配置等。

# • ESP32 硬件资源

压缩包提供了 ESP32 模组和开发板的硬件原理图，PCB 布局图，制造规范和物料清单。

《ESP32 硬件设计指南》该手册提供了 ESP32 系列产品的硬件信息，包括 ESP32 芯片，ESP32 模组以及开发板。

# 《ESP32 AT 指令集与使用示例》

该文档描述 ESP32 AT 指令集功能以及使用方法，并介绍几种常见的 AT 指令使用示例。其中 AT 指令包括基础 AT 指令，Wi-Fi 功能 AT 指令，TCP/IP 相关 AT 指令等；使用示例包括单连接 TCP 客户端，UDP传输，透传，多连接 TCP 服务器等。

# • 乐鑫产品选型工具

# 12.2 必备资源

以下为有关 ESP32 的必备资源。

# • ESP32 在线社区

工程师对工程师 (E2E) 的社区，用户可以在这里提出问题，分享知识，探索观点，并与其他工程师一起解决问题。

• ESP32 GitHub乐鑫在 GitHub 上有众多开源的开发项目。

• ESP32 工具ESP32 flash 下载工具以及《ESP32 认证测试指南》。

• ESP-IDFESP32 所有版本 IDF。

# • ESP32 资源合集

ESP32 相关的所有文档和工具资源。

# 修订历史

<table><tr><td rowspan=1 colspan=1>日期</td><td rowspan=1 colspan=1>版本</td><td rowspan=1 colspan=1>发布说明</td></tr><tr><td rowspan=1 colspan=1>2022-02-22</td><td rowspan=1 colspan=1>v1.5</td><td rowspan=1 colspan=1>替换《乐鑫产品订购信息》为乐鑫产品选型工具更新表2中对TWAI的描述在表2中新增RF认证证书链接更新表1更新表5</td></tr><tr><td rowspan=1 colspan=1>2021-02-07</td><td rowspan=1 colspan=1>V1.4</td><td rowspan=1 colspan=1>更新图8：模组尺寸图更新图9：PCB封装图形</td></tr><tr><td rowspan=1 colspan=1>2021-02-02</td><td rowspan=1 colspan=1>V1.3</td><td rowspan=1 colspan=1>更新 TWAITM为TWAI®删除章节8：外围原理图中的VDD33放电电路图和复位电路图更新图4：回流焊温度曲线下方的说明</td></tr><tr><td rowspan=1 colspan=1>2020-11-02</td><td rowspan=1 colspan=1>V1.2</td><td rowspan=1 colspan=1>更新图3：管脚布局（顶视图）在章节10：PCB封装图形添加关于EPAD的说明更新章节8：外围原理图中关于RC延迟电路的说明</td></tr><tr><td rowspan=1 colspan=1>2020-06-11</td><td rowspan=1 colspan=1>V1.1</td><td rowspan=1 colspan=1>更新以下内容：●图1：ESP32-WROVER-E模组功能块图⚫ 图2：ESP32-WROVER-E模组功能块图</td></tr><tr><td rowspan=1 colspan=1>2020-05-22</td><td rowspan=1 colspan=1>V1.0</td><td rowspan=1 colspan=1>正式发布</td></tr></table>

# 免责声明和版权公告

本文档中的信息，包括供参考的 URL 地址，如有变更，恕不另行通知。

本文档可能引用了第三方的信息，所有引用的信息均为“按现状”提供，乐鑫不对信息的准确性、真实性做任何保证。

乐鑫不对本文档的内容做任何保证，包括内容的适销性、是否适用于特定用途，也不提供任何其他乐鑫提案、规格书或样品在他处提到的任何保证。

乐鑫不对本文档是否侵犯第三方权利做任何保证，也不对使用本文档内信息导致的任何侵犯知识产权的行为负责。本文档在此未以禁止反言或其他方式授予任何知识产权许可，不管是明示许可还是暗示许可。

Wi-Fi 联盟成员标志归 Wi-Fi 联盟所有。蓝牙标志是 Bluetooth SIG 的注册商标。

文档中提到的所有商标名称、商标和注册商标均属其各自所有者的财产，特此声明。

版权归 © 2022 乐鑫信息科技（上海）股份有限公司。保留所有权利。