# 1.54inch OLED SSD1309 SPI&lIC ModuleMSP154W&MSP154B用户手册

# OLED 简介

OLED 即有机发光二级管（Organic Light-Emitting Diode，OLED)。OLED显示技术具有自发光、广视角、几乎无穷高的对比度、较低耗电、极高反应速度、可用于挠曲性面板、使用温度范围广、构造及制程较简单等优点，被认为是下一代的平面显示器新兴应用技术。

OLED显示和传统的LCD显示不同，其可以自发光，所以不需要背光灯，这使得 OLED显示屏相对于LCD显示屏尺寸更薄，同时显示效果更优。

# 产品概述

该款 OLED 模块显示尺寸为1.54 寸，拥有 128x64 分辨率。可以选择3 线制、4 线制SPI以及 IIC 三种通信方式，驱动 IC 为 SSD1309。包含显示黑色、蓝色或者黄蓝双色三款模块。

# 立品特点

• 1.54寸OLED 屏，支持黑白、黑蓝显示

• 128x64 分辨率，显示效果清晰，对比度高

超大可视角度:大于 160°(显示屏中可视角度最大的一种屏幕)

• 宽电压供电（3V\~5V），兼容 3.3V和 5V逻辑电平，无需电平转换芯片

默认4线制SPI总线，可以选择IIC总线

• 超低功耗：正常显示仅为0.06W（远低于TFT显示屏）

军工级工艺标准,长期稳定工作

提供丰富的 STM32、C51、Arduino、Raspberry Pi 以及 MSP430 平台示例程序

提供底层驱动技术支持

# 产品参数

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>显示颜色</td><td rowspan=1 colspan=1>白色、蓝色</td></tr><tr><td rowspan=1 colspan=1>SKU</td><td rowspan=1 colspan=1>MSP154W-MSP154B</td></tr><tr><td rowspan=1 colspan=1>尺寸</td><td rowspan=1 colspan=1>1.54(inch)</td></tr><tr><td rowspan=1 colspan=1>类型</td><td rowspan=1 colspan=1>OLED</td></tr><tr><td rowspan=1 colspan=1>驱动芯片</td><td rowspan=1 colspan=1>SSD1309</td></tr><tr><td rowspan=1 colspan=1>分辨率</td><td rowspan=1 colspan=1>128*64(Pixel)</td></tr><tr><td rowspan=1 colspan=1>模块接口</td><td rowspan=1 colspan=1>4-line SPI、IIC interface</td></tr><tr><td rowspan=1 colspan=1>有效显示区域</td><td rowspan=1 colspan=1>35.052x17.516(mm)</td></tr><tr><td rowspan=1 colspan=1>触摸屏类型</td><td rowspan=1 colspan=1>无触摸屏</td></tr><tr><td rowspan=1 colspan=1>触摸IC</td><td rowspan=1 colspan=1>无触摸IC</td></tr><tr><td rowspan=1 colspan=1>模块尺寸</td><td rowspan=1 colspan=1>42.40x38.00(mm)</td></tr><tr><td rowspan=1 colspan=1>视角</td><td rowspan=1 colspan=1>&gt;160°</td></tr><tr><td rowspan=1 colspan=1>工作温度</td><td rowspan=1 colspan=1>-20℃~60℃</td></tr><tr><td rowspan=1 colspan=1>存储温度</td><td rowspan=1 colspan=1>-30℃~70℃</td></tr><tr><td rowspan=1 colspan=1>工作电压</td><td rowspan=1 colspan=1>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>功耗</td><td rowspan=1 colspan=1>待定</td></tr><tr><td rowspan=1 colspan=1>产品重量（含包装)</td><td rowspan=1 colspan=1>12(g)</td></tr></table>

# 接口说明

![](images/5eca7f0bff2f3c5a1b51eb7cb04907688c40f4d10ed6e2cf9b7c5ba1ad4aa998.jpg)  
图1.模块引脚丝印图

![](images/d8dcea59c033d52a342d284f497f63505f33d6edd096b211872ac6a1d6ca284a.jpg)  
图2.模块背面图

# 注意：

1、本模块支持IIC和4线制SPI接口总线模式切换（如图2红框内所示），具体说明如下：

A、 使用4.7K电阻只焊接R5电阻，则选择4线制SPI总线接口（默认）；

B、使用4.7K电阻只焊接R4、R9电阻，则选择IIC总线接口；

2、接口总线模式切换后，需要选择相应配套的软件和相应的接线引脚（如图1所示），模块才能正常运行。相应的接线引脚说明如下：

A、选择4线制SPI总线接口，所有的引脚都需要使用；  
B、选择ⅡIC总线接口，只需要使用GND、VCC、SCL、SDA、RES这五个引脚，将CS引脚接电源地，DC引脚可以用来选择IIC从设备地址，接高电平选择0x7A，接低电平选择0x78；

3、焊接R8电阻（如图2绿框内所示），则CS引脚不需要接。

# 重要说明：

1．以下引脚序号1\~7是指我司带PCB底板的模块引脚编号，如果您购买的是裸屏，请参考裸屏规格书的引脚定义，按照信号类型来参考接线而不是直接根据下面的模块引腳编号来接线，举例：CS在我们模块上是7脚，可能在不同尺寸裸屏上是x脚，以下接线说明是告诉您，CS这个信号是接到的单片机的A5引脚上的。

2．关于VCC供电电压：该OLED显示模块可以接3.3V或者5V。

<table><tr><td rowspan=1 colspan=1>标号</td><td rowspan=1 colspan=1>模块引脚</td><td rowspan=1 colspan=1>引脚说明</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>OLED电源地</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>OLED电源正(3.3V~5V)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>OLED SPI和IIC总线时钟信号</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>OLED SPI和IIC总线数据信号</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=1>OLED复位信号，低电平复位（选择IIC总线时，该引脚需要接高电平（可以接VCC））</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>选择SPI总线，作为命令/数据输入选择信号，高电平：数据，低电平：命令；选择IIC总线时，该引脚可以用来选择IIC从设备地址，接高电平选择0x7A，接低电平选择0x78;</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>OLED片选信号，低电平使能；焊接R8电阻（如图2绿框内所示），则该引脚不需要接。不焊接R8电阻，选择IIC接口，则该引脚接地</td></tr></table>

# 硬件配置

该模块硬件电路由4 部分组成：OLED 显示控制电路、OLED 升压电路、排针接口、电源稳压电路。

OLED 显示控制电路主要用于控制 OLED显示，包括片选、复位以及数据、命令传输控制，接口选择。

OLED升压电路用于将输入电压升压为OLED发光电压。

排针接口用于外接主控开发板。

电源稳压电路用于3.3V稳压供电。

该 OLED 模块默认采用 4 线制 SPI 通信方式，另外还可以选择 IIC 通信方式，硬件配置7个引脚，不同的通信方式，选择的引脚不一样（具体见接口说明部分）。

# 工作原理

# 1、SSD1309控制器简介

SSD1309 为一款 0LED/PLED 控制器，支持的最大分辨率为128\*64，拥有一个 1024 字节大小的 GRAM。支持8位6800和 8位8080并口数据总线，还支持3线制和4线制SPI串口总线以及 I2C 总线。由于并行控制需要大量的 IO 口，所以最常用的还是SPI 串口总线和 I2C总线。其支持垂直滚动显示，可用于小型便携式设备，如手机、MP3 播放器等。

SSD1309 控制器使用1bit 来控制一个像素点显示，所以每个像素点只能显示黑白双色。其显示的 RAM总共分为8页，每页有 8 行，每行128 个像素点。设置像素点数据时，需要先指定页地址，再分别指定列低地址和列高地址，所以每次同时设置垂直方向的 8 个像素点。为了能够灵活控制任意位置的像素点，软件上先设置一个和显示 RAM一样大小的全局一维数组，先将像素点数据设置到全局数组中，此过程采用或、与操作保证之前写入全局数组的数据不受破坏，然后将全局数组的数据写入到显示 RAM 中，这样就可以通过 OLED 显示出来了。

# 2、SPI通信协议简介

4线制SPI总线写模式时序如下图所示：

![](images/31e50f285f3134cddd7f7fc3d6ac9c6293005df62ad516dca741b8f9464754f5.jpg)

4线制的D/C#信号直接由D/C#输入。

CS#为从机片选信号，仅当 CS#为低电平时，芯片才会被使能。

D/C#为芯片的数据/命令控制信号，当 DC#为低电平时写命令，为高电平时写数据。

SCLK为SPI总线时钟信号，每个上升沿传输1bit数据；

SDIN 为 SPI 总线写数据信号，按照高位在前，先传输的方式，一次传输 8bit 数据，数据对于SPI通信而言，数据有传输时序，即时钟相位（CPHA）与时钟极性(CPOL)的组合：CPOL 的高低决定串行同步时钟的空闲状态电平，CPOL = 0，为低电平。CPOL 对传输协

议没有很多的影响；

CPHA 的高低决定串行同步时钟是在第一时钟跳变沿还是第二个时钟跳变沿数据被采集，当CPHL=0，在第一个跳变沿进行数据采集；这两者组合就成为四种 SPI通信方式，国内通常使用 SPIO,即 CPHL = 0，CPOL = 0

# 3、IIC通信协议简介

IIC总线写数据过程如下图所示：

![](images/ebc6eb8856ca67e6e81bbb76599d13e1137c6284abf6286f6d6404f2ddd3dbe2.jpg)

IIC 总线开始工作后，首先会发送从设备地址，待收到从设备应答后，然后发送一个控制字节，用于通知从设备，接下来要发送的数据是写入IC 寄存器的命令还是写入RAM 的数据，待收到从设备应答后，然后发送多个字节的值，直到发送完成，IIC 总线停止工作。

其中：

Co=0：此为最后一个控制字节，接下里发送的都是数据字节  
Co=1：接下来两份要发送的两个字节分别为数据字节和另外一个控制字节  
D/C=0：为寄存器命令操作字节  
D/C=1：为RAM数据操作字节

IIC 开始和停止时序图如下：

![](images/5ba506510a5aca005fd25bcf14eefb32be8ad9f4a926e9613d0032a4896996bc.jpg)

当IIC 的数据线和时钟线都保持高电平时，IIC 为空闲状态，此时数据线由高电平变为低电平，时钟线继续保持高电平，IIC 总线就启动数据传输。当时钟线保持高电平时，数据线由低电平变为高电平，IIC 总线停止数据传输。

IIC发送一个bit数据的时序图如下：

![](images/309da6fcb533faa75dd5dea29625718e4beba4066430e1bf95397e1d80de6155.jpg)

每一个时钟脉冲（拉高拉低的过程），发送 1bit 数据。当时钟线为高电平时，数据线必须保持稳定，当时钟线为低电平时，才允许数据线改变。

ACK发送时序图如下：

![](images/418983e9a70d31c75a3426efca3477093d7f561edd7bd93e7d2ec2a23ac6761f.jpg)

主设备等待从设备的ACK 时，需要保持时钟线为高电平，从设备发送ACK 时，要将数据线保持为低电平。

# 使用说明

# 1、Arduino使用说明

# 接线说明：

引脚标注见接口说明。

<table><tr><td rowspan=1 colspan=4>Arduino UNO单片机测试程序接线说明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应UNO开发板接线引脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>5V/3.3V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>A5</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>A4</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>3.3V</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>GND</td></tr></table>

Arduino MEGA2560单片机测试程序接线说明  

<table><tr><td rowspan=1 colspan=4>RUUmOM正ORZSoO平少测试J按我优明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应MEGA2560开发板接线引腳</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>5V/3.3V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>53</td><td rowspan=1 colspan=1>21</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>51</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>3.3V</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>GND</td></tr></table>

# 操作步骤：

A、按照上述接线说明将OLED 模块和Arduino单片机连接起来，并上电；  
B、选择需要测试的示例，如下图所示：（测试程序说明请查阅测试程序说明文档）  
project 1.54inch1.540LED_SSD13091.54inch_OLED_SSD1309_SPI&IC_Module_MSP154X_V1.01-DemoDemo_Ardu  
1)  
新建文件夹  
名称L Demo_1.54inch_OLED_64x128_SSD1309_UNO&Mega2560_Hardware_IC 测试程序Demo_1.54inch_OLED_64x128_SSD1309_UNO&Mega2560_Hardware_SPIInstall ibraries T测试程序依赖库picture测试程序效果图  
1.54inch_OLED_64x128_SSD1309_SPI&lIC_Arduino_Demo_Instructions_EN.pdf 1.54inch_OLED_64x128_SSD1309_SPI&IIC_Arduino_Demo_Instructions_CN.pdf 测试程序中英文说明文档  
C、打开所选的示例工程，进行编译和下载。关于Arduino测试程序编译和下载的具体操作方法见如下文档：http://www.lcdwiki.com/res/PublicFile/Arduino IDE Use Ilustration CN.pdf  
D、OLED 模块如果正常显示字符和图形，则说明程序运行成功；

# 2、RaspberryPi使用说明

# 接线说明：

引脚标注见接口说明

# 注意：

物理引脚是指 RaspBerryPi 开发板的 GPI0 引脚编码  
BCM 编码是指使用BCM2835GPI0库时的GPI0 引脚编码  
wiringPi编码是指使用wiringPiGPIO库时的GPIO引脚编码  
在代码里面使用哪个 GPIO 库，引脚定义就需要使用相应的 GPIO 库编码，详情见 GPIO  
map表

![](images/945e9a4a6a6b43542695690ffa689241c818db1800afba0bdb1aa9433155374f.jpg)  
图3.GPIO Map

<table><tr><td colspan="4" rowspan="1">Raspberry Pi测试程序接线说明</td></tr><tr><td colspan="1" rowspan="2">序号</td><td colspan="1" rowspan="2">引脚丝印</td><td colspan="2" rowspan="1">对应开发板接线引脚</td></tr><tr><td colspan="1" rowspan="1">SPI</td><td colspan="1" rowspan="1">IIC</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GND</td><td colspan="2" rowspan="1">GND(物理引脚：6,9,14,20,25,30,34, 39)</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">VCC</td><td colspan="2" rowspan="1">5V/3.3V(物理引脚：1,2,4)</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">SCL</td><td colspan="1" rowspan="1">物理引腳：23BCM编码：11wiringPi编码：14</td><td colspan="1" rowspan="1">物理引腳：5BCM编码：3wiringPi编码：9</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">SDA</td><td colspan="1" rowspan="1">物理引腳：19BCM编码：10wiringPi编码：12</td><td colspan="1" rowspan="1">物理引腳：3BCM编码：2wiringPi编码：8</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">RES</td><td colspan="1" rowspan="1">物理引腳：5BCM编码：3wiringPi编码：9</td><td colspan="1" rowspan="1">物理引腳：23BCM编码：11wiringPi编码：14</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">DC</td><td colspan="1" rowspan="1">物理引腳：3BCM编码：2wiringPi编码：8</td><td colspan="1" rowspan="1">VCC或者GND</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">CS</td><td colspan="1" rowspan="1">物理引腳：24BCM编码：8wiringPi编码：10</td><td colspan="1" rowspan="1">GND</td></tr></table>

# 操作步骤：

A、开启 RaspberryPi 的 SPI 功能 使用串口终端工具（如 putty）登录RaspberryPi，输入如下命令：sudo raspi-config选择 Interfacing Options->SPI->YES启动RaspberryPi 的 SPI 内核驱动  
B、安装函数库关于RaspberryPi 的 bcm2835、wiringPi、python 函数库的详细安装方法见如下文档：http://www.lcdwiki.com/res/PublicFile/Raspberrypi Use llustration CN.pdf  
C、选择需要测试的示例，如下图所示（测试程序说明请查阅测试程序说明文档）  
project1.54inch1.540LED_SD13091.54inch_OLED_SSD1309_SPI&IC_Module_MSP154X_V1.01-DemoDemo_Raspberyp  
(H)  
新建文件夹名称L Demo_IC 测试程序I Demo_SPIⅢ Picture 测试程序效果图1.54inch_OLED_64x128_SSD1309_SPI&IC_RaspberyPi_Demo_Instructions_EN.pdf 1.54inch_OLED_64x128_SSD1309_SPI&IIC_ RaspberyPi_Demo_Instructions_CN.pdf 测试程序中英文说明文档

D、bcm2835使用说明（以4线制硬件SPI测试程序为例）

a）先将 OLED 模块按照上述接线和 RaspberryPi 开发板连接起来b）将测试程序目

Demo_1.54inch_OLED_64x128_SSD1309_bcm2835_Hardware_4-wire_SPI 拷贝到RaspberryPi里（可以通过 SD卡拷贝，也可以通过FTP 工具（如 FileZilla)传输）。

c）执行如下命令运行bcm2835测试程序：

cd Demo_1.54inch_OLED_64x128_SSD1309_bcm2835_Hardware_4-wire_SPI make

sudo ./ 1.54_SPI_OLED如下图所示：

pi@raspberrypi:\~/0821 \$ cd 0.96inch OLED Demo bcm2835 Hardware 4-wire sPI/ pi@raspberrypi:\~/0821/0.96inch_OLED_Demo _bcm2835 Hardware_4-wire_sPI \$ make gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_bcm2835_Hardware_4-wire_sPI/source/src/test. /pi/0821/0.96inch OLED_Demo_bcm2835_Hardware_4-wire _SPI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED _Demo_bcm2835_Hardware_4-wire_sPI/source/src/spi.C i/0821/0.96inch_OLED_Demo_bcm2835 Hardware_4-wire_sPI/source/include gcc -g -00 -c Thome/pi/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_sPI/source/src/gui.C i/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_sPI/source/inciude gcc -g -00 -c Thome/pi/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_sPI/source/src/main. /pi/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_SPI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED _Demo_bcm2835_Hardware_4-wire_sPI/source/src/delay me/pi/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_sPI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_bcm2835_Hardware_4-wire_sPI/source/src/oled. /pi/0821/0.96inch_OLED_Demo_bcm2835_Hardware_4-wire_sPI/source/include gcc -g -00 /home/pi/0821/0.96inch_oLED_Demo_bcm2835_Hardware_4-wire_sPI/output/test.0 /home/ emo_bcm2835_Hardware_4-wire_SPI/output/gui.0 /home/pi/0821/0.96inch_oLED_Demo_bcm2835_Hardwa elay.o /home/pi/0821/0.96inch_oLED_Demo_bcm2835_Hardware_4-wire_sPI/output/oled.0 -o 0.96_sF pieraspberrypi:\~/0821/0.96inch oLED Demo bcm2835 Hardware_4-wire sPI \$ sudo ./0.96_ sPI_OLED

E、wiringPi使用说明（以4线制硬件 SPI测试程序为例）

a）先将 OLED 模块按照上述接线和 RaspberryPi 开发板连接起来  
b）将测试程序目录Demo_1.54inch_OLED_64x128_SSD1309_wiringPi_Hardware_4-wire_SPI 拷贝到RaspberryPi里(可以通过 SD 卡拷贝，也可以通过 FTP 工具(如 FileZilla)传输)。  
c）执行如下命令运行wiringPi测试程序：  
cd Demo_1.54inch_OLED_64x128_SSD1309_wiringPi_Hardware_4-wire_SPI  
make  
sudo ./ 1.54_SPI_OLED

如下图所示：

pi@raspberrypi:\~/0821 \$ cd 0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_sPI/ pi@raspberrypi:\~/0821/0.96inch_oLED_Demo_wiringPi_Hardware_4-wire_SPI \$ make gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_wiringPi_Hardware_4-wire_sPI/source/src/test. ome/pi/0821/0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_SpI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_wiringpi_Hardware_4-wire_sPI/source/src/spi.d e/pi/0821/0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_spI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_wiringPi_Hardware_4-wire_sPI/source/src/gui.C e/pi/0821/0.96inch_OLED_Demo_wiringPi _Hardware_4-wire_sPI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_wiringpi_Hardware_4-wire_sPI/source/src/main. ome/pi/0821/0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_SpI/source/include gcc -g -00 -c /home/pi/0821/0.96inch_oLED_Demo_wiringPi_Hardware_4-wire_sPI/source/src/delay /home/pi/0821/0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_sPI/source/inciude gcc -g -00 -c /home/pi/0821/0.96inch_OLED_Demo_ wiringpi_Hardware_4-wire_sPI/source/src/oled. ome/pi/0821/0.96inch_OLED_Demo_wiringPi_Hardware_4-wire_SpI/source/include gcc -g -00 /home/pi/0821/0.96inch_OLED Demo_wiringPi_Hardware_4-wire_sPI/output/test.o /home/ _Demo_wiringPi_Hardware_4-wire_sPI/output/gui.o /home/pi/0821/0.96inch_oLED _Demo_wiringPi_Har put/delay.0 /home/pi/0821/0.96inch_oLED_Demo_wiringPi_Hardware_4-wire_SpI/output/oled.0 -0 0. pi@raspberrypi:\~/0821/0.96inch oLED Demo wiringPi Hardware 4-wire sPI \$ sudo ./0.96 sPI OLED

F、python使用说明（以4线制硬件SPI测试程序为例）

a）运行python测试程序之前还需要安装图像处理库PIL，具体安装方法见如下文档：  
http://www.lcdwiki.com/res/PublicFile/Python Image Library Install llustration CN.pdf  
b）将 OLED模块按照上述接线和 RaspberryPi 开发板连接起来  
c）将测试程序目录Demo_1.54inch_OLED_64x128_SSD1309_python_Hardware_4-wire_SPI 拷贝到RaspberryPi里（可以通过SD卡拷贝，也可以通过FTP工具（如 FileZilla)传输）。

d）执行如下命令分别运行3个python测试程序：

cd Demo_1.54inch_OLED_64x128_SSD1309_python_Hardware_4-wire_SPI/source   
sudo python show_graph.py   
sudo python show_char.py   
sudo python show_bmp.py

如下图所示：

pi@raspberrypi:\~/0821 \$ cd 0.96inch OLED Demo_python Hardware _4-wire _sPI/source/ pieraspberrypi:\~/0821/0.96inch oLED Demo_python Hardware_4-wire_sPI/source \$ sudo python show_graph.py pieraspberrypi:\~/0821/0.96inch_oLED_ Demo_python_Hardware_4-wire_sPI/source \$ sudo python show_char.pY pieraspberrypi:\~/0821/0.96inch oLED Demo python Hardware 4-wire sPI/source \$ sudo python show bmp.pY

# 3、STM32使用说明

# 接线说明：

引脚标注见接口说明。

<table><tr><td rowspan=1 colspan=4>STM32F103C8T6单片机测试程序接线说明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应STM32F103C8T6开发板接线引I脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>PA5</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>PA7</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>PB8</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>PB7</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>PB9</td><td rowspan=1 colspan=1>GND</td></tr></table>

STM32F103RCT6单片机测试程序接线说明  

<table><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应MiniSTM32开发板接线引|脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>PB13</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>PB15</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>PB12</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>PB10</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>PB11</td><td rowspan=1 colspan=1>GND</td></tr></table>

<table><tr><td colspan="3">STM32F103ZET6单片机测试程序接线说明</td></tr><tr><td>序号</td><td>引脚丝印</td><td>对应Elite STM32开发板接线引I脚</td></tr></table>

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>PB13</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>PB15</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>PB12</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>PB10</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>PB11</td><td rowspan=1 colspan=1>GND</td></tr></table>

STM32F407ZGT6单片机测试程序接线说明  

<table><tr><td rowspan=1 colspan=4>STM32F407ZG16单片机测试程序接线说明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>引脚丝印</td><td rowspan=1 colspan=2>对应Explorer STM32F4开发板接线引|脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>PB3</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>PB5</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>PB12</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>PB14</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>PB15</td><td rowspan=1 colspan=1>GND</td></tr></table>

STM32F429IGT6单片机测试程序接线说明  

<table><tr><td colspan="1" rowspan="2">序号</td><td colspan="1" rowspan="2">引脚丝印</td><td colspan="2" rowspan="1">对应Apollo STM32F4/F7开发板接线</td></tr><tr><td colspan="2" rowspan="1">IIC</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GND</td><td colspan="2" rowspan="1">GND</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">VCC</td><td colspan="2" rowspan="1">3.3V/5V</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">SCL</td><td colspan="2" rowspan="1">PF7</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">SDA</td><td colspan="2" rowspan="1">PF9</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">RES</td><td colspan="2" rowspan="1">PD12</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">DC</td><td colspan="1" rowspan="1">PD5</td><td colspan="1" rowspan="1">VCC或者GND</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">CS</td><td colspan="1" rowspan="1">PD11</td><td colspan="1" rowspan="1">GND</td></tr></table>

# STM32F767IGT6和STM32H743IIT6单片机测试程序接线说明

<table><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=1>对应Apollo STM32F4/F7开发板接线</td></tr><tr><td rowspan=1 colspan=1>SPI</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>PB13</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>PB15</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=1>PD12</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>PD5</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>PD11</td></tr></table>

# 操作步骤：

A、按照上述接线说明将IPS模块和STM32单片机连接起来，并上电；B、根据单片机型号选择测试示例，如下图所示：（测试程序说明请查阅测试程序包中测试程序说明文档）

project1.54inch1.540LED_SSD13091.54inch_OLED_SSD1309_SPI&IC_Module_MSP154X_V1.01-DemoDemo_STM32  
1)  
新建文件夹  
名称  
Demo_IC 测试程序  
Demo_SPIPicture 测试程序效果图  
1.54inch_OLED_64x128_SSD1309_SPI&IC_STM32_Demo_Instructions_CN.pdf  
1.54inch_OLED_64x128_SD1309_SPI&IC_STM32_Demo_Instructions_EN.pdf ·测试程序中英文说明文档

C、打开所选的测试程序工程，进行编译和下载；

关于STM32测试程序编译和下载的详细说明见如下文档：

http://www.lcdwiki.com/res/Publicile/STM32 Keil Use llustration CN.odf

D、OLED 模块如果正常显示字符和图形，则说明程序运行成功；

# 4、C51使用说明

# 接线说明：

引脚标注见接口说明。

<table><tr><td rowspan=1 colspan=4>STC89C52RC和STC12C5A60S2单片机测试程序接线说明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应STC89/STC12开发板接线引I脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>P17</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>P15</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>P33</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>P12</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>P13</td><td rowspan=1 colspan=1>GND</td></tr></table>

# 操作步骤：

A、按照上述接线说明将IPS模块和C51单片机连接起来，并上电；B、选择需要测试的C51测试程序，如下图所示：（测试程序说明请查阅测试程序包中测试程序说明文档)

project 1.54inch 1.54OLED_SSD1309 1.54inch_OLED_SSD1309_SPI&lIC_Module_MSP154X_V1.0 1-Demo  
H)  
新建文件夹  
名称测试程序picture 测试程序效果图1.54inch_OLED_64x128_SSD1309_SPI8&IIC_C51_Demo_Instructions_CN.pdf 测试程序中英文说明文档  
1.54inch_OLED_64x128_SSD1309_SPI&IIC_C51_Demo_Instructions_EN.pdf

C、打开所选的测试程序工程，进行编译和下载；关于C51测试程序编译和下载的详细说明见如下文档：

http://www.lcdwiki.com/res/PublicFile/C51 Keil%26stc-isp Use llustration CN.pdf

D、OLED 模块如果正常显示字符和图形，则说明程序运行成功；

# 5、MSP430使用说明

# 接线说明：

引脚标注见接口说明。

<table><tr><td rowspan=1 colspan=4>MSP430F149单片机测试程序接线说明</td></tr><tr><td rowspan=2 colspan=1>序号</td><td rowspan=2 colspan=1>模块引脚</td><td rowspan=1 colspan=2>对应MSP430开发板接线引脚</td></tr><tr><td rowspan=1 colspan=1>SPI</td><td rowspan=1 colspan=1>IIC</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>GND</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=2>3.3V/5V</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=2>P33</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=2>P31</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>RES</td><td rowspan=1 colspan=2>P22</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>P21</td><td rowspan=1 colspan=1>VCC或者GND</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>P20</td><td rowspan=1 colspan=1>GND</td></tr></table>

# 操作步骤：

A、按照上述接线说明将IPS 模块和 MSP430单片机连接起来，并上电；B、选择需要测试的MSP430测试程序，如下图所示：（测试程序说明请查阅测试程序包中测试程序说明文档）

project1.54inch1.540LED_SSD13091.54inch_OLED_SSD1309_SPI&IC_Module_MSP154X_V1.01-DemoDemo_MSP43  
H)  
新建文件夹  
名称L Demo_IC 测试程序Demo_SPIpicture 测试程序效果图  
1.54inch_OLED_64x128_SSD1309_SPI&IIC_MSP430_Demo_Instructions_CN.pdf测试程序中英文说明文档  
1.54inch_OLED_64x128_SSD1309_SPI&IIC_MSP430_Demo_Instructions_EN.pdf  
C、打开所选的测试程序工程，进行编译和下载；关于 MSP430 测试程序编译和下载的详细说明见如下文档：http://www.lcdwiki.com/res/PublicFile/IAR IDE%26MspFet Use llustration CN.pdf  
C、OLED 模块如果正常显示字符和图形，则说明程序运行成功；

# 软件说明

# 1、代码架构

A、Arduino代码架构说明

代码架构如下图所示：

![](images/15f7ca3232ad57f4dd69a2f3f7009159e24662fd5a243971c367ce7cb475326f.jpg)

Arduino 的测试程序代码由两部分组成：LCDWIKI库和应用代码。

LCDWIKI库包含两部分内容：LCDWIKI_SPI库和LCD_GUI库。

应用程序包含几个测试示例，每个测试示例包含不同的测试内容

LCDWIKI_SPI 为底层库，和硬件有关联，主要负责操作寄存器，包括硬件模块初始化，数据和命令传输，像素点坐标和颜色设置，显示方式配置等。

LCDWIKI_GUI 为中间层库，主要负责使用底层库提供的API 实现图形的绘制，字符显示等操作。

应用程序是利用LCDWIKI 库提供的API，编写一些测试示例，实现某方面的测试功能。

# B、RaspberryPi 代码架构说明：

python测试程序代码架构如下图所示：

![](images/9ca8192e3e257f4a02c219e05de588800b3d2fa679fb683281a47f7c00c83f09.jpg)

python 测试程序由但部分组成：PIL 图像处理库，OLED 初始化代码，测试示例代码  
PIL 图像处理库负责图像绘制，字符和文字显示等操作  
OLDE 初始化代码负责操作寄存器，包括硬件模块初始化，数据和命令传输，像素点坐  
标和颜色设置，显示方式配置等  
测试示例则是利用上述两部分代码提供的 API，实现一些测试功能

Bcm2835和wiringPi测试程序代码架构如下:

![](images/53fa39e97c526138b02348319c186e2d2e9be2b543ecb45514546a33ef2b566d.jpg)

主程序运行时的 Demo API 代码包含在 test 代码中；

OLED初始化以及相关的操作都包含在 OLED 代码中；  
画点、线、图形以及中英文字符显示相关的操作都包含在GUI代码中；GPIO库提供GPIO操作；  
主函数实现应用程序运行；  
平台代码因平台而异；  
SPI 初始化及配置相关的操作包含在SPI代码中；

# C、STM32、C51以及MSP430代码架构说明

STM32和C51测试程序代码架构如下图所示：

![](images/40d94cfd619f00c38101b745a47d89682d5e4034af5273ba9eefd8d9cb267f74.jpg)

主程序运行时的 DemoAPI 代码包含在 test 代码中；  
OLED 初始化以及相关的操作都包含在OLED代码中；  
画点、线、图形以及中英文字符显示相关的操作都包含在GUI代码中；  
主函数实现应用程序运行；  
平台代码因平台而异；   
SPI初始化及配置相关的操作包含在SPI代码中；

# 2、软件SPI和硬件SPI说明

该IPS 模块分别提供了软件 SPI 和硬件 SPI 示例代码（STC89C52RC 只有软件 SPI 功能），两种示例代码在显示内容上没任何区别，但是如下方面有区别：

# A、显示速度

硬件 SPI 明显比软件 SPI 要快，这是由硬件决定的。

# B、GPI0定义

软件 SPI 全部控制引脚都要定义，可以使用任何空闲引脚，硬件 SPI 的数据和时钟信号引脚是固定的（因平台而异），其他控制引脚要自己定义，也可使用任何空闲引脚。

# C、初始化

软件 SPI 初始化时，只需要对用于引脚定义的 GPIO 进行初始化，硬件 SPI 初始化时，需要对相关的控制寄存器以及数据寄存器进行初始化。

# 3、模块GPI0定义说明

# A、Arduino测试程序GPI0定义说明

Arduino 测试程序 GPI0 定义放在应用示例里，每个应用示例都可以定义 GPIO。如下图所示（以 UNO单片机 4 线制软件 SPI测试程序为例）：

//paramters define   
#define MODEL SSD1306   
#define Cs A5   
#define DC A3   
#define D1 11   
#define DO 13   
#define RES A4   
#define LED -1 //if you don't need to control

如果使用软件 SPI，所有引脚定义都可以修改成其他任何空闲的GPIO。

如果使用硬件 SPI，则 DO 和 D1 不可修改，也不需要定义，其他 GPIO 都可修改。

如果使用3线制SPI，则DC不需要定义。

# B、RaspberryPi测试程序GPI0定义说明

RaspberryPi 测试程序都是使用硬件 SPI，所以只需定义 3个 GPI0口。bcm2835和WiringPi 测试程序将 GPIO 定义放在 oled.h 文件里面，如下图所示（以 4线制 sPI测试程序为例):

-OLED module pin definition #define OLED_CS 8 //chip selection control signal bcm:8 #define OLED_DC 2 //data or command selection control signal bcm:2 #define OLED_RST 3 //reset control signal bcm:3

Python 测试程序将 GPIO 定义放在每个测试示例里，如下图所示（以 4 线制 SPI 测试

程序为例）：

# ·RaspberryPi ·pin ·configuration:   
DC·= ·2   
RES ·= · 3   
CS·=·8

此三个GPIO可以根据相应的GPIO库编码来修改。

如果使用 3 线制 SPI，则 OLED_DC 或者DC 不需要定义。

# C、STM32 测试程序GPI0 定义说明

STM32 测试程序 GPI0 定义分为两部分：控制 GPI0 定义和 SPI GPI0 定义控制 GPIO 定义放在 oled.h 里，SPI GPI0 定义放在 spi.h里，分别如下图所示（以STM32F103RCT6 软件4线制SPI测试程序为例)：

OLED端口定义#define OLED CS GPIO Pin 11 //片选信号 PB11#define OLED_DC GPIO_Pin_10 //数据/命令控制信号 PB10#define OLED RST GPIO Pin 12 //复位信号 PB12

-SPI总线引脚定义#define OLED_MOSI GPIO Pin 15 //OLED屏SPI写数据信号#define OLED CLK GPIO_Pin_13 //OLED屏SPI时钟信号如果使用软件SPI，所有引脚定义都可以修改成其他任何空闲的GPIO。

如果使用硬件 SPI，则 OLED_MOSI 和 OLED_CLK 不可修改，也不需要定义，其他GPIO 都可修改。

如果使用3 线制SPI，则OLED_DC 不需要定义修改完 GPI0 定义后，需要到oled.c 文件的 OLED_Init_GPI0 函数里将GPI0 初始化做相应的修改。

# D、C51测试程序GPI0定义说明

C51 测试程序 GPIO 定义分为两部分：控制 GPI0 定义和 SPI GPI0 定义控制 GPI0 定义放在 oled.h 里，SPI GPI0 定义放在 spi.h 里，分别如下图所示（以STC12C5A60S2 软件4线制 SPI测试程序为例)：

-OLED端口定义  
sbit OLED CS = P1^3; //片选信号 P13  
sbit OLED DC = P1^2; //数据/命令控制信号 P12  
sbit OLED RST =P3^3; //复位信号 P33  
sbit OLED MOSI P1^5; //OLED屏SPI写数据引脚 P15  
sbit OLED CLK :P1^7; //OLED屏SPI时钟引脚 P17

如果使用软件 SPI，所有引脚定义都可以修改成其他任何空闲的 GPIO。

如果使用硬件 SPI，则 OLED_MOSI 和 OLED_CLK 不可修改，也不需要定义，其他 GPIO 都可修改。（只有STC12C5A60S2 单片机才有硬件SPI功能）  
如果使用3 线制 SPI，则OLED_DC 不需要定义

# E、MSP430测试程序GPI0定义说明

MSP430 的液晶屏非 SPI 的GPI0 定义放在 1cd.h 里面，如下图所示（以 MSP430F149 软件4线制SPI测试程序为例)：

-OLED端口定义#define OLED_CS BITO 11片选信号 P20#define OLED_DC BIT1 1/数据/命令控制信号 P21#define OLED_ RST BIT2 1/复位信号 P22所有引脚定义都可以修改，可以定义成其他任何空闲的GPI0。

如果使用3线制SPI，则OLED_DC 不需要定义

MSP430的液晶屏 SPI 的GPI0定义放在 spi.h 里面，如下图所示（以 MSP430F149 软件4线制SPI测试程序为例)：

11本测试程序使用的是就件SPI接口驱动  
//SPI时斜信号以及SPI读、写信号引脚都可以更改  
#define SPI_SCLK BIT3 //P33  
#define SPI_MOSI BIT1 //P31

如果使用软件 SPI，所有引脚定义都可以修改，可以定义成其他任何空闲的GPIO。

如果使用硬件 SPI，这些引脚都不需要定义

# 4、SPI通信代码实现

A、Arduino测试程序SPI通信代码实现

SPI通信代码都在LCDWIKI_SPI库里实现。

4线制软件和硬件SPI代码实现如下图所示：

//spi write for hardware and software   
void LCDWIKI_SPI:Spi_Write(uint8_t data)   
{ if(hw_spi) { SPI.transfer(data); } else { uint8_t val = 0x80; while(val) { if(data&val) { MOSI_HIGH; } else { MOSI_LOW; } CLK_LOW; CLK_HIGH; val >>= 1; }   
} 《 end Spi_Write

3 线制软件和硬件SPI代码实现如下图所示：

void LCDWIKI_SPI::Spi_3_wire_Write(uint8_t data,uint8_t cmd)   
」 uint16_t txdata = 0; txdata = （(cmd<<15)I(data<<7)); if(hw_spi) { SPI.transfer16(txdata); } else { uint16_t val = 0x8000; while(val>(1<<6)) { if(txdata&val) { MOSI_HIGH; else - { MOSI_LOW; } CLK_LOW; CLK_HIGH; val >>= 1; } }   
}《 end Spi_3_wire_Write

都是通过标志位来决定使用软件 SPI 还是硬件SPI

# B、RaspberryPi测试程序SPI 通信代码实现

bcm2835 和 wiringPi 测试程序的 SPI通信代码在 spi.c 中实现。python 测试程序的 SPI 通信代码在 oled. py 中实现。bcm2835 测试程序4线制硬件 SPI代码实现如下图所示:

@name :void SPI_WriteByte(uint8_t byte) @date :2018-08-27 \* @function :Write a byte of data using RaspberryPi hardware SPI \* @parameters : Byte:Data to be written \* @retvalue :Data received by the bus

# SPI_WriteByte(uint8_t byte)

bcm2835_spi_transfer(byte);

bcm2835 测试程序3线制硬件 SPI代码实现如下图所示：

@name :void SPI_WriteByte(uint8_t byte, uint8_t cmd) @date :2018-08-27 @function :Write a byte of data using RaspberryPi hardware SPI @parameters : Byte:Data to be written cmd:0-command 1-data 🌟 @retvalue :Data received by the bus

void SPI_WriteByte(uint8_t byte, uint8_t cmd)   
{ uint16_t data=0; char txbuf[2]={0}; data=((cmd<<15)1(byte<<7)）; txbuf[0]=(char)(data>>8); txbuf[1]=(char)(data&0xFF); bcm2835_spi_transfern(txbuf,2);   
}

wiringPi测试程序4线制硬件SPI代码实现如下图所示：

\* @name :void SPI_WriteByte(uint8_t byte)   
\*@date :2018-08-27 @function :Write a byte of data using RaspberryPi hardware SPI   
\* @parameters : Byte:Data to be written   
\* @retvalue :Data received by the bus   
void SPI_WriteByte(uint8_t byte)   
{ wiringPiSPIDataRW(CHANNEL, &byte, 1);   
}

wiringPi测试程序3线制硬件 SPI代码实现如下图所示:

\*@name :void SPI_WriteByte(uint8_t byte, uint8_t cmd)   
\*@date :2018-08-27   
\*@function :Write a byte of data using RaspberryPi hardware SPI @parameters :Byte:Data to be written cmd:0-command 1-data @retvalue :Data received by the bus   
void SPI_WriteByte(uint8_t byte, uint8_t cmd) uint16_t data; unsigned char txbuf[2]={0}; data=((cmd<<15)l(byte<<7)); txbuf[0]=(unsigned char)(data>>8); txbuf{1j=(unsigned char)(data&0xFF); wiringPiSPIDataRW(CHANNEL, txbuf, 2);   
}

python 测试程序4线制硬件 SPI 代码实现如下图所示：

→def ·writebyte (self,val, flag) : >"""send ·one ·byte ·data ·to ·oled ·module""" →if·flag ·== ·OLED_COMMAND : →GPIO.output (self.oleddc,GPIo.LOw) else: →GPIO.output (self.oleddc,GPIO.HIGH) →GPIO.output (self.oledcs,GPIo.Low) >self.oledspi.writebytes([val1) >self.oledspi.xfer([vall,8000000)   
→ >GPIO.output (self.oledcs ,GPIO.HIGH)

python测试程序3线制硬件SPI代码实现如下图所示：

>def ·writebyte (self,val, flag) : >"""send ·two ·byte ·data ·to ·oled ·module""" →data=((flag<<15)\(val<<7)) →txbuf=[(data>>8)&0xFF,data&0xFF] →GPIO.output (self.oledcs,GPIo.Low) >self.oledspi.writebytes (txbuf) →self.oledspi.xfer(txbuf,8000000) →GPIO.output (self.oledcs,GPIO.HIGH)

# C、STM32测试程序SPI通信代码实现

SPI 通信代码都在spi.c 中实现。（以 STM32F103RCT6 测试程序为例）

4线制软、硬件 SPI通信代码实现如下所示：

软件SPI：

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 火 @name :void sPI_WriteByte (u8 Data) @date :2018-08-27 @function :Write a byte of data using STM32's Software SPI @parameters :Data:Data to be written @retvalue :None

void sPI_WriteByte(u8 Data)unsigned char i=0;for(i=8;i>0;i--)if (Data&0x80){OLED_MOSI_SET（）；//写数据1}elsefOLED_MOSI_CLR（）；//写数据0}OLED CLK_CLR() ; //将时钟拉低拉高OLED_CLK_SET() ; //发送1bit数据Data<<=1;]

硬件SPI：

@name :u8 sPI_WriteByte (sPI_TypeDef\* sPIx,u8 Byte) @date :2018-08-27 @function :Write a byte of data using sTM32's hardware sPI @parameters :sPIx: SPI type,x for 1,2,3 Byte:Data to be written @retvalue : Data received by the bus u8 SPI_WriteByte (sPI_TypeDef\* sPIx,u8 Byte) while((SPIx->SR&SPI_I2s_FLAG_TXE)==RESET) ; //等待发送区空 SPIx->DR=Byte; //发送一个byte while（(SPIx->SR&SPI_I2s_FLAG_RxNE)==RESET);//等待接收完一个byte return SPIx->DR; //返回收到的数据 }

3线制软、硬件SPI通信代码实现如下所示：

软件SPI：

火 @name :void SPI_WriteByte (u8 data,u8 Cmd) ★ @date :2018-08-27 火 @function :Write a byte of data using sTM32's Software sPI 火 @parameters :Data:Data to be written Cmd:0-command 1-data @retvalue : None void sPI_WriteByte(u8 data,u8 cmd) f unsigned char i=0; u16 Data; Data = ((cmd<<15)1(data<<7)); for (i=9;i>0;i--) { if(Data&0x8000) f OLED_MOSI_SET（)；//写数据1 } else f OLED_MOSI_CLR（）；//写数据0 } OLED_CLK_CLR() ; //将时钟拉低拉高 OLED_CLK_SET() ; //发送1bit数据 Data<<=1; } }

硬件 SPI:

★★★★★★★ ★★★★★★ @name :u8 sPI_WriteByte (sPI_TypeDef\* sPIx,u8 Byte,u8 cmd) @date :2018-08-27 @function :Write a byte of data using sTm32's hardware sPI eparameters :SpIx: spI type,x for 1,2,3 Byte:Data to be written cmd: 0-write command 1-write data @retvalue : Data received by the bus ★★★★★ u8 SPI_WriteByte(SPI_TypeDef\* SPIx,u8 Byte,u8 cmd) while((SPIx->SR&SPI_I2S_FLAG_TXE)==RESET); //等待发送区空 SPIx->DR=((cmd<<15)(Byte<<7)); //发送两个byte while((SPIx->SR&SPI_I2s_FLAG_RXNE)==RESET);//等待接收完两个byte return SPIx->DR; //返回收到的数据 1

# D、C51测试程序SPI通信代码实现

SPI 通信代码都在spi.c 中实现。（以 STC12C5A60S2 测试程序为例）

4线制软、硬件SPI通信代码实现如下所示：

软件SPI：

火 @name :void SPI_WriteByte(u8 byte) 火 @date :2018- -08-09 火 @function :Write a byte of data using 火 @parameters :byte:Data to be written @retvalue :None void SPI WriteByte(u8 byte) { u8 i; for (i=0;i<8; i if (byte&0x80) { OLED MOSI Set() ; } else { OLED MOSI clr() ; } OLED CLK clr() ; OLED CLK_Set(); byte<<=1; } }

硬件SPI:

★★火火 @name :void SPI_writeByte(u8 byte) @date :2018-08-09 @function :Write a byte of data using C51's Hardware SPI @parameters :byte:Data to be written @retvalue :None void SPI_WriteByte (u8 byte) SPDAT byte; //发送一个字节 while((sPsTAT & SPIF)==0）；//等待发送完成 SPSTAT SPIF+WCOL; //清0 SPIF和WCOL标志 1

3线制软、硬件SPI通信代码实现如下所示：

软件SPI：

★★★★★ @name :void sPI_WriteByte (u8 byte, u8 cmd) @date :2018-08-09 火 @function :Write a byte of data using C51's s0 @parameters :byte:Data to be written cmd: 0-command 1-data @retvalue :None void SPI_WriteByte (u8 byte, u8 cmd) u8 i; u16 Data=0; Data=((cmd<<15)\(byte<<7)) ; for(i=0;i<9;i++) if (Data&0x8000) OLED MosI_Set() ; } else OLED MOSI clr() ; OLED CLK_clr() ; OLED CLK_Set() ; Data<<=1; } }

硬件SPI:

@name :void sPI_WriteByte(u8 byte, u8 cmd) @date :2018-08-09 @function :Write a byte of data using c51's Hardware sPI @parameters :byte:Data to be written cmd:0-command 1-data @retvalue :None void sPI_WriteByte(u8 byte， u8 cmd) f u8 i=0; u16 Data=0; Data=((cmd<<15)\(byte<<7)) ; for(i=2;i>0;i--) { SPDAT (Data>>((i-1)\*8)); //发送一个字节 while（(SPsTAT&SPIF)==0）；//等待发送完成 SPSTAT SPIF+WCOL; //清0SPIF和WCOL标志 } 1

# E、MSP430测试程序SPI通信代码实现

软件SPI通信代码在spi.c中实现。

4 线制软、硬件 SPI 通信代码实现如下所示：

软件SPI：

\*@name :void SPI_WriteByte (u8 Data)   
\*edate :2018-08-09   
\*@function :Write a byte of data using STM32's hardvare SPI \* @parameters :SPIx: SPI type,x for 1,2,3 Byte:Data to be vritten   
\*@retvalue :Data received by the bus   
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
void SPI_WriteByte (u8 Data) unsigned char i=0; for (i=θ;i>0;i--) { if (Datac0x80) SPI_MOSI_SET；//都出数据 else SPI_MOsI_CLR; SPI_SCLK_CLR; SPI_SCLK_SET; Data<<=1;   
]

硬件SPI：

\* @name :u8 SPI_WriteByte (SPI_TypeDef\* SPIx,u8 Byte)   
\* @date :2018-08-09   
\*@function :Write a byte of data using STM32's hardvare SPI   
\* @parameters :spIx: sPI type,x for 1,2,3 Byte:Data to be vritten   
\* @retvalue :Data received by the bus   
u8 SPI_WriteByte (u8 Byte)   
{ while ((IFG1&UTXIFG0) ==0): // vait vhile not ready / for Rx UOTXBUF = Byte; while ((IFG1&URXIFGo)==0) : // vait for RX buffer (full) return (UoRxBUF) :   
]

3线制软、硬件SPI通信代码实现如下所示：

软件SPI：

\*@name :void SPI_WriteByte (u8 Data)   
\*@date :2018-08-09   
\*@function :Write a byte of data using sTM32's hardvare SPI   
\* eparameters :SPIx: SPI type,x for 1,2,3 Byte:Data to be written   
\*@retvalue :Data received by the bus   
void sPI_WriteByte (u8 val, u8 cmd) unsigned char i=0; u16 Data=0; Data = ((cmd<<15) I (val<<7)); for (i=9;i>0;i--) { if (Datas0x8000) SPI_MOSI_SET：//都出数语 else SPI_MOSI_CLR; SPI_SCLK_CLR; SPI_SCLK_SET; Data<<=1;   
1

硬件SPI：

\*ename :void oLED_WR_Byte (unsigned dat, unsigned cmd)   
\* @date :2018-08-27   
\* @function :Write a byte of content to the OLED screen   
\* @parameters :dat:Content to be vritten cmd:0-vrite command   
\*@retvalue :None   
+++++++++++++++++++++\*   
void oLED_wR_ Byte (unsigned dat, unsigned cmd)   
{ u16 data=0; data=((cmd<<15) I (dat<<7)) ; OLED_CS_Clr; SPI_WriteByte((data>>8) &0xFF) ; SPI_WriteByte (data&OxFF) ; OLED_CS_Set;   
]

# 常用软件

本套测试示例需要显示中英文、符号以及图片，所以要用到 PCtoLCD2002 取模软件。这里只针对该套测试程序说明一下取模软件的设置。

本套测试程序PCtoLCD2002 取模软件设置如下：

点阵格式选择阴码

取模方式选择逐行式（c51 和 MSP430 测试程序需要选择行列式）

取模走向选择顺向（高位在前）（C51 和MSP430 测试程序需要选择逆向（低位在前））

输出数制选择十六进制数自定义格式选择 C51 格式

具体设置方法见如下网页：http://www.lcdwiki.com/zh/%E3%80%90%E6%95%99%E7%A8%8B%E3%80%91%E4%B8%AD%E8%8B%B1%E6%96%87%E6%98%BE%E7%A4%BA%E5%8F%96%E6%A8%A1%E8%AE%BE%E7%BD%AE