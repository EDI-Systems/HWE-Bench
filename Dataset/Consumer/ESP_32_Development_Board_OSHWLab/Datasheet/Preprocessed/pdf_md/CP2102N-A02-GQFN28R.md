# USBXpress™ Family CP2102N Data Sheet

The CP2102N devices, part of the USBXpress family, are designed to quickly add USB to your applications by eliminating firmware complexity and reducing development time.

These highly-integrated USB-to-UART bridge controllers provide a simple solution for updating RS-232 designs to USB using a minimum of components and PCB space. CP2102N includes a USB 2.0 full-speed function controller, USB transceiver, oscillator, and Universal Asynchronous Receiver/Transmitter (UART) in packages as small as 3 mm x 3 mm. No other external USB components are required for development. All customization and configuration options can be selected using a simple GUI-based configurator. By eliminating the need for complex firmware and driver development, the CP2102N devices enable quick USB connectivity with minimal development effort.

CP2102N is ideal for a wide range of applications, including the following:

• POS terminals • USB dongles • Gaming controllers • Medical equipment • Data loggers

# KEY FEATURES

• No firmware development required   
• Simple GUI-based configurator   
• Integrated USB transceiver; no external resistors required   
• Integrated clock; no external crystal required   
• USB 2.0 full-speed compatible   
• Data transfer rates up to 3 Mbaud   
• USB Battery Charger Detection (USB BCS 1.2 Specification)   
• Remote wakeup for waking a suspended host   
• Low operating current : 9.5 mA   
• Royalty-free Virtual COM port drivers

![](images/b83129cc79749d9b3651b6cf76a09b1233e61aaa3fb68afa392950d0aaa1ee42.jpg)

# 1. Feature List and Ordering Information

![](images/033427c0914aeac7a80f0865e74443b5eafa752114547d5804e139917dc7a216.jpg)  
Figure 1.1. CP2102N Part Numbering

The CP2102N devices have the following features:

# • Single-Chip USB-to-UART Data Transfer

• Integrated USB transceiver; no external resistors required   
• Integrated clock; no external crystal required   
• Internal 960-byte programmable ROM for vendor ID, product ID, serial number, power descriptor, release number, and product description strings   
• On-chip power-on reset circuit   
• On-chip voltage regulator — 3.3 V output   
• Pin compatible with CP2101/2/9 (QFN28 package)   
• Pin compatible with CP2104 (QFN24 package)

# • USB Function Controller

• USB Specification 2.0 compliant; full-speed (12 Mbps) • USB suspend states supported via SUSPEND pins • USB Battery Charger Detection (USB BCS 1.2 Specification) • Remote wakeup for waking a suspended host

• Single power supply of 3.0 to 3.6 V or 3.0 to 5.25 V

# • Universal Asynchronous Receiver/Transmitter (UART)

• All handshaking and modem interface signals   
• Data formats supported • Data bits — 5, 6, 7, and 8 • Stop bits — 1, 1.5, and 2 • Parity — odd, even, mark, space, no parity   
• Baud rates: 300 baud to 3 Mbaud   
• 512 byte receive buffer   
• 512 byte transmit buffer   
• Hardware or Xon/Xoff handshaking supported

# • Virtual COM Port Device Drivers

• Works with existing COM port Applications • Supported on Windows, Mac, and Linux • Royalty-free distribution license

# • Direct Driver Support

• Royalty-free distribution license

<table><tr><td rowspan=1 colspan=1>Jaqunn uedaao</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>abuey aungenaduar</td><td rowspan=1 colspan=1>aneyoed</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A02-GQFN28</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85 °℃</td><td rowspan=1 colspan=1>QFN28</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A02-GQFN24</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85 ℃</td><td rowspan=1 colspan=1>QFN24</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A02-GQFN20</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85 ℃</td><td rowspan=1 colspan=1>QFN20</td></tr></table>

# Note:

1. Devices with the same ordering part number may have different types of pin 1 indicators. However, all of these variants can use the same landing diagram as long as the recommended landing diagram instructions are followed.

# Table of Contents

1. Feature List and Ordering Information . . . . 2

2. Typical Connection Diagrams . .

2.1 Power . . . . . 5   
2.2 Battery Charger Detect .   
2.3 USB . 8

# 3. Electrical Specifications . 10

3.1 Electrical Characteristics .10

3.1.1 Recommended Operating Conditions . .10   
3.1.2 Power Consumption. .10   
3.1.3 Reset and Supply Monitor . .11   
3.1.4 Configuration Memory .11   
3.1.5 Internal Oscillator. .11   
3.1.6 5 V Voltage Regulator .12   
3.1.7 GPIO. .13   
3.1.8 USB Transceiver . .14

3.2 Thermal Conditions .1

3.3 Absolute Maximum Ratings. . .15

3.4 Typical Performance Curves . .16

# Functional Description . . . . 17

4.1 USB Function Controller and Transceiver . . .17

4.2 Universal Asynchronous Receiver/Transmitter (UART) Interface .17   
4.2.1 Baud Rate Generation . .18   
4.2.2 Sending Break Signaling . .18

4.3 Additional Features .1

4.3.1 General Purpose Input/Outputs (GPIO) . .19

4.3.2 Dynamic Suspend . . . . . . .19

4.3.3 Output Mode . . . . . .19

4.3.4 Battery Charging (CHREN, CHR0, and CHR1) . .20

4.3.5 Remote Wakeup (WAKEUP) . .20

4.3.6 Clock Output (CLK) . . . . . . .20

4.3.7 Hardware Handshaking (RTS and CTS) . . .21

4.3.9 Data Throughput Optimization .22

4.3.10 Transmit and Receive LED Toggles (TXT and RXT) .23

4.3.11 Modem Control (DSR, DTR, DCD, RI) .23   
4.3.12 RS485 (RS485) . .24

4.3.13 Receiver Timeout . .24

.4 Drivers. .24

4.4.1 Virtual COM Port (VCP) Drivers . .25

4.4.2 USBXpress Drivers . .25

4.4.3 Customization and Certification . .25

# 4.5 Device Customization .26

Pin Definitions . . . 2

5.1 CP2102N QFN28 Pin Definitions . .27   
5.2 CP2102N QFN24 Pin Definitions . .29   
5.3 CP2102N QFN20 Pin Definitions . .31

# 6. QFN28 Package Specifications. . . 33

6.1 QFN28 Package Dimensions . .33   
6.2 QFN28 PCB Land Pattern . .35   
6.3 QFN28 Package Marking .36

# 7. QFN24 Package Specifications. . . 37

7.1 QFN24 Package Dimensions . .37   
7.2 PCB Land Pattern . .39   
7.3 Package Marking . .40

# 8. QFN20 Package Specifications. . . 4

8.1 QFN20 Package Dimensions . . .41   
8.2 QFN20 PCB Land Pattern . .43   
8.3 QFN20 Package Marking .44

9. Relevant Application Notes . . . 45

10. Revision History. . . . . 46

# 2. Typical Connection Diagrams

# 2.1 Power

In all cases, a 1 kΩ pull-up on the RSTb pin is recommended. This pull-up should be tied to VIO on devices that have it. On devices where VIO is connected to VDD or devices that do not have VIO, this pull-up should be tied to VDD. The RSTb pin will be driven low during power-on and power failure reset events.

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal regulator is used and USB is connected (bus-powered).

4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.

![](images/f68184fb3dca895713ad5be6ed33b152e869d6a0cfabd9bbb827207081604a23.jpg)  
Figure 2.1. Connection Diagram with Voltage Regulator Used and USB Connected (Bus-Powered)

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal regulator is used and USB is connected (self-powered).

4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.

![](images/e85120363e38118fd69ae8dfa2b1d72ef8043897c42657bae8fed3068f4319df.jpg)  
Figure 2.2. Connection Diagram with Voltage Regulator Used and USB Connected (Self-Powered)

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal 5 V-to-3.3 V regulator is not used.

![](images/90d63329dd0dadb6bc144f71628a3dacbf5fb5097ce3820e9edccf1c9fc47e2b.jpg)  
4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.   
Figure 2.3. Connection Diagram with Voltage Regulator Not Used

# 2.2 Battery Charger Detect

he CP2102N Battery Charger Detect notifies an external battery charger the amount of current available from the USB interface.

The figure below shows an example connection diagram for external battery charging circuitry. If using an external battery charging IC consult the data sheet for more information about the specific recommended connection diagrams.

![](images/be5268ac27e29ed4e7884b420965293cd39ed7f8b829b12d9762f08e219f2cfc.jpg)  
Figure 2.4. Battery Charging Connection Diagram

# 2.3 USB

The figure below shows a typical connection bus-powered diagram for the USB pins of the CP2102N devices including ESD protection diodes on the USB pins.

Note: There are two relevant restrictions on the VBUS pin voltage in self-powered and bus-powered configurations. The first is the absolute maximum voltage on the VBUS pin, which is defined as VIO + 2.5 V in Table 3.10 Absolute Maximum Ratings on page 15. The second is the Input High Voltage (VIH) for VBUS to detect when the device is connected to a bus, which is defined as VIO – 0.6 V in Table 3.7 GPIO on page 13. A resistor divider (or functionally-equivalent circuit) on VBUS is required to meet these specifications and ensure reliable device operation. In this case, the current limitation of the resistor divider prevents high VBUS pin leakage current, even though the VIO + 2.5 V specification is not strictly met while the device is not powered.

![](images/9258098e036f89f955269f0390bc6a9ae90db632d7d9f666b464bdcca1be2633.jpg)  
Figure 2.5. Bus-Powered Connection Diagram for USB Pins

The figure below shows a typical connection self-powered diagram for the USB pins of the CP2102N devices including ESD protection diodes on the USB pins.

Note: There are two relevant restrictions on the VBUS pin voltage in self-powered and bus-powered configurations. The first is the absolute maximum voltage on the VBUS pin, which is defined as VIO + 2.5 V in Table 3.10 Absolute Maximum Ratings on page 15. The second is the Input High Voltage (VIH) for VBUS to detect when the device is connected to a bus, which is defined as VIO – 0.6 V in Table 3.7 GPIO on page 13. A resistor divider (or functionally-equivalent circuit) on VBUS is required to meet these specifications and ensure reliable device operation. In this case, the current limitation of the resistor divider prevents high VBUS pin leakage current, even though the VIO + 2.5 V specification is not strictly met while the device is not powered.

![](images/68af12b7fccb8c1a193036af0b59404cc0eea4a0bdcf54d035c165aae453841a.jpg)  
Figure 2.6. Self-Powered Connection Diagram for USB Pins

# 3. Electrical Specifications

# 3.1 Electrical Characteristics

All electrical parameters in all tables are specified under the conditions listed in Table 3.1 Recommended Operating Conditions on page 0, unless stated otherwise.

# 3.1.1 Recommended Operating Conditions

Table 3.1. Recommended Operating Conditions   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Operating Supply Voltage on VDD1</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Operating Supply Voltage on VI0 3</td><td rowspan=1 colspan=1>Vio</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Operating Supply Voltage on VRE-GIN</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Operating Ambient Temperature</td><td rowspan=1 colspan=1>TA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>C</td></tr></table>

# Note:

1. Standard USB compliance tests require 3.0 V on VDD for compliant operation.   
2. All voltages with respect to GND.   
3. On devices without a VIO pin, VIO = VDD.   
4. GPIO levels are undefined whenever VIO is less than 1 V.

# 3.1.2 Power Consumption

Table 3.2. Power Consumption   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=2 colspan=1>Normal Operation1, 2</td><td rowspan=2 colspan=1>IDD</td><td rowspan=1 colspan=1>115200 baud transmitting continu-ous bidirectional data</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>9.5</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>3 Mbaud transmitting continuousbidirectional data</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>USB Suspend1, 2</td><td rowspan=1 colspan=1>1DD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>195</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Held in Reset1, 2</td><td rowspan=1 colspan=1>IDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>USB Pull-up3</td><td rowspan=1 colspan=1>IPU</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>230</td><td rowspan=1 colspan=1>μA</td></tr></table>

# Note:

1. Includes supply current from internal LDO regulator, supply monitor, and internal oscillators. These power consumption numbers are only for the CP2102N and do not include an external RS232 transceiver or other external circuitry.

2. USB Pull-up current should be added for total supply current. Normal and suspended supply current is current flowing into VREGIN.

3. The USB Pull-up supply current values are calculated values based on USB specifications. USB Pull-up supply current is current flowing from VDD to GND through USB pull-down/pull-up resistors on D+ and D-.

# 3.1.3 Reset and Supply Monitor

Table 3.3. Reset and Supply Monitor   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>VDD Supply Monitor Threshold</td><td rowspan=1 colspan=1>VVDDM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.95</td><td rowspan=1 colspan=1>2.05</td><td rowspan=1 colspan=1>2.15</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Power-On Reset (POR) Threshold</td><td rowspan=2 colspan=1>VPOR</td><td rowspan=1 colspan=1>Rising Voltage on VDD</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Falling Voltage on VDD</td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.36</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VDD Ramp Time</td><td rowspan=1 colspan=1>tRMP</td><td rowspan=1 colspan=1>Time to VDD &gt; 2.2 V</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Reset Delay from POR</td><td rowspan=1 colspan=1>tPOR</td><td rowspan=1 colspan=1>Relative to VDD &gt;VpOR</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>Reset Delay from non-POR source</td><td rowspan=1 colspan=1>tRST</td><td rowspan=1 colspan=1>Time between release of resetsource and code execution</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>RSTb Low Time to Generate Reset</td><td rowspan=1 colspan=1>RSTL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μs</td></tr></table>

1. The RSTb pin will be driven low during power-on and power failure reset events.

# Note:

# 3.1.4 Configuration Memory

Table 3.4. Configuration Memory   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=1>VDD Voltage During Programming</td><td rowspan=1 colspan=1>VPROG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Endurance (Write/Erase Cycles)</td><td rowspan=1 colspan=1>NWE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20k</td><td rowspan=1 colspan=1>100k</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Cycles</td></tr></table>

# Note:

1. The device can be safely programmed at any voltage above the supply monitor threshold (VVDDM).

2. Data Retention Information is published in the Quarterly Quality and Reliability Report.

# 3.1.5 Internal Oscillator

Table 3.5. Internal Oscillator   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1> Internal Oscillator Frequency</td><td rowspan=1 colspan=1>fosc</td><td rowspan=1 colspan=1>Full Temperature and SupplyRange</td><td rowspan=1 colspan=1>47.3</td><td rowspan=1 colspan=1>48</td><td rowspan=1 colspan=1>48.7</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>Power Supply Sensitivity</td><td rowspan=1 colspan=1>PSSosc</td><td rowspan=1 colspan=1>TA=25C$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>/</td><td rowspan=1 colspan=1>%N</td></tr><tr><td rowspan=1 colspan=1>Temperature Sensitivity</td><td rowspan=1 colspan=1>TSoSC</td><td rowspan=1 colspan=1>VDD=3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>ppm/°℃</td></tr></table>

# 3.1.6 5 V Voltage Regulator

Table 3.6. 5V Voltage Regulator   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Input Voltage Range 1</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Voltage on VDD 2</td><td rowspan=2 colspan=1>VREGOUT</td><td rowspan=1 colspan=1>Output Current = 1 to 100 mARegulation range (VREGIN ≥ 4.1V)</td><td rowspan=1 colspan=1>3.1</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Current = 1 to 100 mADropout range (VREGIN &lt; 4.1V)</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>VREGIN-VDROPOUT</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Current 2</td><td rowspan=1 colspan=1>IREGOUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Dropout Voltage</td><td rowspan=1 colspan=1>VDROPOUT</td><td rowspan=1 colspan=1>Output Current = 100 mA</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr></table>

# Note:

1. Input range to meet the Output Voltage on VDD specification. If the 5 V voltage regulator is not used, VREGIN should be tied to VDD.   
2. Output current is total regulator output, including any current required by the device.

# 3.1.7 GPIO

Table 3.7. GPIO   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=2 colspan=1>Output High Voltage (High Drive)</td><td rowspan=2 colspan=1>VOH</td><td rowspan=1 colspan=1>IOH = -7 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>V10-0.7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IOH = -3.3 mA, 2.2V≤Vio&lt;3.0VIOH = -1.8 mA, 1.71 V≤ Vio &lt;2.2 V</td><td rowspan=1 colspan=1>V\o×0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Low Voltage (High Drive)</td><td rowspan=2 colspan=1>VoL</td><td rowspan=1 colspan=1>IoL = 13.5 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IoL = 7mA, 2.2 V≤ V1o&lt; 3.0 VIoL = 3.6 mA, 1.71V≤ VIo&lt;2.2V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V1o×0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output High Voltage (Low Drive)</td><td rowspan=2 colspan=1>VOH</td><td rowspan=1 colspan=1>IOH = -4.75 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>V10-0.7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IOH = -2.25 mA, 2.2 V≤Vio &lt;3.0VIOH = -1.2 mA, 1.71 V≤ Vio&lt;2.2 V</td><td rowspan=1 colspan=1>V\10×0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Low Voltage (Low Drive)</td><td rowspan=2 colspan=1>VoL</td><td rowspan=1 colspan=1>1OL =6.5 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IoL = 3.5 mA, 2.2V≤V1o&lt;3.0VIoL = 1.8 mA, 1.71V≤Vio&lt;2.2V</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V1o×0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input High Voltage(all GPIO pins including VBUS)</td><td rowspan=1 colspan=1>VH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V10-0.6</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Low Voltage(all GPIO including VBUS)</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Pin Capacitance</td><td rowspan=1 colspan=1>C1o</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>pF</td></tr><tr><td rowspan=1 colspan=1>Weak Pull-Up CUurrent(ViN = 0V)</td><td rowspan=1 colspan=1>IpU</td><td rowspan=1 colspan=1>VDD=3.6</td><td rowspan=1 colspan=1>-30</td><td rowspan=1 colspan=1>-20</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Input Leakage (Pullups ff or Ana-10g)</td><td rowspan=1 colspan=1>ILK</td><td rowspan=1 colspan=1>GND &lt;VIN &lt;VIO</td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Input Leakage Current wit VNabove Vio</td><td rowspan=1 colspan=1>ILK</td><td rowspan=1 colspan=1>VI0&lt;ViN&lt;V1o+2.0V</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>MA</td></tr><tr><td rowspan=1 colspan=1>RS485 Setup Time before StartBit1</td><td rowspan=1 colspan=1>tRS485S</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>64.02</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>RS485 Hold Time after Stop Bit&#x27;1</td><td rowspan=1 colspan=1>tRS485H</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>64.02</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>TX Toggle Rate</td><td rowspan=1 colspan=1>fTxTOGGLE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>RX Toggle Rate</td><td rowspan=1 colspan=1>fRXTOGGLE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Hz</td></tr></table>

# Note:

1. Programmable from 0 ms to 64 ms in 1 µs steps. The programmed time is the guaranteed minimum, and the actual time may be up to 20 µs longer.

# 3.1.8 USB Transceiver

Table 3.8. USB Transceiver   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=7>Transmitter</td></tr><tr><td rowspan=1 colspan=1>Output High Voltage</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>VDD≥3.0V</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage</td><td rowspan=1 colspan=1>VOL</td><td rowspan=1 colspan=1>VD≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Crossover Point</td><td rowspan=1 colspan=1>VCRS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Impedance</td><td rowspan=1 colspan=1>ZDRV</td><td rowspan=1 colspan=1>Driving HighDriving Low</td><td rowspan=1 colspan=1>2828</td><td rowspan=1 colspan=1>3636</td><td rowspan=1 colspan=1>4444</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>Pull-up Resistance</td><td rowspan=1 colspan=1>RpU</td><td rowspan=1 colspan=1>Full Speed (D+ Pul-up)</td><td rowspan=1 colspan=1>1.425</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.575</td><td rowspan=1 colspan=1>ko</td></tr><tr><td rowspan=1 colspan=1>Output Rise Time</td><td rowspan=1 colspan=1>Tr</td><td rowspan=1 colspan=1>Full Speed</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>Output Fall Time</td><td rowspan=1 colspan=1>TF$</td><td rowspan=1 colspan=1>Full peed</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=6>Receiver</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Differentia InputSensitivity</td><td rowspan=1 colspan=1>VD1</td><td rowspan=1 colspan=1>| (D+) - (D-) |1</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Differential Input Common ModeRange</td><td rowspan=1 colspan=1>VcM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1> Input Leakage Current</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>Pullups Disabled</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>&lt;1.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>Refer to the USB Specification for timing diagrams and symbol definitions.</td></tr></table>

# 3.2 Thermal Conditions

Table 3.9. Thermal Conditions   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=3 colspan=1>Thermal Resistance (Junction toAmbient)</td><td rowspan=3 colspan=1>θJA</td><td rowspan=1 colspan=1>QFN20 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN24 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN28 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=3 colspan=1>Thermal Resistance (Junction toCase)</td><td rowspan=3 colspan=1>θJc</td><td rowspan=1 colspan=1>QFN20 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>32.9</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=1 colspan=1>QFN24 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>24.2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN28 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>18.8</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=3 colspan=1>Thermal Characterization Parame-ter (Junction to Top)</td><td rowspan=3 colspan=1>4JT</td><td rowspan=1 colspan=1>QFN20 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.88</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN24 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN28 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr></table>

ote: 1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.

# 3.3 Absolute Maximum Ratings

Stresses above those listed in 3.3 Absolute Maximum Ratings may cause permanent damage to the device. This is a stress rating only and functional operation of the devices at those or any other conditions above those indicated in the operation listings of this specification is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability. For more information on the available quality and reliability data, see the Quality and Reliability Monitor Report at http://www.silabs.com/support/quality/pages/ default.aspx.

Table 3.10. Absolute Maximum Ratings   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Ambient Temperature Under Bias</td><td rowspan=1 colspan=1>TBIAS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>C$</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature</td><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-65</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Voltage on VDD</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>4.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on VIO2</td><td rowspan=1 colspan=1>V10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>4.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on VREGIN</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on D+ or D-</td><td rowspan=1 colspan=1>VUSBD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>VD+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Voltage on UART pins, GPIO, VBUS,RSTb, or any other non-power, non-USB pin</td><td rowspan=2 colspan=1>ViN</td><td rowspan=1 colspan=1>V10&gt;3.3V</td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>V10&lt;3.3V</td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>V10+2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Total Current Sunk into Supply Pin</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Total Current Sourced out of GroundPin</td><td rowspan=1 colspan=1>IGND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Current Sourced or Sunk by any UARTpins, GPIO, VBUS, RSTb, or any othernon-power, non-USB pin</td><td rowspan=1 colspan=1>l1o</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-100</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Operating Junction Temperature</td><td rowspan=1 colspan=1>T\$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>C$</td></tr></table>

1. Exposure to maximum rating conditions for extended periods may affect device reliability. 2. On devices without a VIO pin, VIO = VDD

# Note:

![](images/2485721ac13550e5d377972cbfb0853b31a9febaba9e26b4beda69a4d94fa666.jpg)  
Figure 3.1. Typical VOH Curves

![](images/9bab9ba88957baf070c843c3e938771c5cdb7b2490bcfa6a347ed360fd7125d4.jpg)  
Figure 3.2. Typical VOL Curves

# 4. Functional Description

# 4.1 USB Function Controller and Transceiver

The Universal Serial Bus function controller in the CP2102N is a USB 2.0 compliant full-speed device with integrated transceiver and on-chip matching and pull-up resistors. The USB function controller manages all data transfers between the USB and the UART as well as command requests generated by the USB host controller and commands for controlling the function of the UART.

The USB Suspend and Resume signals are supported for power management of both the CP2102N device as well as external circuitry. The CP2102N will enter Suspend mode when Suspend signaling is detected on the bus. On entering Suspend mode, the CP2102N asserts the SUSPEND and SUSPENDb signals. SUSPEND and SUSPENDb are also asserted after a CP2102N reset until device configuration during USB Enumeration is complete.

The CP2102N exits Suspend mode when any of the following occur:

1. Resume signaling is detected or generated.   
2. A USB Reset signal is detected.   
3. A device reset occurs.   
4. USB Remote Wakeup functionality is enabled and the WAKEUP pin is grounded.

On exit of Suspend mode, the SUSPEND and SUSPENDb signals are de-asserted. Both SUSPEND and SUSPENDb temporarily float high during a CP2102N reset. If this behavior is undesirable, a strong pull-down (10 kΩ) can be used to ensure SUSPENDb remains low during reset.

# 4.2 Universal Asynchronous Receiver/Transmitter (UART) Interface

The CP2102N UART interface consists of the TX (transmit) and RX (receive) data signals as well as the RTS, CTS, DSR, DTR, DCD, and RI control signals. The UART supports RTS/CTS, DSR/DTR, and Xon/Xoff handshaking.

The UART is programmable to support a variety of data formats and baud rates. If the Virtual COM Port drivers are used, the data format and baud rate are set during COM port configuration on the PC. If the USBXpress drivers are used, the CP2102N is configured through the USBXpress API. The data formats and baud rates available are listed in the table below.

Table 4.1. Data Formats and Baud Rates   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Available Values</td></tr><tr><td rowspan=1 colspan=1>Data Bits</td><td rowspan=1 colspan=1>5,6, 7, and 8</td></tr><tr><td rowspan=1 colspan=1>Stop Bits</td><td rowspan=1 colspan=1>1, 1.51, and 2</td></tr><tr><td rowspan=1 colspan=1>Party Types</td><td rowspan=1 colspan=1>none, even, odd, mark, space</td></tr><tr><td rowspan=1 colspan=1>Baud Rates</td><td rowspan=1 colspan=1>300, 600, 1200, 1800, 2400, 4000, 4800, 7200, 9600, 14400,16000, 19200,28800,38400,51200, 56000, 57600, 64000,76800, 115200,128000, 153600, 230400, 250000,256000,460800, 500000, 576000,921600, 1000000, 1200000, 1500000,2000000,3000000</td></tr><tr><td rowspan=1 colspan=2>Note:1.5-bit only.</td></tr></table>

# 4.2.1 Baud Rate Generation

The baud rate generator is very flexible, allowing the user to request any baud rate in the range from 300 baud to 3 Mbaud. If the baud rate cannot be directly generated from the 48 MHz oscillator, the device will choose the closest possible option. The actual baud rate is dictated by the following equations.

Clock Divider = 48 MHz2 × Prescale × Requested Baud Rate 48 MHz Actual Baud Rate = 2 × Prescale × Clock Divider

In both cases, the Prescale value is 4 if the Requested Baud Rate is ≤ 365 baud and 1 if the Requested Baud Rate value is > 36 baud.

Most baud rates can be generated with an error of less than 1.0%. A general rule of thumb for the majority of UART applications is to limit the baud rate error on both the transmitter and the receiver to no more than ±2%. The Clock Divider value is rounded to the nearest integer, which may produce an error source. Another error source will be the 48 MHz oscillator, which is accurate to ±0.25%. Knowing the actual and requested baud rates, the total baud rate error can be found using the equation below.

Baud Rate Error (%) = 100 × (1 – Actual Baud RateRequested Baud Rate ) ± 0.25%

# 4.2.2 Sending Break Signaling

The CP2102N supports break signaling with an external 10k Ohm resistor between TXD and ground. This resistor is sufficient for break signaling across all baud rates.

When a Send Break command is received, the CP2102N halts adding new data to the transmitter FIFO and will wait 6 byte times for inflight data to complete transmission. It will not process other USB transactions such as RX data reception or GPIO commands while waiting - transactions will be processed once break is initiated. During this time, if enabled, the RS-485 signal will begin asserting. If RTS TX Control is enabled, RTS will also begin asserting. Once the 6 byte time has expired, the CP2102N places the TXD line in a high-impedance state - ignoring flow control status - and the external resistor pulls down TXD to initiate a break.

While sending break the TXT LED toggle is active. USB transactions including RX data reception and GPIO commands function nor mally.

When a Stop Break command is received, the CP2102N removes TXD from the high impedance state. It is held for 1 byte time to allow for stabilization. After that time has expired the transmitter resumes normal operations, and the RS485 and RTS (if RTS TX Control is enabled) signals wait the specified hold time.

# 4.3 Additional Features

# 4.3.1 General Purpose Input/Outputs (GPIO)

The CP2102N has up to 7 GPIO that can be controlled from the host. By default and during reset, these pins are set to open-drain with a weak pull-up enabled and the port latch set to 1. The pins can be made push-pull to drive external circuitry like LEDs. In addition, the state of these pins can be configured during standard operation, during Suspend, and immediately following reset.

Note: All pins temporarily float high during a device reset. If this behavior is undesirable, a strong pull-down (10 kΩ) can be used to ensure the pin remains low during reset.

The GPIO pins may also have alternate functions which are listed in the table below.

Table 4.2. GPIO Pin Alternate Functions   

<table><tr><td rowspan=1 colspan=1>GPIO Pin</td><td rowspan=1 colspan=1>QFN28 Package</td><td rowspan=1 colspan=1>QFN24 Package</td><td rowspan=1 colspan=1>QFN20 Package</td></tr><tr><td rowspan=1 colspan=1>GPIO.0</td><td rowspan=1 colspan=1>TXT</td><td rowspan=1 colspan=1>TXT</td><td rowspan=1 colspan=1>CLK1</td></tr><tr><td rowspan=1 colspan=1>GPIO.1</td><td rowspan=1 colspan=1>RXT</td><td rowspan=1 colspan=1>RXT</td><td rowspan=1 colspan=1>RS485</td></tr><tr><td rowspan=1 colspan=1>GPI0.2</td><td rowspan=1 colspan=1>RS485</td><td rowspan=1 colspan=1>RS485</td><td rowspan=1 colspan=1>TXT</td></tr><tr><td rowspan=1 colspan=1>GPI0.3</td><td rowspan=1 colspan=1>WAKEUP</td><td rowspan=1 colspan=1>WAKEUP</td><td rowspan=1 colspan=1>RXT</td></tr><tr><td rowspan=1 colspan=1>GPI0.4</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr><tr><td rowspan=1 colspan=1>GPI0.5</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr><tr><td rowspan=1 colspan=1>GPIO.6</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr></table>

# Note:

1. On QFN28 and QFN24 packages, the CLK signal is available on the same pin as RI.

By default, all of the GPIO pins are configured as a GPIO input. The speed of reading and writing the GPIO pins is subject to the timing of the USB bus. GPIO pins configured as inputs or outputs are not recommended for real-time signaling.

More information regarding the configuration of these pins can be found in Xpress Configurator in Simplicity Studio and AN721: CP21xx Device Customization Guide. Guidance on GPIO usage can be found in AN223: Runtime GPIO Control for CP210x.

# 4.3.2 Dynamic Suspend

By default, the latch values for all pins remains static during USB Suspend.

Alternatively, the dynamic suspend feature sets the pin latch to a predefined state when the CP2102N device moves from the configured USB state to the suspend USB state (see chapter nine of USB 2.0 specification for more information on USB device states). When the device exits the suspend USB state, the pin latch is restored to the previous value before entering the suspend state. Dynamic Suspend is configured separately for the GPIO pins and UART/Modem Control pins.

# 4.3.3 Output Mode

Each pin has two options for the output mode: push-pull and open-drain.

By configuring for push-pull operation, a pin operates as a push-pull output. The output voltage is determined by pin’s latch value. Thi type of output is most often used to connect directly to another device or drive external circuitry like an LED.

By configuring for open-drain operation, a pin operates as an open-drain output or input. The output voltage is determined by the pin's latch value. If the pin latch value is 1, the pin is pulled up to VIO (or VDD if the device does not have a VIO pin) through an on-chip pullup resistor. Open-drain outputs are typically used when interfacing to logic at a higher voltage than the VIO pin. These pins can be safely pulled to the higher, external voltage through an external pull-up resistor if VDD meets the 3.3 Absolute Maximum Ratings requirements.

# 4.3.4 Battery Charging (CHREN, CHR0, and CHR1)

When battery charging is enabled, the D+/D- signals will detect the type of current source attached and set the CHREN, CHR0, and CHR1 pins appropriately. CHREN enables 100 mA source current, CHR0 enables 500 mA source current, and CHR1 enables 1.5 A source current.

The charging system may draw up to the limit specified by CHREN, CHR0, and CHR1. If the system also is operational while charging, the current set points for the ISET resistors should be decreased based on how much the system could be using during battery charge.

When configuring a device to enable battery charging, the GPIO associated with the battery charging pins must also be configured corectly in Xpress Configurator as shown in the following table.

Table 4.3. Configuring GPIO for Battery Charging   
Note: Battery charging pins (CHREN, CHR1, CHR0) are disabled in Suspend only when using a Standard Data Port. If attached to a Dedicated Charging Port or Charging Downstream Port, the battery charging pins are left on while in Suspend.   

<table><tr><td rowspan=1 colspan=1>Charge Detect Mode</td><td rowspan=1 colspan=1>Pins</td><td rowspan=1 colspan=1>State</td></tr><tr><td rowspan=3 colspan=1>Up to 100 mA</td><td rowspan=1 colspan=1>CHREN</td><td rowspan=1 colspan=1>Push-Pul/High</td></tr><tr><td rowspan=1 colspan=1>CHR1</td><td rowspan=1 colspan=1>Open Drain/Low</td></tr><tr><td rowspan=1 colspan=1>CHRO</td><td rowspan=1 colspan=1>Open Drain/Low</td></tr><tr><td rowspan=3 colspan=1>Up to 500 mA</td><td rowspan=1 colspan=1>CHREN</td><td rowspan=1 colspan=1>Push-Pul/High</td></tr><tr><td rowspan=1 colspan=1>CHR1</td><td rowspan=1 colspan=1>Open Drain/Low</td></tr><tr><td rowspan=1 colspan=1>CHRO</td><td rowspan=1 colspan=1>Push-Pul/High</td></tr><tr><td rowspan=3 colspan=1>Above 500 mA</td><td rowspan=1 colspan=1>CHREN</td><td rowspan=1 colspan=1>Push-Pul/High</td></tr><tr><td rowspan=1 colspan=1>CHR1</td><td rowspan=1 colspan=1>Push-Pul/High</td></tr><tr><td rowspan=1 colspan=1>CHRO</td><td rowspan=1 colspan=1>Push-Pull/High</td></tr></table>

# 4.3.5 Remote Wakeup (WAKEUP)

The WAKEUP pin is an optional active low remote wakeup input. When the wakeup pin toggles from inactive to active (i.e. grounded) and the CP2102N is in USB suspend, the CP2102N will begin the wakeup sequence.

Host software must enable USB remote wakeup for the device. In Windows, this is under Device Manager. To set this, right-click on th device, select [Properties]>[Power Management] and enable the [Allow this device to wake the computer] feature.

# 4.3.6 Clock Output (CLK)

An optional clock output is available on CP2102N devices.

![](images/248d94652a01c3d67f229e988a8d52575284f5d6a7e9253662ce2a9587070c66.jpg)

The valid values for N are 1 to 256.

Note: The clock output stops and is no longer present on the pin when the CP2102N device is in USB Suspend. This occurs when the device is connected to USB and the host controller suspends the device (either through a feature like Selective Suspend or when the host PC is in Hibernate or Sleep modes) or when the CP2102N is disconnected from the host in self-powered mode.

# 4.3.7 Hardware Handshaking (RTS and CTS)

To utilize the functionality of the RTS and CTS pins of the CP2102N, the device must be configured to use hardware flow control on the USB host.

RTS, or Ready To Send, is an active-low output from the CP2102N and indicates to the external UART device that the CP2102N’s UART RX FIFO has not reached the FLOW OFF watermark level of 448 bytes and is ready to accept more data. When the amount of data in the RX FIFO reaches the watermark, the CP2102N pulls RTS high to indicate to the external UART device to stop sending data. The CP2102N does not pull RTS low again until the UART RX FIFO is at the FLOW ON watermark level of 384 bytes (at least 128 free bytes). This hysteresis allows for optimal operation. These RTS watermark levels are configurable using Xpress Configurator in Simplicity Studio.

Note: RTS TX Control signaling is a special mode that asserts RTS while the CP2102N is transmitting. This mode is not available below 300 baud. RTS hardware flow control works at all baud rates.

CTS, or Clear To Send, is an active-low input to the CP2102N and is used by the external UART device to indicate to the CP2102N when the external UART device’s RX FIFO is getting full. The CP2102N will not send more than two bytes of data once CTS is pulled high.

Hardware handshaking allows for optimal continuous transmission speeds at high baud rates (greater than 1 MBaud). The effective throughput depends on USB bus loading and host USB stack efficiency. The typical maximum continuous bidirectional data transfer is > 450 kbytes/s at 3 Mbaud.

![](images/caf64e5974dc5435848c094a277d9fd831f1800633e151e2391b9f93f2ca804c.jpg)  
Figure 4.1. Using Hardware Flow Control with the CP2102N

# 4.3.8 Software Handshaking

The CP2102N also supports software handshaking using the XON and XOFF event characters. The characters used for XON/XOFF is set by the host software.

If the CP2102N receives an XOFF request, it will stop transmission, even if the CP2102N receiver needs to transmit an XOFF over UART. This can potentially allow an overflow to occur or a deadlock condition if both the CP2102N and the connected UART device transmit XOFF at the same time. The XOFF_CONTINUE setting allows the CP2102N transmitter to send XOFF/XON requests even if it has received an XOFF request from the connected UART device. Once the connected UART device transmits XON, normal transmission from the CP2102N resumes.

Software handshaking uses the same watermark levels as hardware handshaking and can be configured dynamically by host software. Watermark levels greater than 512 are converted to an XON limit of 192 bytes and an XOFF limit of 64 bytes. If the XON limit crosses over the XOFF limit, the XON limit will automatically be modified to not cross over the XOFF limit. An XOFF limit of 0 is converted to 64 to guarantee buffer space is available until the UART end device stops transmission. When setting the XON and XOFF limits, it's recommended to use values where the XON limit added to the XOFF limit is less than 512 bytes, like 192/192 or 128/128. CP2102N testing shows that the XON limit set to 192 and XOFF limit set to 192 provides optimal software flow control behavior.

![](images/8f0bb2845cdd42e87e7fce9d4bcffc8ebba084916976b1770a9165a0c049bf62.jpg)  
Figure 4.2. Software Flow Control Timing Diagram

# 4.3.9 Data Throughput Optimization

Effective throughput depends on several factors:

• CP2102N placement on the physical USB device tree   
• USB bus load from other devices   
• Host OS USB stack efficiency   
• CP2102N configuration options

Handshaking is required at high baud rates (greater than 1 MBaud) to avoid receiver overrun. A request to stop transmission is only initiated once the RX FIFO has reached the FLOW OFF watermark level. Once the USB bus lowers the RX FIFO level below the FLOW ON watermark, a request to continue transmission is sent.

Hardware handshaking allows for optimal continuous transmission speeds at high baud rates. Using a Windows host PC, the CP2102N's typical maximum continuous bidirectional throughput is > 450 kbytes/s at 3 Mbaud (> 70% efficiency).

Software handshaking using XON/XOFF transmission requires more overhead. Using a Windows host PC, the CP2102N's typical maxi mum continuous bidirectional throughput is > 330 kbytes/s at 3 Mbaud (> 55% efficiency).

For these performance numbers, the CP2102N is placed on a USB hub connected to the Windows host PC with a third party UART adapter. The only significant USB traffic is generated by the USB to UART devices. The Windows host PC is running automated tests with minimal CPU load.

Certain conditions will reduce the maximum throughput at high baud rates (> 1Mbaud):

• Using DSR, DTR, or DCD handshaking signals lowers maximum performance. Use hardware CTS/RTS only for peak performance. • Embedded events or error character insertion requires free space in the UART RX FIFO to post events to the host. At high baud rates with continuous data reception, this space may not be available. Limit maximum baud rates with continuous data reception to 1 MBaud when using embedded events or error character insertion to guarantee reception of events or the error character. Transmitting an immediate character momentarily causes lower bidirectional throughput as the character forces a bypass of the current transmit FIFO. Once the character has been transmitted, the typical bidirectional throughput is restored.

Using Remote Wakeup, Charge Enable, Clock Out, or the GPIOs will not impact UART throughput.

# 4.3.10 Transmit and Receive LED Toggles (TXT and RXT)

The TX and RX LED toggle pins will toggle on and off at a fixed rate specified in Table 3.7 GPIO on page 13 whenever a byte is transmitted or received by the CP2102N. These pins are logic high whenever a device is not transmitting or receiving data and can directly drive basic LEDs within the device specification limits.

![](images/b392ea5479d5e18d906711ba9258f4557d469b7c728a90423029edf3a34b2b2c.jpg)  
Figure 4.3. Transmit and Receive Toggle

# 4.3.11 Modem Control (DSR, DTR, DCD, RI)

The modem control pins are enabled when requested on the host. If the Virtual COM Port drivers are used, the modem control pins are enabled during COM port configuration on the PC. If the USBXpress drivers are used, the CP2102N is configured through the USBXpress API. The behavior of the modem control pins may vary between operating systems.

Table 4.4. Modem Control Signals   

<table><tr><td rowspan=1 colspan=1>Modem Control Signal</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>DSR</td><td rowspan=1 colspan=1>Input to the CP2102N. Data Set Ready control input (active low).</td></tr><tr><td rowspan=1 colspan=1>DTR</td><td rowspan=1 colspan=1>Output from the CP2102N. Data Terminal Ready control output (active low).Note that this pin may toggle when opening a COM port on some operating systems.</td></tr><tr><td rowspan=1 colspan=1>DCD</td><td rowspan=1 colspan=1>Input to the CP2102N. Data Carier Detect control input (active low).</td></tr><tr><td rowspan=1 colspan=1>RI</td><td rowspan=1 colspan=1>Input to the CP2102N. Ring Indicator control input (active low).</td></tr></table>

# 4.3.12 RS485 (RS485)

The RS485 pin is an optional control pin that can be connected to the DE and RE inputs of the transceiver. When configured for RS485 mode, the pin is asserted during UART data transmission. The RS485 pin is active-high by default and is also configurable for activelow mode using Xpress Configurator.

The RS485 pin setup and hold times are programmable using Xpress Configurator to enable maximum flexibility.

Note: Note The RS485 pin is not available at baud rates below 300 baud.

![](images/1b5c6a0ff6714b99a808c4bd3d34ec9c979be3bb2b94a16563aa5c9cb7b07145.jpg)  
Figure 4.4. Using the CP2102N with a RS485 Transceiver

![](images/82076fe72965fcbe3c332b0e491ee042ed5d9aab7472f474b6c6b7459175873b.jpg)  
Figure 4.5. RS485 Output Timing Diagram for a Single-Byte Transfer

# 4.3.13 Receiver Timeout

The CP2102N supports a new custom vendor command to configure the internal buffer receive timeout. During normal operation, when data is received the receive buffer waits up to 2 ms or 128 character times, whichever is fewer, before transferring data to host. This timer is reset each time new data is received. For some usage models, this response time causes unwanted extra latency between receiving a byte at the UART and the byte being available on the host. The Set Receiver Max Timeout custom vendor command allows applications to set the timeout from .001 ms to 2 ms. Small values will cause the receiver to inefficiently use the 512 byte Receive Buffer and should not be used at high data rates (greater than 230400).

# 4.4 Drivers

There are two sets of device drivers available for the CP2102N devices: the Virtual COM Port (VCP) drivers and the USBXpress Direct Access drivers. Only one set of drivers is necessary to interface with the device.

# 4.4.1 Virtual COM Port (VCP) Drivers

The CP2102N Virtual COM Port (VCP) device drivers allow a CP2102N-based USB device to appear to the PC's application software as a COM port. Application software running on the PC accesses the CP2102N-based device as it would access a standard hardware COM port. However, actual data transfer between the PC and the CP2102N device is performed over the USB interface. Therefore, existing COM port applications may be used to transfer data via the USB to the CP2102N-based device without modifying the application. See AN197: Serial Communications Guide for the CP210x for Example Code for Interfacing to a CP2102N using the Virtual COM drivers.

Note: Because the CP2102N uses a USB-based communication interface, timing will not be controllable or guaranteed as it is with a standard COM port. Full-speed USB operates on 1 ms frames, and the host schedules packets for each USB device where it can in the 1 ms frame. It is recommended to use large data transfers when reading and writing from the host to send data as quickly as possible.

# 4.4.2 USBXpress Drivers

The Silicon Labs USBXpress drivers provide an alternate solution for interfacing with CP2102N devices. No serial port protocol expertise is required. Instead, a simple, high-level application program interface (API) is used to provide simpler CP210x connectivity and functionality. The USBXpress for CP210x Development Kit includes Windows device drivers, Windows device driver installer and uninstallers, and a host interface function library (host API) provided in the form of a Windows Dynamic Link Library (DLL). The USBXpress driver set is recommended for new products that also include new PC software. The USBXpress interface is described in AN169: USBXpress® Programmer's Guide.

# 4.4.3 Customization and Certification

n addition to customizing the device as described in 4.5 Device Customization, the drivers can be also be customized. See AN220 USB Driver Customization for more information on generating customized VCP and USBXpress drivers.

The default drivers that are shipped with the CP2102N are Microsoft WHQL (Windows Hardware Quality Labs) certified. The certification means that the drivers have been tested by Microsoft and their latest operating systems will allow the drivers to be installed without any warnings or errors. Some installations of Windows will prevent unsigned drivers from being installed at all. The customized drivers that are generated using the AN220 software are not automatically certified. They must first go through the Microsoft Driver Reseller Submission process. See AN807: Recertifying a Customized Windows HCK Driver Package for more information and contact Silicon Labs support for assistance with this process.

# 4.5 Device Customization

The CP2102N includes an internal electrically erasable programmable read-only memory (EEPROM). This memory may be used to customize the USB Vendor ID (VID), Product ID (PID), Product Description String, Power Descriptor, Device Release Number and Device Serial Number as desired for OEM applications. If the EEPROM is not programmed with OEM data, the default configuration data shown in the table below is used.

Table 4.5. Default USB Configuration Data   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Default Value</td></tr><tr><td rowspan=1 colspan=1>Vendor ID (VID)</td><td rowspan=1 colspan=1>The Vendor ID is a four digit hexadecimal number that isunique to a particular vendor. 0x10C4, for example, is theSilicon Labs Vendor ID.</td><td rowspan=1 colspan=1>0x10C4</td></tr><tr><td rowspan=1 colspan=1>Product ID (PID)</td><td rowspan=1 colspan=1>The Product ID is a four digit hexadecimal number thatidentifies the vendor&#x27;s device. 0xEA60, for example, is thedefault Product ID for Silicon Labs&#x27; CP210x USB to UARTBridge devices.</td><td rowspan=1 colspan=1>0xEA60</td></tr><tr><td rowspan=1 colspan=1>Power Mode</td><td rowspan=1 colspan=1>This setting determines whether the device is Bus-Pow-ered, i.e. it is powered by the host, or Self-Powered, i.e. itis powered from a supply on the device.</td><td rowspan=1 colspan=1>0x80 (Bus-Powered)</td></tr><tr><td rowspan=1 colspan=1>Max Power</td><td rowspan=1 colspan=1>This describes the maximum amount of power that the de-vice wil draw from the host in mA multiplied by 2. For ex-ample, 0x32 equates to 100 mA.</td><td rowspan=1 colspan=1>0x32</td></tr><tr><td rowspan=1 colspan=1>Release Version</td><td rowspan=1 colspan=1>The Release Version is a binary-coded-decimal value thatis assigned by the device manufacturer.</td><td rowspan=1 colspan=1>0x0100</td></tr><tr><td rowspan=1 colspan=1>Serial String</td><td rowspan=1 colspan=1>The Serial String is an optional string that is used by thehost to distinguish between multiple devices with the sameVID and PID combination. It is limited to 63 characters.</td><td rowspan=1 colspan=1>128-bit unique ID assigned by Silicon Labs</td></tr><tr><td rowspan=1 colspan=1>Product String</td><td rowspan=1 colspan=1>The Product String is an optional string that describes theproduct. It is limited to 126 characters.</td><td rowspan=1 colspan=1>&quot;CP2102N USB to UART Bridge Controller&quot;</td></tr></table>

While customization of the USB configuration data is optional, it is recommended to customize the VID/PID combination. A unique VID/PID combination will prevent the driver from conflicting with any other USB driver. A vendor ID can be obtained from http:// www.usb.org/ or Silicon Labs can provide a free PID for the OEM product that can be used with the Silicon Laboratories VID (http:// www.silabs.com/products/mcu/Pages/request-PID.aspx).

If the OEM application supports multiple CP2102N-based devices attached to the same PC, each CP2102N must have a unique serial number. By default, the CP2102N uses a unique 128 bit identifier as the serial number. Alternatively, sequential serial numbers can be pre-programmed by Silicon Labs using settings provided by Xpress Configurator and delivered as a custom CP2102N part number. These serial numbers can be unique per custom part number, or multiple part numbers can share the same group of sequential serial numbers. For more details, see Xpress Configurator in Simplicity Studio.

The internal programmable ROM is programmed via the USB. This allows the OEM's USB configuration data and serial number to be written to the CP2102N on-board ROM during the manufacturing and testing process. A simple GUI-based or command-line customization utility for programming the internal programmable ROM is available from Silicon Labs as a part of Simplicity Studio or available separately on the Silicon Labs website (www.silabs.com/interface-software).

The device parameters can be locked to prevent future modification on the CP2102N.

# 5. Pin Definitions

# 5.1 CP2102N QFN28 Pin Definitions

![](images/204676839eb996cff1b1541a59d9fe21d8baad919c52155ef7f70e3a15e6cb84.jpg)  
Figure 5.1. CP2102N QFN28 Pinout

Table 5.1. Pin Definitions for CP2102N QFN28   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DCD</td><td colspan="1" rowspan="1">Digital Input. Data Carrier Detect control input (active low).</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">RI/CLK</td><td colspan="1" rowspan="1">Digital Input. Ring Indicator control input (active low).Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin floating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">CHREN</td><td colspan="1" rowspan="1">Digital Output. Enable charging circuit (100 mA).</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">CHR1</td><td colspan="1" rowspan="1">Digital Output. Enable highest current (1.5 A).</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">CHRO</td><td colspan="1" rowspan="1">Digital Output. Enable higher current (500 mA).</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">GPIO.3 /WAKEUP</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Input. Remote USB wakeup interrupt input.</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">GPIO.2 /RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">GPIO.1/RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">GPIO.0/TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">GPIO.6</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose IO.</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">GPIO.5</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose IO.</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">GPIO.4</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">DSR</td><td colspan="1" rowspan="1">Digital Input. Data Set Ready control input (active low).</td></tr><tr><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1">DTR</td><td colspan="1" rowspan="1">Digital Output. Data Terminal Ready control output (active low).</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

![](images/99d92e6a6578a098c0ac97a868beeafb68d3d9ed7f0af0479b09dbdc96eb487c.jpg)  
Figure 5.2. CP2102N QFN24 Pinout

Table 5.2. Pin Definitions for CP2102N QFN24   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">RI/CLK</td><td colspan="1" rowspan="1">Digital Input. Ring Indicator control input (active low).Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">vIO</td><td colspan="1" rowspan="1">IO Supply Power Input</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin floating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">GPIO.3 /WAKEUP</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Input. Remote USB wakeup interrupt input.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">GPIO.2 /RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">GPIO.1/RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">GPIO.0/TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin flating).</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">DSR</td><td colspan="1" rowspan="1">Digital Input. Data Set Ready control input (active low).</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">DTR</td><td colspan="1" rowspan="1">Digital Output. Data Terminal Ready control output (active low).</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">DCD</td><td colspan="1" rowspan="1">Digital Input. Data Carrier Detect control input (active low).</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

![](images/4783c87950fa9a576a1a3393e9108fd733c7535f4bf16d1569198e1b7982efef.jpg)  
Figure 5.3. CP2102N QFN20 Pinout

Table 5.3. Pin Definitions for CP2102N QFN20   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GPIO.1/RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose VO.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">GPIO.0 /CLK</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin floating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">WAKEUP</td><td colspan="1" rowspan="1">Digital Input. Remote USB wakeup interupt input.</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">GPIO.3 /RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">GPIO.2 /TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

# 6. QFN28 Package Specifications

6.1 QFN28 Package Dimensions

![](images/d39850c961652594f9c6b24431e434b9ed76a5c2595382a7c89ecac24be4b898.jpg)  
Figure 6.1. QFN28 Package Drawing

Table 6.1. QFN28 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">A3</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0.20 REF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.20</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="3" rowspan="1">5.00 BSC</td></tr><tr><td colspan="1" rowspan="1">D2}$</td><td colspan="1" rowspan="1">3.15</td><td colspan="1" rowspan="1">3.25</td><td colspan="1" rowspan="1">3.35</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="3" rowspan="1">5.00 BSC</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3.15</td><td colspan="1" rowspan="1">3.25</td><td colspan="1" rowspan="1">3.35</td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.45</td><td colspan="1" rowspan="1">0.55</td><td colspan="1" rowspan="1">0.65</td></tr><tr><td colspan="1" rowspan="1">aaa</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="3" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">eee</td><td colspan="3" rowspan="1">0.08</td></tr><tr><td colspan="1" rowspan="1">Z</td><td colspan="3" rowspan="1">0.44</td></tr><tr><td colspan="1" rowspan="1">Y</td><td colspan="3" rowspan="1">0.18</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.   
3. This drawing conforms to JEDEC outline MO-220 except for custom features D2, E2, L, Z, and Y which are toleranced per suppli  
er designation.   
4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

![](images/19bbb9b2e59b6d1b8bb17537fb7c145a9a4b4553258e559143c1407adfb92e86.jpg)  
Figure 6.2. QFN28 PCB Land Pattern Drawing

Table 6.2. QFN28 PCB Land Pattern Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=2>4.80</td></tr><tr><td rowspan=1 colspan=1>$C^2$</td><td rowspan=1 colspan=2>4.80</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=2>0.50</td></tr><tr><td rowspan=1 colspan=1>×1</td><td rowspan=1 colspan=2>0.30</td></tr><tr><td rowspan=1 colspan=1>$×2$</td><td rowspan=1 colspan=2>3.35</td></tr><tr><td rowspan=1 colspan=1>$Y1</td><td rowspan=1 colspan=2>0.95</td></tr><tr><td rowspan=1 colspan=1>$Y^2$</td><td rowspan=1 colspan=2>3.35</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. This Land Pattern Design is based on the IPC-7351 guidelines.   
3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm   
minimum, all the way around the pad.   
4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.   
5. The stencil thickness should be 0.125 mm (5 mils).   
6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.   
7. A 2 x 2 array of 1.2 mm square openings on a 1.5 mm pitch should be used for the center pad.   
8. A No-Clean, Type-3 solder paste is recommended.   
9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

# 6.3 QFN28 Package Marking

![](images/5752ffb0759dabee7c13818e4971d3b133d8ba8bb4563e8ae4f090adc741f8ae.jpg)  
Figure 6.3. QFN28 Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• YY – The last two digits of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

Note: Firmware revision is not part of the package marking.

# 7. QFN24 Package Specifications

# 7.1 QFN24 Package Dimensions

![](images/8dd971fe057625692e3f8184de894dc7da26b3e8f481940c539c708cf73de042.jpg)  
Figure 7.1. QFN24 Package Drawing

Table 7.1. QFN24 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.18</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="3" rowspan="1">4.00 BSC</td></tr><tr><td colspan="1" rowspan="1">D2$</td><td colspan="1" rowspan="1">2.35</td><td colspan="1" rowspan="1">2.45</td><td colspan="1" rowspan="1">2.55</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="3" rowspan="1">4.00 BSC</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">2.35</td><td colspan="1" rowspan="1">2.45</td><td colspan="1" rowspan="1">2.55</td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.40</td><td colspan="1" rowspan="1">0.50</td></tr><tr><td colspan="1" rowspan="1">aaa</td><td colspan="1" rowspan="1">−</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">Ccc</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">0.08</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.10</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.   
3. This drawing conforms to JEDEC Solid State Outline MO-220.   
4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.

![](images/6358b4b45d610cc63453d69836e7653de5a89308251f8c654a110669c26bb2a9.jpg)  
Figure 7.2. PCB Land Pattern Drawing

Table 7.2. PCB Land Pattern Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=2>3.90</td></tr><tr><td rowspan=1 colspan=1>C2$</td><td rowspan=1 colspan=2>3.90</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=2>0.50</td></tr><tr><td rowspan=1 colspan=1>×1</td><td rowspan=1 colspan=2>0.30</td></tr><tr><td rowspan=1 colspan=1>×2$</td><td rowspan=1 colspan=2>2.55</td></tr><tr><td rowspan=1 colspan=1>$Y1</td><td rowspan=1 colspan=2>0.85</td></tr><tr><td rowspan=1 colspan=1>Y^2$</td><td rowspan=1 colspan=2>2.55</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. This Land Pattern Design is based on the IPC-7351 guidelines.   
3. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm   
minimum, all the way around the pad.   
4. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.   
5. The stencil thickness should be 0.125 mm (5 mils).   
6. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pads.   
7. A 2 x 2 array of 0.9 mm square openings on a 1.2 mm pitch should be used for the center pad.   
8. A No-Clean, Type-3 solder paste is recommended.   
9. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

# 7.3 Package Marking

![](images/70c62e57fcd2afbbf9394c3966dd9ecfdc2556cc6b332cd493ed2710f0648df2.jpg)  
Figure 7.3. Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• YY – The last two digits of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

Note: Firmware revision is not part of the package marking.

# 8. QFN20 Package Specifications

# 8.1 QFN20 Package Dimensions

![](images/45c23d741a265527baddf6385e001a4fd8427e0718397f1bd6ac99c5b05a9e70.jpg)  
Figure 8.1. QFN20 Package Drawing

Table 8.1. QFN20 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.02</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">A3</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0.20 REF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.18</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.35</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3.00 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">D2$</td><td colspan="1" rowspan="1">1.6</td><td colspan="1" rowspan="1">1.70</td><td colspan="1" rowspan="1">1.80</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="3" rowspan="1">3.00 BSC</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">1.60</td><td colspan="1" rowspan="1">1.70</td><td colspan="1" rowspan="1">1.80</td></tr><tr><td colspan="1" rowspan="1">f</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">2.50 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.40</td><td colspan="1" rowspan="1">0.50</td></tr><tr><td colspan="1" rowspan="1">K</td><td colspan="3" rowspan="1">0.25REF</td></tr><tr><td colspan="1" rowspan="1">R</td><td colspan="1" rowspan="1">0.09</td><td colspan="1" rowspan="1">0.125</td><td colspan="1" rowspan="1">0.15</td></tr><tr><td colspan="1" rowspan="1">aa</td><td colspan="3" rowspan="1">0.15</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">CCc</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="3" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">eee</td><td colspan="3" rowspan="1">0.08</td></tr><tr><td colspan="1" rowspan="1">fff</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="4" rowspan="1">Note:1. All dimensions shown are in millimeters (mm) unless otherwise noted.2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.3. The drawing complies with JEDEC MO-220.4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.</td></tr></table>

![](images/0e54718b18f80a15056a81b0d08f0aa619b8d63ae8eff1c6252cce1d3556d85e.jpg)  
Figure 8.2. QFN20 PCB Land Pattern Drawing

Table 8.2. QFN20 PCB Land Pattern Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=2>3.10</td></tr><tr><td rowspan=1 colspan=1>$C^2$</td><td rowspan=1 colspan=2>3.10</td></tr><tr><td rowspan=1 colspan=1>C3</td><td rowspan=1 colspan=2>2.50</td></tr><tr><td rowspan=1 colspan=1>C4$</td><td rowspan=1 colspan=2>2.50</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=2>0.50</td></tr><tr><td rowspan=1 colspan=1>×1</td><td rowspan=1 colspan=2>0.30</td></tr><tr><td rowspan=1 colspan=1>$×2$</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.35</td></tr><tr><td rowspan=1 colspan=1>$×3</td><td rowspan=1 colspan=2>1.80</td></tr><tr><td rowspan=1 colspan=1>Y1</td><td rowspan=1 colspan=2>0.90</td></tr><tr><td rowspan=1 colspan=1>$^2}$</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.35</td></tr><tr><td rowspan=1 colspan=1>Y3</td><td rowspan=1 colspan=2>1.80</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.   
3. This Land Pattern Design is based on the IPC-7351 guidelines.   
4. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm   
minimum, all the way around the pad.   
5. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.   
6. The stencil thickness should be 0.125 mm (5 mils).   
7. The ratio of stencil aperture to land pad size should be 1:1 for the perimeter pads.   
8. A 2 x 2 array of 0.75 mm openings on a 0.95 mm pitch should be used for the center pad to assure proper paste volume.   
9. A No-Clean, Type-3 solder paste is recommended.   
10. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

# 8.3 QFN20 Package Marking

![](images/989bc024605d5aa416552025fee424e65d85e33b5fc66331f6377b72f5ef03e3.jpg)  
Figure 8.3. QFN20 Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• Y – The last digit of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

Note: Firmware revision is not part of the package marking.

# 9. Relevant Application Notes

The following Application Notes are applicable to the CP2102N devices:

• AN721: CP210x Device Customization Guide — This application note guides developers through the configuration process of   
USBXpress devices using Simplicity Studio [Xpress Configurator].   
AN220: USB Driver Customization — This document and accompanying software enable the customization of the CP210x Virtual COM Port (VCP) and USBXpress drivers.   
• AN197: Serial Communications Guide for CP210x — This document describes recommendations for communicating with USBXpress CP210x devices using the Virtual COM Port (VCP) driver.   
AN976: Migrating from a CP2102 to a CP2102N — This document guides developers on how to migrate existing systems using the CP2102 to the CP2102N.   
AN169: USBXpress Programmer’s Guide — This application note provides recommendations and examples for developing using   
the USBXpress direct-access driver.   
• AN807: Recertifying a Customized Windows HCK Driver Package — This document describes the WHQL certification process re  
quired for customized drivers.   
• AN223: Runtime GPIO Control for CP210x — This document describes how to toggle GPIO pins from the USB host.

pplication Notes can be accessed on the Silicon Labs website (www.silabs.com/interface-appnotes) or in Simplicity Studio using the Application Notes] tile.

# 10. Revision History

# Revision 1.5

November, 2020

• Updated Figure 2.6 Self-Powered Connection Diagram for USB Pins on page 9 to add back VBUS voltage divider that was accidentally removed in previous revision.

# Revision 1.4

October, 2020

• Updated Figure 2.4 Battery Charging Connection Diagram on page 7, Figure 2.5 Bus-Powered Connection Diagram for USB Pins on page 8, and Figure 2.6 Self-Powered Connection Diagram for USB Pins on page 9 to reflect new SP0503BAHTG protection device RoHS-compliant part number.   
• Added firmware note to the package marking sections.

# Revision 1.3

March, 2019

• Updated Table 1.1 Product Selection Guide on page 2 to reflect revison change to CP2102N-A02 devices.   
• Added section 4.2.2 Sending Break Signaling describing how to send line breaks   
• Added section 4.3.13 Receiver Timeout describing the new custom vendor command to configure the internal buffer receive timeout Changed note in 4.3.12 RS485 (RS485) to indicate that in CP2102N-A02, the RS485 pin is not available at baud rates below 300 baud.   
• Changed information in 4.3.8 Software Handshaking to indicate that in CP2102N-A02, watermark levels greater than 512 are converted to an XON limit of 192 and an XOFF limit of 64 bytes.   
• Updated PCB land pattern diagram in 8.2 QFN20 PCB Land Pattern.

# Revision 1.2

November, 2017

• Added a note to Table 1.1 Product Selection Guide on page 2 to clarify the multiple types of pin 1 indicators for each package.   
• Added a description of the RSTb pin behavior during reset to 2.1 Power and as a note on 3.1.3 Reset and Supply Monitor.   
• Updated the note regarding the resistor divider on VBUS, added the resistor divider to Figure 2.5 Bus-Powered Connection Diagram for USB Pins on page 8, and duplicated the note to this area in 2.3 USB.   
• Added the resistor divider on VBUS to Figure 2.4 Battery Charging Connection Diagram on page 7.   
• Updated Thermal Resistance to Thermal Resistance (Junction to Ambient) and added Thermal Resistance (Junction to Case) and Thermal Characterization Parameter (Junction to Top) for all packages to 3.2 Thermal Conditions.   
• Updated 4.3.4 Battery Charging (CHREN, CHR0, and CHR1) to include information about configuring GPIO for battery charging.   
• Updated 4.3.7 Hardware Handshaking (RTS and CTS) and 4.3.12 RS485 (RS485) with a note that RTS control signaling and RS485 features are not supported below 1200 baud.   
• Added Z and Y dimensions and updated Note 3 in Table 6.1 QFN28 Package Dimensions on page 33.   
• Updated revision history format and moved table of contents.

# Revision 1.1

August, 2016

• Updated the minimum Operating Supply Voltage on VDD to 3.0 V in 1. Feature List and Ordering Information, 3.1.1 Recommende Operating Conditions, 3.1.4 Configuration Memory, and Figure 2.3 Connection Diagram with Voltage Regulator Not Used on page 6.

• Updated 4.3.6 Clock Output (CLK) to specify that the clock is not present when the device is in USB Suspend.   
• Updated QFN24 bottom pad label to GND instead of VSS.   
• Adjusted D, E, and aaa in QFN28 Package Dimensions.   
• Adjusted D, E, and L in QFN24 Package Dimensions.

# Revision 1.0

May, 2016

• Initial release.

# Simplicity Studio

One-click access to MCU and wireless tools, documentation, software, source code libraries & more. Available for Windows, Mac and Linux!

![](images/0333436c8be752392592b8ea15fc8b5e16e4398d2f996adca0671a1bf90f19cb.jpg)

![](images/c86ac5a23eb569bea9464e4e73a5dae0170982e00aec80750fe6ac119b25aca6.jpg)

![](images/a21a988cb5d035d3b831c998d0e0eceadc637e67565fceeca08bbd030f0222a5.jpg)

![](images/5171485c87a460a5d883779e4c66ec92db48aa3f8b84ceb20ff923e8230fba00.jpg)

# IoT Portfolio

www.silabs.com/IoT

# SW/HW

www.silabs.com/simplicity

Quality www.silabs.com/quality

# Support & Community

www.silabs.com/community

# Disclaimer

Silicon Labs intends to provide customers with the latest, accurate, and in-depth documentation of all peripherals and modules available for system and software implementers using or intending to use the Silicon Labs products. Characterization data, available modules and peripherals, memory sizes and memory addresses refer to each specific device, and “Typical” parameters provided can and do vary in different applications. Application examples described herein are for illustrative purposes only. Silicon Labs reserves the right to make changes without further notice to the product information, specifications, and descriptions herein, and does not give warranties as to the accuracy or completeness of the included information. Without prior notification, Silicon Labs may update product firmware during the manufacturing process for security or reliability reasons. Such changes will not alter the specifications or the performance of the product. Silicon Labs shall have no liability for the consequences of use of the information supplied in this document. This document does not imply or expressly grant any license to design or fabricate any integrated circuits. The products are not designed or authorized to be used within any FDA Class III devices, applications for which FDA premarket approval is required, or Life Support Systems without the specific written consent of Silicon Labs. A “Life Support System” is any product or system intended to support or sustain life and/or health, which, if it fails, can be reasonably expected to result in significant personal injury or death. Silicon Labs products are not designed or authorized for military applications. Silicon Labs products shall under no circumstances be used in weapons of mass destruction including (but not limited to) nuclear, biological or chemical weapons, or missiles capable of delivering such weapons. Silicon Labs disclaims all express and implied warranties and shall not be responsible or liable for any injuries or damages related to use of a Silicon Labs product in such unauthorized applications.

# Trademark Information

Silicon Laboratories Inc.®, Silicon Laboratories®, Silicon Labs®, SiLabs® and the Silicon Labs logo®, Bluegiga®, Bluegiga Logo®, ClockBuilder®, CMEMS®, DSPLL®, EFM®, EFM32®, EFR, Ember®, Energy Micro, Energy Micro logo and combinations thereof, “the world’s most energy friendly microcontrollers”, Ember®, EZLink®, EZRadio®, EZRadioPRO®, Gecko®, Gecko OS, Gecko OS Studio, ISOmodem®, Precision32®, ProSLIC®, Simplicity Studio®, SiPHY®, Telegesis, the Telegesis Logo®, USBXpress®, Zentri, the Zentri logo and Zentri DMS, Z-Wave®, and others are trademarks or registered trademarks of Silicon Labs. ARM, CORTEX, Cortex-M3 and THUMB are trademarks or registered trademarks of ARM Holdings. Keil is a registered trademark of ARM Limited. Wi-Fi is a registered trademark of the Wi-Fi Alliance. All other products or brand names mentioned herein are trademarks of their respective holders.