# ESP32-WROOM-32D & ESP32-WROOM-32U

Datasheet

# About This Document

This document provides the specifications for the ESP32-WROOM-32D and ESP32-WROOM-32U modules.

# Revision History

For revision history of this document, please refer to the last page.

# Documentation Change Notification

Espressif provides email notifications to keep customers updated on changes to technical documentation. Please subscribe at www.espressif.com/en/subscribe.

# Certification

Download certificates for Espressif products from www.espressif.com/en/certificates.

# Disclaimer and Copyright Notice

Information in this document, including URL references, is subject to change without notice. THIS DOCUMENT IS PROVIDED AS IS WITH NO WARRANTIES WHATSOEVER, INCLUDING ANY WARRANTY OF MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR ANY WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, SPECIFICATION OR SAMPLE.

All liability, including liability for infringement of any proprietary rights, relating to use of information in this document is disclaimed. No licenses express or implied, by estoppel or otherwise, to any intellectual property rights are granted herein. The Wi-Fi Alliance Member logo is a trademark of the Wi-Fi Alliance. The Bluetooth logo is a registered trademark of Bluetooth SIG.

All trade names, trademarks and registered trademarks mentioned in this document are property of their respective owners, and are hereby acknowledged.

Copyright © 2019 Espressif Inc. All rights reserved.

# Contents

1 Overview

2 Pin Definitions 3

2.1 Pin Layout 3   
2.2 Pin Description 3   
2.3 Strapping Pins 5

# 3 Functional Description 6

3.1 CPU and Internal Memory 6   
3.2 External Flash and SRAM 6   
3.3 Crystal Oscillators 6   
3.4 RTC and Low-Power Management 7

4 Peripherals and Sensors 8

# 5 Electrical Characteristics 9

5.1 Absolute Maximum Ratings 9

5.2 Recommended Operating Conditions 9

5.3 DC Characteristics (3.3 V, 25 °C) 9

5.4 Wi-Fi Radio 10

5.5.1 Receiver 11

5.5.2 Transmitter 11

5.6 Reflow Profile 12

6 Schematics 13

7 Peripheral Schematics 15

8 Physical Dimensions 17

Recommended PCB Land Pattern 19

0U.FL Connector Dimensions 21

# 11Learning Resources

# 22

1.2 Must-Have Resources 22

Revision History 23

# List of Tables

ESP32-WROOM-32D vs. ESP32-WROOM-32U 1   
2 ESP32-WROOM-32D and ESP32-WROOM-32U Specifications 2   
3 Pin Definitions 3   
4 Strapping Pins 5

5 Absolute Maximum Ratings 9

6 Recommended Operating Conditions 9

DC Characteristics (3.3 V, 25 °C) 9

8 Wi-Fi Radio Characteristics 10

9 Receiver Characteristics – BLE 11

10 Transmitter Characteristics – BLE 11

# List of Figures

ESP32-WROOM-32D Pin Layout (Top View) 3   
Reflow Profile 12   
3 ESP32-WROOM-32D Schematics 13   
4 ESP32-WROOM-32U Schematics 14   
5 ESP32-WROOM-32D & ESP32-WROOM-32U Peripheral Schematics 15   
6 Physical Dimensions of ESP32-WROOM-32D 17   
Physical Dimensions of ESP32-WROOM-32U 18   
8 Recommended PCB Land Pattern of ESP32-WROOM-32D 19   
9 Recommended PCB Land Pattern of ESP32-WROOM-32U 20   
10 ESP32-WROOM-32U U.FL Dimensions 21

# Overview

ESP32-WROOM-32D and ESP32-WROOM-32U are powerful, generic Wi-Fi+BT+BLE MCU modules that target a wide variety of applications, ranging from low-power sensor networks to the most demanding tasks, such as voice encoding, music streaming and MP3 decoding.

ESP32-WROOM-32U is different from ESP32-WROOM-32D in that ESP32-WROOM-32U integrates a U.FL connector. For detailed information of the U.FL connector please see Chapter 10. Note that the information in this data sheet is applicable to both modules. Any differences between them will be clearly specified in the course of this document. Table 1 lists the difference between ESP32-WROOM-32D and ESP32-WROOM-32U.

Table 1: ESP32-WROOM-32D vs. ESP32-WROOM-32U   

<table><tr><td rowspan=1 colspan=1>Module</td><td rowspan=1 colspan=1>ESP32-WROOM-32D</td><td rowspan=1 colspan=1>ESP32-WROOM-32U</td></tr><tr><td rowspan=1 colspan=1>Core</td><td rowspan=1 colspan=1>ESP32-D0WD</td><td rowspan=1 colspan=1>ESP32-D0WD</td></tr><tr><td rowspan=1 colspan=1>SPI flash</td><td rowspan=1 colspan=1>32 Mbits, 3.3 V</td><td rowspan=1 colspan=1>32 Mbits, 3.3 V</td></tr><tr><td rowspan=1 colspan=1>Crystal</td><td rowspan=1 colspan=1>40 MHz</td><td rowspan=1 colspan=1>40 MHz</td></tr><tr><td rowspan=1 colspan=1>Antenna</td><td rowspan=1 colspan=1>onboard antenna</td><td rowspan=1 colspan=1>U.FL connector (which needs to be connectedto an external IPEX antenna)</td></tr><tr><td rowspan=1 colspan=1>Dimensions(Unit: mm)</td><td rowspan=1 colspan=1>(18.00±0.10)×(25.50±0.10)×(3.10±0.10)(See Figure 6 for details)</td><td rowspan=1 colspan=1>(18.00±0.10) × (19.20±0.10) × (3.20±0.10)(See Figure 7 for details)</td></tr><tr><td rowspan=1 colspan=1>Schematics</td><td rowspan=1 colspan=1>See Figure 3 for details.</td><td rowspan=1 colspan=1>See Figure 4 for details.</td></tr></table>

At the core of the two modules is the ESP32-D0WD chip that belongs to the ESP32 series\* of chips. The chip embedded is designed to be scalable and adaptive. There are two CPU cores that can be individually controlled, and the CPU clock frequency is adjustable from 80 MHz to 240 MHz. The user may also power off the CPU and make use of the low-power co-processor to constantly monitor the peripherals for changes or crossing of thresholds. ESP32 integrates a rich set of peripherals, ranging from capacitive touch sensors, Hall sensors, SD card interface, Ethernet, high-speed SPI, UART, I²S and I²C.

# Note:

\* For details on the part numbers of the ESP32 family of chips, please refer to the document ESP32 Datasheet.

The integration of Bluetooth, Bluetooth LE and Wi-Fi ensures that a wide range of applications can be targeted, and that the module is all-around: using Wi-Fi allows a large physical range and direct connection to the Internet through a Wi-Fi router, while using Bluetooth allows the user to conveniently connect to the phone or broadcast low energy beacons for its detection. The sleep current of the ESP32 chip is less than 5 µA, making it suitable for battery powered and wearable electronics applications. The module supports a data rate of up to 150 Mbps, and 20 dBm output power at the antenna to ensure the widest physical range. As such the module does offer industry-leading specifications and the best performance for electronic integration, range, power consumption, and connectivity.

The operating system chosen for ESP32 is freeRTOS with LwIP; TLS 1.2 with hardware acceleration is built in as well. Secure (encrypted) over the air (OTA) upgrade is also supported, so that users can upgrade their products even after their release, at minimum cost and effort.

Table 2 provides the specifications of ESP32-WROOM-32D and ESP32-WROOM-32U.

Table 2: ESP32-WROOM-32D and ESP32-WROOM-32U Specifications   

<table><tr><td rowspan=1 colspan=1>Categories</td><td rowspan=1 colspan=1>Items</td><td rowspan=1 colspan=1>Specifications</td></tr><tr><td rowspan=4 colspan=1>Certification</td><td rowspan=1 colspan=1>RF Certification</td><td rowspan=1 colspan=1>FCC/CE-RED/IC/TELEC/KCC/SRRC/NCC</td></tr><tr><td rowspan=1 colspan=1>Wi-Fi Certification</td><td rowspan=1 colspan=1>Wi-Fi Alliance</td></tr><tr><td rowspan=1 colspan=1>Bluetooth certification</td><td rowspan=1 colspan=1>BQB</td></tr><tr><td rowspan=1 colspan=1>Green Certification</td><td rowspan=1 colspan=1>REACH/RoHS</td></tr><tr><td rowspan=1 colspan=1>Test</td><td rowspan=1 colspan=1>Reliablity</td><td rowspan=1 colspan=1>HTOL/HTSL/uHAST/TCT/ESD</td></tr><tr><td rowspan=3 colspan=1>Wi-Fi</td><td rowspan=2 colspan=1>Protocols</td><td rowspan=1 colspan=1>802.11 b/g/n (802.11n up to 150 Mbps)</td></tr><tr><td rowspan=1 colspan=1>A-MPDU and A-MSDU aggregation and 0.4 s guardinterval support</td></tr><tr><td rowspan=1 colspan=1>Frequency range</td><td rowspan=1 colspan=1>2.4 GHz ~2.5 GHz</td></tr><tr><td rowspan=5 colspan=1>Bluetooth</td><td rowspan=1 colspan=1>Protocols</td><td rowspan=1 colspan=1>Bluetooth v4.2 BR/EDR and BLE specification</td></tr><tr><td rowspan=3 colspan=1>Radio</td><td rowspan=1 colspan=1>NZIF receiver with -97 dBm sensitivity</td></tr><tr><td rowspan=1 colspan=1>Class-1, class-2 and class-3 transmitter</td></tr><tr><td rowspan=1 colspan=1>AFH</td></tr><tr><td rowspan=1 colspan=1>Audio</td><td rowspan=1 colspan=1>CVSD and SBC</td></tr><tr><td rowspan=9 colspan=1>Hardware</td><td rowspan=1 colspan=1>Module interfaces</td><td rowspan=1 colspan=1>SD card, UART, SPI, SDIO, I²C, LED PWM, MotorPWM, I²S, IR, pulse counter, GPIO, capacitive touchsensor, ADC, DAC</td></tr><tr><td rowspan=1 colspan=1>On-chip sensor</td><td rowspan=1 colspan=1>Hall sensor</td></tr><tr><td rowspan=1 colspan=1>Integrated crystal</td><td rowspan=1 colspan=1>40 MHz crystal</td></tr><tr><td rowspan=1 colspan=1>Integrated SPI flash 1</td><td rowspan=1 colspan=1>4MB</td></tr><tr><td rowspan=1 colspan=1>Operating voltage/Power supply</td><td rowspan=1 colspan=1>3.0V~3.6V</td></tr><tr><td rowspan=1 colspan=1>Operating current</td><td rowspan=1 colspan=1>Average: 80 mA</td></tr><tr><td rowspan=1 colspan=1>Minimum current delivered by powersupply</td><td rowspan=1 colspan=1>500mA</td></tr><tr><td rowspan=1 colspan=1>Recommended operating temperaturerange2</td><td rowspan=1 colspan=1>-40℃~+85℃</td></tr><tr><td rowspan=1 colspan=1>Moisture sensitivity level (MSL)</td><td rowspan=1 colspan=1>Level 3</td></tr></table>

# Notice:

1. ESP32-WROOM-32D and ESP32-WROOM-32U with 8 MB flash or 16 MB flash are available for custom order.

2. ESP32-WROOM-32D and ESP32-WROOM-32U with high temperature range (–40 °C \~ +105 °C) option are available for custom order. 4 MB SPI flash is supported on the high temperature range version.

3. For detailed ordering information, please see Espressif Product Ordering Information.

# 2. Pin Definitions

# 2.1 Pin Layout

![](images/9727b2f8d94c09a3dacfc22cc32e6bea9c270fe577b4fe2e977a832aaf5886f8.jpg)  
Figure 1: ESP32-WROOM-32D Pin Layout (Top View)

# Note:

The pin layout of ESP32-WROOM-32U is the same as that of ESP32-WROOM-32D, except that ESP32-WROOM-32U has no keepout zone.

# 2.2 Pin Description

The ESP32-WROOM-32D and ESP32-WROOM-32U have 38 pins. See pin definitions in Table 3.

Table 3: Pin Definitions   

<table><tr><td colspan="1" rowspan="1">Name</td><td colspan="1" rowspan="1">No.</td><td colspan="1" rowspan="1">Type</td><td colspan="1" rowspan="1">Function</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">3V3</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">Power supply</td></tr><tr><td colspan="1" rowspan="1">EN</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Module-enable signal. Active high.</td></tr><tr><td colspan="1" rowspan="1">SENSOR_VP</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GPIO36, ADC1_CH0, RTC_GPIO0</td></tr><tr><td colspan="1" rowspan="1">SENSOR_VN</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">I</td><td colspan="1" rowspan="1">GPIO39, ADC1__CH3, RTC_GPIO3</td></tr><tr><td colspan="1" rowspan="1">1034</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">I</td><td colspan="1" rowspan="1">GPIO34, ADC1__CH6, RTC_GPIO4</td></tr><tr><td colspan="1" rowspan="1">1035</td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">I</td><td colspan="1" rowspan="1">GPIO35, ADC1_CH7, RTC_GPIO5</td></tr><tr><td colspan="1" rowspan="1">1032</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO32, XTAL_32K_P (32.768 kHz crystal oscillator input), ADC1_CH4,TOUCH9, RTC_GPIO9</td></tr><tr><td colspan="1" rowspan="1">1033</td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPlO33, XTAL_32K_N (32.768 kHz crystal oscilator output), ADC1_CH5,TOUCH8, RTC_GPIO8</td></tr><tr><td colspan="1" rowspan="1">1025</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">GPIO25, DAC_1, ADC2_CH8, RTC_GPIO6, EMAC_RXD0</td></tr><tr><td colspan="1" rowspan="1">1026</td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO26, DAC_2, ADC2_CH9, RTC_GPIO7, EMAC_RXD1</td></tr><tr><td colspan="1" rowspan="1">1027</td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO27, ADC2_CH7, TOUCH7, RTC_GPIO17, EMAC_RX_DV</td></tr><tr><td colspan="1" rowspan="1">1014</td><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO14, ADC2_CH6, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK,SD_CLK, EMAC_TXD2</td></tr><tr><td colspan="1" rowspan="1">1012</td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO12, ADC2_CH5, TOUCH5, RTC_GPIO15, MTDI, HSPIQ, HS2_DATA2,SD_DATA2, EMAC_TxD3</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">1013</td><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO13, ADC2_CH4, TOUCH4, RTC_GPIO14, MTCK, HSPID, HS2_DATA3,SD_DATA3, EMAC_RX_ER</td></tr><tr><td colspan="1" rowspan="1">SHD/SD2*</td><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO9, SD_DATA2, SPIHD, HS1_DATA2, U1RXD</td></tr><tr><td colspan="1" rowspan="1">SWP/SD3*</td><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO10, SD_DATA3, SPIWP, HS1_DATA3, U1TXD</td></tr><tr><td colspan="1" rowspan="1">SCS/CMD*</td><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO11, SD_CMD, SPICS0, HS1_CMD, U1RTS</td></tr><tr><td colspan="1" rowspan="1">SCK/CLK*</td><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO6, SD_CLK, SPICLK, HS1_CLK, U1CTS</td></tr><tr><td colspan="1" rowspan="1">SDO/SDO*</td><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO7, SD_DATAO, SPIQ, HS1_DATAO, U2RTS</td></tr><tr><td colspan="1" rowspan="1">SDI/SD1*</td><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO8, SD_DATA1, SPID, HS1_DATA1, U2CTS</td></tr><tr><td colspan="1" rowspan="1">1015</td><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO15, ADC2_CH3, TOUCH3, MTDO, HSPICS0, RTC_GPIO13, HS2_CMD,SD_CMD, EMAC_RXD3</td></tr><tr><td colspan="1" rowspan="1">102</td><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO2, ADC2_CH2, TOUCH2, RTC_GPIO12, HSPIWP, HS2_DATAO,SD_DATAO</td></tr><tr><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">1O</td><td colspan="1" rowspan="1">GPIO0, ADC2_CH1, TOUCH1, RTC_GPIO11, CLK_OUT1, EMAC_TX_CLK</td></tr><tr><td colspan="1" rowspan="1">104</td><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO4, ADC2_CHO, TOUCHO, RTC_GPIO10, HSPIHD, HS2_DATA1,SD_DATA1, EMAC_TX_ER</td></tr><tr><td colspan="1" rowspan="1">1016</td><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO16, HS1_DATA4, U2RXD, EMAC_CLK_OUT</td></tr><tr><td colspan="1" rowspan="1">1017</td><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO17, HS1_DATA5, U2TXD, EMAC_CLK_OUT_180</td></tr><tr><td colspan="1" rowspan="1">105</td><td colspan="1" rowspan="1">29</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO5, VSPICS0, HS1_DATA6, EMAC_RX_CLK</td></tr><tr><td colspan="1" rowspan="1">1018</td><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO18, VSPICLK, HS1_DATA7</td></tr><tr><td colspan="1" rowspan="1">1019</td><td colspan="1" rowspan="1">31</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO19, VSPIQ, U0CTS, EMAC_TxD0</td></tr><tr><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">-</td><td></td></tr><tr><td colspan="1" rowspan="1">1021</td><td colspan="1" rowspan="1">33</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">GPIO21, VSPIHD, EMAC_TX_EN</td></tr><tr><td colspan="1" rowspan="1">RXDO</td><td colspan="1" rowspan="1">34</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO3, UORXD, CLK_OUT2</td></tr><tr><td colspan="1" rowspan="1">TXDO</td><td colspan="1" rowspan="1">35</td><td colspan="1" rowspan="1">1VO</td><td colspan="1" rowspan="1">GPIO1, U0TxD, CLK_OUT3, EMAC_RXD2</td></tr><tr><td colspan="1" rowspan="1">1022</td><td colspan="1" rowspan="1">36</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO22, VSPIWP, U0RTS, EMAC_TXD1</td></tr><tr><td colspan="1" rowspan="1">1023</td><td colspan="1" rowspan="1">37</td><td colspan="1" rowspan="1">VO</td><td colspan="1" rowspan="1">GPIO23, VSPID, HS1_STROBE</td></tr><tr><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">P</td><td colspan="1" rowspan="1">Ground</td></tr></table>

# Notice:

\* Pins SCK/CLK, SDO/SD0, SDI/SD1, SHD/SD2, SWP/SD3 and SCS/CMD, namely, GPIO6 to GPIO11 are connected to the integrated SPI flash integrated on the module and are not recommended for other uses.

# 2.3 Strapping Pins

ESP32 has five strapping pins, which can be seen in Chapter 6 Schematics:

• MTDI • GPIO0 • GPIO2 • MTDO • GPIO5

Software can read the values of these five bits from register ”GPIO_STRAPPING”.

During the chip’s system reset release (power-on-reset, RTC watchdog reset and brownout reset), the latches of the strapping pins sample the voltage level as strapping bits of ”0” or ”1”, and hold these bits until the chip is powered down or shut down. The strapping bits configure the device’s boot mode, the operating voltage of VDD_SDIO and other initial system settings.

Each strapping pin is connected to its internal pull-up/pull-down during the chip reset. Consequently, if a strapping pin is unconnected or the connected external circuit is high-impedance, the internal weak pull-up/pull-down will determine the default input level of the strapping pins.

To change the strapping bit values, users can apply the external pull-down/pull-up resistances, or use the host MCU’s GPIOs to control the voltage level of these pins when powering on ESP32.

After reset release, the strapping pins work as normal-function pins.

Refer to Table 4 for a detailed boot-mode configuration by strapping pins.

Table 4: Strapping Pins   

<table><tr><td rowspan=1 colspan=6>Voltage of Internal LDO (VDD_SDIO)</td></tr><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Default</td><td rowspan=1 colspan=2>3.3V</td><td rowspan=1 colspan=2>1.8V</td></tr><tr><td rowspan=1 colspan=1>MTDI</td><td rowspan=1 colspan=1>Pull- down</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=2>1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>Booting Mode</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Default</td><td rowspan=1 colspan=2>SPI Boot</td><td rowspan=1 colspan=2>Download Boot</td></tr><tr><td rowspan=1 colspan=1>GPIO0</td><td rowspan=1 colspan=1>Pull-up</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=1>GPIO2</td><td rowspan=1 colspan=1>Pull-down</td><td rowspan=1 colspan=2>Don&#x27;t-care</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>Enabling/Disabling Debugging Log Print over UoTXD During Booting</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Default</td><td rowspan=1 colspan=2>UOTXD Active</td><td rowspan=1 colspan=2>UOTXD Silent</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>Pull-up</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=2>0</td></tr><tr><td rowspan=1 colspan=6>Timing of SDIO Slave</td></tr><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Default</td><td rowspan=1 colspan=1>Falling-edge SamplingFalling-edge Output</td><td rowspan=1 colspan=1>Falling-edge SamplingRising-edge Output</td><td rowspan=1 colspan=1>Rising-edge SamplingFaling-edge Output</td><td rowspan=1 colspan=1>Rising-edge SamplingRising-edge Output</td></tr><tr><td rowspan=1 colspan=1>MTDO</td><td rowspan=1 colspan=1>Pull-up</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>GPIO5</td><td rowspan=1 colspan=1>Pull-up</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td></tr></table>

# Note:

• Firmware can configure register bits to change the settings of ”Voltage of Internal LDO (VDD_SDIO)” and ”Timing of SDIO Slave” after booting.   
• Both ESP32-WROOM-32D and ESP32-WROOM-32U integrate a 3.3 V SPI flash, so the pin MTDI cannot be set to 1 when the modules are powered up.

# 3. Functional Description

This chapter describes the modules and functions integrated in ESP32-WROOM-32D and ESP32-WROOM32U.

# 3.1 CPU and Internal Memory

ESP32-D0WD contains a dual-core Xtensa® 32-bit LX6 MCU. The internal memory includes:

• 448 KB of ROM for booting and core functions.   
• 520 KB of on-chip SRAM for data and instructions.   
• 8 KB of SRAM in RTC, which is called RTC FAST Memory and can be used for data storage; it is accessed by the main CPU during RTC Boot from the Deep-sleep mode.   
• 8 KB of SRAM in RTC, which is called RTC SLOW Memory and can be accessed by the co-processor during the Deep-sleep mode.   
• 1 Kbit of eFuse: 256 bits are used for the system (MAC address and chip configuration) and the remaining 768 bits are reserved for customer applications, including flash-encryption and chip-ID.

# 3.2 External Flash and SRAM

ESP32 supports multiple external QSPI flash and SRAM chips. More details can be found in Chapter SPI in the ESP32 Technical Reference Manual. ESP32 also supports hardware encryption/decryption based on AES to protect developers’ programs and data in flash.

ESP32 can access the external QSPI flash and SRAM through high-speed caches.

• The external flash can be mapped into CPU instruction memory space and read-only memory space simultaneously.

– When external flash is mapped into CPU instruction memory space, up to 11 MB + 248 KB can be mapped at a time. Note that if more than 3 MB + 248 KB are mapped, cache performance will be reduced due to speculative reads by the CPU.

– When external flash is mapped into read-only data memory space, up to 4 MB can be mapped at a time. 8-bit, 16-bit and 32-bit reads are supported.

• External SRAM can be mapped into CPU data memory space. Up to 4 MB can be mapped at a time. 8-bit, 16-bit and 32-bit reads and writes are supported.

Both ESP32-WROOM-32D and ESP32-WROOM-32U integrate a 4 MB of external SPI flash. The integrated SPI flash is connected to GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 and GPIO11. These six pins cannot be used as regular GPIOs.

# 3.3 Crystal Oscillators

The module uses a 40-MHz crystal oscillator.

# 3.4 RTC and Low-Power Management

With the use of advanced power-management technologies, ESP32 can switch between different power modes.

For details on ESP32’s power consumption in different power modes, please refer to section ”RTC and Low-Power Management” in ESP32 Datasheet.

# 4. Peripherals and Sensors

Please refer to Section Peripherals and Sensors in ESP32 Datasheet.

# Note:

External connections can be made to any GPIO except for GPIOs in the range 6-11. These six GPIOs are connected to the module’s integrated SPI flash. For details, please see Section 6 Schematics.

# 5. Electrical Characteristics

# 5.1 Absolute Maximum Ratings

Stresses beyond the absolute maximum ratings listed in Table 5 below may cause permanent damage to the device. These are stress ratings only, and do not refer to the functional operation of the device that should follow the recommended operating conditions.

Table 5: Absolute Maximum Ratings   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=1>Power supply voltage</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>loutput1</td><td rowspan=1 colspan=1>Cumulative lO output current</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1,100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Tstore</td><td rowspan=1 colspan=1>Storage temperature</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>℃</td></tr></table>

1. The module worked properly after a 24-hour test in ambient temperature at 25 °C, and the IOs in three domains (VDD3P3_RTC, VDD3P3_CPU, VDD_SDIO) output high logic level to ground. Please note that pins occupied by flash and/or PSRAM in the VDD_SDIO power domain were excluded from the test.

# 5.2 Recommended Operating Conditions

Table 6: Recommended Operating Conditions   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typical</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>VDD33</td><td rowspan=1 colspan=1>Power supply voltage</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IVDD</td><td rowspan=1 colspan=1>Current delivered by external power supply</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>Operating temperature</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>℃</td></tr></table>

# 5.3 DC Characteristics (3.3 V, 25 °C)

Table 7: DC Characteristics (3.3 V, 25 °C)   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>CIN</td><td rowspan=1 colspan=2>Pin capacitance</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>pF</td></tr><tr><td rowspan=1 colspan=1>$VIH</td><td rowspan=1 colspan=2>High-level input voltage</td><td rowspan=1 colspan=1>0.75×VDD1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>VDD1+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=2>Low-level input voltage</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.25×VDD1</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>1H</td><td rowspan=1 colspan=2>High-level input current</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>nA</td></tr><tr><td rowspan=1 colspan=1>IL</td><td rowspan=1 colspan=2>Low-level input current</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>nA</td></tr><tr><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=2>High-level output voltage</td><td rowspan=1 colspan=1>0.8×VDD1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOL</td><td rowspan=1 colspan=2>Low-level output voltage</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.1×VDD1</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=3 colspan=1>lOH</td><td rowspan=3 colspan=1>High-level source currentVDD1 = 3.3V, VoH &gt;= 2.64 V,output drive strength set to themaximum)</td><td rowspan=1 colspan=1>VDD3P3_CPU power domain 1, 2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>VDD3P3_RTC power domain 1, 2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>VDD_SDIO power domain 1, 3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>l0L</td><td rowspan=1 colspan=1>Low-level sink currentWDD1 = 3.3 V, VoL = 0.495 V,output drive strength set to the maximum)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>RPU</td><td rowspan=1 colspan=1>Resistance of internal pull-up resistor</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kΩ2</td></tr><tr><td rowspan=1 colspan=1>RPD</td><td rowspan=1 colspan=1>Resistance of internal pull-down resistor</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kΩ</td></tr><tr><td rowspan=1 colspan=1>VIL_nRST</td><td rowspan=1 colspan=1>Low-level input voltage of CHlP_PU to power of the chip</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr></table>

# Notes:

1. Please see Appendix IO_MUX of ESP32 Datasheet for IO’s power domain. VDD is the I/O voltage for a particular power domain of pins. 2. For VDD3P3_CPU and VDD3P3_RTC power domain, per-pin current sourced in the same domain is gradually reduced from around 40 mA to around 29 mA, VOH>=2.64 V, as the number of current-source pins increases. 3. Pins occupied by flash and/or PSRAM in the VDD_SDIO power domain were excluded from the test.

# 5.4 Wi-Fi Radio

Table 8: Wi-Fi Radio Characteristics   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typical</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Operating frequency range notel1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2412</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2484</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>Output impedance note2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>note 2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=2 colspan=1>TX power note3</td><td rowspan=1 colspan=1>11n, MCS7</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11b mode</td><td rowspan=1 colspan=1>17.5</td><td rowspan=1 colspan=1>18.5</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=8 colspan=1>Sensitivity</td><td rowspan=1 colspan=1>11b,1 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-98</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11b,11 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-89</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-92</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-74</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-91</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-71</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-89</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>11n, HT40, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-69</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=4 colspan=1>Adjacent channel rejection</td><td rowspan=1 colspan=1>11g, 6 Mbps</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11g, 54 Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>11n, HT20, MCS7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr></table>

1. Device should operate in the frequency range allocated by regional regulatory authorities. Target operating frequency range is configurable by software. 2. For the modules that use IPEX antennas, the output impedance is 50 Ω. For other modules without IPEX antennas, users do not need to concern about the output impedance. 3. Target TX power is configurable based on device or certification requirements.

# 5.5 BLE Radio

# 5.5.1 Receiver

Table 9: Receiver Characteristics – BLE   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Sensitivity @30.8% PER</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-97</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>Maximum received signal @30.8% PER</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>Co-channel C/I</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>+10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=6 colspan=1>Adjacent channel selectivity C/I</td><td rowspan=1 colspan=1>F = FO + 1 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO- 1 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO-2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-35</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO + 3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>F = FO-3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-45</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=4 colspan=1>Out-of-band blocking performance</td><td rowspan=1 colspan=1>30 MHz~2000 MHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2000 MHz~2400 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>2500 MHz~3000 MHz</td><td rowspan=1 colspan=1>-27</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>3000 MHz~12.5 GHz</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>Intermodulation</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-36</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr></table>

# 5.5.2 Transmitter

Table 10: Transmitter Characteristics – BLE   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>RF transmit power</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>Gain control step</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>RF power control range</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-12</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>+9</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=3 colspan=1>Adjacent channel transmit power</td><td rowspan=1 colspan=1>F = FO ± 2 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-52</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = FO ± 3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-58</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>F = FO ± &gt; 3 MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-60</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dBm</td></tr><tr><td rowspan=1 colspan=1>∆ flavg</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>265</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2max</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>247</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>∆ f2avg/Δ flavg</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-0.92</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>ICFT</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>Drift rate</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>KHz/50μS</td></tr><tr><td rowspan=1 colspan=1>Driftt</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>kHz</td></tr></table>

# 5.6 Reflow Profile

![](images/7ac8a3ad59e1a84fd845cb19d19f0c779b7530205f0d25eda4a441ce9d060e26.jpg)  
Figure 2: Reflow Profile

Ramp-up zone — Temp.: <150℃ Time: 60 \~ 90s Ramp-up rate: 1 \~ 3℃/s   
Preheating zone — Temp.: 150 \~ 200℃ Time: 60 \~ 120s Ramp-up rate: 0.3 \~ 0.8℃/s   
Reflow zone — Temp.: >217℃ 7LPH60 \~ 90s; Peak Temp.: 235 \~ 250℃ (<245℃ recommended) Time: 30 \~ 70s   
Cooling zone — Peak Temp. \~ 180℃ Ramp-down rate: -1 \~ -5℃/s   
Solder — Sn&Ag&Cu Lead-free solder (SAC305)

![](images/8e0f3f68d376db98b381795995821348b164164f4f98e4d15af2ce19b88d4c17.jpg)  
Figure 3: ESP32-WROOM-32D Schematics

![](images/ba177740ab54fd05a80932f5c0a653866558f27ffd6b30b75d1fbda9c41be570.jpg)  
Figure 4: ESP32-WROOM-32U Schematics

![](images/f8cef596cd12722a862741ed7eecb17ccbe95fd7f1ff0ee9a8277cbba5cc4849.jpg)  
Figure 5: ESP32-WROOM-32D & ESP32-WROOM-32U Peripheral Schematics

# Note:

• Solderi ng Pad 39 to the G rou nd is not necessary for a satisfactory thermal performance . If users do want to solder it , they need to ensu re that the correct q uantity of solderi ng paste is appl ied .   
• When ESP32 is powered on and off repeated ly by switch i ng the power rai ls , and there is a large capacitor on the 3V3 rai l , a d ischarge ci rcu it can be added to the 3V3 rai l to ensu re proper power-on - reset . Please fi nd the d ischarge ci rcu it i n Chapter Peripheral Schematics , i n ESP32- WROOM-32 Datasheet.   
• When battery is used as the power su pply for ESP32 series of ch i ps and mod u les , a su pply voltage su pervisor is recom mended to avoid boot fai l u re d ue to low voltage . Users are recom mended to pu l l CH I P_PU low if the power su pply for ESP32 is below 2 . 3 V. For the reset ci rcu it , please refer to Chapter Peripheral Schematics , i n ESP32- WROOM-32 Datasheet.   
To ensu re the power su pply to the ESP32 ch i p d u ri ng power- u p , it is advised to add an RC delay ci rcu it at the EN pi n . The recom mended setti ng for the RC delay ci rcu it is usual ly and C = 0 . 1 µF. However, specific parameters shou ld be adj usted based on the power- u p ti m i ng of the mod u le and the power- u p and reset seq uence ti m i ng of the ch i p . Power Scheme i n ESP32 Datasheet.

![](images/a126fdbeb5af66b12bb40680ca1a9c33fe121bbd8c7557c32849e37429f673cb.jpg)  
Unit: mm   
Figure 6: Physical Dimensions of ESP32-WROOM-32D

![](images/17903ab50d4e90c4ddf265230ef010e94b6dbc3adddffa394e1cbec63ab51a58.jpg)  
Figure 7: Physical Dimensions of ESP32-WROOM-32U

# 9. Recommended PCB Land Pattern

![](images/dd18210237bc5720685fda43ecd50ea7d185559fc266bbeee57177db3ef829a4.jpg)  
Figure 8: Recommended PCB Land Pattern of ESP32-WROOM-32D

![](images/bc3e9366d3f2ab6f3f2dd3ea7538e2a21d85e1dd50b6cdc50ab92e7be6cd6cf4.jpg)  
Figure 9: Recommended PCB Land Pattern of ESP32-WROOM-32U

# 10. U.FL Connector Dimensions

![](images/560fa43e101d0db75baa53c83ce9f3dd2a2056259fd1ab17a3a8e889a2677a86.jpg)  
Figure 10: ESP32-WROOM-32U U.FL Dimensions

# 11. Learning Resources

# 11.1 Must-Read Documents

The following link provides documents related to ESP32.

# • ESP32 Datasheet

This document provides an introduction to the specifications of the ESP32 hardware, including overview, pin definitions, functional description, peripheral interface, electrical characteristics, etc.

• ESP-IDF Programming Guide It hosts extensive documentation for ESP-IDF ranging from hardware guides to API reference.

ESP32 Technical Reference Manual The manual provides detailed information on how to use the ESP32 memory and peripherals.

• ESP32 Hardware Resources

The zip files include the schematics, PCB layout, Gerber and BOM list of ESP32 modules and development boards.

• ESP32 Hardware Design Guidelines

The guidelines outline recommended design practices when developing standalone or add-on systems based on the ESP32 series of products, including the ESP32 chip, the ESP32 modules and development boards.

• ESP32 AT Instruction Set and Examples

This document introduces the ESP32 AT commands, explains how to use them, and provides examples of several common AT commands.

• Espressif Products Ordering Information

# 11.2 Must-Have Resources

Here are the ESP32-related must-have resources.

# • ESP32 BBS

This is an Engineer-to-Engineer (E2E) Community for ESP32 where you can post questions, share knowledge, explore ideas, and help solve problems with fellow engineers.

# • ESP32 GitHub

ESP32 development projects are freely distributed under Espressif’s MIT license on GitHub. It is established to help developers get started with ESP32 and foster innovation and the growth of general knowledge about the hardware and software surrounding ESP32 devices.

# • ESP32 Tools

This is a webpage where users can download ESP32 Flash Download Tools and the zip file ”ESP32 Certification and Test”.

# • ESP-IDF

This webpage links users to the official IoT development framework for ESP32.

# • ESP32 Resources

This webpage provides the links to all available ESP32 documents, SDK and tools.

# Revision History

<table><tr><td>Date</td><td>Version</td><td>Release notes</td></tr><tr><td>2019.09</td><td>V1.9</td><td>• Changed the supply voltage range from 2.7 V ~ 3.6 V to 3.0 V ~ 3.6 V; • Added Moisture sensitivity level (MSL) 3 in Table 2 ESP32-WROOM-32D and ESP32-WROOM-32U Specifications; • Added notes about &quot;Operating frequency range&quot; and &quot;TX power&quot; under Table 8 Wi-Fi Radio Characteristics; • Updated Section 7 Peripheral Schematics and added a note about RC delay circuit under it;</td></tr><tr><td>2019.01</td><td>V1.8</td><td>• Updated Figure 8 and Figure 9 Recommended PCB Land Pattern. Changed the RF power control range in Table 10 from -12 ~ +12 to -12 ~ +9 dBm.</td></tr><tr><td>2018.10</td><td>V1.7</td><td>Added notice on module custom options under Table 2; Added &quot;Cumulative IO output current&quot; entry to Table 5: Absolute Maximum Ratings;</td></tr><tr><td>2018.09</td><td>V1.6</td><td>Added more parameters to Table 7: DC Characteristics. Updated the hole diameter in the shield from 1.00 mm to 0.50 mm, in Figure 6.</td></tr><tr><td>2018.08</td><td>V1.5</td><td>• Added certifications and reliability test items the module has passed in Table 2: ESP32-WROOM-32D and ESP32-WROOM-32U Specifications, and removed software-specific information; • Updated section 3.4: RTC and Low-Power Management; • Changed the modules&#x27; dimensions; • Updated Figure 8 and 7: Physical Dimensions; • Updated Table 8: Wi-Fi Radio.</td></tr><tr><td>2018.06</td><td>V1.4</td><td>• Deleted Temperature Sensor in Table 2: ESP32-WROOM-32D &amp; ESP32- WROOM-32U Specifications; • Updated Chapter 3: Functional Description; • Added notes to Chapter 7: Peripheral Schematics; • Added Chapter 8: Recommended PCB Land Pattern; Changes to electrical characteristics: • Updated Table 5: Absolute Maximum Ratings; • Added Table 6: Recommended Operating Conditions; • Added Table 7: DC Characteristics; • Updated the values of &quot;Gain control step&quot;, &quot;Adjacent channel transmit power&quot;</td></tr><tr><td>2018.04</td><td>V1.3</td><td>in Table 10: Transmitter Characteristics - BLE. Updated Figure 4 ESP32-WROOM-32U Schematics and Figure 3 ESP32-WROOM- 32D Schematics.</td></tr><tr><td>2018.02</td><td>V1.2</td><td>Update Figure 4 ESP32-WROOM-32U Schematics. Updated Chapter 6 Schematics.</td></tr><tr><td>2018.02</td><td>V1.1</td><td>Deleted description of low-noise amplifier. Replaced the module name ESP-WROOM-32D with ESP32-WROOM-32D. Added information about module certification in Table 2.</td></tr><tr><td>2017.11</td><td>V1.0</td><td>Updated the description of eFuse bits in Section 3.1. First release.</td></tr></table>