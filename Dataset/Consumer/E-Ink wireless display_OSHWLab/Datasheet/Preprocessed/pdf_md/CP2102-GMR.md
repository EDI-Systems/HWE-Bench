# SINGLE-CHIP USB TO UART BRIDGE

# Single-Chip USB to UART Data Transfer

- Integrated USB transceiver; no external resistors required   
- Integrated clock; no external crystal required   
- Internal 1024-byte programmable ROM for vendor ID, product ID, serial number, power descriptor, release number, and product description strings - EEPROM (CP2102) - EPROM (One-time programmable) (CP2109)   
- On-chip power-on reset circuit   
- On-chip voltage regulator - 3.3 V output (CP2102) - 3.45 V output (CP2109)   
- 100% pin and software compatible with CP2101

# USB Function Controller

- USB Specification 2.0 compliant; full-speed (12 Mbps) - USB suspend states supported via SUSPEND pins

# Asynchronous Serial Data BUS (UART)

- All handshaking and modem interface signals   
- Data formats supported: - Data bits: 5, 6, 7, and 8 - Stop bits: 1, 1.5, and 2 - Parity: odd, even, mark, space, no parity   
- Baud rates: 300 bps to 1 Mbps   
- 576 Byte receive buffer; 640 byte transmit buffer   
- Hardware or X-On/X-Off handshaking supported   
- Event character support   
- Line break transmission

# Virtual COM Port Device Drivers

- Works with existing COM port PC Applications   
- Royalty-free distribution license   
- Windows 8/7/Vista/Server 2003/XP/2000   
- Mac OS-X/OS-9   
- Linux

# USBXpress™ Direct Driver Support

- Royalty-Free Distribution License - Windows 7/Vista/XP/Server 2003/2000 - Windows CE

# Example Applications

- Upgrade of RS-232 legacy devices to USB - Cellular phone USB interface cable - USB interface cable - USB to RS-232 serial adapter

# Supply Voltage

- Self-powered: 3.0 to 3.6 V - USB bus powered: 4.0 to 5.25 V

# Package

- RoHS-compliant 28-pin QFN (5x5 mm)

Ordering Part Numbers - CP2102-GM - CP2109-A01-GM

# Temperature Range: –40 to +85 °C

Note: For newer designs, the CP2102N devices offer compatible footprints and are recommended for use instead of the CP2102/9. See the Silicon Labs website (www.silabs.com/usbxpress) for more information.

![](images/d7624d4c56e912a71bdf70cefc1c2ee428a8f0a05ab7db44f4fe7eedf2c19ee9.jpg)  
Figure 1. Example System Diagram

# TABLE OF CONTENTS

# Section

# Page

# 1. System Overview . . .

2. Ordering Information . . .

3. Electrical Specifications . . .

4. Pinout and Package Definitions . . . . . 10

5. QFN-28 Package Specifications . . . .12

6. USB Function Controller and Transceiver . . . . . 14

7. Asynchronous Serial Data Bus (UART) Interface . . . . . . 15

8. Internal Programmable ROM . . . 16

9. CP2102/9 Device Drivers . . . . . 17

9.1. Virtual COM Port Drivers 17   
9.2. USBXpress Drivers 17   
9.3. Driver Customization .17   
9.4. Driver Certification . .17

10. Voltage Regulator . . . .18

11. Porting Considerations from CP2102 to CP2109 . . 21

11.1. Pin-Compatibility .21   
11.2. Distinguishing Factors . 21   
11.3. Differences in Electrical Specifications . 21

12. Relevant Application Notes . . . .23

Document Change List . .

Contact Information . . . . . 26

# 1. System Overview

The CP2102/9 is a highly-integrated USB-to-UART Bridge Controller providing a simple solution for updating RS232 designs to USB using a minimum of components and PCB space. The CP2102/9 includes a USB 2.0 fullspeed function controller, USB transceiver, oscillator, EEPROM or EPROM, and asynchronous serial data bus (UART) with full modem control signals in a compact 5 x 5 mm QFN-28 package. No other external USB components are required.

The on-chip programmable ROM may be used to customize the USB Vendor ID, Product ID, Product Description String, Power Descriptor, Device Release Number, and Device Serial Number as desired for OEM applications. The programmable ROM is programmed on-board via the USB, allowing the programming step to be easily integrated into the product manufacturing and testing process.

Royalty-free Virtual COM Port (VCP) device drivers provided by Silicon Laboratories allow a CP2102/9-based product to appear as a COM port to PC applications. The CP2102/9 UART interface implements all RS-232 signals, including control and handshaking signals, so existing system firmware does not need to be modified. In many existing RS-232 designs, all that is required to update the design from RS-232 to USB is to replace the RS232 level-translator with the CP2102/9. Direct access driver support is available through the Silicon Laboratories USBXpress driver set.

An evaluation kit for the CP2102 (Part Number: CP2102EK) is available. The kit includes a CP2102-based USB-toUART/RS-232 evaluation board, a complete set of VCP device drivers, USB and RS-232 cables, and full documentation. Contact a Silicon Labs sales representative or go to www.silabs.com to order the CP2102 Evaluation Kit. The CP2102 Evaluation Kit serves as an evaluation kit for both the CP2102 and CP2109.

# 2. Ordering Information

Table 1. Product Selection Guide   

<table><tr><td rowspan=1 colspan=1>Ordering PartNumber</td><td rowspan=1 colspan=1>InternalProgrammableROM (Byte)</td><td rowspan=1 colspan=1>EEPROM</td><td rowspan=1 colspan=1>EPROM</td><td rowspan=1 colspan=1>CalibratedInternal48MHzOscillator</td><td rowspan=1 colspan=1>SupplyVoltageRegulator</td><td rowspan=1 colspan=1>Lead-free(RoHS-Compliant)</td><td rowspan=1 colspan=1>Package</td></tr><tr><td rowspan=1 colspan=1>CP2102-GM*</td><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>QFN28</td></tr><tr><td rowspan=1 colspan=1>CP2109-A01-GM*</td><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>QFN28</td></tr><tr><td rowspan=1 colspan=8>*Note: Pin compatible with the CP2101-GM.</td></tr></table>

# 3. Electrical Specifications

Table 2. Absolute Maximum Ratings   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Ambient Temperature under Bias</td><td rowspan=1 colspan=1>TBIAS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature</td><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-65</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Voltage on VDD with respect to GND</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>4.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Maximum Total Current through VDDand GND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Maximum Output Current sunk byRST or any I/O pin</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=7>CP2102</td></tr><tr><td rowspan=1 colspan=1>Voltage on any IO Pin, VBUS, or RSTwith respect to GND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=7>CP2109</td></tr><tr><td rowspan=1 colspan=1>Voltage on any IO Pin, VBUS, or RSTwith respect to GND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD≥3.0VVDD not powered</td><td rowspan=1 colspan=1>-0.3-0.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.8V_D+$3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=7>Note: Stresses above thoselited may cause permanent device damage. This is a stressrating only and functional operationof the devices at or exceeding the conditions in the operation listings of this specification is not implied. Exposure tomaximum rating conditions for extended periods may affect device reliability.</td></tr></table>

Table 3. Recommended Operating Conditions VDD = 3.0 to 3.6 V, –40 to +85 °C unless otherwise specified   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Supply Voltage</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Supply Current - USB Pull-up1</td><td rowspan=1 colspan=1>lpu</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>230</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Specified Operating TemperatureRange</td><td rowspan=1 colspan=1>TA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Thermal Resistance2</td><td rowspan=1 colspan=1>θJA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>CP2102</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=1 colspan=1>Supply Current—Normal3</td><td rowspan=2 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Normal Operation;VREG Enabled</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Supply Current—Suspended3</td><td rowspan=1 colspan=1>Bus Powered;VREG Enabled</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>CP2109</td><td rowspan=1 colspan=6></td></tr><tr><td rowspan=1 colspan=1>Supply Current—Normal3</td><td rowspan=2 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Normal Operation;VREG Enabled</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Supply Current—Suspended3</td><td rowspan=1 colspan=1>Bus Powered;VREG Enabled</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>230</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>Notes:1. The USB Pullup supply current values are calculated vlues based on USB specifications. USB Pulup supply current is current flowing from Vpp to GND through USB pull-down/pull-up resistors on D+ and D-.</td></tr></table>

2. Thermal resistance assumes a multi-layer PCB with any exposed pad soldered to a PCB pad. 3. USB Pull-up current should be added for total supply current. Normal and suspended supply current is current flowing into VREGIN. Normal and suspended supply current is guaranteed by characterization.

Table 4. UART and Suspend I/O DC Electrical Characteristics VDD = 3.0 to 3.6 V, –40 to +85 °C unless otherwise specified   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Baud Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>921600</td><td rowspan=1 colspan=1>bps</td></tr><tr><td rowspan=1 colspan=1>Input Leakage Current</td><td rowspan=1 colspan=1>1L</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=4>CP2102</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Output High Voltage</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>1OH = -10 μA1OH = -3 mA1OH = -10 mA</td><td rowspan=1 colspan=1>VDD-0.1VDD-0.7</td><td rowspan=1 colspan=1>VDD-0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>10L = 10 μA1OL = 8.5 mA1OL = 25 mA</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一1.0</td><td rowspan=1 colspan=1>0.10.6一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input High Voltage</td><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Low Voltage</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>CP2109</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Output High Voltage</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>lOH = −10 μAOH = -3mA1OH =-10mA</td><td rowspan=1 colspan=1>VDD-0.1VDD-0.2</td><td rowspan=1 colspan=1>_VDD-0.4</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>1OL = 10 μA1OL = 8.5mA1OL = 25 mA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一/0.6</td><td rowspan=1 colspan=1>0.10.4一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input High Voltage</td><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7×VDD</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Low Voltage</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr></table>

Table 5. Reset Electrical Characteristics –40 to +85 °C unless otherwise specified   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>VDD Ramp Time</td><td rowspan=1 colspan=1>tRMP</td><td rowspan=1 colspan=1>Time to VDD ≥ 2.7 V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>RsT Low Time to Generate a SystemReset</td><td rowspan=1 colspan=1>tRSTL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=7>CP2102</td></tr><tr><td rowspan=1 colspan=1>RST Input High Voltage</td><td rowspan=1 colspan=1>VIHRESET</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7×VDD</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>RST Input Low Voltage</td><td rowspan=1 colspan=1>VILRESET</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>0.25×VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=7>CP2109</td></tr><tr><td rowspan=1 colspan=1>RST Input High Voltage</td><td rowspan=1 colspan=1>VIHRESET</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>0.75×VDD</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>RST Input Low Voltage</td><td rowspan=1 colspan=1>VILRESET</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr></table>

Table 6. Voltage Regulator Electrical Specifications –40 to +85 °C unless otherwise specified.   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=7>CP2102</td></tr><tr><td rowspan=1 colspan=1>Input Voltage Range</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Voltage</td><td rowspan=1 colspan=1>VDDOUT</td><td rowspan=1 colspan=1>Output Current = 1 to 100 mA*</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VBUS Detection Input Threshold</td><td rowspan=1 colspan=1>VVBUSTH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>2.9</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Bias Current</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>CP2109</td></tr><tr><td rowspan=1 colspan=1>Input Voltage Range</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Voltage</td><td rowspan=1 colspan=1>VDDOUT</td><td rowspan=1 colspan=1>Output Current = 1 to 100 mA*</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.45</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VBUS Detection Input Threshold</td><td rowspan=1 colspan=1>VVBUSTH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Bias Current</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>83</td><td rowspan=1 colspan=1>99</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>*Note: The maximum regulator supply current is 100 mA.</td></tr></table>

# Table 7. USB Transceiver Electrical Specifications

VDD = 3.0 V to 3.6 V, –40 to +85 °C unless otherwise specified.

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=7>Transmitter</td></tr><tr><td rowspan=1 colspan=1>Output High Voltage</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Crossover Point</td><td rowspan=1 colspan=1>VCRS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Impedance (CP2102)</td><td rowspan=2 colspan=1>ZDRV</td><td rowspan=1 colspan=1>Driving HighDriving Low</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>3838</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>Output Impedance (CP2109)</td><td rowspan=1 colspan=1>Driving HighDriving Low</td><td rowspan=1 colspan=1>一一</td><td rowspan=1 colspan=1>3636</td><td rowspan=1 colspan=1>一一</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>Pull-up Resistance</td><td rowspan=1 colspan=1>RpU</td><td rowspan=1 colspan=1>Full Speed (D+ Pull-up)Low Speed (D- Pull-up)</td><td rowspan=1 colspan=1>1.425</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.575</td><td rowspan=1 colspan=1>kΩ</td></tr><tr><td rowspan=1 colspan=1>Output Rise Time</td><td rowspan=1 colspan=1>TR</td><td rowspan=1 colspan=1>Low SpeedFull Speed</td><td rowspan=1 colspan=1>754</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>30020</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>Output Fall Time</td><td rowspan=1 colspan=1>$TF$</td><td rowspan=1 colspan=1>Low SpeedFull Speed</td><td rowspan=1 colspan=1>754</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>30020</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=7>Receiver</td></tr><tr><td rowspan=1 colspan=1>Differential Input Sensitivity</td><td rowspan=1 colspan=1>VDI</td><td rowspan=1 colspan=1>| (D+) − (D-) |</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Diferential Input CommonMode Range</td><td rowspan=1 colspan=1>VCM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Leakage Current</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Pullups Disabled</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>&lt;1.0</td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>*Note: Refer to the USB Specification for timing diagrams and symbol definitions.</td></tr></table>

Table 8. EPROM Electrical Characteristics   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=2>CP2109</td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=1 colspan=1>Voltage on Vpp with respect to GND during aROM programming operation</td><td rowspan=1 colspan=1>VDD≥3.3 V</td><td rowspan=1 colspan=1>5.75</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>$V_+$3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Capacitor on Vpp for In-system Programming</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>4.7</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>μF</td></tr></table>

# 4. Pinout and Package Definitions

Table 9. CP2102/9 Pin Definitions   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Pin#</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Power InPower Out</td><td rowspan=1 colspan=1>3.0–3.6 V Power Supply Voltage Input.3.3 V Voltage Regulator Output.See &quot;10. Voltage Regulator&quot; on page 18.</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Ground</td></tr><tr><td rowspan=1 colspan=1>RST</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>D IO</td><td rowspan=1 colspan=1>Device Reset. Open-drain output of internal POR or VDD monitor. Anexternal source can initiate a system reset by driving this pin low forat least 15 us.</td></tr><tr><td rowspan=1 colspan=1>REGIN</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Power In</td><td rowspan=1 colspan=1>5 V Regulator Input. This pin is the input to the on-chip voltage regu-lator.</td></tr><tr><td rowspan=1 colspan=1>VBUS</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>D In</td><td rowspan=1 colspan=1>VBUS Sense Input. This pin should be connected to the VBUS signalof a USB network. A 5 V signal on this pin indicates a USB networkconnection.</td></tr><tr><td rowspan=1 colspan=1>NC1/$\pp{2}$</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>A Power</td><td rowspan=1 colspan=1>This pin should be left unconnected or tied to VDD. This pin is unusedon the CP2102 and may be connected to the Vpp programmingcapacitor to maintain board compatibiity with the CP2109.Vpp Programming Supply Voltage</td></tr><tr><td rowspan=1 colspan=1>D+</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>D IO</td><td rowspan=1 colspan=1>USB D+</td></tr><tr><td rowspan=1 colspan=1>D-</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>D IO</td><td rowspan=1 colspan=1>USB D-</td></tr><tr><td rowspan=1 colspan=1>TXD</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>D Out</td><td rowspan=1 colspan=1>Asynchronous data output (UART Transmit)</td></tr><tr><td rowspan=1 colspan=1>RXD</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>D In</td><td rowspan=1 colspan=1>Asynchronous data input (UART Receive)</td></tr><tr><td rowspan=1 colspan=1>CTS</td><td rowspan=1 colspan=1>233</td><td rowspan=1 colspan=1>D In</td><td rowspan=1 colspan=1>Clear To Send control input (active low)</td></tr><tr><td rowspan=1 colspan=1>RTS</td><td rowspan=1 colspan=1>243</td><td rowspan=1 colspan=1>D Out</td><td rowspan=1 colspan=1>Ready to Send control output (active low)</td></tr><tr><td rowspan=1 colspan=1>DSR</td><td rowspan=1 colspan=1>273</td><td rowspan=1 colspan=1>D in</td><td rowspan=1 colspan=1>Data Set Ready control input (active low)</td></tr><tr><td rowspan=1 colspan=1>DTR</td><td rowspan=1 colspan=1>283</td><td rowspan=1 colspan=1>D Out</td><td rowspan=1 colspan=1>Data Terminal Ready control output (active low)</td></tr><tr><td rowspan=1 colspan=1>DCD</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>D In</td><td rowspan=1 colspan=1>Data Carrier Detect control input (active low)</td></tr><tr><td rowspan=1 colspan=1>RI</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>D In</td><td rowspan=1 colspan=1>Ring Indicator control input (active low)</td></tr><tr><td rowspan=1 colspan=1>SUSPEND</td><td rowspan=1 colspan=1>123</td><td rowspan=1 colspan=1>D Out</td><td rowspan=1 colspan=1>This pin is driven high when the CP2102/9 enters the USB suspendstate.</td></tr><tr><td rowspan=1 colspan=1>SUSPEND</td><td rowspan=1 colspan=1>113</td><td rowspan=1 colspan=1>D Out</td><td rowspan=1 colspan=1>This pin is driven low when the CP2102/9 enters the USB suspendstate.</td></tr><tr><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>10,13-22</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>These pins should be left unconnected or tied to VDD.</td></tr><tr><td rowspan=1 colspan=4>Netoe</td></tr></table>

1. For CP2102, pin is no connect (NC). 2. For CP2109, pin is VPP. VPP can be left unconnected when not used for in-application programming. 3. Pins can be left unconnected when not used.

# Notes:

![](images/bb8b1b5068a3929f262b8ce22218562996abe5c8fa30cf126882aab50c9e2fac.jpg)  
Figure 2. QFN-28 Pinout Diagram (Top View)

# 5. QFN-28 Package Specifications

![](images/dfcd644fda410a69ef262dee6424388d9244a62fa51c8234bb641bc3d43193b1.jpg)  
Figure 3. QFN-28 Package Drawing

Table 10. QFN-28 Package Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0.80</td><td rowspan=1 colspan=1>0.90</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.05</td></tr><tr><td rowspan=1 colspan=1>A3</td><td rowspan=1 colspan=3>0.25 REF</td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>0.23</td><td rowspan=1 colspan=1>0.30</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=3>5.00 BSC.</td></tr><tr><td rowspan=1 colspan=1>D2</td><td rowspan=1 colspan=1>2.90</td><td rowspan=1 colspan=1>3.15</td><td rowspan=1 colspan=1>3.35</td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>0.50 BSC.</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=3>5.00 BSC.</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>2.90</td><td rowspan=1 colspan=1>3.15</td><td rowspan=1 colspan=1>3.35</td></tr></table>

# Notes:

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.35</td><td rowspan=1 colspan=1>0.55</td><td rowspan=1 colspan=1>0.65</td></tr><tr><td rowspan=1 colspan=1>L1</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>0.15</td></tr><tr><td rowspan=1 colspan=1>aaa</td><td rowspan=1 colspan=3>0.15</td></tr><tr><td rowspan=1 colspan=1>bbb</td><td rowspan=1 colspan=3>0.10</td></tr><tr><td rowspan=1 colspan=1>ddd</td><td rowspan=1 colspan=3>0.05</td></tr><tr><td rowspan=1 colspan=1>eee</td><td rowspan=1 colspan=3>0.08</td></tr><tr><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=3>0.44</td></tr><tr><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=3>0.18</td></tr></table>

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing per ANSI Y14.5M-1994.   
3. This drawing conforms to the JEDEC Solid State Outline MO-220, variation VHHD except for custom features D2, E2, Z, Y, and L, which are toleranced per supplier designation.   
4. Recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

![](images/69662abd7eee4fcc99f2688cf28a72774ebca8d3cbdc72de8cda8b13484516ff.jpg)  
Figure 4. QFN-28 Recommended PCB Land Pattern

Table 11. QFN-28 PCB Land Pattern Dimensions   

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=2>4.80</td></tr><tr><td rowspan=1 colspan=1>C2</td><td rowspan=1 colspan=2>4.80</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=2>0.50</td></tr><tr><td rowspan=1 colspan=1>X1</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.30</td></tr></table>

Notes: General

<table><tr><td rowspan=1 colspan=1>Dimension</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>X2</td><td rowspan=1 colspan=1>3.20</td><td rowspan=1 colspan=1>3.30</td></tr><tr><td rowspan=1 colspan=1>Y1</td><td rowspan=1 colspan=1>0.85</td><td rowspan=1 colspan=1>0.95</td></tr><tr><td rowspan=1 colspan=1>Y2</td><td rowspan=1 colspan=1>3.20</td><td rowspan=1 colspan=1>3.30</td></tr></table>

1. All dimensions shown are in millimeters (mm) unless otherwise noted.   
2. Dimensioning and Tolerancing is per the ANSI Y14.5M-1994 specification.   
3. This Land Pattern Design is based on the IPC-7351 guidelines.

# Solder Mask Design

4. All metal pads are to be non-solder mask defined (NSMD). Clearance between the solder mask and the metal pad is to be 60 µm minimum, all the way around the pad.

# Stencil Design

5. A stainless steel, laser-cut and electro-polished stencil with trapezoidal walls should be used to assure good solder paste release.

6. The stencil thickness should be 0.125 mm (5 mils).

7. The ratio of stencil aperture to land pad size should be 1:1 for all perimeter pins.

8. A 3x3 array of 0.90 mm openings on a 1.1 mm pitch should be used for the center pad to assure the proper paste volume (67% Paste Coverage).

# Card Assembly

9. A No-Clean, Type-3 solder paste is recommended.

10. The recommended card reflow profile is per the JEDEC/IPC J-STD-020 specification for Small Body Components.

# 6. USB Function Controller and Transceiver

The Universal Serial Bus function controller in the CP2102/9 is a USB 2.0 compliant full-speed device with integrated transceiver and on-chip matching and pull-up resistors. The USB function controller manages all data transfers between the USB and the UART as well as command requests generated by the USB host controller and commands for controlling the function of the UART.

The USB Suspend and Resume signals are supported for power management of both the CP2102/9 device as well as external circuitry. The CP2102/9 will enter Suspend mode when Suspend signaling is detected on the bus. On entering Suspend mode, the CP2102/9 asserts the SUSPEND and SUSPEND signals. SUSPEND and SUSPEND are also asserted after a CP2102/9 reset until device configuration during USB Enumeration is complete.

The CP2102/9 exits Suspend mode when any of the following occur: (1) Resume signaling is detected or generated, (2) a USB Reset signal is detected, or (3) a device reset occurs. On exit of Suspend mode, the SUSPEND and SUSPEND signals are de-asserted.

Both SUSPEND and SUSPEND temporarily float high during a CP2102/9 reset. If this behavior is undesirable, a strong pulldown (10 k) can be used to ensure SUSPEND remains low during reset. See Figure 5 for other recommended options.

![](images/710408cd7fde5bb418c24a7cd7c93fa6f193aa0656eeecc57bcd5d2f4ddf9138.jpg)  
Figure 5. Typical Connection Diagram

Option 1: A 4.7 k pull-up resistor can be added to increase noise immunity.   
Option 2: A 4.7 µF capacitor can be added if powering other devices from the on-chip regulator.   
Option 3: Avalanche transient voltage suppression diodes should be added for ESD protection.   
Use Littlefuse p/n SP0503BAHT or equivalent.   
Option 4: 10 k resistor to ground to hold SUSPEND low on initial power on or device reset.   
Option 5: A 4.7 µF capacitor can be added for in-system programming (CP2109 only).

# 7. Asynchronous Serial Data Bus (UART) Interface

The CP2102/9 UART interface consists of the TX (transmit) and RX (receive) data signals as well as the RTS, CTS, DSR, DTR, DCD, and RI control signals. The UART supports RTS/CTS, DSR/DTR, and X-On/X-Off handshaking.

The UART is programmable to support a variety of data formats and baud rates. If the Virtual COM Port drivers are used, the data format and baud rate are set during COM port configuration on the PC. If the USBXpress drivers are used, the CP2102/9 is configured through the USBXpress API. The data formats and baud rates available are listed in Table 12.

Table 12. Data Formats and Baud Rates   

<table><tr><td rowspan=1 colspan=1>Data Bits</td><td rowspan=1 colspan=1>5, 6, 7, and 8</td></tr><tr><td rowspan=1 colspan=1>Stop Bits</td><td rowspan=1 colspan=1>1,1.51, and 2</td></tr><tr><td rowspan=1 colspan=1>Parity Type</td><td rowspan=1 colspan=1>None, Even, Odd, Mark, Space</td></tr><tr><td rowspan=1 colspan=1>Baud Rates²</td><td rowspan=1 colspan=1>300,600, 1200,1800, 2400,4000, 4800,7200, 9600, 14400, 16000, 19200,28800, 38400,51200, 56000, 57600, 64000, 76800, 115200, 128000, 153600, 230400, 250000, 256000,460800, 500000, 576000, 9216003</td></tr><tr><td rowspan=1 colspan=2>Notes:1. 5-bit only.2. Additional baud rates are supported. See “AN721: CP210x/CP211x Device Customization Guide&quot;.3.7or 8 data bits only.</td></tr></table>

# 8. Internal Programmable ROM

The CP2102 includes an internal electrically erasable programmable read-only memory (EEPROM), and the CP2109 includes an internal one-time programmable (OTP) erasable programmable read-only memory (EPROM). Either may be used to customize the USB Vendor ID (VID), Product ID (PID), Product Description String, Power Descriptor, Device Release Number and Device Serial Number as desired for OEM applications. If the EEPROM/ EPROM is not programmed with OEM data, the default configuration data shown in Table 13 is used. The EEPROM has a typical endurance of 100,000 write cycles with a data retention of 100 years. The EPROM can only be written one time and cannot be erased.

While customization of the USB configuration data is optional, it is recommended to customize the VID/PID combination. A unique VID/PID combination will prevent the driver from conflicting with any other USB driver. A vendor ID can be obtained from http://www.usb.org/ or Silicon Laboratories can provide a free PID for the OEM product that can be used with the Silicon Laboratories VID. It is also recommended to customize the serial number if the OEM application is one in which it is possible for multiple CP2102/9-based devices to be connected to the same PC.

The internal programmable ROM is programmed via the USB. This allows the OEM's USB configuration data and serial number to be written to the CP2102/9 on-board ROM during the manufacturing and testing process. A standalone utility for programming the internal programmable ROM is available from Silicon Laboratories. A library of routines provided in the form of a Windows® DLL is also available. This library can be used to integrate the programmable ROM programming step into custom software used by the OEM to streamline testing and serial number management during manufacturing.

USB descriptors can be locked to prevent future modification on the CP2102. The CP2109 can be programmed insystem over the USB interface by adding a capacitor to the PCB. If configuration ROM is to be programmed insystem, a 4.7 μF capacitor must be added between the VPP pin and ground. No other circuitry should be connected to VPP during a programming operation, and VDD must remain at 3.3 V or higher to successfully write to the configuration ROM.

Table 13. Default USB Configuration Data   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>Vendor ID</td><td rowspan=1 colspan=1>10C4h</td></tr><tr><td rowspan=1 colspan=1>Product ID</td><td rowspan=1 colspan=1>EA60h</td></tr><tr><td rowspan=1 colspan=1>Power Descriptor (Attributes)</td><td rowspan=1 colspan=1>80h</td></tr><tr><td rowspan=1 colspan=1>Power Descriptor(Max. Power)</td><td rowspan=1 colspan=1>32h</td></tr><tr><td rowspan=1 colspan=1>Release Number</td><td rowspan=1 colspan=1>0100h</td></tr><tr><td rowspan=1 colspan=1>CP2102 Serial Number</td><td rowspan=1 colspan=1>0001 (63 characters maximum)</td></tr><tr><td rowspan=1 colspan=1>CP2109 Serial Number</td><td rowspan=1 colspan=1>Unique 8 character ASCll string (63 characters maximum)</td></tr><tr><td rowspan=1 colspan=1>CP2102 Product Description String</td><td rowspan=1 colspan=1>&quot;CP2102 USB to UART Bridge Controller” (126 characters maximum)</td></tr><tr><td rowspan=1 colspan=1>CP2109 Product Description String</td><td rowspan=1 colspan=1>&quot;CP2109 USB to UART Bridge Controller” (126 characters maximum)</td></tr></table>

# 9. CP2102/9 Device Drivers

There are two sets of device drivers available for the CP2102/9 devices: the Virtual COM Port (VCP) drivers and the USBXpress Direct Access drivers. Only one set of drivers is necessary to interface with the device.

The latest drivers are available at http://www.silabs.com/support/Pages/software-downloads.aspx.

# 9.1. Virtual COM Port Drivers

The CP2102/9 Virtual COM Port (VCP) device drivers allow a CP2102/9-based device to appear to the PC's application software as a COM port. Application software running on the PC accesses the CP2102/9-based device as it would access a standard hardware COM port. However, actual data transfer between the PC and the CP2102/ 9 device is performed over the USB interface. Therefore, existing COM port applications may be used to transfer data via the USB to the CP2102/9-based device without modifying the application. See “AN197: Serial Communications Guide for the CP210x” for Example Code for Interfacing to a CP2102/9 using the Virtual COM drivers.

# 9.2. USBXpress Drivers

The Silicon Laboratories USBXpress drivers provide an alternate solution for interfacing with CP2102/9 devices. No Serial Port protocol expertise is required. Instead, a simple, high-level application program interface (API) is used to provide simpler CP210x connectivity and functionality. The USBXpress for CP210x Development Kit includes Windows device drivers, Windows device driver installer and uninstallers, and a host interface function library (host API) provided in the form of a Windows Dynamic Link Library (DLL). The USBXpress driver set is recommended for new products that also include new PC software. The USBXpress interface is described in “AN169: USBXpress® Programmer's Guide.”

# 9.3. Driver Customization

In addition to customizing the device as described in "8. Internal Programmable ROM" on page 16, the drivers and the drivers installation package can be also be customized. See “AN220: USB Driver Customization” for more information on generating customized VCP and USBXpress drivers.

# 9.4. Driver Certification

The default drivers that are shipped with the CP2102/9 are Microsoft WHQL (Windows Hardware Quality Labs) certified. The certification means that the drivers have been tested by Microsoft and their latest operating systems (2000, Server 2003, XP, Vista, 7, and 8) will allow the drivers to be installed without any warnings or errors. Some installations of Windows will prevent unsigned drivers from being installed at all.

The customized drivers that are generated using the AN220 software are not automatically certified. They must first go through the Microsoft Driver Reseller Submission process. Contact Silicon Laboratories support for assistance with this process.

# 10. Voltage Regulator

The CP2102/9 includes an on-chip 5 to 3 V voltage regulator. This allows the CP2102/9 to be configured as either a USB bus-powered device or a USB self-powered device. These configurations are shown in Figure 6, Figure 7, Figure 8, Figure 9, and Figure 10. When enabled, the 3 V voltage regulator output appears on the VDD pin and can be used to power external 3 V devices. See Table 6 for the voltage regulator electrical characteristics.

Alternatively, if 3 V power is supplied to the VDD pin, the CP2102/9 can function as a USB self-powered device with the voltage regulator disabled. For this configuration, it is recommended that the REGIN input be tied to the 3 V net to disable the voltage regulator. In addition, if VDD or REGIN may be unpowered while VBUS is 5 V, a resistor divider (or functionally-equivalent circuit) shown in Note 1 of Figure 8 and Figure 10 is required to meet the absolute maximum voltage on VBUS specification in Table 2.

The USB max power and power attributes descriptor must match the device power usage and configuration. See “AN721: CP210x/CP211x Device Customization Guide” for information on how to customize USB descriptors for the CP2102/9.

Note: It is recommended to connect additional decoupling capacitance (e.g., 0.1 µF in parallel with 1.0 µF) to the REGIN input.

![](images/2d9c5ee5595e0b8ccf29b10a4238b841aa329b9e641e4b3da1486384f19d29c4.jpg)  
Figure 6. Configuration 1: USB Bus-Powered

![](images/5cfb437bc83068258bc3556c8e53051b2e6b16b2c1ca3d664dc0fbc9e4a7a033.jpg)  
Figure 7. CP2102 Configuration 2: USB Self-Powered

![](images/adde458a4f8730f7b50d8574616d74310f0774b0656eef1e6f281ece8e110c71.jpg)  
Figure 8. CP2109 Configuration 2: USB Self-Powered

Note 1 : For self-powered systems where VDD or REGIN may be unpowered when VBUS is connected to 5 V, a resistor divider (or functionally-equivalent circuit) on VBUS is required to meet the absolute maximum voltage on VBUS specification in the Electrical Characteristics section.

![](images/230efe7fcfd2444e869eabb3bce9f660de7ac3a1a0c2325e5c6c68e3211fdd39.jpg)  
Figure 9. CP2102 Configuration 3: USB Self-Powered, Regulator Bypassed

![](images/ac864a38ce12badb6441a6274b2c89e56c29895cc472b7e614f78bac77c5d88a.jpg)  
Figure 10. CP2109 Configuration 3: USB Self-Powered, Regulator Bypassed

Note 1 : For self-powered systems where VDD or REGIN may be unpowered when VBUS is connected to 5 V, a resistor divider (or functionally-equivalent circuit) on VBUS is required to meet the absolute maximum voltage on VBUS specification in the Electrical Characteristics section.

# 11. Porting Considerations from CP2102 to CP2109

This section highlights the differences between the CP2102 and CP2109. These devices are designed to be pincompatible, and thus require very minor changes when porting hardware between devices. The CP2109 is an updated, cost-reduced version of the CP2102 with a one-time programmable ROM.

# 11.1. Pin-Compatibility

The CP2109 is pin-compatible with the CP2102 with a single exception; the CP2109 requires an additional capacitor between VPP and GND for in-application programming. This capacitor is not required after the CP2109 EPROM has been successfully programmed or if the CP2109 does not need to be customized in system.

# 11.2. Distinguishing Factors

The CP2102 has 1024 bytes of EEPROM for vendor ID (VID), product ID (PID), serial number, power descriptor, release number, and product description strings. This configuration EEPROM can be written and re-written multiple times. The CP2109 has 1024 bytes of one-time programmable EPROM for configuration. This configuration EPROM can only be written one time.

The CP2109 may require an additional capacitor on VPP if in-application programming is desired.

The CP2102 default serial number is always “0001”. Every CP2109 is programmed from the factory with a unique serial number.

# 11.3. Differences in Electrical Specifications

Table 14 and Table 15 list differences in absolute maximum and electrical specifications between the CP2102 and CP2109. Refer to "3. Electrical Specifications" on page 5 for the comprehensive electrical specifications.

Table 14. Differences in Absolute Maximum Specifications between CP2102 and CP2109   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>CP2102</td><td rowspan=1 colspan=1>CP2109</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Voltage on any I/O Pin, VBUS, or RST withrespect to GND, Maximum</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD&gt;3.0VVD not powered</td><td rowspan=1 colspan=1>5.85.8</td><td rowspan=1 colspan=1>5.8VDD +3.6</td><td rowspan=1 colspan=1>V</td></tr></table>

Table 15. Differences in Electrical Specifications between CP2102 and CP2109   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>CP2102</td><td rowspan=1 colspan=1>CP2109</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Supply Current—Normal, Typical</td><td rowspan=1 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Normal Operation;VREG Enabled</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Supply Current—Normal, Maximum</td><td rowspan=1 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Normal Operation;VREG Enabled</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Supply Current——Suspended, Typical</td><td rowspan=1 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Bus Powered;VREG Enabled</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Supply Current—Suspended, Maximum</td><td rowspan=1 colspan=1>IREGIN</td><td rowspan=1 colspan=1>Bus Powered;VREG Enabled</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>230</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Output High Voltage, Minimum</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>1 H = -3 mA</td><td rowspan=1 colspan=1>VDD-0.7</td><td rowspan=1 colspan=1>$VD-0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output High Voltage, Typical</td><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>1OH =-10mA</td><td rowspan=1 colspan=1>VD-0.8</td><td rowspan=1 colspan=1>VDD -0.4</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage, Maximum</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>1OL=8.5mA</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Output Low Voltage, Typical</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>1OL=25mA</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input High Voltage, Minimum</td><td rowspan=1 colspan=1>VIH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>0.7×VD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input Low Voltage, Maximum</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr></table>

Table 15. Differences in Electrical Specifications between CP2102 and CP2109 (Continued)   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>CP2102</td><td rowspan=1 colspan=1>CP2109</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>RST Input High Voltage, Minimum</td><td rowspan=1 colspan=1>VIHRESET</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7×VDD</td><td rowspan=1 colspan=1>0.75×VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>RST Input Low Voltage, Maximum</td><td rowspan=1 colspan=1>VILRESET</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.25×VDD</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Regulator Input Voltage Range, Minimum</td><td rowspan=1 colspan=1>VREGIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Regulator Output Voltage, Minimum</td><td rowspan=1 colspan=1>VDDOUT</td><td rowspan=1 colspan=1>Output Current = 1to100mA*</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Regulator Output Voltage, Typical</td><td rowspan=1 colspan=1>VDDOUT</td><td rowspan=1 colspan=1>Output Current = 1to100mA*</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>3.45</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VBUS Detection Input Threshold, Minimum</td><td rowspan=1 colspan=1>VVBUSTH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VBUS Detection Input Threshold, Typical</td><td rowspan=1 colspan=1>VVBUSTH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VBUS Detection Input Threshold, Maximum</td><td rowspan=1 colspan=1>VVBUSTH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.9</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Regulator Bias Current, Typical</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>83</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Regulator Bias Current, Maximum</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>99</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>USB Transceiver Output Impedance, Typical</td><td rowspan=1 colspan=1>ZDRV</td><td rowspan=1 colspan=1>Driving HighDriving Low</td><td rowspan=1 colspan=1>3838</td><td rowspan=1 colspan=1>3636</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>Voltage on Vpp with respect to GND during aROM programming operation, Minimum</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD&gt;3.3V</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>5.75</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Voltage on Vpp with respect to GND during aROM programming operation, Maximum</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD&gt;3.3 V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD + 3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Capacitor on Vpp for In-applicationProgramming, Typical</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>4.7</td><td rowspan=1 colspan=1>μF</td></tr></table>

# 12. Relevant Application Notes

The following application notes are applicable to the CP2102/9. The latest versions of these application notes and their accompanying software are available at:   
http://www.silabs.com/products/mcu/Pages/ApplicationNotes.aspx.

 AN169: USBXpress® Programmer's Guide—This application note describes the USBXpress API interface and includes example code.

AN197: Serial Communications Guide for the CP210x—This application note describes how to use the standard Windows COM port function to communicate with the CP2102/9 and includes example code.

 AN220: USB Driver Customization—This application note describes how to use the AN220 software to customize the VCP or USBXpress drivers with OEM information.

AN721: CP210x/CP211x Device Customization Guide—This application note describes how to use the AN721 software to configure the USB parameters on the CP2102/9 devices.

# DOCUMENT CHANGE LIST

# Revision 1.0 to Revision 1.1

Updated “Linux 2.40” bullet on page 1.   
Changed MLP to QFN throughout.

# Revision 1.1 to Revision 1.2

Added additional supported operating systems on page 1.   
Changed VDD conditions of Tables 3 and 4 from a minimum of 2.7 to 3.0 V.   
Updated typical and max Supply Current number in Table 3.   
Removed tantalum requirement in Figure 5.   
Consolidated Sections 8 and 9.   
Added Section "12. Relevant Application Notes" on page 23.

# Revision 1.2 to Revision 1.3

Updated Figure 1 on page 1.   
Updated Figure 5 on page 14.   
Updated Maximum VBUS Detection Input Threshold in Table 6 on page 8.

# Revision 1.3 to Revision 1.4

Updated Table 4 RST Input Low Voltage Updated Table 10, Note 4. Updated Table 11, Note 10.

# Revision 1.4 to Revision 1.5

 Added CP2109. Updated Single-Chip USB to UART Data Transfer bullet on page 1. Added CP2109 to Ordering Part Numbers on page 1. Updated Section "1. System Overview" on page 3. Updated Figure 1. Added Section "2. Ordering Information" on page 4. Added Symbol columns to Tables in Section "3. Electrical Specifications" on page 5. Updated Table 3. - Added CP2109, Note 1, Note 2. - Updated thermal resistance spec. - Updated normal supply current spec. Updated Table 4, added CP2109, added Baud Rate. Updated Table 5, added CP2109, added VDD Ramp Time. Moved Table 6. Updated Table 6, added CP2109. Added Table 7. Added Table 8. Updated Table 9. - Updated pin 18 spec, Note 1, Note 2. Updated Figure 2, added CP2109, pin 18. Updated Section "6. USB Function Controller and Transceiver" on page 14, added CP2109. Updated Figure 5, added CP2109, Option 5.

Updated Section "8. Internal Programmable ROM" on page 16, added CP2109.   
Updated Table 12.   
- Updated Note 2 app note reference.   
Updated Table 13.   
- Added CP2109.   
Updated Table 15.   
- Updated normal maximum and suspended maximum supply current specs.   
Updated Section "10. Voltage Regulator" on page 18, changed AN144 to AN721.   
Added Section "11. Porting Considerations from CP2102 to CP2109" on page 21.   
Updated "11.2. Distinguishing Factors" on page 21. - Updated CP2102 default serial number to “0001”. Updated Section "12. Relevant Application Notes" on page 23.   
- Replaced AN144/AN205 with AN721.

# Revision 1.5 to Revision 1.6

Added mention of VBUS in Table 2, “Absolute Maximum Ratings,” on page 5 and split out port I/O maximums for CP2102 and CP2109. Added VPP voltage specifications to Table 8, “EPROM Electrical Characteristics,” on page 9. Updated "10. Voltage Regulator" on page 18 to add CP2109 absolute maximum voltage on VBUS requirements in self-powered systems. Updated "11.3. Differences in Electrical Specifications" on page 21 to include the new or modified specifications.

# Revision 1.6 to Revision 1.7

 Added Note to front page

# Simplicity Studio"4

![](images/d5b4310b88cf5ae5982b2d869741af45881b945404a6e41bedb676aa8e3c82b1.jpg)

# Simplicity Studio

One-click access to MCU and wireless tools, documentation, software, source code libraries & more. Available for Windows, Mac and Linux!

![](images/3527527d8b6add186cf8a5f436c9ad51d28a17873581f60bcf8fed74f1a015f9.jpg)

![](images/a65d07e42f71ac92cf0234201ca15f0f7f8e67abc4b634528d4446c874e4af19.jpg)

![](images/bb2e24ab7ca9e29bb56b73591fb6d2a86a3b57f51925d0d3bc5402fba2b1c54d.jpg)

![](images/bdc02278c7fa1c4858e4013e9703a171d3b329a01754d24e265c1e1c741a945b.jpg)

IoT Portfolio www.silabs.com/IoT

SW/HW www.silabs.com/simplicity

Quality www.silabs.com/quality

Support and Community community.silabs.com

# Disclaimer

Silicon Laboratories intends to provide customers with the latest, accurate, and in-depth documentation of all peripherals and modules available for system and software implementers using or intending to use the Silicon Laboratories products. Characterization data, available modules and peripherals, memory sizes and memory addresses refer to each specific device, and "Typical" parameters provided can and do vary in different applications. Application examples described herein are for illustrative purposes only. Silicon Laboratories reserves the right to make changes without further notice and limitation to product information, specifications, and descriptions herein, and does not give warranties as to the accuracy or completeness of the included information. Silicon Laboratories shall have no liability for the consequences of use of the information supplied herein. This document does not imply or express copyright licenses granted hereunder to design or fabricate any integrated circuits. The products are not designed or authorized to be used within any Life Support System without the specific written consent of Silicon Laboratories. A "Life Support System" is any product or system intended to support or sustain life and/or health, which, if it fails, can be reasonably expected to result in significant personal injury or death. Silicon Laboratories products are not designed or authorized for military applications. Silicon Laboratories products shall under no circumstances be used in weapons of mass destruction including (but not limited to) nuclear, biological or chemical weapons, or missiles capable of delivering such weapons.

# Trademark Information

Silicon Laboratories Inc.® , Silicon Laboratories®, Silicon Labs®, SiLabs® and the Silicon Labs logo®, Bluegiga®, Bluegiga Logo®, Clockbuilder®, CMEMS®, DSPLL®, EFM®, EFM32®, EFR, Ember®, Energy Micro, Energy Micro logo and combinations thereof, "the world’s most energy friendly microcontrollers", Ember®, EZLink®, EZRadio®, EZRadioPRO®, Gecko®, ISOmodem®, Precision32®, ProSLIC®, Simplicity Studio®, SiPHY®, Telegesis, the Telegesis Logo®, USBXpress® and others are trademarks or registered trademarks of Silicon Laboratories Inc. ARM, CORTEX, Cortex-M3 and THUMB are trademarks or registered trademarks of ARM Holdings. Keil is a registered trademark of ARM Limited. All other products or brand names mentioned herein are trademarks of their respective holders.

Silicon Laboratories Inc. 400 West Cesar Chavez Austin, TX 78701 USA