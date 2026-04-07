# USBXpress™ Family CP2102N Data Sheet

The CP2102N devices, part of the USBXpress family, are designed to quickly add USB to your applications by eliminating firmware complexity and reducing development time.

These highly-integrated USB-to-UART bridge controllers provide a simple solution for updating RS-232 designs to USB using a minimum of components and PCB space. CP2102N includes a USB 2.0 full-speed function controller, USB transceiver, oscillator, and Universal Asynchronous Receiver/Transmitter (UART) in packages as small as 3 mm x 3 mm. No other external USB components are required for development. All customization and configuration options can be selected using a simple GUI-based configurator. By eliminating the need for complex firmware and driver development, the CP2102N devices enable quick USB connectivity with minimal development effort.

CP2102N is ideal for a wide range of applications, including the following:

• POS terminals • USB dongles • Gaming controllers • Medical equipmen • Data loggers

# KEY FEATURES

• No firmware development required   
Simple GUI-based configurator   
Integrated USB transceiver; no external resistors required   
Integrated clock; no external crystal required   
USB 2.0 full-speed compatible   
Data transfer rates up to 3 Mbaud USB Battery Charger Detection (USB BCS 1.2 Specification)   
Remote wakeup for waking a suspended   
host   
Low operating current : 9.5 mA   
Royalty-free Virtual COM port drivers

![](images/f9fa312331bdacc66f2b45d915742e6c340f13cc17abd25bd4ba1d5327838a85.jpg)

# 1. Feature List and Ordering Information

![](images/74c7203e701ba50eb87f62d9f9505e5419afd01f0a46a2cbb6391076e3ac783a.jpg)  
Figure 1.1. CP2102N Part Numbering

The CP2102N devices have the following features:

• Single-Chip USB-to-UART Data Transfer • Integrated USB transceiver; no external resistors required • Integrated clock; no external crystal required Internal 960-byte programmable ROM for vendor ID, product ID, serial number, power descriptor, release number, and product description strings On-chip power-on reset circuit • On-chip voltage regulator — 3.3 V output • Pin compatible with CP2101/2/9 (QFN28 package) • Pin compatible with CP2104 (QFN24 package)

• USB Function Controller

• USB Specification 2.0 compliant; full-speed (12 Mbps) • USB suspend states supported via SUSPEND pins • USB Battery Charger Detection (USB BCS 1.2 Specification) • Remote wakeup for waking a suspended host • Single power supply of 3.0 to 3.6 V or 3.0 to 5.25 V

• Universal Asynchronous Receiver/Transmitter (UART)

• All handshaking and modem interface signals • Data formats supported • Data bits — 5, 6, 7, and 8 • Stop bits — 1, 1.5, and 2 • Parity — odd, even, mark, space, no parity

• Baud rates: 300 baud to 3 Mbaud   
• 512 byte receive buffer   
• 512 byte transmit buffer   
• Hardware or Xon/Xoff handshaking supported

• Virtual COM Port Device Drivers • Works with existing COM port Applications • Supported on Windows, Mac, and Linux • Royalty-free distribution license

• USBXpress™ Direct Driver Support • Royalty-free distribution license

Table 1.1. Product Selection Guide   

<table><tr><td rowspan=1 colspan=1>aao</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>oin aneredas </td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>auey aunenadwn</td><td rowspan=1 colspan=1>aee</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A01-GQFN28</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85 ℃</td><td rowspan=1 colspan=1>QFN28</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A01-GQFN24</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85 ℃</td><td rowspan=1 colspan=1>QFN24</td></tr><tr><td rowspan=1 colspan=1>CP2102N-A01-GQFN20</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>-40 to +85℃</td><td rowspan=1 colspan=1>QFN20</td></tr></table>

# 2. Typical Connection Diagrams

# 2.1 Power

In all cases, a 1 kΩ pull-up on the RSTb pin is recommended. This pull-up should be tied to VIO on devices that have it. On devices where VIO is connected to VDD or devices that do not have VIO, this pull-up should be tied to VDD.

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal regulator is used and USB is connected (bus-powered).

![](images/20585e938800367e5a875cdecc4184e13c59ad50371a2c2846372a2235366234.jpg)  
4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal regulator is used and USB is connected (self-powered).

4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.

![](images/6b471ebbef48385f4f7af0b6d7212a3d8a3e2a3007f31a2561b1d4ca9a199868.jpg)  
Figure 2.1. Connection Diagram with Voltage Regulator Used and USB Connected (Bus-Powered)   
Figure 2.2. Connection Diagram with Voltage Regulator Used and USB Connected (Self-Powered)

The figure below shows a typical connection diagram for the power pins of the CP2102N devices when the internal 5 V-to-3.3 V regulator is not used.

![](images/9d09dc84258d07b8e415b4ec827868a9f653672fbabf4318bf546aedf1167d9c.jpg)  
4.7 µF and 0.1 µF bypass capacitors required for each power pin placed as close to the pins as possible.   
Figure 2.3. Connection Diagram with Voltage Regulator Not Used

# 2.2 Battery Charger Detect

The CP2102N Battery Charger Detect notifies an external battery charger the amount of current available from the USB interface.

The figure below shows an example connection diagram for external battery charging circuitry. If using an external battery charging IC consult the data sheet for more information about the specific recommended connection diagrams.

![](images/274db5df524791289c73252cfcf9cb5b61c5c1fe3c5f0d553bb220e13fe0e56d.jpg)  
Figure 2.4. Battery Charging Connection Diagram

# 2.3 USB

The figure below shows a typical connection bus-powered diagram for the USB pins of the CP2102N devices including ESD protectio iodes on the USB pins.

![](images/460fd8b087e06a7722dabcb79f2a554cb4e2932c29b5dd0c9ecf4a6740867f2e.jpg)  
CP2102N Device   
Figure 2.5. Bus-Powered Connection Diagram for USB Pins

The figure below shows a typical connection self-powered diagram for the USB pins of the CP2102N devices including ESD protection diodes on the USB pins.

Note: There are two relevant restrictions on the VBUS pin voltage in this self-powered configuration. The first is the absolute maximum voltage on the VBUS pin, which is defined as VIO + 2.5 V in Table 3.10 Absolute Maximum Ratings on page 12. The second is the Input High Voltage (VIH) for VBUS to detect when the device is connected to a bus, which is defined as VIO – 0.6 V in Table 3.7 GPIO on page 10. For self-powered systems where VDD and VIO may be unpowered when VBUS is connected to 4.4 V to 5.5 V, a resistor divider (or functionally-equivalent circuit) on VBUS is required to meet these specifications and ensure reliable device operation. In this case, the current limitation of the resistor divider prevents high VBUS pin leakage current, even though the VIO + 2.5 V specification is not strictly met.

![](images/3c961241c84c3f5009acc973c63925dbfcdc27243b3a4e082b802ff34c902231.jpg)  
Figure 2.6. Self-Powered Connection Diagram for USB Pins

# 3. Electrical Specifications

# 3.1 Electrical Characteristics

All electrical parameters in all tables are specified under the conditions listed in Table 3.1 Recommended Operating Conditions on page 7, unless stated otherwise.

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

# 3.1.4 Configuration Memory

Table 3.4. Configuration Memory   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=1>VDD Voltage During Programming</td><td rowspan=1 colspan=1>VPROG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Endurance (Write/Erase Cycles)</td><td rowspan=1 colspan=1>NWE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20k</td><td rowspan=1 colspan=1>100k</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Cycles</td></tr></table>

# Note:

1. The device can be safely programmed at any voltage above the supply monitor threshold (VVDDM).

2. Data Retention Information is published in the Quarterly Quality and Reliability Report.

# 3.1.5 Internal Oscillator

Table 3.5. Internal Oscillator   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Internal Oscillator Frequency</td><td rowspan=1 colspan=1>fosc</td><td rowspan=1 colspan=1>Full Temperature and SupplyRange</td><td rowspan=1 colspan=1>47.3</td><td rowspan=1 colspan=1>48</td><td rowspan=1 colspan=1>48.7</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>Power Supply Sensitivity</td><td rowspan=1 colspan=1>PSSosc</td><td rowspan=1 colspan=1>TA = 25 °℃C$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%N</td></tr><tr><td rowspan=1 colspan=1>Temperature Sensitivity</td><td rowspan=1 colspan=1>TSosC</td><td rowspan=1 colspan=1>VDD = 3.0V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ppm/°℃</td></tr></table>

# 3.1.6 5 V Voltage Regulator

Table 3.6. 5V Voltage Regulator   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Input Voltage Range 1</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Voltage on VDD 2</td><td rowspan=2 colspan=1>VREGOUT</td><td rowspan=1 colspan=1>Output Current = 1 to 100 mARegulation range (VREGIN ≥ 4.1V)</td><td rowspan=1 colspan=1>3.1</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Current = 1 to 100 mADropout range (VREGIN &lt; 4.1V)</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>VREGIN-VDROPOUT</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Current 2</td><td rowspan=1 colspan=1>IREGOUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Dropout Voltage</td><td rowspan=1 colspan=1>VDROPOUT</td><td rowspan=1 colspan=1>Output Current = 100 mA</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr></table>

# Note:

1. Input range to meet the Output Voltage on VDD specification. If the 5 V voltage regulator is not used, VREGIN should be tied to VDD.   
2. Output current is total regulator output, including any current required by the device.

# 3.1.7 GPIO

Table 3.7. GPIO   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=2 colspan=1>Output High Voltage (High Drive)</td><td rowspan=2 colspan=1>VOH</td><td rowspan=1 colspan=1>IOH = -7 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>V10-0.7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IOH = -3.3 mA, 2.2 V≤Vio &lt;3.0VIOH = -1.8 mA, 1.71 V≤ V1o &lt;2.2 V</td><td rowspan=1 colspan=1>$V\o×0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Low Voltage (High Drive)</td><td rowspan=2 colspan=1>VoL</td><td rowspan=1 colspan=1>IoL = 13.5 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>1OL = 7mA,2.2V≤V1o&lt;3.0VIoL = 3.6 mA, 1.71 V≤V1o&lt;2.2 V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V1o×0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output High Voltage (Low Drive)</td><td rowspan=2 colspan=1>VOH</td><td rowspan=1 colspan=1>IOH = -4.75 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>V1O-0.7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IoH = -2.25 mA, 2.2 V≤ Vio &lt; 3.0 VIOH = -1.2 mA, 1.71V≤ V1o&lt;2.2 V</td><td rowspan=1 colspan=1>V1o×0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Output Low Voltage (Low Drive)</td><td rowspan=2 colspan=1>VoL</td><td rowspan=1 colspan=1>IOL =6.5 mA, Vio≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>1oL = 3.5 mA,2.2V≤V1o&lt;3.0VIoL = 1.8 mA, 1.71 V≤ VIo &lt; 2.2 V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V\o×0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input High Voltage(all GPIO pins including VBUS)</td><td rowspan=1 colspan=1>VH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Vio-0.6</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Low Voltage(all GPIO including VBUS)</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Pin Capacitance</td><td rowspan=1 colspan=1>C1o</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>pF</td></tr><tr><td rowspan=1 colspan=1>Weak Pull-Up CUurrent(ViN = 0V)</td><td rowspan=1 colspan=1>lpU</td><td rowspan=1 colspan=1>VDD= 3.6</td><td rowspan=1 colspan=1>-30</td><td rowspan=1 colspan=1>-20</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Input Leakage (Pullups off or Ana-10g)</td><td rowspan=1 colspan=1>LK</td><td rowspan=1 colspan=1>GND&lt;VIN &lt;VIO</td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Input Leakage Current with Vinabove Vio</td><td rowspan=1 colspan=1>ILK</td><td rowspan=1 colspan=1>VI0&lt;ViN&lt;V1o+2.0V</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>RS485 Setup Time before StartBit1</td><td rowspan=1 colspan=1>tRS485S</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>64.02</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>RS485 Hold Time after Stop Bit1</td><td rowspan=1 colspan=1>tRS485H</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>64.02</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>TX Toggle Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>RX Toggle Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Hz</td></tr></table>

# Note:

1. Programmable from 0 ms to 64 ms in 1 µs steps. The programmed time is the guaranteed minimum, and the actual time may be up to 20 µs longer.

# 3.1.8 USB Transceiver

Table 3.8. USB Transceiver   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=7>Transmitter</td></tr><tr><td rowspan=1 colspan=1>Output High Voltage</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>VDD≥3.0V</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage</td><td rowspan=1 colspan=1>VOL</td><td rowspan=1 colspan=1>VD≥3.0V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Crossover Point</td><td rowspan=1 colspan=1>VCRS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Impedance</td><td rowspan=1 colspan=1>ZDRV</td><td rowspan=1 colspan=1>Driving HighDriving Low</td><td rowspan=1 colspan=1>2828</td><td rowspan=1 colspan=1>3636</td><td rowspan=1 colspan=1>4444</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>Pull-up Resistance</td><td rowspan=1 colspan=1>RpU</td><td rowspan=1 colspan=1>Full Speed (D+ Pul-up)</td><td rowspan=1 colspan=1>1.425</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.575</td><td rowspan=1 colspan=1>ko</td></tr><tr><td rowspan=1 colspan=1>Output Rise Time</td><td rowspan=1 colspan=1>Tr</td><td rowspan=1 colspan=1>Full Speed</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>Output Fall Time</td><td rowspan=1 colspan=1>TF$</td><td rowspan=1 colspan=1>Full peed</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=6>Receiver</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Differentia InputSensitivity</td><td rowspan=1 colspan=1>VD1</td><td rowspan=1 colspan=1>| (D+) - (D-) |1</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Differential Input Common ModeRange</td><td rowspan=1 colspan=1>VcM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1> Input Leakage Current</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>Pullups Disabled</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>&lt;1.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>Refer to the USB Specification for timing diagrams and symbol definitions.</td></tr></table>

# 3.2 Thermal Conditions

Table 3.9. Thermal Conditions   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=3 colspan=1>Thermal Resistance</td><td rowspan=3 colspan=1>θJA</td><td rowspan=1 colspan=1>QFN20 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>QFN24 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=1 colspan=1>QFN28 Packages</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>CW</td></tr></table>

1. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad.

# Note:

# 3.3 Absolute Maximum Ratings

Stresses above those listed in 3.3 Absolute Maximum Ratings may cause permanent damage to the device. This is a stress rating only and functional operation of the devices at those or any other conditions above those indicated in the operation listings of this specification is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability. For more information on the available quality and reliability data, see the Quality and Reliability Monitor Report at http://www.silabs.com/support/quality/pages/ default.aspx.

Table 3.10. Absolute Maximum Ratings   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Ambient Temperature Under Bias</td><td rowspan=1 colspan=1>TBIAS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>C$</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature</td><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-65</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Voltage on VDD</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>4.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on VIO2</td><td rowspan=1 colspan=1>V10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>4.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on VREGIN</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on D+ or D-</td><td rowspan=1 colspan=1>VUSBD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>VD+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>Voltage on UART pins, GPIO, VBUS,RSTb, or any other non-power, non-USB pin</td><td rowspan=2 colspan=1>ViN</td><td rowspan=1 colspan=1>V10&gt;3.3V</td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>V10&lt;3.3V</td><td rowspan=1 colspan=1>GND-0.3</td><td rowspan=1 colspan=1>V10+2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Total Current Sunk into Supply Pin</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Total Current Sourced out of GroundPin</td><td rowspan=1 colspan=1>IGND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Current Sourced or Sunk by any UARTpins, GPIO, VBUS, RSTb, or any othernon-power, non-USB pin</td><td rowspan=1 colspan=1>l1o</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-100</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Operating Junction Temperature</td><td rowspan=1 colspan=1>T\$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>105</td><td rowspan=1 colspan=1>C$</td></tr></table>

1. Exposure to maximum rating conditions for extended periods may affect device reliability. 2. On devices without a VIO pin, VIO = VDD

# Note:

![](images/46b3c2e3be35a38da669a60cd77ee8b00a7a703abfa0b6cdf712e875611db18d.jpg)  
Figure 3.1. Typical VOH Curves

![](images/514cb9d4bf12187d4a534a1d37f4dd0c1e11c7bfe643d0e176259b934f5240d9.jpg)  
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

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Available Values</td></tr><tr><td rowspan=1 colspan=1>Data Bits</td><td rowspan=1 colspan=1>5,6, 7, and 8</td></tr><tr><td rowspan=1 colspan=1>Stop Bits</td><td rowspan=1 colspan=1>1, 1.51, and 2</td></tr><tr><td rowspan=1 colspan=1>Party Types</td><td rowspan=1 colspan=1>none, even, odd, mark, space</td></tr><tr><td rowspan=1 colspan=1>Baud Rates</td><td rowspan=1 colspan=1>300, 600, 1200,1800, 2400, 4000, 4800, 7200, 9600, 14400,16000, 19200, 28800, 38400,51200,56000,57600,64000,76800, 115200,128000, 153600, 230400, 250000,256000,460800, 500000, 576000, 921600, 1000000,1200000, 1500000,2000000,3000000</td></tr><tr><td rowspan=1 colspan=2>Note:1.5-bit only.</td></tr></table>

# 4.2.1 Baud Rate Generation

The baud rate generator is very flexible, allowing the user to request any baud rate in the range from 300 baud to 3 Mbaud. If the baud rate cannot be directly generated from the 48 MHz oscillator, the device will choose the closest possible option. The actual baud rate is dictated by the following equations.

Clock Divider = 48 MHz2 × Prescale × Requested Baud Rate 48 MHz Actual Baud Rate = 2 × Prescale × Clock Divider

In both cases, the Prescale value is 4 if the Requested Baud Rate is ≤ 365 baud and 1 if the Requested Baud Rate value is > 365 baud.

Most baud rates can be generated with an error of less than 1.0%. A general rule of thumb for the majority of UART applications is to limit the baud rate error on both the transmitter and the receiver to no more than ±2%. The Clock Divider value is rounded to the nearest integer, which may produce an error source. Another error source will be the 48 MHz oscillator, which is accurate to ±0.25%. Knowing the actual and requested baud rates, the total baud rate error can be found using the equation below.

Baud Rate Error (%) = 100 × (1 – Actual Baud RateRequested Baud Rate ) ± 0.25%

# 4.3 Additional Features

# 4.3.1 General Purpose Input/Outputs (GPIO)

The CP2102N has up to 7 GPIO that can be controlled from the host. By default and during reset, these pins are set to open-drain with a weak pull-up enabled and the port latch set to 1. The pins can be made push-pull to drive external circuitry like LEDs. In addition, the state of these pins can be configured during standard operation, during Suspend, and immediately following reset.

Note: All pins temporarily float high during a device reset. If this behavior is undesirable, a strong pull-down (10 kΩ) can be used to ensure the pin remains low during reset.

The GPIO pins may also have alternate functions which are listed in the table below.

Table 4.2. GPIO Pin Alternate Functions   

<table><tr><td rowspan=1 colspan=1>GPIO Pin</td><td rowspan=1 colspan=1>QFN28 Package</td><td rowspan=1 colspan=1>QFN24 Package</td><td rowspan=1 colspan=1>QFN20 Package</td></tr><tr><td rowspan=1 colspan=1>GPIO.0</td><td rowspan=1 colspan=1>TXT</td><td rowspan=1 colspan=1>TXT</td><td rowspan=1 colspan=1>CLK1</td></tr><tr><td rowspan=1 colspan=1>GPI0.1</td><td rowspan=1 colspan=1>RXT</td><td rowspan=1 colspan=1>RXT</td><td rowspan=1 colspan=1>RS485</td></tr><tr><td rowspan=1 colspan=1>GPI0.2</td><td rowspan=1 colspan=1>RS485</td><td rowspan=1 colspan=1>RS485</td><td rowspan=1 colspan=1>TXT</td></tr><tr><td rowspan=1 colspan=1>GPIO.3</td><td rowspan=1 colspan=1>WAKEUP</td><td rowspan=1 colspan=1>WAKEUP</td><td rowspan=1 colspan=1>RXT</td></tr><tr><td rowspan=1 colspan=1>GPIO.4</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr><tr><td rowspan=1 colspan=1>GPIO.5</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr><tr><td rowspan=1 colspan=1>GPIO.6</td><td rowspan=1 colspan=1>No alternate function</td><td rowspan=1 colspan=1>Not available</td><td rowspan=1 colspan=1>Not available</td></tr></table>

# Note:

1. On QFN28 and QFN24 packages, the CLK signal is available on the same pin as RI.

By default, all of the GPIO pins are configured as a GPIO input. The speed of reading and writing the GPIO pins is subject to the timing of the USB bus. GPIO pins configured as inputs or outputs are not recommended for real-time signaling.

More information regarding the configuration of these pins can be found in Xpress Configurator in Simplicity Studio and AN721: CP21xx Device Customization Guide. Guidance on GPIO usage can be found in AN223: Runtime GPIO Control for CP210x.

# 4.3.2 Dynamic Suspend

By default, the latch values for all pins remains static during USB Suspend.

Alternatively, the dynamic suspend feature sets the pin latch to a predefined state when the CP2102N device moves from the configured USB state to the suspend USB state (see chapter nine of USB 2.0 specification for more information on USB device states). When the device exits the suspend USB state, the pin latch is restored to the previous value before entering the suspend state. Dynamic Suspend is configured separately for the GPIO pins and UART/Modem Control pins.

# 4.3.3 Output Mode

Each pin has two options for the output mode: push-pull and open-drain.

y configuring for push-pull operation, a pin operates as a push-pull output. The output voltage is determined by pin’s latch value. This ype of output is most often used to connect directly to another device or drive external circuitry like an LED.

By configuring for open-drain operation, a pin operates as an open-drain output or input. The output voltage is determined by the pin's latch value. If the pin latch value is 1, the pin is pulled up to VIO (or VDD if the device does not have a VIO pin) through an on-chip pullup resistor. Open-drain outputs are typically used when interfacing to logic at a higher voltage than the VIO pin. These pins can be safely pulled to the higher, external voltage through an external pull-up resistor if VDD meets the 3.3 Absolute Maximum Ratings requirements.

# 4.3.4 Battery Charging (CHREN, CHR0, and CHR1)

When battery charging is enabled, the D+/D- signals will detect the type of current source attached and set the CHREN, CHR0, and CHR1 pins appropriately. CHREN enables 100 mA source current, CHR0 enables 500 mA source current, and CHR1 enables 1.5 A source current.

The charging system may draw up to the limit specified by CHREN, CHR0, and CHR1. If the system also is operational while charging, the current set points for the ISET resistors should be decreased based on how much the system could be using during battery charge.

# 4.3.5 Remote Wakeup (WAKEUP)

he WAKEUP pin is an optional active low remote wakeup input. When the wakeup pin toggles from inactive to active (i.e. grounded) and the CP2102N is in USB suspend, the CP2102N will begin the wakeup sequence.

Host software must enable USB remote wakeup for the device. In Windows, this is under Device Manager. To set this, right-click on the device, select [Properties]>[Power Management] and enable the [Allow this device to wake the computer] feature.

# 4.3.6 Clock Output (CLK)

An optional clock output is available on CP2102N devices.

![](images/4b44afd845534a20f230073a9295aa6952c1539a8a2877bf2a3fff2f5d8d641d.jpg)

The valid values for N are 1 to 256.

Note: The clock output stops and is no longer present on the pin when the CP2102N device is in USB Suspend. This occurs when the device is connected to USB and the host controller suspends the device (either through a feature like Selective Suspend or when the host PC is in Hibernate or Sleep modes) or when the CP2102N is disconnected from the host in self-powered mode.

# 4.3.7 Hardware Handshaking (RTS and CTS)

To utilize the functionality of the RTS and CTS pins of the CP2102N, the device must be configured to use hardware flow control on the USB host.

RTS, or Ready To Send, is an active-low output from the CP2102N and indicates to the external UART device that the CP2102N’s UART RX FIFO has not reached the FLOW OFF watermark level of 448 bytes and is ready to accept more data. When the amount of data in the RX FIFO reaches the watermark, the CP2102N pulls RTS high to indicate to the external UART device to stop sending data. The CP2102N does not pull RTS low again until the UART RX FIFO is at the FLOW ON watermark level of 384 bytes (at least 128 free bytes). This hysteresis allows for optimal operation. These RTS watermark levels are configurable using Xpress Configurator in Simplicity Studio.

CTS, or Clear To Send, is an active-low input to the CP2102N and is used by the external UART device to indicate to the CP2102N when the external UART device’s RX FIFO is getting full. The CP2102N will not send more than two bytes of data once CTS is pulled high.

Hardware handshaking allows for optimal continuous transmission speeds at high baud rates (greater than 1 MBaud). The effective throughput depends on USB bus loading and host USB stack efficiency. The typical maximum continuous bidirectional data transfer is > 450 kbytes/s at 3 Mbaud.

![](images/60f5e1ec9c8b610e8dc47d353dfa7e14d5eaacd8f2e8303635f80324a3a63c19.jpg)  
Figure 4.1. Using Hardware Flow Control with the CP2102N

# 4.3.8 Software Handshaking

The CP2102N also supports software handshaking using the XON and XOFF event characters. The characters used for XON/XOFF is set by the host software.

If the CP2102N receives an XOFF request, it will stop transmission, even if the CP2102N receiver needs to transmit an XOFF over UART. This can potentially allow an overflow to occur or a deadlock condition if both the CP2102N and the connected UART device transmit XOFF at the same time. The XOFF_CONTINUE setting allows the CP2102N transmitter to send XOFF/XON requests even if it has received an XOFF request from the connected UART device. Once the connected UART device transmits XON, normal transmission from the CP2102N resumes.

Software handshaking uses the same watermark levels as hardware handshaking and can be configured dynamically by host software. Watermark levels greater than 512 are converted to an XON limit of 448 bytes and an XOFF limit of 512 bytes. If the XON limit crosses over the XOFF limit, the XON limit will automatically be modified to not cross over the XOFF limit. An XOFF limit of 0 is converted to 64 to guarantee buffer space is available until the UART end device stops transmission. When setting the XON and XOFF limits, it's recommended to use values where the XON limit added to the XOFF limit is less than 512 bytes, like 192/192 or 128/128. CP2102N testing shows that the XON limit set to 192 and XOFF limit set to 192 provides optimal software flow control behavior.

![](images/cda5fb96177fd3e60b60aca5b2f6dc0d7ace7877f6c72ee6803e421784a1a31e.jpg)  
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

• Using DSR, DTR, or DCD handshaking signals lowers maximum performance. Use hardware CTS/RTS only for peak performance. • Embedded events or error character insertion requires free space in the UART RX FIFO to post events to the host. At high baud rates with continuous data reception, this space may not be available. Limit maximum baud rates with continuous data reception to 1 MBaud when using embedded events or error character insertion to guarantee reception of events or the error character. • Transmitting an immediate character momentarily causes lower bidirectional throughput as the character forces a bypass of the current transmit FIFO. Once the character has been transmitted, the typical bidirectional throughput is restored.

Using Remote Wakeup, Charge Enable, Clock Out, or the GPIOs will not impact UART throughput.

# 4.3.10 Transmit and Receive LED Toggles (TXT and RXT)

The TX and RX LED toggle pins will toggle on and off at a fixed rate specified in Table 3.7 GPIO on page 10 whenever a byte is transmitted or received by the CP2102N. These pins are logic high whenever a device is not transmitting or receiving data and can directly drive basic LEDs within the device specification limits.

![](images/b4c7032cd098adbccb0a84fa19d37a3647bb06b7d6972f8fa80402c92dfff4e6.jpg)  
Figure 4.3. Transmit and Receive Toggle

# 4.3.11 Modem Control (DSR, DTR, DCD, RI)

The modem control pins are enabled when requested on the host. If the Virtual COM Port drivers are used, the modem control pins are enabled during COM port configuration on the PC. If the USBXpress drivers are used, the CP2102N is configured through the USBXpress API. The behavior of the modem control pins may vary between operating systems.

Table 4.3. Modem Control Signals   

<table><tr><td rowspan=1 colspan=1>Modem Control Signal</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>DSR</td><td rowspan=1 colspan=1>Input to the CP2102N. Data Set Ready control input (active low).</td></tr><tr><td rowspan=1 colspan=1>DTR</td><td rowspan=1 colspan=1>Output from the CP2102N. Data Terminal Ready control output (active low). Note that this pin may toggle when opening a COM port on some operating systems.</td></tr><tr><td rowspan=1 colspan=1>DCD</td><td rowspan=1 colspan=1>Input to the CP2102N. Data Carrier Detect control input (active low).</td></tr><tr><td rowspan=1 colspan=1>RI</td><td rowspan=1 colspan=1>Input to the CP2102N. Ring Indicator control input (active low).</td></tr></table>

# 4.3.12 RS485 (RS485)

The RS485 pin is an optional control pin that can be connected to the DE and RE inputs of the transceiver. When configured for RS485 mode, the pin is asserted during UART data transmission. The RS485 pin is active-high by default and is also configurable for activelow mode using Xpress Configurator.

The RS485 pin setup and hold times are programmable using Xpress Configurator to enable maximum flexibility.

![](images/4189bf7ce24260978e576bed3e27dd6cec6a8ae94a57b492ccf90edaebbf406f.jpg)  
Figure 4.4. Using the CP2102N with a RS485 Transceiver

![](images/c81f35996a5c86b7651e5173304ecbd35d37193dce3651bc9a0af72cd2afe4d2.jpg)  
Figure 4.5. RS485 Output Timing Diagram for a Single-Byte Transfer

# 4.4 Drivers

There are two sets of device drivers available for the CP2102N devices: the Virtual COM Port (VCP) drivers and the USBXpress Direct Access drivers. Only one set of drivers is necessary to interface with the device.

The latest drivers are available at www.silabs.com/interface-software.

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

Table 4.4. Default USB Configuration Data   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Default Value</td></tr><tr><td rowspan=1 colspan=1>Vendor ID (VID)</td><td rowspan=1 colspan=1>The Vendor ID is a four digit hexadecimal number that isunique to a particular vendor. 0x10C4, for example, is theSilicon Labs Vendor ID.</td><td rowspan=1 colspan=1>0x10C4</td></tr><tr><td rowspan=1 colspan=1>Product ID (PID)</td><td rowspan=1 colspan=1>The Product ID is a four digit hexadecimal number thatidentifies the vendor&#x27;s device. 0xEA60, for example, is thedefault Product ID for Silicon Labs&#x27; CP210x USB to UARTBridge devices.</td><td rowspan=1 colspan=1>0xEA60</td></tr><tr><td rowspan=1 colspan=1>Power Mode</td><td rowspan=1 colspan=1>This setting determines whether the device is Bus-Pow-ered, i.e. it is powered by the host, or Self-Powered, i.e. itis powered from a supply on the device.</td><td rowspan=1 colspan=1>0x80 (Bus-Powered)</td></tr><tr><td rowspan=1 colspan=1>Max Power</td><td rowspan=1 colspan=1>This describes the maximum amount of power that the de-vice wil draw from the host in mA multiplied by 2. For ex-ample, 0x32 equates to 100 mA.</td><td rowspan=1 colspan=1>0x32</td></tr><tr><td rowspan=1 colspan=1>Release Version</td><td rowspan=1 colspan=1>The Release Version is a binary-coded-decimal value thatis assigned by the device manufacturer.</td><td rowspan=1 colspan=1>0x0100</td></tr><tr><td rowspan=1 colspan=1>Serial String</td><td rowspan=1 colspan=1>The Serial String is an optional string that is used by thehost to distinguish between multiple devices with the sameVID and PID combination. It is limited to 63 characters.</td><td rowspan=1 colspan=1>128-bit unique ID assigned by Silicon Labs</td></tr><tr><td rowspan=1 colspan=1>Product String</td><td rowspan=1 colspan=1>The Product String is an optional string that describes theproduct. It is limited to 126 characters.</td><td rowspan=1 colspan=1>&quot;CP2102N USB to UART Bridge Controller&quot;</td></tr></table>

While customization of the USB configuration data is optional, it is recommended to customize the VID/PID combination. A unique VID/PID combination will prevent the driver from conflicting with any other USB driver. A vendor ID can be obtained from http:// www.usb.org/ or Silicon Labs can provide a free PID for the OEM product that can be used with the Silicon Laboratories VID (http:// www.silabs.com/products/mcu/Pages/request-PID.aspx).

If the OEM application supports multiple CP2102N-based devices attached to the same PC, each CP2102N must have a unique serial number. By default, the CP2102N uses a unique 128 bit identifier as the serial number. Alternatively, sequential serial numbers can be pre-programmed by Silicon Labs using settings provided by Xpress Configurator and delivered as a custom CP2102N part number. These serial numbers can be unique per custom part number, or multiple part numbers can share the same group of sequential serial numbers. For more details, see Xpress Configurator in Simplicity Studio.

The internal programmable ROM is programmed via the USB. This allows the OEM's USB configuration data and serial number to be written to the CP2102N on-board ROM during the manufacturing and testing process. A simple GUI-based or command-line customization utility for programming the internal programmable ROM is available from Silicon Labs as a part of Simplicity Studio or available separately on the Silicon Labs website (www.silabs.com/interface-software).

The device parameters can be locked to prevent future modification on the CP2102N.

# 5. Pin Definitions

# 5.1 CP2102N QFN28 Pin Definitions

![](images/17f554b37194989da33f43c757ef2e028588930d417aff43f92abe7cb22692c4.jpg)  
Figure 5.1. CP2102N QFN28 Pinout

Table 5.1. Pin Definitions for CP2102N QFN28   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DCD</td><td colspan="1" rowspan="1">Digital Input. Data Carrier Detect control input (active low).</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">RI/CLK</td><td colspan="1" rowspan="1">Digital Input. Ring Indicator control input (active low).Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pinfloating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">CHREN</td><td colspan="1" rowspan="1">Digital Output. Enable charging circuit (100 mA).</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">CHR1</td><td colspan="1" rowspan="1">Digital Output. Enable highest current (1.5 A).</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">CHRO</td><td colspan="1" rowspan="1">Digital Output. Enable higher current (500 mA).</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">GPIO.3 /WAKEUP</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Input. Remote USB wakeup interrupt input.</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">GPIO.2 /RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">GPIO.1/RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose /O.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">GPIO.0/TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">GPIO.6</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose IO.</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">GPIO.5</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose IO.</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">GPIO.4</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">DSR</td><td colspan="1" rowspan="1">Digital Input. Data Set Ready control input (active low).</td></tr><tr><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1">DTR</td><td colspan="1" rowspan="1">Digital Output. Data Terminal Ready control output (active low).</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

![](images/884b208b8da97e75ae71640b703ff86f8c47c0024198e7fea70ec7c98ecd3d6a.jpg)  
Figure 5.2. CP2102N QFN24 Pinout

Table 5.2. Pin Definitions for CP2102N QFN24   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">RI/CLK</td><td colspan="1" rowspan="1">Digital Input. Ring Indicator control input (active low).Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">vIO</td><td colspan="1" rowspan="1">IO Supply Power Input</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin floating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">GPIO.3 /WAKEUP</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Input. Remote USB wakeup interrupt input.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">GPIO.2 /RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">GPIO.1/RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">GPIO.0/TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin flating).</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">DSR</td><td colspan="1" rowspan="1">Digital Input. Data Set Ready control input (active low).</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">DTR</td><td colspan="1" rowspan="1">Digital Output. Data Terminal Ready control output (active low).</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">DCD</td><td colspan="1" rowspan="1">Digital Input. Data Carrier Detect control input (active low).</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

![](images/5c9e608970baedf2a35d7b9e8af7c20c5d64d4f9b695402a1d78211f6b8f8e32.jpg)  
Figure 5.3. CP2102N QFN20 Pinout

Table 5.3. Pin Definitions for CP2102N QFN20   

<table><tr><td colspan="1" rowspan="1">PinNumber</td><td colspan="1" rowspan="1">Pin Name</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GPIO.1/RS485</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. RS485 control signal.</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">GPIO.0 /CLK</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Clock output.</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">D+</td><td colspan="1" rowspan="1">USB Data Positive</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">D-</td><td colspan="1" rowspan="1">USB Data Negative</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">VDD</td><td colspan="1" rowspan="1">Supply Power Input /5V Regulator Output</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">VREGIN</td><td colspan="1" rowspan="1">5V Regulator Input</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">VBUS</td><td colspan="1" rowspan="1">Digital Input. VBUS Sense Input. This pin should be connected to the VBUS signal of a USBnetwork. A 5 V signal on this pin indicates a USB network connection.</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">RSTb</td><td colspan="1" rowspan="1">Active-low Reset</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">NC</td><td colspan="1" rowspan="1">No Connect (leave this pin floating).</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">SUSPENDb</td><td colspan="1" rowspan="1">Digital Output. This pin is driven low when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">WAKEUP</td><td colspan="1" rowspan="1">Digital Input. Remote USB wakeup interupt input.</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">SUSPEND</td><td colspan="1" rowspan="1">Digital Output. This pin is driven high when the device enters the USB suspend state.</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">CTS</td><td colspan="1" rowspan="1">Digital Input. Clear To Send control input (active low).</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">RTS</td><td colspan="1" rowspan="1">Digital Output. Ready To Send control output (active low).</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">RXD</td><td colspan="1" rowspan="1">Digital Input. Asynchronous data input (UART Receive).</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">TXD</td><td colspan="1" rowspan="1">Digital Output. Asynchronous data output (UART Transmit).</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">GPIO.3 /RXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose IO.Digital Output. Receive LED toggle.</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">GPIO.2 /TXT</td><td colspan="1" rowspan="1">Digital Input/Output. General Purpose I/O.Digital Output. Transmit LED toggle.</td></tr><tr><td colspan="1" rowspan="1">Center</td><td colspan="1" rowspan="1">GND</td><td colspan="1" rowspan="1">Ground</td></tr></table>

# 6. QFN28 Package Specifications

6.1 QFN28 Package Dimensions

![](images/ed852976bc192a987a104bb9975e0428340239128d89a980d4771dd743b74bf6.jpg)  
Figure 6.1. QFN28 Package Drawing

Table 6.1. QFN28 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">A 3</td><td colspan="2" rowspan="1">0.20 REF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.20</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="2" rowspan="1">5.00 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">D2}$</td><td colspan="1" rowspan="1">3.15</td><td colspan="1" rowspan="1">3.25</td><td colspan="1" rowspan="1">3.35</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="3" rowspan="1">5.00 BSC</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3.15</td><td colspan="1" rowspan="1">3.25</td><td colspan="1" rowspan="1">3.35</td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.45</td><td colspan="1" rowspan="1">0.55</td><td colspan="1" rowspan="1">0.65</td></tr><tr><td colspan="1" rowspan="1">aaa</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="3" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">eee</td><td colspan="3" rowspan="1">0.08</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.   
3. This drawing conforms to JEDEC Solid State Outline MO-220.   
4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

![](images/3909f1820b53371e54daa386f11ec4dc84a313901ea2e58a4cf38b414e577db8.jpg)  
Figure 6.2. QFN28 PCB Land Pattern Drawing

Table 6.2. QFN28 PCB Land Pattern Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">C1</td><td colspan="2" rowspan="1">4.80</td></tr><tr><td colspan="1" rowspan="1">$C^2$</td><td colspan="2" rowspan="1">4.80</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="2" rowspan="1">0.50</td></tr><tr><td colspan="1" rowspan="1">×1</td><td colspan="2" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">×2$</td><td colspan="2" rowspan="1">3.35</td></tr><tr><td colspan="1" rowspan="1">Y1</td><td colspan="2" rowspan="1">0.95</td></tr><tr><td colspan="1" rowspan="1">Y2</td><td colspan="2" rowspan="1">3.35</td></tr></table>

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

![](images/40bbea8410ae76f318c4680b1e8fb30f197c65694ad4ae3c83ee1c6080424fac.jpg)  
Figure 6.3. QFN28 Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• YY – The last two digits of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

# 7. QFN24 Package Specifications

# 7.1 QFN24 Package Dimensions

![](images/22d8d7d883f9f944123323f4521df411869e97d09af324a6a833214f24ec6dce.jpg)  
Figure 7.1. QFN24 Package Drawing

Table 7.1. QFN24 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.18</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4.00 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">D2</td><td colspan="1" rowspan="1">2.35</td><td colspan="1" rowspan="1">2.45</td><td colspan="1" rowspan="1">2.55</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="3" rowspan="1">4.00 BSC</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">2.35</td><td colspan="1" rowspan="1">2.45</td><td colspan="1" rowspan="1">2.55</td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.40</td><td colspan="1" rowspan="1">0.50</td></tr><tr><td colspan="1" rowspan="1">aaa</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">Cc</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">0.08</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">0.10</td></tr></table>

# Note:

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.   
3. This drawing conforms to JEDEC Solid State Outline MO-220.   
4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020C specification for Small Body Components.

![](images/a85224d2f17982dbf91dcc5fc9079fd0672f9e34c2bf26415bc19eb9e1403919.jpg)  
Figure 7.2. QFN24 PCB Land Pattern Drawing

Table 7.2. QFN24 PCB Land Pattern Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=2>3.90</td></tr><tr><td rowspan=1 colspan=1>$C^2$</td><td rowspan=1 colspan=2>3.90</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=2>0.50</td></tr><tr><td rowspan=1 colspan=1>×1</td><td rowspan=1 colspan=2>0.30</td></tr><tr><td rowspan=1 colspan=1>$×2r$</td><td rowspan=1 colspan=2>2.55</td></tr><tr><td rowspan=1 colspan=1>$Y1</td><td rowspan=1 colspan=2>0.85</td></tr><tr><td rowspan=1 colspan=1>$Y^2$</td><td rowspan=1 colspan=2>2.55</td></tr></table>

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

# 7.3 QFN24 Package Marking

![](images/19f5fb918d30c7c1be64bc805a69a08b12342e1059e0781c5d05d4c5382b6eb3.jpg)  
Figure 7.3. QFN24 Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• YY – The last two digits of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

# 8. QFN20 Package Specifications

# 8.1 QFN20 Package Dimensions

![](images/565a9ab627699cb882448bf9d67b28e1a84876607af4ba1360a4292255dc50b2.jpg)  
Figure 8.1. QFN20 Package Drawing

Table 8.1. QFN20 Package Dimensions   

<table><tr><td colspan="1" rowspan="1">Dimension</td><td colspan="1" rowspan="1">Min</td><td colspan="1" rowspan="1">Typ</td><td colspan="1" rowspan="1">Max</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">0.70</td><td colspan="1" rowspan="1">0.75</td><td colspan="1" rowspan="1">0.80</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.02</td><td colspan="1" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">A3</td><td colspan="3" rowspan="1">0.20 REF</td></tr><tr><td colspan="1" rowspan="1">b</td><td colspan="1" rowspan="1">0.18</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td></tr><tr><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1">0.25</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.35</td></tr><tr><td colspan="1" rowspan="1">D</td><td colspan="2" rowspan="1">3.00 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">D2$</td><td colspan="1" rowspan="1">1.6</td><td colspan="1" rowspan="1">1.70</td><td colspan="1" rowspan="1">1.80</td></tr><tr><td colspan="1" rowspan="1">e</td><td colspan="3" rowspan="1">0.50 BSC</td></tr><tr><td colspan="1" rowspan="1">E</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3.00 BSC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">1.60</td><td colspan="1" rowspan="1">1.70</td><td colspan="1" rowspan="1">1.80</td></tr><tr><td colspan="1" rowspan="1">f</td><td colspan="3" rowspan="1">2.50 BSC</td></tr><tr><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">0.30</td><td colspan="1" rowspan="1">0.40</td><td colspan="1" rowspan="1">0.50</td></tr><tr><td colspan="1" rowspan="1">K</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0.25 REF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">R</td><td colspan="1" rowspan="1">0.09</td><td colspan="1" rowspan="1">0.125</td><td colspan="1" rowspan="1">0.15</td></tr><tr><td colspan="1" rowspan="1">aaa</td><td colspan="3" rowspan="1">0.15</td></tr><tr><td colspan="1" rowspan="1">bbb</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">ccc</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="1" rowspan="1">ddd</td><td colspan="3" rowspan="1">0.05</td></tr><tr><td colspan="1" rowspan="1">eee</td><td colspan="3" rowspan="1">0.08</td></tr><tr><td colspan="1" rowspan="1">f</td><td colspan="3" rowspan="1">0.10</td></tr><tr><td colspan="4" rowspan="1">Note:1. All dimensions shown are in millimeters (mm) unless otherwise noted.2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.3. The drawing complies with JEDEC MO-220.4.Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.</td></tr></table>

![](images/2222ce08f3e6fb1a4255f3bd42bf13738516d6d72660e833164360995bedbd36.jpg)  
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

![](images/d76b311261fc338b008c9ff57ba21fcdc22810e8f35df369cf8ab5758598fe92.jpg)  
Figure 8.3. QFN20 Package Marking

The package marking consists of:

• PPPPPPPP – The part number designation.   
• TTTTTT – A trace or manufacturing code.   
• Y – The last digit of the assembly year.   
• WW – The two-digit workweek when the device was assembled.   
• # – Indicates the hardware revision.

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

# 10.1 Revision 1.1

August 16th, 2016

Updated the minimum Operating Supply Voltage on VDD to 3.0 V in 1. Feature List and Ordering Information, 3.1.1 Recommended Operating Conditions, 3.1.4 Configuration Memory, and Figure 2.3 Connection Diagram with Voltage Regulator Not Used on page 3.

Updated 4.3.6 Clock Output (CLK) to specify that the clock is not present when the device is in USB Suspend.

Updated QFN24 bottom pad label to GND instead of VSS.

Adjusted D, E, and aaa in QFN28 Package Dimensions.

Adjusted D, E, and L in QFN24 Package Dimensions.

# 10.2 Revision 1.0

May 11th, 2016 Initial release.

# Table of Contents

1. Feature List and Ordering Information . . . . . . 1

2. Typical Connection Diagrams . . .

2.1 Power 2   
2.2 Battery Charger Detect .   
2.3 USB . 5   
3. Electrical Specifications   
3.1 Electrical Characteristics   
3.1.1 Recommended Operating Conditions   
3.1.2 Power Consumption 7   
3.1.3 Reset and Supply Monitor 8   
3.1.4 Configuration Memory 8   
3.1.5 Internal Oscillator 8   
3.1.6 5 V Voltage Regulator . 9   
3.1.7 GPIO .10   
3.1.8 USB Transceiver .11   
3.2 Thermal Conditions . .11   
3.3 Absolute Maximum Ratings .12   
3.4 Typical Performance Curves . .13   
4. Functional Description. 14   
4.1 USB Function Controller and Transceiver .14   
4.2 Universal Asynchronous Receiver/Transmitter (UART) Interface . .14   
4.2.1 Baud Rate Generation .15   
4.3 Additional Features . .15   
4.3.1 General Purpose Input/Outputs (GPIO). .15   
4.3.2 Dynamic Suspend . .16   
4.3.3 Output Mode .16   
4.3.4 Battery Charging (CHREN, CHR0, and CHR1) .16   
4.3.5 Remote Wakeup (WAKEUP) .16   
4.3.6 Clock Output (CLK) .16   
4.3.7 Hardware Handshaking (RTS and CTS) .17   
4.3.8 Software Handshaking .17   
4.3.9 Data Throughput Optimization. .18   
4.3.10 Transmit and Receive LED Toggles (TXT and RXT) . .18   
4.3.11 Modem Control (DSR, DTR, DCD, RI) .19   
4.3.12 RS485 (RS485) .19   
4.4 Drivers .19   
4.4.1 Virtual COM Port (VCP) Drivers .20   
4.4.2 USBXpress Drivers .20   
4.4.3 Customization and Certification .20   
4.5 Device Customization .21   
5. Pin Definitions . . . 22

5.1 CP2102N QFN28 Pin Definitions .22   
5.2 CP2102N QFN24 Pin Definitions 24   
5.3 CP2102N QFN20 Pin Definitions .26

# 6. QFN28 Package Specifications. . 28

6.1 QFN28 Package Dimensions .28   
6.2 QFN28 PCB Land Pattern .30   
6.3 QFN28 Package Marking . .31

# 7. QFN24 Package Specifications. . . 32

7.1 QFN24 Package Dimensions. .32   
7.2 QFN24 PCB Land Pattern . .34   
7.3 QFN24 Package Marking . .35

# 8. QFN20 Package Specifications. . 36

8.1 QFN20 Package Dimensions .36   
8.2 QFN20 PCB Land Pattern .38   
8.3 QFN20 Package Marking . .39

9. Relevant Application Notes . . . . 4

# 10. Revision History. . . . 4

10.1 Revision 1.1 . .41   
10.2 Revision 1.0 . .41

Table of Contents . . . 42

# Simplicity Studio"4

![](images/22c8d7ea5719476f8e67dbb71f00890fcf6d54b200ad04ce1730bf8faa084f10.jpg)

# Simplicity Studio

One-click access to MCU and wireless tools, documentation, software, source code libraries & more. Available for Windows, Mac and Linux!

![](images/addb502da78ba6f5bdcbe621eae221d9c2cb20ff78241bee4efad16b21cb706e.jpg)

![](images/f619235ac27b2553d4e3942c8e5ca01e907017b7e0e31e621ba168783ff49a09.jpg)

![](images/962f0e2d6fb40387743fda14ea7c65f67240c425feea9f1543ff23f23c08f714.jpg)

IoT Portfolio www.silabs.com/IoT

SW/HW www.silabs.com/simplicity

Quality www.silabs.com/quality

Support and Community community.silabs.com

# Disclaimer

Silicon Labs intends to provide customers with the latest, accurate, and in-depth documentation of all peripherals and modules available for system and software implementers using or intending to use the Silicon Labs products. Characterization data, available modules and peripherals, memory sizes and memory addresses refer to each specific device, and "Typical" parameters provided can and do vary in different applications. Application examples described herein are for illustrative purposes only. Silicon Labs reserves the right to make changes without further notice and limitation to product information, specifications, and descriptions herein, and does not give warranties as to the accuracy or completeness of the included information. Silicon Labs shall have no liability for the consequences of use of the information supplied herein. This document does not imply or express copyright licenses granted hereunder to design or fabricate any integrated circuits. The products are not designed or authorized to be used within any Life Support System without the specific written consent of Silicon Labs. A "Life Support System" is any product or system intended to support or sustain life and/or health, which, if it fails, can be reasonably expected to result in significant personal injury or death. Silicon Labs products are not designed or authorized for military applications. Silicon Labs products shall under no circumstances be used in weapons of mass destruction including (but not limited to) nuclear, biological or chemical weapons, or missiles capable of delivering such weapons.

# Trademark Information

Silicon Laboratories Inc.® , Silicon Laboratories®, Silicon Labs®, SiLabs® and the Silicon Labs logo®, Bluegiga®, Bluegiga Logo®, Clockbuilder®, CMEMS®, DSPLL®, EFM®, EFM32®, EFR, Ember®, Energy Micro, Energy Micro logo and combinations thereof, "the world’s most energy friendly microcontrollers", Ember®, EZLink®, EZRadio®, EZRadioPRO®, Gecko®, ISOmodem®, Precision32®, ProSLIC®, Simplicity Studio®, SiPHY®, Telegesis, the Telegesis Logo®, USBXpress® and others are trademarks or registered trademarks of Silicon Labs. ARM, CORTEX, Cortex-M3 and THUMB are trademarks or registered trademarks of ARM Holdings. Keil is a registered trademark of ARM Limited. All other products or brand names mentioned herein are trademarks of their respective holders.

Silicon Laboratories Inc. 400 West Cesar Chavez Austin, TX 78701 USA