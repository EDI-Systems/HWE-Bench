# bq25895 I2C Controlled Single Cell 5-A Fast Charger with MaxChargeTM for High Input Voltage and Adjustable Voltage 3.1-A Boost Operation

# 1 Features

High Efficiency 5-A, 1.5-MHz Switch Mode Buck Charge

93% Charge Efficiency at 2 A and 91% Charge Efficiency at 3 A Charge Current Optimize for High Voltage Input (9 V to 12 V) Low Power PFM mode for Light Load Operations

Boost Mode Operation with Adjustable Output from 4.5 V to 5.5 V

Selectable 500-KHz to 1.5-MHz Boost Converter with up to 3.1-A Output – 93% Boost Efficiency at 5 V at 1 A Output

Ship Mode • High Accuracy

±0.5% Charge Voltage Regulation – ±5% Charge Current Regulation – ±7.5% Input Current Regulation

Safety Battery Temperature Sensing for Charge and Boost Mode Thermal Regulation and Thermal Shutdown Create a Custom Design Using the bq25895 With the WEBENCH® Power Designer

Integrated Control to Switch Between Charge and Boost Mode

Single Input to Support USB Input and Adjustable High Voltage Adapters

# 2 Applications

• Power Bank, Mobile Wi-Fi Hotspot• Wireless Bluetooth SpeakerC Portable Internet Devices

Support 3.9-V to 14-V Input Voltage Range Input Current Limit (100 mA to 3.25 A with 50- mA resolution) to Support USB2.0, USB3.0 standard and High Voltage Adapters Maximum Power Tracking by Input Voltage Limit up-to 14V for Wide Range of Adapters Auto Detect USB SDP, CDP, DCP, and Nonstandard Adapters

Input Current Optimizer (ICO) to Maximize Input Power without Overloading Adapters

Resistance Compensation (IRCOMP) from Charger Output to Cell Terminal

Highest Battery Discharge Efficiency with 11-mΩ Battery Discharge MOSFET up to 9 A

# 3 Description

The bq25895 is a highly-integrated 5-A switch-mode battery charge management and system power path management device for single cell Li-Ion and Lipolymer battery. The devices support high input voltage fast charging. The low impedance power path optimizes switch-mode operation efficiency, reduces battery charging time and extends battery life during discharging phase.

Integrated ADC for System Monitor (Voltage, Temperature, Charge Current)

• Narrow VDC (NVDC) Power Path Management

Instant-on Works with No Battery or Deeply Discharged Battery   
Ideal Diode Operation in Battery Supplement Mode

Device Information(1)   

<table><tr><td rowspan=1 colspan=1>PART NUMBER</td><td rowspan=1 colspan=1>PACKAGE</td><td rowspan=1 colspan=1>BODY SIZE (NOM)</td></tr><tr><td rowspan=1 colspan=1>bq25895</td><td rowspan=1 colspan=1>WQFN (24)</td><td rowspan=1 colspan=1>4.00mm ×4.00mm</td></tr></table>

BATFET Control to Support Ship Mode, Wake Up, and Full System Reset

Flexible Autonomous and I2C Mode for Optimal System Performance

High Integration includes all MOSFETs, Current Sensing and Loop Compensation

• 12-µA Low Battery Leakage Current to Support (1) For all available packages, see the orderable addendum at the end of the datasheet.

# Simplified Schematic

![](images/e5a19b0279302922ce3f7d2a9febf6875c5de5d52c7090ced31c5d6dd4ed0f59.jpg)

# Table of Contents

# 1 Features.. 1

5 Description (continued).. 3

6 Pin Configuration and Functions. 4

# 7 Specifications... 6

7.1 Absolute Maximum Ratings ... 6   
7.2 ESD Ratings.. 6   
7.3 Recommended Operating Conditions.. 6   
7.4 Thermal Information. 7   
7.5 Electrical Characteristics. 7   
7.6 Timing Requirements. 11   
7.7 Typical Characteristics . 12

# 8 Detailed Description . 14

8.1 Functional Block Diagram .. 14   
8.2 Feature Description.. 15   
8.3 Device Functional Modes. 30

# 8.4 Register Maps. 32

# 9 Application and Implementation . 49

9.1 Application Information.. 49   
9.2 Typical Application .. 49   
9.3 System Examples . 54

# 10 Power Supply Recommendations .. 55

11 Layout.. 55

11.1 Layout Guidelines . 55   
11.2 Layout Example .. 55

# 12 Device and Documentation Support .. 56

12.1 Development Support . 56   
12.2 Receiving Notification of Documentation Updates 56   
12.3 Community Resources. 56   
12.4 Trademarks. 56   
12.5 Electrostatic Discharge Caution..   
12.6 Glossary ... 56

# 13 Mechanical, Packaging, and Orderable

Information .. 56

# 4 Revision History

# Changes from Revision A (May 216) to Revision B

#

Added "SW (peak for 10 ns duration)" To the Absolute Maximum Rating 6   
Updated the Thermal Information values .... 7   
Changed VSYS TYP value From: VBAT + 50 mV To: I(SYS) + 150 mV .. ... 7   
Changed the title of Figure 4 From: Charge Current Accuracy To: I2C Setting .... . 12   
Changed axis title of Figure 8 From: BAT Voltage (V) To: Input Current Limit (mA). 12   
Changed VVREF to VREGN in Figure 15.. 23   
Changed VVREF to VREGN in Equation 2.. 23   
Changed VREF to VREGN in Figure 16 . 24   
Added sentence to the Battery Monitor secton "In battery only mode, ..". . 24   
Changed bit 5 From: 0 To: 1 in Figure 29 . . 35   
Changed the Description values of Table 26 From: mV To: mA. . 47   
Changed the Type values of Bits 6 to Bit 0 in Table 28 From: R/W To: R . 48   
Added VREF system pullup voltage to Table 29 . 49   
Changed Figure 49.. 52

# Changes from Original (March 2015) to Revision A

Added Pin Configuration and Functions section, ESD Rating table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section. . 1

# 5 Description (continued)

The I2C Serial interface with charging and system settings makes the device a truly flexible solution.

The device supports a wide range of input sources, including standard USB host port, USB charging port, and USB compliant adjustable high voltage adapter. To support fast charging using adjustable high voltage adapter, the bq25895 provides support MaxChargeTM using D+/D– pins and DSEL pin for USB switch control. In addition, the device includes interface to support adjustable high voltage adapter using input current pulse protocol. To set the default input current limit, device uses the built-in USB interface. The device is compliant with USB 2.0 and USB 3.0 power spec with input current and voltage regulation. In addition, the Input Current Optimizer (ICO) supports the detection of maximum power point detection of the input source without overload. The device supports battery boost operation by supplying adjustable 4.5 V to 5.5 V on PMID pin with up to 3.1 A with integrated charge and boost mode detection

# 6 Pin Configuration and Functions

![](images/a071c0372074f8d08bc0a86b740217f489a714096da582efef8dd488ee5036a7.jpg)

Pin Functions   

<table><tr><td rowspan=1 colspan=2>PIN</td><td rowspan=2 colspan=1>TYPE(1)</td><td rowspan=2 colspan=1>DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>NAME</td><td rowspan=1 colspan=1>NO.</td></tr><tr><td rowspan=1 colspan=1>VBUS</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>Charger Input Voltage.The internal n-channel reverse block MOSFET (RBFET) is connected between VBUS and PMID with VBUS onsource. Place a 1-uF ceramic capacitor from VBUS to PGND and place it as close as possible to IC.</td></tr><tr><td rowspan=1 colspan=1>D+</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>AIO</td><td rowspan=1 colspan=1>Positive line of the USB data line pair.D+/D- based USB host/charging port detection. The detection includes data contact detection (DCD), primaryand secondary detection in BC1.2, and Adjustable high voltage adapter (MaxCharge).</td></tr><tr><td rowspan=1 colspan=1>D-</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>AIO</td><td rowspan=1 colspan=1>Negative line of the USB data line pair.D+/D- based USB host/charging port detection. The detection includes data contact detection (DCD), primaryand secondary detection in Bc1.2, and Adjustable high voltage adapter (MaxCharge).</td></tr><tr><td rowspan=1 colspan=1>STAT</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>DO</td><td rowspan=1 colspan=1>Open drain charge status output to indicate various charger operation.Connect to the pullup rail via 10-kΩ2 resistor. LOW indicates charge in progress. HIGH indicates chargecomplete or charge disabled. When any fault condition occurs, STAT pin blinks in 1 Hz.The STAT pin function can be disabled when STAT_DIS bit is set.</td></tr><tr><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>DI</td><td rowspan=1 colspan=1>|2C Interface clock.Connect SCL to the logic rail through a 10-kΩ resistor.</td></tr><tr><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DIO</td><td rowspan=1 colspan=1>2C Interface data.Connect SDA to the logic rail through a 10-kΩ resistor.</td></tr><tr><td rowspan=1 colspan=1>INT</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>DO</td><td rowspan=1 colspan=1>Open-drain Interrupt Output.Connect the INT to a logic rail via 10-kΩ resistor. The INT pin sends active low, 256-us pulse to host to reportcharger device status and fault.</td></tr><tr><td rowspan=1 colspan=1>OTG</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>DI</td><td rowspan=1 colspan=1>Boost mode enable pin.The boost mode is activated when OTG_CONFIG =1, OTG pin is high, and no input source is detected atVBUS</td></tr><tr><td rowspan=1 colspan=1>CE</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>DI</td><td rowspan=1 colspan=1>Active low Charge Enable pin.Battery charging is enabled when CHG_CONFIG = 1 and CE pin = Low. CE pin must be pulled High or Low.</td></tr></table>

# Pin Functions (continued)

<table><tr><td rowspan=1 colspan=2>PIN</td><td rowspan=2 colspan=1>TYPE(1)</td><td rowspan=2 colspan=1>DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>NAME</td><td rowspan=1 colspan=1>NO.</td></tr><tr><td rowspan=1 colspan=1>ILIM</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Al</td><td rowspan=1 colspan=1>Input current imit Input. ILIM pin sets the maximum input current and can be used to monitor input currentILiM pin sets the maximum input current limit by regulating the ILIM voltage at 0.8 V. A resistor is connectedfrom ILiM pin to grund to set the maximum imit as linmax = Kum/RLm.The actual input current limit is thelower limit set by ILIM pin (when EN_ILIM bit is high) or INLIM register bits. Input current limit of less than 500mA is not support on ILIM pin.ILIM pin can also be used to monitor input current when the voltage is below 0.8V. The input current isproportional to the voltage on ILIM pin and can be calculated by lin = (KiLim × ViLim)/ (RiLim × 0.8)The ILIM pin function can be disabled when EN_ILIM bit is 0.</td></tr><tr><td rowspan=1 colspan=1>TS</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>Al</td><td rowspan=1 colspan=1>Temperature qualification voltage input.Connect a negative temperature coefficient thermistor. Program temperature window with a resistor dividerfrom REGN to TS to GND. Charge suspends when either TS pin is out of range. Recommend 103AT-2thermistor.</td></tr><tr><td rowspan=1 colspan=1>QON</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>DI</td><td rowspan=1 colspan=1>BATFET enable/reset control input.When BATFET is in ship mode, a logic low of tsHipmoDE (typical 1sec) duration turns on BATFET to exitshipping mode. .When VBUs is not plugged-in, a logic low of taon_Rst (typical 10sec) duration resets SYS (system power) byturning BATFET off for tBATFET_RsT (typical O.sec) and then re-enable BATFET to provide ful system powerreset.The pin contains an internal pull-up to maintain default high logic</td></tr><tr><td rowspan=1 colspan=1>BAT</td><td rowspan=1 colspan=1>13,14</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>Battery connection point to the positive terminal of the battery pack.The internal BATFET is connected between BAT and SYS. Connect a 10uF closely to the BAT pin.</td></tr><tr><td rowspan=1 colspan=1>SYS</td><td rowspan=1 colspan=1>15,16</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>System connection point.The internal BATFET is connected between BAT and SYS. When the battery falls below the minimum systemvoltage, switch-mode converter keeps SYS above the minimum system voltage. Connect a 20uF closely to theSYS pin.</td></tr><tr><td rowspan=1 colspan=1>PGND</td><td rowspan=1 colspan=1>17,18</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>Power ground connection for high-current power converter node.Internally, PGND is connected to the source of the n-channel LSFET. On PCB layout, connect directl toground connection of input and output capacitors of the charger. A single point connection is recommendedbetween power PGND and the analog GND near the IC PGND pin.</td></tr><tr><td rowspan=1 colspan=1>SW</td><td rowspan=1 colspan=1>19,20</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>Switching node connecting to output inductor.Internally SW is connected to the source of the n-channel HSFET and the drain of the n-channel LSFET.Connect the 0.047μF bootstrap capacitor from SW to BTST.</td></tr><tr><td rowspan=1 colspan=1>BTST</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>PWM high side driver positive supply.Internally, the BTST is connected to the anode of the boost-strap diode. Connect the 0.047F bootstrapcapacitor from SW to BTST.</td></tr><tr><td rowspan=1 colspan=1>REGN</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>PWM low side driver positive supply output.Internally, REGN is connected to the cathode of the boost-strap diode. Connect a 4.7μF (10 V rating) ceramiccapacitor from REGN to analog GND. The capacitor should be placed close to the IC. REGN also serves asbias rail of TS pin.</td></tr><tr><td rowspan=1 colspan=1>PMID</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>DO</td><td rowspan=1 colspan=1>Battery boost mode output.Connected to the drain of the reverse blocking MOSFET (RBFET) and the drain of HSFET. The minimumcapacitance required on PMID to PGND is 40μF for up-to 2.4A output and 60μF for up-to 3.1A output</td></tr><tr><td rowspan=1 colspan=1>DSEL</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>DO</td><td rowspan=1 colspan=1>Open-drain D+/D- multiplexer selection control.Connect the DSEL to a logic rail via 10-KQ resistor. The pin is normall float and pull-up by external resistor.During Input Source Type Detection , the pin drives low to indicate the device D+/D- detection is in progressand needs to take control of D+, D- signals. When detection is completed, the pin keeps low when MaxChargeis detected. The pin returns to float and pulls high by external resistor when other input source type is detected.</td></tr><tr><td rowspan=1 colspan=1>PowerPAD TM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>Exposed pad beneath the IC for heat dissipation. Always solder PowerPAD Pad to the board, and have vias onthe PowerPAD plane star-connecting to PGND and ground plane for high-current power converter.</td></tr></table>

# 7 Specifications

# 7.1 Absolute Maximum Ratings(1)

over operating free-air temperature range (unless otherwise noted)

<table><tr><td colspan="2"></td><td>MIN</td><td>MAX</td><td>VALUE</td></tr><tr><td rowspan="12">Voltage range (with respect to GND)</td><td>VBUS (converter not switching)</td><td>-2</td><td>22</td><td>V</td></tr><tr><td>PMID (converter not switching)</td><td>-0.3</td><td>22</td><td>V</td></tr><tr><td>STAT</td><td>-0.3</td><td>20</td><td>V</td></tr><tr><td>DSEL</td><td>-0.3</td><td>20</td><td>V</td></tr><tr><td>BTST</td><td>-0.3</td><td>20</td><td>V</td></tr><tr><td>SW</td><td>-2</td><td>16</td><td>V</td></tr><tr><td>SW (peak for 10 ns duration)</td><td>-3</td><td>16</td><td>V</td></tr><tr><td>BAT, SYS (converter not switching)</td><td>-0.3</td><td>6</td><td>V</td></tr><tr><td>SDA, SCL, INT, OTG, REGN, TS, CE, QON</td><td>-0.3</td><td>7</td><td>V</td></tr><tr><td>D+,D-</td><td>-0.3</td><td>7</td><td>V</td></tr><tr><td>BTST TO SW PGND to GND</td><td>-0.3</td><td>7</td><td>V</td></tr><tr><td>ILIM</td><td>-0.3</td><td>0.3</td><td>V</td></tr><tr><td rowspan="2">Output sink current</td><td>INT, STAT</td><td>-0.3</td><td>5</td><td>V</td></tr><tr><td>DSEL</td><td></td><td>6</td><td>mA</td></tr><tr><td>Junction temperature</td><td></td><td>-40</td><td>6</td><td>mA</td></tr><tr><td>Storage temperature range, Tstg</td><td></td><td>-65</td><td>150 150</td><td>℃ ℃</td></tr></table>

(1) Stresses beyond those listed under absolute maximum ratings may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under recommended operating conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. All voltage values are with respect to the network ground terminal unless otherwise noted.

# 7.2 ESD Ratings

<table><tr><td></td><td></td><td rowspan=1 colspan=1>VALUE</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=2 colspan=1>VESD       Electrostatic discharge</td><td rowspan=1 colspan=1>Human body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1)</td><td rowspan=1 colspan=1>±2000</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Charged device model (CDM), per JEDEC specificationJESD22-C101(2)</td><td rowspan=1 colspan=1>±250</td><td rowspan=1 colspan=1>V</td></tr></table>

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.   
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

# 7.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

<table><tr><td></td><td></td><td rowspan=1 colspan=1>MIN  NOM                     MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=2>ViN       Input voltage</td><td rowspan=1 colspan=1>3.9                              14(1)</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=2>liN        Input current (VBUS)</td><td rowspan=1 colspan=1>3.25</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=2>1sys      Output current (SW)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=2>VBAT      Battery voltage</td><td rowspan=1 colspan=1>4.608</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=3 colspan=1>BAT</td><td rowspan=1 colspan=1>Fast charging current</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=2 colspan=1>Discharging current with internal MOSFET</td><td rowspan=1 colspan=1>Up to 6 (continuos)</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>9 (peak)(Up to 1 sec duration)</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=2>T d:        Operating free-air temperature range</td><td rowspan=1 colspan=1>-40                                 85</td><td rowspan=1 colspan=1>°℃</td></tr></table>

(1) The inherent switching noise voltage spikes should not exceed the absolute maximum rating on either the BTST or SW pins. A tight layout minimizes switching noise.

# 7.4 Thermal Information

<table><tr><td rowspan=3 colspan=1>THERMAL METRIC (1)</td><td rowspan=1 colspan=1>bq25895</td><td rowspan=3 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>RTW (WQFN)</td></tr><tr><td rowspan=1 colspan=1>24-PINS</td></tr><tr><td rowspan=1 colspan=1>ROJA           Junction-to-ambient thermal resistance</td><td rowspan=1 colspan=1>31.8</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>RaJC(op)       Junction-to-case (top) thermal resistance</td><td rowspan=1 colspan=1>27.9</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>ROJB           Junction-to-board thermal resistance</td><td rowspan=1 colspan=1>8.7</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>YJT            Junction-to-top characterization parameter</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>YJB            Junction-to-board characterization parameter</td><td rowspan=1 colspan=1>8.7</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>ReJC(bot)       Junction-to-case (bottom) thermal resistance</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>CW</td></tr></table>

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

# 7.5 Electrical Characteristics

VVBUS_UVLOZ < VVBUS < VACOV and VVBUS > VBAT + VSLEEP, TJ = –40°C to +125°C and TJ = 25°C for typical values (unless otherwise noted)

<table><tr><td colspan="2">PARAMETER</td><td>TEST CONDITIONS</td><td>MIN</td><td>TYP</td><td>MAX</td><td>UNIT</td></tr><tr><td colspan="2">QUIESCENT CURRENTS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">1BAT</td><td rowspan="4">Battery discharge current (BAT, SW, SYS) in buck mode</td><td>VBAT =4.2V, VBus)&lt;V(uvLO), leaage eeen BATnVBUS</td><td></td><td></td><td></td><td>μA</td></tr><tr><td>High-Z mode, no VBUS, BATFET disabled (REG09[5]=1), battery monitor disabled, TJ &lt; 85℃</td><td></td><td>12</td><td>23</td><td>μA</td></tr><tr><td>High-Z mode, no VBUS, BATFET enabled (REG09[5]=0), battery monitor disabled, TJ&lt;</td><td></td><td>32</td><td>60</td><td>μA</td></tr><tr><td>85℃ us=5, Hghmode, nobatery, batte monitor disabled</td><td></td><td>15</td><td>35</td><td>μA</td></tr><tr><td rowspan="2">is enabled</td><td>V(vBus)= 12 V, High-Z mode, no battery, battery monitor disabled</td><td></td><td>25</td><td>50d</td><td>μA</td></tr><tr><td>us&gt;),Vu&gt;AT, e switching</td><td></td><td>1.5</td><td></td><td>mA</td></tr><tr><td rowspan="4">l(vBuS)</td><td rowspan="4">Input supply current (Vsus) in buck mode</td><td>VBUs &gt;V(uO),VBus&gt;VBAT, COvee Sihing,VBAT=3.2V, Is=0A</td><td>3</td><td></td><td>3</td><td></td></tr><tr><td>Vus &gt;)Vu&gt;VBAT, Ce</td><td></td><td></td><td></td><td>mA</td></tr><tr><td>Sitching,VBAT=3.8V,Iss=0A VBAT = 4.2 V, boost mode, vBus)= 0A,</td><td></td><td>3</td><td></td><td>mA</td></tr><tr><td>converter switching</td><td></td><td>5</td><td></td><td>mA</td></tr><tr><td colspan="8">VBUS/BAT POWER UP</td></tr><tr><td>V(VBUS_OP)</td><td>VBUS operating range</td><td></td><td>3.9</td><td></td><td>14</td><td>V</td></tr><tr><td>VvBUSs_UWLOZ)</td><td>VBUS for active I²C, no battery</td><td></td><td>3.6</td><td></td><td></td><td>V</td></tr><tr><td>V(SLEEP)</td><td>Sleep mode falling threshold</td><td></td><td>25</td><td>65</td><td>120d</td><td>mV</td></tr><tr><td>V(SLEEPZ))</td><td>Sleep mode rising threshold</td><td></td><td>130</td><td>250</td><td>370</td><td>mV</td></tr><tr><td>VACOV</td><td>VBUS over-voltage rising threshold</td><td></td><td>14</td><td></td><td>14.6</td><td>V</td></tr><tr><td></td><td>VBUS over-voltage falling threshold</td><td></td><td>13.5</td><td></td><td>14</td><td>V</td></tr><tr><td>VBAT(UVLOZ)</td><td>Battery for active I2C, no VBUS Battery depletion falling threshold</td><td></td><td>2.3</td><td></td><td></td><td>V</td></tr><tr><td>VBAT(DPL)</td><td>Battery depletion rising threshold</td><td></td><td>2.15</td><td></td><td>2.5</td><td>V</td></tr><tr><td>VBAT(DPLZ)</td><td>Bad adapter detection threshold</td><td></td><td>2.35</td><td></td><td>2.7</td><td>V</td></tr><tr><td>VvBUSMIN) (BADSRC)</td><td>Bad adapter detection current source</td><td></td><td></td><td>3.8</td><td></td><td>V</td></tr><tr><td colspan="2">POWER-PATH MANAGEMENT</td><td></td><td></td><td>30</td><td></td><td>mA</td></tr><tr><td rowspan="2">Vsrs</td><td rowspan="2">Typical system regulation voltage</td><td>ISS) = OA, VBAT&gt; VsYS(MN, BATFET Disabled (REG09[5]=1)</td><td>50mV</td><td>$VBAT+</td><td></td><td>V</td></tr><tr><td>)=OA,VBAT&lt;V(,BATFETDisabl (REG09[5]=1) VBAT&lt;VsS(MN, SYS_MIN = 3.5V</td><td>VsyS(MiN) + 150mV</td><td></td><td></td><td>V</td></tr><tr><td>VsYS(MIN))</td><td>Minimum DC system voltage output</td><td>(REG03[3:1]=101), Isys= 0A VBAT =4.35V, SYS_MIN =3.5V</td><td>3.50</td><td>3.65</td><td></td><td>V</td></tr><tr><td>VsYS(MAXx))</td><td>Maximum DC system voltage output</td><td>(REG03[3:1]=101), sys= 0 A</td><td></td><td>4.40</td><td>4.42</td><td>V</td></tr><tr><td>RON(RBFET))</td><td>Top reverse blocking MOSFET(RBFET) on-resistance between VBUS and PMID</td><td>Tj = −40°C to +85°℃ Tj = −40°C to +125°℃</td><td></td><td>27 27</td><td>38 44</td><td>mΩ2 mΩ</td></tr></table>

# Electrical Characteristics (continued)

VVBUS_UVLOZ < VVBUS < VACOV and VVBUS > VBAT + VSLEEP, TJ = –40°C to +125°C and TJ = 25°C for typical values (unless otherwise noted)   

<table><tr><td colspan="3">otnerwise Totea) PARAMETER</td><td rowspan="2">MIN</td><td rowspan="2">TYP</td><td rowspan="2">MAX</td><td rowspan="2">UNIT</td></tr><tr><td></td><td>Top switching MOSFET (HSFET) on-resistance between PMID</td><td>TEST CONDITIONS T = 40°℃C to+85°℃C</td><td>27</td></tr><tr><td rowspan="2">RON(HSFET) and SW</td><td rowspan="2"></td><td></td><td></td><td>27</td><td>39</td><td>mΩ2</td></tr><tr><td>Tj= -40^cC to +125°℃C</td><td></td><td></td><td>47</td><td>mΩ2</td></tr><tr><td>RON(LSFET)</td><td>Bottom switching MOSFET (LSFET) on-resistance between SW and GND</td><td>$Tj = -40^℃C to +85°℃</td><td></td><td>16</td><td>24 28</td><td>mΩ2 mΩ</td></tr><tr><td>V(WD</td><td></td><td>Tj= -40^℃C to +125°℃C</td><td></td><td>16</td><td></td><td>mV</td></tr><tr><td>VBAT(GD)</td><td>BATFET forward voltage in supplement mode</td><td>BAT discharge current 10 mA</td><td>3.4</td><td>30</td><td>3.7</td><td>V</td></tr><tr><td>VBAT(GD HYST)</td><td>Battery good comparator rising threshold Battery good comparator alling threshold</td><td>VaAT rising</td><td></td><td>3.55</td><td></td><td>mV</td></tr><tr><td>BATTERY CHARGER</td><td></td><td>VBAT faliing</td><td></td><td>100</td><td></td><td></td></tr><tr><td>VBAT(REG RANGE) Typical charge voltage range</td><td></td><td></td><td>3.840</td><td></td><td>4.608</td><td>V</td></tr><tr><td>VBAT(REG STEP)</td><td>Typical charge voltage step</td><td></td><td></td><td>16</td><td></td><td>mV</td></tr><tr><td rowspan="2">VBAT(REG)</td><td>Charge voltage resolution acuracy</td><td>VBAT = 4.208V (REG06[7:2]=010111) or</td><td>-0.5%</td><td></td><td></td><td></td></tr><tr><td></td><td>VBAT=4.352V(REG06[7:2]=10000) $Tj=-40^Cto+85°℃</td><td></td><td></td><td>0.5%</td><td></td></tr><tr><td>ICHG REG RANGE) (CHG_REG_STEP)</td><td>Typical fast charge current regulation range Typical fast charge current regulation step</td><td></td><td>0</td><td>64</td><td>5056</td><td>mA mA</td></tr><tr><td rowspan="3">(CHG_ REG_ ACC)</td><td rowspan="3">Fast charge curent regulation accuracy</td><td></td><td>-20%</td><td></td><td></td><td></td></tr><tr><td>VBAT = 3.1VOr3.8V, ICHG = 128mA $Tj=-40^℃Cto+85°℃</td><td>-10%</td><td></td><td>20%</td><td></td></tr><tr><td>VBAT=3.1VOr3.V，CHG=256mA $Tj= 40^℃C to+85^℃C$ VBA=3.V3V, CH=1792A</td><td>-5%</td><td></td><td>10%</td><td></td></tr><tr><td rowspan="3">VBATLOW)</td><td rowspan="3">Battery LOWV falling threshold Batery LOWV rising threshold</td><td>$Tj=40^℃Cto +85°℃</td><td>2.6</td><td></td><td>5%</td><td></td></tr><tr><td>Fast charge to precharge, BATLOWV (REG06[1) = 1</td><td></td><td>2.8</td><td>2.9</td><td>V</td></tr><tr><td>Precharge to fast charge, BATLOWV (REG06[1])=1 (Typical 200-mV hysteresis)</td><td>2.8</td><td>3</td><td>3.1</td><td>V</td></tr><tr><td>IPRECHG ANGE)</td><td>Precharge current range</td><td></td><td>64</td><td></td><td>1024</td><td>mA</td></tr><tr><td>IPRECHG STEP)</td><td>Typical precharge current tep</td><td></td><td></td><td>64</td><td></td><td>mA</td></tr><tr><td>IPRECHG ACC)</td><td>Precharge current acuracy</td><td>VBAT=2.6V, PRECHG = 256mA</td><td>-10%</td><td></td><td>+10%</td><td></td></tr><tr><td>I(TERM RANGE)</td><td>Termination curent range</td><td></td><td>64</td><td></td><td>1024</td><td>mA</td></tr><tr><td>(TERM STEP)</td><td>Typical termination current step</td><td></td><td></td><td>64</td><td></td><td>mA</td></tr><tr><td>(TERM ACC))</td><td rowspan="2"></td><td>ERM=256mA，CH&lt;=1344mA $Tj=-20{°Cto+85°C</td><td>-12%</td><td></td><td>12%</td><td></td></tr><tr><td>Terminatin current accuracy</td><td>ERM=256mA CH&gt;1344 mA</td><td>-20%</td><td></td><td></td><td></td></tr><tr><td>V(SHORT))</td><td>Battery short voltage</td><td>Tj=-20^{Ct0+85C VBAT falingg</td><td></td><td></td><td>20%</td><td></td></tr><tr><td>V(SHORT HNSTT)</td><td>Battery short voltage hysteresis</td><td>VBAT rising</td><td></td><td>2 200</td><td></td><td>V mV</td></tr><tr><td>(SHORT))</td><td>Battery short current</td><td>VBAT&lt;2.2 V</td><td></td><td>100</td><td></td><td>mA</td></tr><tr><td></td><td>Recharge threshold belowVBATREG</td><td>VBAT falling, VRECHG (REG06[0]=0) = 0</td><td></td><td>100</td><td></td><td>mV</td></tr><tr><td>V(RECHG))</td><td></td><td>VBAT falling, VRECHG (REG06[0]=0) = 1</td><td></td><td>200</td><td></td><td>mV</td></tr><tr><td>BATLOAD))</td><td>Batterydischarge load current</td><td>VBAT = 4.2 V</td><td>15</td><td></td><td></td><td>mA</td></tr><tr><td>IsYS(LOAD)</td><td>System discharge load current</td><td>$VsYs = 4.2V</td><td>30</td><td></td><td></td><td>mA</td></tr><tr><td>RON(BATFET)</td><td></td><td>T =25cC$</td><td></td><td>11</td><td>13</td><td>mΩ2</td></tr><tr><td></td><td>SYS-BAT MOSFET (BATFET) on-resistance</td><td>$Tj = -40^C o +125°℃</td><td></td><td>11</td><td>19</td><td>mΩ</td></tr><tr><td>INPUT VOLTAGE / CURRENT REGULATION</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ViNDPM RANGE)</td><td>Typical Input voltage regulation range</td><td></td><td>3.9</td><td></td><td>15.3</td><td>V</td></tr><tr><td>VIN(DPM STEP)</td><td>Typical Iput oltage regulation tep</td><td></td><td></td><td>100</td><td></td><td>mV</td></tr><tr><td>VINDPM AC)</td><td>Input voltage regulation accuracy</td><td>VINDPM = 4.4V, 9V</td><td>3%</td><td></td><td>3%</td><td></td></tr><tr><td>IN(DPM_ RANGE)</td><td>Typical Input current regulation range Typical Input current regulation step</td><td></td><td>100</td><td></td><td>3250</td><td>mA</td></tr><tr><td>IN(DPM _STEP) IN(DPM10AC)</td><td>u nt  ela</td><td>INLIM (REG00[5:0]) =100 mA</td><td></td><td>50</td><td></td><td>mA</td></tr><tr><td></td><td>VAT=, </td><td>USB150,IINLIM (REG00[5:0]) = 150 mA</td><td>85</td><td>90</td><td>100</td><td>mA</td></tr><tr><td rowspan="4">IN(DPM_ACC)</td><td rowspan="4">Input curent reulation accu VBAT= 5V, crent pule f </td><td>USB500, IINLIM (REG00[5:0]) = 500 mA</td><td>125 440</td><td>135 470</td><td>150 500</td><td>mA mA</td></tr><tr><td>USB900, IINLIM (REG00[5:0]) = 900 mA</td><td></td><td></td><td></td><td></td></tr><tr><td>Adapter 1.5A, INLM (REG00[5:0]) = 1500</td><td>750</td><td>825</td><td>900</td><td>mA</td></tr><tr><td>mA</td><td>1300</td><td>1400</td><td>1500</td><td>mA</td></tr><tr><td>INISTART))</td><td>Input current regulation during system start u</td><td>VsYS =2.2V, INLIM (REG00[5:0)&gt;= 200A</td><td></td><td></td><td>200</td><td>mA</td></tr></table>

# Electrical Characteristics (continued)

VVBUS_UVLOZ < VVBUS < VACOV and VVBUS > VBAT + VSLEEP, TJ = –40°C to +125°C and TJ = 25°C for typical values (unless

<table><tr><td colspan="7">otherwise noted)</td></tr><tr><td></td><td>PARAMETER</td><td>TEST CONDITIONS Input current regulation by LIM pin = 1.5 A</td><td>MIN 320</td><td>TYP 355</td><td>MAX 390</td><td>UNIT $Ax_$</td></tr><tr><td colspan="7">KLM INMAX = KL/RILIM</td></tr><tr><td colspan="7">D+/D- DETECTION</td></tr><tr><td>V(OP6_VSRC)</td><td>D+/D– voltage source (0.6 V)</td><td></td><td>0.5</td><td>0.6</td><td>0.7</td><td>V</td></tr><tr><td>V(3p45 VSRC))</td><td>D+/D– voltage source (3.45 V)</td><td></td><td>3.3</td><td>3.45</td><td>3.6</td><td>V</td></tr><tr><td>(10UA ISRC))</td><td>D+ connection check current source</td><td></td><td>7</td><td>10</td><td>14</td><td>μA</td></tr><tr><td>(100UA_ISINK))</td><td>D+/D- current sink (100 μA)</td><td></td><td>50</td><td>100</td><td>150</td><td>μA</td></tr><tr><td rowspan="2">(DPDM_LKG)</td><td rowspan="2">D+/D– Leakage current</td><td>D-, switch open</td><td>-1</td><td></td><td>1 μA</td><td></td></tr><tr><td>D+, switch open</td><td>-1</td><td></td><td>1</td><td>μA</td></tr><tr><td>(1P6MA_SINKR)</td><td>D+/D- current sink (1.6 mA)</td><td></td><td>1.45</td><td>1.60</td><td>1.75</td><td>μA</td></tr><tr><td>V(OP4_VTH)</td><td>D+/D- low comparator threshold</td><td></td><td>250</td><td></td><td>400</td><td>mV</td></tr><tr><td>V(OPBVTH))</td><td>D+ low comparator threshold</td><td></td><td></td><td></td><td>0.8</td><td>V</td></tr><tr><td>V(2P7- T)</td><td>D+/D- comparator threshold for non-standard adapter detection (divider 1, 3, or 4)</td><td></td><td>2.55</td><td></td><td>2.85</td><td>V</td></tr><tr><td>V(2PO.VT)</td><td>D+/D– comparator threshold for non-standard adapter detection (divider 1, 3)</td><td></td><td>1.85</td><td></td><td>2.15</td><td>V</td></tr><tr><td>V(1P2√TH))</td><td>D+/D– comparator threshold for non-standard adapter detection (divider 2)</td><td></td><td>1.05 14.25</td><td>24.8</td><td>1.35</td><td>V</td></tr><tr><td colspan="7">R(D-DOWN) D- pulldown for connection check BAT OVER-VOLTAGE/CURRENT PROTECTION</td></tr><tr><td colspan="7">Battery over-voltage threshold</td></tr><tr><td>VBAT(OVP) VBAT(OVP_HYST</td><td>Battery over-voltage hysteresis</td><td>VBAT rising, as percentage of VBA(REG) VaA alling  erentag of AE)</td><td colspan="3">104%</td><td></td></tr><tr><td>BAT(FET_OCP)</td><td>System over-current threshold</td><td></td><td>9</td><td>2%</td><td></td><td>A</td></tr><tr><td colspan="7"></td></tr><tr><td>THERMAL REGULATION AND THERMAL SHUTDOWN TREG</td><td>Junction temperature regulation accuracy</td><td>REG08[1:0] = 11</td><td></td><td>120</td><td>C</td><td></td></tr><tr><td>TSHUT</td><td>Thermal shutdown rising temperature</td><td>Temperature rising</td><td></td><td>160</td><td></td><td>C</td></tr><tr><td>TSHUTHVS)</td><td>Thermal shutdown hysteresis</td><td>Temperature falling</td><td></td><td>30</td><td></td><td>C</td></tr><tr><td>V(LTF$</td><td>Cold temperature threshold, TS pin voltage rising threshold</td><td>As percentage to V(REGN)</td><td>72.75%</td><td>73.25%</td><td>73.75%</td><td></td></tr><tr><td>VLTF HYS))</td><td>Cold temperature hysteresis, TS pin voltage falling</td><td>As percentage to V(REGN)</td><td></td><td>0.4%</td><td></td><td></td></tr><tr><td>V(HTF))</td><td>Hot temperature TS pin voltage rising threshold</td><td>As percentage to V(REGN)</td><td>47.75%</td><td>48.25%</td><td>48.75%</td><td></td></tr><tr><td>V(πco)</td><td>Cut-off temperature TS pin voltage falling threshold</td><td>As percentage to V(REGN)</td><td>44.25%</td><td>44.75%</td><td>45.25%</td><td></td></tr><tr><td colspan="7">COLD/HOT THERMISTOR COMPARATOR (BOOST MODE)</td></tr><tr><td>V(BCOLD1)</td><td>Cold temperature threshold 1, TS pin voltage rising threshold</td><td>As percentage to VREGN REG01[5] = 1 (Approximately -20°C w/ 103AT)</td><td>79.5%</td><td>80%</td><td>80.5%</td><td></td></tr><tr><td>V(BCOLD1 HVS))</td><td>Cold temperature threshold 1, TS pin voltage falling threshold</td><td>As percentage to VREGn REG01[5] = 1 As percentage to VReGN REG01[7:6] = 10</td><td></td><td>1%</td><td></td><td></td></tr><tr><td>V(BHOT2)</td><td>Hot temperature threshold 2, TS pin voltage falling threshold</td><td>(Approx. 65°℃ w/ 103AT)</td><td>30.75%</td><td>31.25%</td><td>31.75%</td><td></td></tr><tr><td>V(BHOT2 HYS)) PWM</td><td>Hot temperature threshold 2, TS pin voltage rising threshold</td><td>As percentage to VReGn REG01[7:6] =10</td><td></td><td>3%</td><td></td><td></td></tr><tr><td colspan="7"></td></tr><tr><td>FsW</td><td>PWM switching frequency, and digital clock</td><td>Oscillator frequency</td><td>1.32</td><td></td><td>1.68</td><td>MHz</td></tr><tr><td>DMAx BOOST MODE OPERATION</td><td>Maximum PWM duty cycle</td><td></td><td></td><td>97%</td><td></td><td></td></tr><tr><td colspan="7">Typical boost mode regulation voltage range</td></tr><tr><td>V(OTG REG RANGE) V(OTG REG STEP)</td><td>Typical boost mode regulation voltage step</td><td></td><td>4.55</td><td>64</td><td>5.55 V mV</td><td></td></tr><tr><td>V(OTG_REG_ACC)</td><td>Boost mode regulation voltage accuracy</td><td>I(PMID) = 0 A, BOOSTV=5.126V (REG0A[7:4] =1001)</td><td>-3%</td><td></td><td>3%</td><td></td></tr><tr><td>V(OTG BAT)</td><td>Battery voltage exiting boost mode</td><td>BAT fallingg</td><td>2.6</td><td></td><td>2.9</td><td>V</td></tr><tr><td>(oTG)</td><td>Boost mode output current range</td><td></td><td>3.1</td><td></td><td></td><td>A</td></tr><tr><td>V(OTG OVP)</td><td>Boost mode over-voltage threshold</td><td>Rising threshold</td><td>5.8</td><td>6</td><td>V</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Electrical Characteristics (continued)

VVBUS_UVLOZ < VVBUS < VACOV and VVBUS > VBAT + VSLEEP, TJ = –40°C to +125°C and TJ = 25°C for typical values (unless otherwise noted)

<table><tr><td colspan="3">otnerwise hotea)</td><td>MIN</td><td></td><td></td><td></td></tr><tr><td>PARAMETER</td><td colspan="3">TEST CONDITIONS</td><td>TYP</td><td>MAX</td><td>UNIT</td></tr><tr><td>REGN LDO</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>V(REGN))</td><td>REGN LDO output voltage</td><td>VVBUS) = 9V, (REGN) = 40mA</td><td>5.6</td><td>6</td><td>6.4</td><td>V</td></tr><tr><td>(REGN)</td><td></td><td>V BUS) = 5V, (REGN)= 20mA VVBUS)=9V, V(REGN) =3.8V</td><td>4.7</td><td>4.8</td><td></td><td>V</td></tr><tr><td colspan="3">REGN LDO current limit</td><td>50</td><td></td><td></td><td>mA</td></tr><tr><td>ANALOG-TO-DIGITAL CONVERTER (ADC) RES Resolution</td><td></td><td>Rising threshold</td><td></td><td>7</td><td></td><td></td></tr><tr><td></td><td></td><td>VVBUs) &gt; VBAT + V(SLEEP) Or OTG mode is</td><td>2.304</td><td></td><td>4.848</td><td>bits</td></tr><tr><td rowspan="2">VBAT(RANGE)</td><td rowspan="2">Typical battery voltage range</td><td>enabled BUS)AT+V(S) nOG me i</td><td></td><td></td><td></td><td>V</td></tr><tr><td>disabled</td><td>VsYS_MIN</td><td></td><td>4.848</td><td>V</td></tr><tr><td>V(BAT RES)</td><td>Typical battery voltage resolution</td><td>VBUS) &gt; VBAT + V(SLEEP) Or OTG mode is</td><td></td><td>20</td><td></td><td>mV</td></tr><tr><td>V(SYS_RANGE))</td><td>Typical system voltage range</td><td>enabled SAT+V(S) nOG e i</td><td>2.304</td><td></td><td>4.848</td><td>V</td></tr><tr><td></td><td></td><td>disabled</td><td>VsYS_MIN</td><td></td><td>4.848</td><td>V</td></tr><tr><td>V(SYS RES)</td><td>Typical system voltage resolution</td><td></td><td></td><td>20</td><td></td><td>mV</td></tr><tr><td>V(VBUS_RANGE)</td><td>Typical VvBus voltage range</td><td>V) VBAT+V() O  e enabled</td><td>2.6</td><td></td><td>15.3</td><td>V</td></tr><tr><td>VVBUS RES)</td><td>Typical VvBus voltage resolution</td><td></td><td></td><td>100</td><td></td><td>mV</td></tr><tr><td>BAT(RANGE)</td><td>Typical battery charge current range</td><td>VBuS) &gt; VBAT + V(sLEEP) nd VBAT&gt; VBAT(SHORT)</td><td>0</td><td></td><td>6.4</td><td>A</td></tr><tr><td>BAT(RES))</td><td>Typical battery charge current resolution</td><td></td><td></td><td>50</td><td></td><td>mA</td></tr><tr><td>V(TS RANGE)</td><td>Typical TS voltage range</td><td></td><td>21%</td><td></td><td>80%</td><td></td></tr><tr><td>V(TS_RES)</td><td>Typical TS voltage resolution</td><td></td><td></td><td>0.47%</td><td></td><td></td></tr><tr><td>LOGIC VO PIN (OTG, cE, PSEL, QON)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ViH Input high threshold level</td><td></td><td></td><td>1.3</td><td></td><td></td><td></td></tr><tr><td>$Vi Input low threshold level</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IN(BAS)</td><td>High Level Leakage Current</td><td>Pull-up rail 1.8 V</td><td></td><td></td><td>0.4</td><td>V</td></tr><tr><td rowspan="3">V(aoN) Internal /QON pull-up</td><td rowspan="3"></td><td></td><td></td><td></td><td>1</td><td>μA</td></tr><tr><td>Battery only mode</td><td></td><td>BAT</td><td></td><td>V</td></tr><tr><td>VvBUs) = 9V V vBU)= V</td><td></td><td>5.8</td><td></td><td>V</td></tr><tr><td>R(aoN)</td><td>Internal /QON pull-up resistance</td><td></td><td></td><td>4.3 200</td><td></td><td>V</td></tr><tr><td>LOGIC VO PIN (INT, STAT, PG, DSEL) Output low threshold level</td><td></td><td></td><td></td><td></td><td></td><td>$k{2$</td></tr><tr><td>VoL lOUT BIAS High level leakage current</td><td></td><td>Sink current = 5 mA, sink current</td><td></td><td></td><td>0.4</td><td>V</td></tr><tr><td>²C INTERFACE (SCL, SDA)</td><td></td><td>Pull-up rail 1.8 V</td><td></td><td></td><td>1</td><td>μA</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$V\H$</td><td>Input high threshold level, SCL and SDA</td><td>Pull-up rail 1.8 V</td><td>1.3</td><td></td><td></td><td></td></tr><tr><td>$VL Input low threshold level</td><td></td><td>Pull-up rail 1.8 V</td><td></td><td></td><td>0.4</td><td>V</td></tr><tr><td>VoL</td><td>Output low threshold level</td><td>Sink current = 5 mA, sink current</td><td></td><td></td><td>0.4</td><td>V</td></tr><tr><td>1BIAS</td><td>High level leakage current</td><td>Pull-up rail 1.8 V</td><td></td><td></td><td>1</td><td>μA</td></tr></table>

# 7.6 Timing Requirements

<table><tr><td></td><td></td><td></td><td rowspan=1 colspan=2>MIN  NOM  MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=3>VBUS/BAT POWER UP</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>BADSRC</td><td rowspan=1 colspan=1>Bad Adapter detection duration</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>30</td><td rowspan=1 colspan=1>msec</td></tr><tr><td rowspan=1 colspan=6>D+/D- DETECTION</td></tr><tr><td rowspan=1 colspan=1>tSDP_DEFAULT</td><td rowspan=1 colspan=1>Charging timer with USB1q0 in default mode</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mins</td></tr><tr><td rowspan=1 colspan=2>BAT OVER-VOLTAGE PROTECTION</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>BATOVP</td><td rowspan=1 colspan=1>Battery over-voltage deglitch time to disablecharge</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>μs</td></tr><tr><td rowspan=1 colspan=2>BATTERY CHARGER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tRECHG</td><td rowspan=1 colspan=1>Recharge deglitch time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>20</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=2>CURRENT PULSE CONTROL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tpUMPX_STOP</td><td rowspan=1 colspan=1>Current pulse control stop pulse</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>430              570</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tPUMPX_ON1</td><td rowspan=1 colspan=1>Current pulse control long on pulse</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>240             360</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tPUMPX ON2</td><td rowspan=1 colspan=1>Current pulse control short on pulse</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>70             130</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tPUMPX_OFF</td><td rowspan=1 colspan=1>Current pulse control off pulse</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>70             130</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tPUMPX DLY</td><td rowspan=1 colspan=1>Current pulse control stop start delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>80             225</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>BATTERY MONITOR</td><td rowspan=1 colspan=1>TOR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tcoNV</td><td rowspan=1 colspan=1>Conversion time</td><td rowspan=1 colspan=1>CONV_RATE(REG02[6]) = 0</td><td rowspan=1 colspan=2>8   1000</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>QON AND SHIPMODE TIMING</td><td rowspan=1 colspan=4>QON AND SHIPMODE TIMING</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsHIPMODE</td><td rowspan=1 colspan=1>QON low time to turn on BATFET and exit shipmode</td><td rowspan=1 colspan=1>Tj = −10°C to +60°℃</td><td rowspan=1 colspan=2>1.25             2.25</td><td rowspan=1 colspan=1>s</td></tr><tr><td rowspan=1 colspan=1>tQON RST</td><td rowspan=1 colspan=1>QON low time to enable full system reset</td><td rowspan=1 colspan=1>Tj = -10°C to +60°℃</td><td rowspan=1 colspan=2>12               18</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>tBATFETRST</td><td rowspan=1 colspan=1>BATFET ff time during full system reset</td><td rowspan=1 colspan=1>Tj =-10°C to+60°℃</td><td rowspan=1 colspan=2>350             550</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tSM DLY</td><td rowspan=1 colspan=1>Enter ship mode delay</td><td rowspan=1 colspan=1>$Tj =-10°C to+60°℃</td><td rowspan=1 colspan=2>10               15</td><td rowspan=1 colspan=1>s</td></tr><tr><td rowspan=1 colspan=1>I2C INTERFACE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>fsCL</td><td rowspan=1 colspan=1>SCL clock frequency</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>400</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>DIGITAL CLOCK</td><td rowspan=1 colspan=1>DIGITAL CLOCK and WATcHDOG TIMER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>fLPDIG</td><td rowspan=1 colspan=1>Digital low power clock</td><td rowspan=1 colspan=1>REGN LDO disabled</td><td rowspan=1 colspan=2>18    30    45</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>fD1G</td><td rowspan=1 colspan=1>Digital clock</td><td rowspan=1 colspan=1>REGN LDO enabled</td><td rowspan=1 colspan=2>1320  1500  1680</td><td rowspan=1 colspan=1>KHz</td></tr><tr><td rowspan=2 colspan=1>tWDT</td><td rowspan=2 colspan=1>Watchdog reset time</td><td rowspan=1 colspan=1>WATCHDOG(REG07[5:4])=11, REGN LDOdisabled</td><td rowspan=1 colspan=2>100    160</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>WATCHDOG(REG07[5:4])=11, REGN LDOenabled</td><td rowspan=1 colspan=2>136   160</td><td rowspan=1 colspan=1>S</td></tr></table>

# 7.7 Typical Characteristics

![](images/afce42e79eb0f09eba3701dd6c229c987217769f8a2fa3b7c8e927fa6c52ded1.jpg)  
Figure 1. Charge Efficiency vs Charge Current

![](images/324a72213b895d425f284110abf975227bd81bbd96b82e95684cd4cbc18849c6.jpg)

![](images/6788eba7ef530e6d3d643930eb9c0529972ed5f5262e0f43b33bb5bcfc7a644d.jpg)  
Figure 2. System Light Load Efficiency vs System Light Load Current

![](images/f7340566b723ea264a66e552ee764b4dfdff4cca1fe7b6a44cb5f1c6a342157c.jpg)  
Figure 3. Boost Mode Efficiency vs PMID Load Current

![](images/21e038562c38294fc367b1a106ba5f060a91a543b52bf3376e50adbd81e798a3.jpg)  
Figure 5. SYS Voltage Regulation vs System Load Current

![](images/00cf983d6db7a78c8d58a942d31419f907b0ca40b836946d6d52ee33cbebb828.jpg)  
Figure 4. Charge Current Accuracy vs Charge Current I2C Setting   
Figure 6. SYS Voltage Regulation vs System Load Current

# Typical Characteristics (continued)

![](images/ea7024bffc754f6b23130aaf1f479e5752993a494ef217924c5f0f8807347def.jpg)  
Figure 7. BAT Voltage vs Temperature

![](images/4d9443f01f49975876bd2a5a8f6e6098d9dd6e0114d04ed3ffa01f89c268a33a.jpg)  
Figure 8. Input Current Limit vs Temperature

# 8 Detailed Description

The device is a highly integrated 5-A siwtch-mode battery charger for single cell Li-Ion and Li-polymer battery. It is highly integrated with the input reverse-blocking FET (RBFET, Q1), high-side siwtching FET (HSFET, Q2) , low-side switching FET (LSFET, Q3), and battery FET (BATFET, Q4). The device also integrates the boostrap diode for the high-side gate drive.

# 8.1 Functional Block Diagram

![](images/f161f10e8d63f8a4bf4d47844d8e554ef78537bf217de746f9857f31f847dd31.jpg)

# 8.2 Feature Description

# 8.2.1 Device Power-On-Reset (POR)

The internal bias circuits are powered from the higher voltage of VBUS and BAT. When VBUS rises above VVBUS_UVLOZ or BAT rises above VBAT_UVLOZ , the sleep comparator, battery depletion comparator and BATFET driver are active. I2C interface is ready for communication and all the registers are reset to default value. The host can access all the registers after POR.

# 8.2.2 Device Power Up from Battery without Input Source

If only battery is present and the voltage is above depletion threshold (VBAT_DPLZ), the BATFET turns on and connects battery to system. The REGN LDO stays off to minimize the quiescent current. The low RDS(ON) of BATFET and the low quiescent current on BAT minimize the conduction loss and maximize the battery run time. The device always monitors the discharge current through BATFET (Supplement Mode). When the system is overloaded or shorted (IBAT > IBATFET_OCP), the device turns off BATFET immediately and set BATFET_DIS bit to indicate BATFET is disabled until the input source plugs in again or one of the methods describe in BATFET Enable (Exit Shipping Mode) is applied to re-enable BATFET.

# 8.2.3 Device Power Up from Input Source

When an input source is plugged in, the device checks the input source voltage to turn on REGN LDO and all the bias circuits. It detects and sets the input current limit before the buck converter is started when AUTO_DPDM_EN bit is set. The power up sequence from input source is as listed:

1. Power Up REGN LDO   
2. Poor Source Qualification   
3. Input Source Type Detection based on D+/D- to set default Input Current Limit (IINLIM) register and input   
source type   
4. Input Voltage Limit Threshold Setting (VINDPM threshold)   
5. Converter Power-up

# 8.2.3.1 Power Up REGN Regulation (LDO)

The REGN LDO supplies internal bias circuits as well as the HSFET and LSFET gate drive. The LDO also provides bias rail to TS external resistors. The pull-up rail of STAT can be connected to REGN as well. The REGN is enabled when all the below conditions are valid.

1. VBUS above VVBUS_UVLOZ   
2. VBUS above VBAT + VSLEEPZ in buck mode or VBUS below VBAT + VSLEEP in boost mode   
3. After 220 ms delay is completed

If one of the above conditions is not valid, the device is in high impedance mode (HIZ) with REGN LDO off. The device draws less than IVBUS_HIZ from VBUS during HIZ state. The battery powers up the system when the device is in HIZ.

# 8.2.3.2 Poor Source Qualification

After REGN LDO powers up, the device checks the current capability of the input source. The input source has to meet the following requirements in order to start the buck converter.

1. VBUS voltage below VACOV   
2. VBUS voltage above VVBUSMIN when pulling IBADSRC (typical 30mA)

Once the input source passes all the conditions above, the status register bit VBUS_GD is set high and the INT pin is pulsed to signal to the host. If the device fails the poor source detection, it repeats poor source qualification every 2 seconds.

# Feature Description (continued)

# 8.2.3.3 Input Source Type Detection

After the VBUS_GD bit is set and REGN LDO is powered, the charger device runs Input Source Type Detection when AUTO_DPDM_EN bit is set.

The bq25895 follows the USB Battery Charging Specification 1.2 (BC1.2) and to detect input source (SDP/CDP/DCP) and non-standard adapter through USB D+/D- lines. In addition, when USB DCP is detected, it initiates adjustable high voltage adapter handshake on D+/D-. The device supports MaxCharge™ handshake when MAXC_EN or HVDCP_EN is set.

After input source type detection, an INT pulse is asserted to the host. In addition, the following registers and pin are changed:

1. Input Current Limit (IINLIM) register is changed to set current limit   
2. PG_STAT bit is set   
3. SDP_STAT bit is updated to indicate USB100 or other input source

The host can over-write IINLIM register to change the input current limit if needed. The charger input current is always limited by the lower of IINLIM register or ILIM pin at all-time regardless of Input Current Optimizer (ICO) is enable or disabled.

When AUTO_DPDM_EN is disabled, the Input Source Type Detection is bypassed. The Input Current Limi (IINLIM) register, VBUS_STAT, and SPD_STAT bits are unchanged from previous values.

# 8.2.3.3.1 D+/D– Detection Sets Input Current Limit

The bq25890 contains a D+/D– based input source detection to set the input current limit automatically. The D+/D- detection includes standard USB BC1.2, non-standard adapter, and adjustable high voltage adapter detections. When input source is plugged-in, the device starts standard USB BC1.2 detections. The USB BC1.2 is capable to identify Standard Downstream Port (SDP), Charging Downstream Port (CDP), and Dedicated Charging Port (DCP). When the Data Contact Detection (DCD) timer of 500ms is expired, the non-standard adapter detection is applied to set the input current limit.

When DCP is detected, the device initates adjustable high voltage adapter handshake including MaxCharge™, etc. The handshake connects combinations of voltage source(s) and/or current sink on D+/D- to signal input source to raise output voltage from 5 V to 9 V / 12 V. The adjustable high voltage adapter handshake can be disabled by clearing MAXC_EN and/or HVDCP_EN bits .

![](images/b28a2dbfd8058e589615731893071d591efa30efd8bb5ff1a5a465b5c027caf1.jpg)  
Figure 9. USB D+/D- Detection

Table 1. Non-Standard Adapter Detection   

<table><tr><td rowspan=1 colspan=1>NON-STANDARDADAPTER</td><td rowspan=1 colspan=1>D+ THRESHOLD</td><td rowspan=1 colspan=1>D- THRESHOLD</td><td rowspan=1 colspan=1>INPUT CURRENT LIMIT</td></tr><tr><td rowspan=1 colspan=1>Divider 1</td><td rowspan=1 colspan=1>VD+ within V2P7_VTH</td><td rowspan=1 colspan=1>VD. within V2PO_VTH</td><td rowspan=1 colspan=1>2.1A</td></tr><tr><td rowspan=1 colspan=1>Divider 2</td><td rowspan=1 colspan=1>VD++ within V1P2_VTH</td><td rowspan=1 colspan=1>VD. within V1P2_VTH</td><td rowspan=1 colspan=1>2A</td></tr><tr><td rowspan=1 colspan=1>Divider 3</td><td rowspan=1 colspan=1>VD+ within V2PO_ VTH</td><td rowspan=1 colspan=1>VD. Within V2P7 VTH</td><td rowspan=1 colspan=1>1A</td></tr><tr><td rowspan=1 colspan=1>Divider 4</td><td rowspan=1 colspan=1>VD+ within V2P7_VTH</td><td rowspan=1 colspan=1>VD. within V2P7_VTH</td><td rowspan=1 colspan=1>2.4A</td></tr></table>

Table 2. Adjustable High Voltage Adapter D+/D- Output Configurations   

<table><tr><td rowspan=1 colspan=1>ADJUSTABLE HIGH VOLTAGE HANDSHAKE</td><td rowspan=1 colspan=1>D+</td><td rowspan=1 colspan=1>D-</td><td rowspan=1 colspan=1>OUTPUT</td></tr><tr><td rowspan=1 colspan=1>MaxCharge (12V)</td><td rowspan=1 colspan=1>I1P6MA_SINK</td><td rowspan=1 colspan=1>V3p45_VSRC</td><td rowspan=1 colspan=1>12V</td></tr><tr><td rowspan=1 colspan=1>MaxCharge (9V)</td><td rowspan=1 colspan=1>V3p45 VSRC</td><td rowspan=1 colspan=1>I1P6MA ISINK</td><td rowspan=1 colspan=1>9V</td></tr></table>

After the Input Source Type Detection is done, an INT pulse is asserted to the host. In addition, the following registers including Input Current Limit register (IINLIM), VBUS_STAT, and SDP_STAT are updated as below:

Table 3. bq25895 Result   

<table><tr><td rowspan=1 colspan=1>D+/D- DETECTION</td><td rowspan=1 colspan=1>INPUT CURRENT LIMIT(IINLIM)</td><td rowspan=1 colspan=1>SDP_STAT</td><td rowspan=1 colspan=1>VBUS_STAT</td></tr><tr><td rowspan=1 colspan=1>USB SDP (USB500)</td><td rowspan=1 colspan=1>500mA</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>001</td></tr><tr><td rowspan=1 colspan=1>USB CDP</td><td rowspan=1 colspan=1>1.5A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>010</td></tr><tr><td rowspan=1 colspan=1>USB DCP</td><td rowspan=1 colspan=1>3.25A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>011</td></tr><tr><td rowspan=1 colspan=1>Divider 3</td><td rowspan=1 colspan=1>1A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>110</td></tr><tr><td rowspan=1 colspan=1>Divider 1</td><td rowspan=1 colspan=1>2.1A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>110</td></tr><tr><td rowspan=1 colspan=1>Divider 4</td><td rowspan=1 colspan=1>2.4A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>110</td></tr><tr><td rowspan=1 colspan=1>Divider 2</td><td rowspan=1 colspan=1>2A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>110</td></tr><tr><td rowspan=1 colspan=1>MaxCharge</td><td rowspan=1 colspan=1>1.5A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>100</td></tr><tr><td rowspan=1 colspan=1>Unknown Adapter</td><td rowspan=1 colspan=1>500 mA</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>101</td></tr></table>

# 8.2.3.3.2 Force Input Current Limit Detection

In host mode, the host can force the device to run by setting FORCE_DPDM bit. After the detection is completed, FORCE_DPDM bit returns to 0 by itself and Input Result is updated.

# 8.2.3.4 Input Voltage Limit Threshold Setting (VINDPM Threshold)

The device supports wide range of input voltage limit (3.9 V – 14 V) for high voltage charging and provides two methods to set Input Voltage Limit (VINDPM) threshold to facilitate autonomous detection.

1. Absolute VINDPM (FORCE_VINDPM=1)

By setting FORCE_VINDPM bit to 1, the VINDPM threshold setting algorithm is disabled. Register VINDPM is writable and allows host to set the absolute threshold of VINDPM function.

2. Relative VINDPM based on VINDPM_OS registers (FORCE_VINDPM=0) (Default)

When FORCE_VINDPM bit is 0 (default), the VINDPM threshold setting algorithm is enabled. The VINDPM register is read only and the charger controls the register by using VINDPM Threshold setting algorithm. The algorithm allows a wide range of adapter (VVBUS_OP) to be used with flexible VINDPM threshold.

After Input Voltage Limit Threshold is set, an INT pulse is generated to signal to the host.

# 8.2.3.5 Converter Power-Up

After the input current limit is set, the converter is enabled and the HSFET and LSFET start switching. If battery charging is disabled, BATFET turns off. Otherwise, BATFET stays on to charge the battery.

The device provides soft-start when system rail is ramped up. When the system rail is below 2.2 V, the input current limit is forced to the lower of 200 mA or IINLIM register setting. After the system rises above 2.2 V, the device limits input current to the lower value of ILIM pin and IILIM register (ICO_EN = 0) or IDPM_LIM register (ICO_EN = 1).

As a battery charger, the device deploys a highly efficient 1.5 MHz step-down switching regulator. The fixed frequency oscillator keeps tight control of the switching frequency under all conditions of input voltage, battery voltage, charge current and temperature, simplifying output filter design.

A type III compensation network allows using ceramic capacitors at the output of the converter. An internal sawtooth ramp is compared to the internal error control signal to vary the duty cycle of the converter. The ramp height is proportional to the PMID voltage to cancel out any loop gain variation due to a change in input voltage.

In order to improve light-load efficiency, the device switches to PFM control at light load when battery is below minimum system voltage setting or charging is disabled. During the PFM operation, the switching duty cycle is set by the ratio of SYS and VBUS.

# 8.2.4 Input Current Optimizer (ICO)

The device provides innovative Input Current Optimizer (ICO) to identify maximum power point without overload the input source. The algorithm automatically identify maximum input current limit of power source without entering VINDPM to avoid input source overload.

This feature is enabled by default (ICO_EN=1) and can be disabled by setting ICO_EN bit to 0. After DCP or MaxCharge type input source is detected based on the procedures previously described (Input Source Type Detection ). The algorithm runs automatically when ICO_EN bit is set. The algorithm can also be forced to execute by setting FORCE_ICO bit regardless of input source type detected.

The actual input current limit used by the Dynamic Power Management is reported in IDPM_LIM register while Input Current Optimizer is enabled (ICO_EN = 1) or set by IINLIM register when the algorithm is disabled (ICO_EN = 0). In addition, the current limit is clamped by ILIM pin unless EN_ILIM bit is 0 to disable ILIM pin function.

# 8.2.5 Boost Mode Operation from Battery

The device supports boost converter operation to deliver power from the battery to other portable devices through PMID pin. The boost mode output current rating supports maximum output current up to 3.1 A to charge smartphone and tablet at fast charging rate. The boost operation can be enabled if the conditions are valid:

1. BAT above BATLOWV   
2. VBUS less than BAT+VSLEEP (in sleep mode)   
3. Boost mode operation is enabled (OTG pin HIGH and OTG_CONFIG bit =1)   
4. Voltage at TS (thermistor) pin is within range configured by Boost Mode Temperature Monitor as configured   
by BHOT and BCOLD bits   
5. After 30 ms delay from boost mode enable

In boost mode, the device employs a 500 KHz or 1.5 MHz (selectable using BOOST_FREQ bit) step-up switching regulator based on system requirements. To avoid frequency change during boost mode operations, write to boost frequency configuration bit (BOOST_FREQ) is ignored when OTG_CONFIG is set.

During boost mode, the status register VBUS_STAT bits is set to 111, the VBUS output is 5V by default (selectable via BOOSTV register bits). The boost output is maintained when BAT is above VOTG_BAT threshold

# 8.2.6 Power Path Management

The device accommodates a wide range of input sources from USB, wall adapter, to car battery. The device provides automatic power path selection to supply the system (SYS) from input source (VBUS), battery (BAT), or both.

# 8.2.6.1 Narrow VDC Architecture

The device deploys Narrow VDC architecture (NVDC) with BATFET separating system from battery. The minimum system voltage is set by SYS_MIN bits. Even with a fully depleted battery, the system is regulated above the minimum system voltage (default 3.5 V).

When the battery is below minimum system voltage setting, the BATFET operates in linear mode (LDO mode), and the system is regulated above the minimum system voltage setting. As the battery voltage rises above the minimum system voltage, BATFET is fully on and the voltage difference between the system and battery is the VDS of BATFET. The status register VSYS_STAT bit goes high when the system is in minimum system voltage regulation.

![](images/4281deaa93534ae643f27ad7151017da5f6d9be50456f4074e1b350ff11ee2be.jpg)  
Figure 10. V(SYS) vs V(BAT)

# 8.2.6.2 Dynamic Power Management

To meet maximum current limit in USB spec and avoid over loading the adapter, the device features Dynamic Power Management (DPM), which continuously monitors the input current and input voltage. When input source is over-loaded, either the current exceeds the input current limit (IINLIM or IDPM_LIM) or the voltage falls below the input voltage limit (VINDPM). The device then reduces the charge current until the input current falls below the input current limit and the input voltage rises above the input voltage limit.

When the charge current is reduced to zero, but the input source is still overloaded, the system voltage starts to drop. Once the system voltage falls below the battery voltage, the device automatically enters the Supplement Mode where the BATFET turns on and battery starts discharging so that the system is supported from both the input source and battery.

During DPM mode, the status register bits VDPM_STAT (VINDPM) and/or IDPM_STAT (IINDPM) is/are set high. Figure 11 shows the DPM response with 9V/1.2A adapter, 3.2-V battery, 2.8-A charge current and 3.4-V minimum system voltage setting.

![](images/a6b598cce44859d997b6f4523baa718aee30f67ab25d6f03248d65a7b2b47273.jpg)  
Figure 11. DPM Response

# 8.2.6.3 Supplement Mode

When the system voltage falls below the battery voltage, the BATFET turns on and the BATFET gate is regulated the gate drive of BATFET so that the minimum BATFET VDS stays at 30 mV when the current is low. This prevents oscillation from entering and exiting the Supplement Mode. As the discharge current increases, the BATFET gate is regulated with a higher voltage to reduce RDS(ON) until the BATFET is in full conduction. At this point onwards, the BATFET VDS linearly increases with discharge current. Figure 12 shows the V-I curve of the BATFET gate regulation operation. BATFET turns off to exit Supplement Mode when the battery is below battery depletion threshold.

![](images/d05793955e0574b9e0ef8de070b6aedd58589e7e228d1d1a677e8135545d5c7b.jpg)  
Figure 12. BATFET V-I Curve

# 8.2.7 Battery Charging Management

The device charges 1-cell Li-Ion battery with up to 5-A charge current for high capacity battery. The 11-mΩ BATFET improves charging efficiency and minimize the voltage drop during discharging.

# 8.2.7.1 Autonomous Charging Cycle

With battery charging is enabled (CHG_CONFIG bit = 1 and CE pin is low), the device autonomously completes a charging cycle without host involvement. The device default charging parameters are listed in Table 4. The host can always control the charging operations and optimize the charging parameters by writing to the corresponding registers through I2C.

Table 4. Charging Parameter Default Setting   

<table><tr><td rowspan=1 colspan=1>DEFAULT MODE</td><td rowspan=1 colspan=1>bq25895</td></tr><tr><td rowspan=1 colspan=1>Charging Voltage</td><td rowspan=1 colspan=1>4.208V</td></tr><tr><td rowspan=1 colspan=1>Charging Current</td><td rowspan=1 colspan=1>2.048A</td></tr><tr><td rowspan=1 colspan=1>Pre-charge Current</td><td rowspan=1 colspan=1>128mA</td></tr><tr><td rowspan=1 colspan=1>Termination Current</td><td rowspan=1 colspan=1>256 mA</td></tr><tr><td rowspan=1 colspan=1>Temperature Profile</td><td rowspan=1 colspan=1>Cold/Hot</td></tr><tr><td rowspan=1 colspan=1>Safety Timer</td><td rowspan=1 colspan=1>12 hour</td></tr></table>

A new charge cycle starts when the following conditions are valid:

Converter starts   
Battery charging is enabled by setting CHG_CONFIG bit, /CE pin is low and ICHG register is not 0 mA   
No thermistor fault on TS pin   
No safety timer fault   
BATFET is not forced to turn off (BATFET_DIS bit = 0)

The charger device automatically terminates the charging cycle when the charging current is below termination threshold, charge voltage is above recharge threshold, and device not in DPM mode or thermal regulation. When a full battery voltage is discharged below recharge threshold (threshold selectable via VRECHG bit), the device automatically starts a new charging cycle. After the charge is done, either toggle CE pin or CHG_CONFIG bit can initiate a new charging cycle.

The STAT output indicates the charging status of charging (LOW), charging complete or charge disable (HIGH) or charging fault (Blinking). The STAT output can be disabled by setting STAT_DIS bit. In addition, the status register (CHRG_STAT) indicates the different charging phases: 00-charging disable, 01-precharge, 10-fast charge (constant current) and constant voltage mode, 11-charging done. Once a charging cycle is completed, an INT is asserted to notify the host.

# 8.2.7.2 Battery Charging Profile

The device charges the battery in three phases: preconditioning, constant current and constant voltage. At the beginning of a charging cycle, the device checks the battery voltage and regulates current / voltage.

Table 5. Charging Current Setting   

<table><tr><td rowspan=1 colspan=1>VBAT</td><td rowspan=1 colspan=1>CHARGING CURRENT</td><td rowspan=1 colspan=1>REG DEFAULT SETTING</td><td rowspan=1 colspan=1>CHRG_STAT</td></tr><tr><td rowspan=1 colspan=1>&lt;2V</td><td rowspan=1 colspan=1>IBATSHORT</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>01</td></tr><tr><td rowspan=1 colspan=1>2V-3V</td><td rowspan=1 colspan=1>IPRECHG</td><td rowspan=1 colspan=1>128mA</td><td rowspan=1 colspan=1>01</td></tr><tr><td rowspan=1 colspan=1>&gt;3V</td><td rowspan=1 colspan=1>ICHG</td><td rowspan=1 colspan=1>2048mA</td><td rowspan=1 colspan=1>10</td></tr></table>

If the charger device is in DPM regulation or thermal regulation during charging, the charging current can be less than the programmed value. In this case, termination is temporarily disabled and the charging safety timer is counted at half the clock rate.

![](images/fa544df60ed3034c643a39ed41c8fe46b65e2f4371eb6b77763f576030be1402.jpg)  
Figure 13. Battery Charging Profile

# 8.2.7.3 Charging Termination

The device terminates a charge cycle when the battery voltage is above recharge threshold, and the current is below termination current. After the charging cycle is completed, the BATFET turns off. The converter keeps running to power the system, and BATFET can turn on again to engage Supplement Mode.

When termination occurs, the status register CHRG_STAT is set to 11, and an INT pulse is asserted to the host.   
Termination is temporarily disabled when the charger device is in input current, voltage or thermal regulation.   
Termination can be disabled by writing 0 to EN_TERM bit prior to charge termination.

# 8.2.7.4 Resistance Compensation (IRCOMP)

For high current charging system, resistance between charger output and battery cell terminal such as board routing, connector, MOSFETs and sense resistor can force the charging process to move from constant current to constant voltage too early and increase charge time. To speed up the charging cycle, the device provides resistance compensation (IRCOMP) feature which can extend the constant current charge time to delivery maximum power to battery.

The device allows the host to compensate for the resistance by increasing the voltage regulation set point based on actual charge current and the resistance as shown below. For safe operation, the host should set the maximum allowed regulation voltage register (VCLAMP) and the minimum resistance compensation (BATCOMP).

VREG_ACTUAL = VREG + min(ICHRG_ACTUAL x BATCOMP, VCLAMP)

# 8.2.7.5 Thermistor Qualification

# 8.2.7.5.1 Cold/Hot Temperature Window in Charge Mode

The device continuously monitors battery temperature by measuring the voltage between the TS pins and ground, typically determined by a negative temperature coefficient thermistor (NTC) and an external voltage divider. The device compares this voltage against its internal thresholds to determine if charging is allowed. To initiate a charge cycle, the battery temperature must be within the VLTF to VHTF thresholds. During the charge cycle the battery temperature must be within the VLTF to VTCO thresholds, else the device suspends charging and waits until the battery temperature is within the VLTF to VHTF range.

![](images/2c18dd06abbed1eabf9616a695f430edcf6c2fc62bf13b4da8a4cec173e1c9fa.jpg)  
Figure 14. TS Resistor Network

When the TS fault occurs, the fault register REG0C[2:0] indicates the actual condition on each TS pin and an INT is asserted to the host. The STAT pin indicates the fault when charging is suspended.

![](images/0f7a8b26b6917b7338f6c51719a729a25b76def1f30599386159a2085d8770d3.jpg)  
Figure 15. TS Pin Thermistor Sense Thresholds

Assuming a 103AT NTC thermistor on the battery pack as shown in Figure 14, the value RT1 and RT2 can be determined by using Equation 2: :

![](images/2de5a6053e134cb533ff86d04114f5e714f6d3598e228de66d04b04c3f41504c.jpg)

![](images/a469eb92d4dafe7da23c07579b1b8692759ea6d620d821db83a2c47b91b257f5.jpg)

Select 0°C to 45°C range for Li-ion or Li-polymer battery,   
RTHCOLD = 27.28 kΩ   
RTHHOT = 4.91 kΩ   
RT1 = 5.21 kΩ   
RT2 = 29.87 kΩ

# 8.2.7.5.2 Cold/Hot Temperature Window in Boost Mode

For battery protection during boost mode, the device monitors the battery temperature to be within the VBCOLDx to VBHOTx thresholds unless boost mode temperature is disabled by setting BHOT bits to 11. When temperature is outside of the temperature thresholds, the boost mode and BATFET are disabled and BATFET_DIS bit is set to reduce leakage current on PMID. Once temperature returns within thresholds, the host can clear BATFET_DIS bit or provide logic low to high transition on QON pin to enable BATFET and boost mode.

![](images/0ee8f8089608e5ca0bb39fd0803303024555983836afb175bac53fa2731dfb64.jpg)  
Figure 16. TS Pin Thermistor Sense Thresholds in Boost Mode

# 8.2.7.6 Charging Safety Timer

The device has built-in safety timer to prevent extended charging cycle due to abnormal battery conditions. The safety timer is 4 hours when the battery is below VBATLOWV threshold. The user can program fast charge safety timer through I2C (CHG_TIMER bits). When safety timer expires, the fault register CHRG_FAULT bits are set to 11 and an INT is asserted to the host. The safety timer feature can be disabled via I2C by setting EN_TIMER bit.

During input voltage, current or thermal regulation, the safety timer counts at half clock rate as the actual charge current is likely to be below the register setting. For example, if the charger is in input current regulation (IDPM_STAT = 1) throughout the whole charging cycle, and the safety time is set to 5 hours, the safety timer will expire in 10 hours. This half clock rate feature can be disabled by writing 0 to TMR2X_EN bit.

# 8.2.8 Battery Monitor

The device includes a battery monitor to provide measurements of VBUS voltage, battery voltage, system voltage, thermistor ratio, and charging current, and charging current based on the device modes of operation. The measurements are reported in Battery Monitor Registers (REG0E-REG12). The battery monitor can be configured as two conversion modes by using CONV_RATE bit: one-shot conversion (default) and 1 second continuous conversion.

For one-shot conversion (CONV_RATE = 0), the CONV_START bit can be set to start the conversion. During the conversion, the CONV_START is set and it is cleared by the device when conversion is completed. The conversion result is ready after tCONV (maximum 1 second).

For continuous conversion (CONV_RATE = 1), the CONV_RATE bit can be set to initiate the conversion. During active conversion, the CONV_START is set to indicate conversion is in progress. The battery monitor provides conversion result every 1 second automatically. The battery monitor exits continuous conversion mode when CONV_RATE is cleared.

When battery monitor is active, the REGN power is enabled and can increase device quiescent current. In battery only mode, the battery monitor is only active when V(BAT) > SYS_MIN setting in REG03.

Table 6. Battery Monitor Modes of Operation   

<table><tr><td rowspan=2 colspan=1>PARAMETER</td><td rowspan=2 colspan=1>REGISTER</td><td rowspan=1 colspan=4>MODES OF OPERATION</td></tr><tr><td rowspan=1 colspan=1>CHARGEMODE</td><td rowspan=1 colspan=1>BOOST MODE</td><td rowspan=1 colspan=1>DISABLE CHARGEMODE</td><td rowspan=1 colspan=1>BATTERY ONLYMODE</td></tr><tr><td rowspan=1 colspan=1>Battery Voltage (VBAT)</td><td rowspan=1 colspan=1>REGOE</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>System Voltage (Vsys)</td><td rowspan=1 colspan=1>REGOF</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>Temperature (TS) Voltage (VTs)</td><td rowspan=1 colspan=1>REG10</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>VBUS Voltage (VvBus)</td><td rowspan=1 colspan=1>REG11</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>NA</td></tr><tr><td rowspan=1 colspan=1>Charge Current (lBAT)</td><td rowspan=1 colspan=1>REG12</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>NA</td></tr></table>

# 8.2.9 Status Outputs (STAT, and INT)

# 8.2.9.1 Charging Status Indicator (STAT)

The device indicates charging state on the open drain STAT pin. The STAT pin can drive LED as shown in Figure 47. The STAT pin function can be disable by setting STAT_DIS bit.

Table 7. STAT Pin State   

<table><tr><td rowspan=1 colspan=1>CHARGING STATE</td><td rowspan=1 colspan=1>STAT INDICATOR</td></tr><tr><td rowspan=1 colspan=1>Charging in progress (including recharge)</td><td rowspan=1 colspan=1>LOW</td></tr><tr><td rowspan=1 colspan=1>Charging complete</td><td rowspan=1 colspan=1>HIGH</td></tr><tr><td rowspan=1 colspan=1>Sleep mode, charge disable</td><td rowspan=1 colspan=1>HIGH</td></tr><tr><td rowspan=1 colspan=1>Charge suspend (Input overvoltage, TS fault, timer fault, input or system overvoltage).Boost Mode suspend (due to Ts Fault)</td><td rowspan=1 colspan=1>blinking at 1 Hz</td></tr></table>

# 8.2.9.2 Interrupt to Host (INT)

In some applications, the host does not always monitor the charger operation. The INT notifies the system on the device operation. The following events will generate 256-µs INT pulse.

USB/adapter source identified (through PSEL or DPDM detection, with OTG pin) Good input source detected – VBUS above battery (not in sleep) – VBUS below VACOV threshold VBUS above VVBUSMIN (typical 3.8 V) when IBADSRC (typical 30 mA) current is applied (not a poor source) Input removed Charge Complete • Any FAULT event in REG0C

When a fault occurs, the charger device sends out INT and keeps the fault state in REG0C until the host reads the fault register. Before the host reads REG0C and all the faults are cleared, the charger device would not send any INT upon new faults. To read the current fault status, the host has to read REG0C two times consecutively. The 1st read reports the pre-existing fault register status and the 2nd read reports the current fault register status.

# 8.2.10 BATET (Q4) Control

# 8.2.10.1 BATFET Disable Mode (Shipping Mode)

To extend battery life and minimize power when system is powered off during system idle, shipping, or storage, the device can turn off BATFET so that the system voltage is zero to minimize the battery leakage current. When the host set BATFET_DIS bit, the charger can turn off BATFET immediately or delay by tSM_DLY as configurated by BATFET_DLY bit.

# 8.2.10.2 BATFET Enable (Exit Shipping Mode)

When the BATFET is disabled (in shipping mode) and indicated by setting BATFET_DIS, one of the following events can enable BATFET to restore system power:

1. Plug in adapter

2. Clear BATFET_DIS bit

3. Set REG_RST bit to reset all registers including BATFET_DIS bit to default (0)   
4. A logic high to low transition on QON pin with tSHIPMODE deglitch time to enable BATFET to exit shipping mode

# 8.2.10.3 BATFET Full System Reset

The BATFET functions as a load switch between battery and system when input source is not plugged-in. By changing the state of BATFET from off to on, system connects to SYS can be effectively have a power-on-reset. The QON pin supports push-button interface to reset system power without host by change the state of BATFET.

When the QON pin is driven to logic low for tQON_RST (typical 15 seconds) while input source is not plugged in and BATFET is enabled (BATFET_DIS=0), the BATFET is turned off for tBATFET_RST and then it is re-enabled to reset system power. This function can be disabled by setting BATFET_RST_EN bit to 0.

# 8.2.11 Current Pulse Control Protocol

The device provides the control to generate the VBUS current pulse protocol to communicate with adjustable high voltage adapter in order to signal adapter to increase or decrease output voltage. To enable the interface, the EN_PUMPX bit must be set. Then the host can select the increase/decrease voltage pulse by setting one of the PUMPX_UP or PUMPX_DN bit (but not both) to start the VBUS current pulse sequence. During the current pulse sequence, the PUMPX_UP and PUMPX_DN bits are set to indicate pulse sequence is in progress and the device pulses the input current limit between current limit set forth by IINLIM or IDPM_LIM register and the 100mA current limit (IINDPM100_ACC). When the pulse sequence is completed, the input current limit is returned to value set by IINLIM or IDPM_LIM register and the PUMPX_UP or PUMPX_DN bit is cleared. In addition, the EN_PUMPX can be cleared during the current pulse sequence to terminate the sequence and force charger to return to input current limit as set forth by the IINLIM or IDPM_LIM register immediately. When EN_PUMPX bit is low, write to PUMPX_UP and PUMPX_DN bit would be ignored and have no effect on VBUS current limit.

# 8.2.12 Input Current Limit on ILIM

For safe operation, the device has an additional hardware pin on ILIM to limit maximum input current on ILIM pin. The input maximum current is set by a resistor from ILIM pin to ground as:

![](images/c6a0eca2c76968d3a921c51046b466fab9c0b01da0b60c4479717c3e56fb2d4d.jpg)

The actual input current limit is the lower value between ILIM setting and register setting (IINLIM). For example, if the register setting is 111111 for 3.25 A, and ILIM has a 260-Ω resistor (KILIM = 390 max.) to ground for 1.5 A, the input current limit is 1.5 A. ILIM pin can be used to set the input current limit rather than the register settings when EN_ILIM bit is set. The device regulates ILIM pin at 0.8 V. If ILIM voltage exceeds 0.8 V, the device enters input current regulation (Refer to Dynamic Power Management section).

The ILIM pin can also be used to monitor input current when EN_ILIM is enabled. The voltage on ILIM pin is proportional to the input current. ILIM pin can be used to monitor the input current following Equation 4:

![](images/4e129c479b7e41224b16bd229e56f868a66d1e10dc9b8d1a41fbb28f12dd42ec.jpg)

For example, if ILIM pin is set with 260-Ω resistor, and the ILIM voltage is 0.4 V, the actual input current 0.615 A - 0.75 A (based on KILM specified). If ILIM pin is open, the input current is limited to zero since ILIM voltage floats above 0.8 V. If ILIM pin is short, the input current limit is set by the register.

The ILIM pin function can be disabled by setting EN_ILIM bit to 0. When the pin is disabled, both input current limit function and monitoring function are not available.

# 8.2.13 Thermal Regulation and Thermal Shutdown

# 8.2.13.1 Thermal Protection in Buck Mode

The device monitors the internal junction temperature TJ to avoid overheat the chip and limits the IC surface temperature in buck mode. When the internal junction temperature exceeds the preset thermal regulation limit (TREG bits), the device lowers down the charge current. The wide thermal regulation range from 60ºC to 120ºC allows the user to optimize the system thermal performance.

During thermal regulation, the actual charging current is usually below the programmed battery charging current. Therefore, termination is disabled, the safety timer runs at half the clock rate, and the status register THERM_STAT bit goes high.

Additionally, the device has thermal shutdown to turn off the converter and BATFET when IC surface temperature exceeds TSHUT. The fault register CHRG_FAULT is set to 10 and an INT is asserted to the host. The BATFET and converter is enabled to recover when IC temperature is below TSHUT_HYS.

# 8.2.13.2 Thermal Protection in Boost Mode

The device monitors the internal junction temperature to provide thermal shutdown during boost mode. When IC surface temperature exceeds TSHUT, BATFET is turned off to disable battery discharge. When IC surface temperature is below TSHUT_HYS, the host can use one of the method describes in section BATFET Enable (Exit Shipping Mode) to recover.

# 8.2.14 Voltage and Current Monitoring in Buck and Boost Mode

# 8.2.14.1 Voltage and Current Monitoring in Buck Mode

The device closely monitors the input and system voltage, as well as HSFET current for safe buck and boost mode operations.

# 8.2.14.1.1 Input Overvoltage (ACOV)

The input voltage for buck mode operation is VVBUS_OP. If VBUS voltage exceeds VACOV, the device stops switching immediately. During input over voltage (ACOV), the fault register CHRG_FAULT bits sets to 01. An INT is asserted to the host..

# 8.2.14.1.2 System Overvoltage Protection (SYSOVP)

The charger device clamps the system voltage during load transient so that the components connect to system would not be damaged due to high voltage. When SYSOVP is detected, the converter stops immediately to clamp the overshoot.

# 8.2.14.2 Current Monitoring in Boost Mode

The device closely monitors the VBUS voltage, as well as LSFET current to ensure safe boost mode operation.

# 8.2.14.2.1 Boost Mode Overvoltage Protection

When PMID voltage rises above regulation target and exceeds VOTG_OVP, the device enters overvoltage protection which stops switching and pauses boost mode (OTG_CONFIG bit remains set) until OVP fault is removed. During the overvoltage, the fault register bit (BOOST_FAULT) is set high to indicate fault in boost operation. An INT is also asserted to the host.

# 8.2.15 Battery Protection

# 8.2.15.1 Battery Overvoltage Protection (BATOVP)

The battery overvoltage limit is clamped at 4% above the battery regulation voltage. When battery over voltage occurs, the charger device immediately disables charge. The fault register BAT_FAULT bit goes high and an INT is asserted to the host.

# 8.2.15.2 Battery Over-Discharge Protection

When battery is discharged below VBAT_DPL, the BATFET is turned off to protect battery from over discharge. To recover from over-discharge, an input source is required at VBUS. When an input source is plugged in, the BATFET turns on. Thy is charged with IBATSHORT (typically 100 mA) current when the VBAT < VSHORT, or precharge current as set in IPRECHG register when the battery voltage is between VSHORT and VBATLOWV.

# 8.2.15.3 System Overcurrent Protection

When the system is shorted or significantly overloaded (IBAT > IBATOP) so that its current exceeds the overcurrent limit, the device latches off BATFET. Section BATFET Enable (Exit Shipping Mode) can reset the latch-off condition and turn on BATFET

# 8.2.16 Serial Interface

The device uses I2C compatible interface for flexible charging parameter programming and instantaneous device status reporting. I2C is a bi-directional 2-wire serial interface. Only two open-drain bus lines are required: a serial data line (SDA) and a serial clock line (SCL). Devices can be considered as masters or slaves when performing data transfers. A master is the device which initiates a data transfer on the bus and generates the clock signals to permit that transfer. At that time, any device addressed is considered a slave.

The device operates as a slave device with address 6AH, receiving control inputs from the master device like micro controller or a digital signal processor through REG00-REG14. Register read beyond REG14 (0x14) returns 0xFF. The I2C interface supports both standard mode (up to 100 kbits), and fast mode (up to 400 kbits). When the bus is free, both lines are HIGH. The SDA and SCL pins are open drain and must be connected to the positive supply voltage via a current source or pull-up resistor.

# 8.2.16.1 Data Validity

The data on the SDA line must be stable during the HIGH period of the clock. The HIGH or LOW state of the data line can only change when the clock signal on the SCL line is LOW. One clock pulse is generated for each data bit transferred.

![](images/f53079eeb6af2bf5e511109a0a49212d82b0bc0d9ce646ffcd4a9a90ecf8727a.jpg)  
Figure 17. Bit Transfer on the I2C Bus

# 8.2.16.2 START and STOP Conditions

All transactions begin with a START (S) and can be terminated by a STOP (P). A HIGH to LOW transition on the SDA line while SCl is HIGH defines a START condition. A LOW to HIGH transition on the SDA line when the SCL is HIGH defines a STOP condition.

START and STOP conditions are always generated by the master. The bus is considered busy after the START condition, and free after the STOP condition.

![](images/bd73b6dcfa52d6ff340a1d0c88cb621a485de47dffd8d2419953e97160c70697.jpg)  
Figure 18. START and STOP conditions

# 8.2.16.3 Byte Format

Every byte on the SDA line must be 8 bits long. The number of bytes to be transmitted per transfer is unrestricted. Each byte has to be followed by an Acknowledge bit. Data is transferred with the Most Significant Bit (MSB) first. If a slave cannot receive or transmit another complete byte of data until it has performed some other function, it can hold the clock line SCL low to force the master into a wait state (clock stretching). Data transfer then continues when the slave is ready for another byte of data and release the clock line SCL.

![](images/da3b3ec1ecbe12aba75f4770155e76f28c428226c15516c05fc5f45a0ca61b26.jpg)  
Figure 19. Data Transfer on the I2C Bus

# 8.2.16.4 Acknowledge (ACK) and Not Acknowledge (NACK)

The acknowledge takes place after every byte. The acknowledge bit allows the receiver to signal the transmitter that the byte was successfully received and another byte may be sent. All clock pulses, including the acknowledge 9th clock pulse, are generated by the master.

The transmitter releases the SDA line during the acknowledge clock pulse so the receiver can pull the SDA line LOW and it remains stable LOW during the HIGH period of this clock pulse.

When SDA remains HIGH during the 9th clock pulse, this is the Not Acknowledge signal. The master can then generate either a STOP to abort the transfer or a repeated START to start a new transfer.

# 8.2.16.5 Slave Address and Data Direction Bit

After the START, a slave address is sent. This address is 7 bits long followed by the eighth bit as a data directio bit (bit R/W). A zero indicates a transmission (WRITE) and a one indicates a request for data (READ).

![](images/858965ef19f5b232a5dd82f7c561651387911a70954a7ceeab8ada0fcfb4490e.jpg)  
Figure 20. Complete Data Transfer

# 8.2.16.6 Single Read and Write

![](images/5834bcb6273c32eb030bd2b7b291487995b38d4c70737a9870ff091983675a3a.jpg)  
Figure 21. Single Write

![](images/4bb202ce95fb66584af7004f7d0e1da054794ad7b968316170b47923129b100d.jpg)  
Figure 22. Single Read

If the register address is not defined, the charger IC send back NACK and go back to the idle state.

# 8.2.16.7 Multi-Read and Multi-Write

The charger device supports multi-read and multi-write on REG00 through REG14 except REG0C.

![](images/2a8b4855b2bf6904127dd09dcb8403ec2b7c7f89bd9527cb0f06849b152a9f9b.jpg)  
Figure 23. Multi-Write

![](images/f6e779510d9450e42fc89a3f52bb2c389f1d81c97d5553bea2e46cd6b4a072ae.jpg)  
Figure 24. Multi-Read

REG0C is a fault register. It keeps all the fault information from last read until the host issues a new read. For example, if Charge Safety Timer Expiration fault occurs but recovers later, the fault register REG0C reports the fault when it is read the first time, but returns to normal when it is read the second time. In order to get the fault information at present, the host has to read REG0C for the second time. The only exception is NTC_FAULT which always reports the actual condition on the TS pin. In addition, REG0C does not support multi-read and multi-write.

# 8.3 Device Functional Modes

# 8.3.1 Host Mode and Default Mode

The device is a host controlled charger, but it can operate in default mode without host management. In default mode, the device can be used an autonomous charger with no host or while host is in sleep mode. When the charger is in default mode, WATCHDOG_FAULT bit is HIGH. When the charger is in host mode, WATCHDOG_FAULT bit is LOW.

After power-on-reset, the device starts in default mode with watchdog timer expired, or default mode. All the registers are in the default settings.

# Device Functional Modes (continued)

In default mode, the device keeps charging the battery with 12-hour fast charging safety timer. At the end of the 12-hour, the charging is stopped and the buck converter continues to operate to supply system load. Any write command to device transitions the charger from default mode to host mode. All the device parameters can be programmed by the host. To keep the device in host mode, the host has to reset the watchdog timer by writing 1 to WD_RST bit before the watchdog timer expires (WATCHDOG_FAULT bit is set), or disable watchdog timer by setting WATCHDOG bits=00.

When the watchdog timer (WATCHDOG_FAULT bit = 1) is expired, the device returns to default mode and all registers are reset to default values except IINLIM, VINDPM, VINDPM_OS, BATFET_RST_EN, BATFET_DLY, and BATFET_DIS bits.

![](images/b57d8083c6aa8f5a6487dec007dd8bc755ad9285851f2a29cbef01f67fab5dbf.jpg)  
Figure 25. Watchdog Timer Flow Chart

# 8.4 Register Maps

I2C Slave Address: 6AH (1101010B + R/W)

# 8.4.1 REG00

Figure 26. REG00   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 8. REG00   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>EN_HIZ</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Enable HIZ Mode0 - Disable (default)1-Enable</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>EN_ILIM</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Enable ILIM Pin0- Disable1– Enable (default: Enable ILIM pin (1))</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>INLIM[5]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>1600mA</td><td rowspan=6 colspan=1>Input Current LimitOffset: 100mARange: 100mA (000000) – 3.25A (111111)Default:0001000 (500mA)(Actual input current limit is the lower of I2C or ILIM pin)iNLIM bits are changed automatically after input sourcetype detection is completedUSB Host SDP w/ OTG=Hi (USB500) = 500mAUSB Host SDP w/ OTG=Lo (USB100) = 500mAUSB CDP = 1.5AUSB DCP = 3.25AAdjustable High Voltage (MaxCharge) DCP = 1.5AUnknown Adapter = 500mANon-Standard Adapter = 1A/2A/2.1A/2.4A</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>IINLIM[4]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>800mA</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>INLIM[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>400mA</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>INLIM[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>200mA</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>INLIM[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>100mA</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>IINLIM[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>50mA</td></tr></table>

# 8.4.2 REG01

Figure 27. REG01   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 9. REG01   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>BHOT[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=2 colspan=2>Boost Mode Hot Temperature Monitor Threshold00-VHoT1 Threshold (34.75%)(default)01- VBHOTo Threshold(Typ. 37.75%)10-VBHoT2 Threshold (Typ. 31.25%)11– Disable boost mode thermal protection</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>BHOT[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>byREG_RSTby Watchdog</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BCOLD</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Boost Mode Cold Temperature Monitor Threshold0-VBcoLDo Threshold(Typ.77%)(default)1-VBCOLD1Threshold (Typ. 80%)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VINDPM_OS[4]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>1600mV</td><td rowspan=5 colspan=1>Input Voltage Limit OffsetDefault: 600mV (00110)Range: 0mV – 3100mVMinimum VINDPM threshold is clamped at 3.9VMaximum VINDPM threshold is clamped at 15.3VWhen VBUS at noLoad is ≤ 6V, the VINDPM_OS is usedto calculate VINDPM threholdWhen VBUS at noLoad is &gt; 6V, the VINDPM_OS multipleby 2 is used to calculate VINDPM threshold.</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VINDPM_OS[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>800mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VINDPM_OS[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>400mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>VINDPM_OS[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>200mV</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>VINDPM_OS[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>100mV</td></tr></table>

# 8.4.3 REG02

Figure 28. REG02   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 10. REG02   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>CONV_START</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=1>ADC Conversion Start Control0 – ADC conversion not active (default).1- Start ADC ConversionThis bit is read-only when CONV_RATE = 1. The bit stays high duringADC conversion and during input source detection.</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>CONV_RATE</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=1>ADC Conversion Rate Selection0– One shot ADC conversion (default)1 – Start 1s Continuous Conversion</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BOOST_FREQ</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=1>Boost Mode Frequency Selection0-1.5MHz1-500KHz(default)Note: Write to this bit is ignored when OTG_CONFIG is enabled.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>ICO_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>Input Current Optimizer (ICO) Enable0– Disable ICO Algorithm1 – Enable ICO Algorithm (default)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>HVDCP_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>High Voltage DCP Enable0- Disable HVDCP handshake1 – Enable HVDCP handshake (default)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>MAXC_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>MaxCharge Adapter Enable0 – Disable MaxCharge handshake1 – Enable MaxCharge handshake (default)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>FORCE_DPDM</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=1>Force D+/D- Detection0-Not in D+/D- or PSEL detection (default)1–Force D+/D- detection</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>AUTO_DPDM_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>Automatic D+/D- Detection Enable0 –Disable D+/D- or PSEL detection when VBUS is plugged-in1 –Enable D+/D- or PEL detection when VBUS is plugged-in (default)</td></tr></table>

# 8.4.4 REG03

Figure 29. REG03   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>RW</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 11. REG03   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>BAT_LOADEN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Battery Load (lBATLOAD) Enable0-Disabled (default)1-Enabled</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>WD_RST</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>I2C Watchdog Timer Reset0 – Normal (default)1 – Reset (Back to 0 after timer reset)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>OTG_CONFIG</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Boost (OTG) Mode Configuration0-OTG Disable1– OTG Enable (default)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CHG_CONFIG</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RSTby Watchdog</td><td rowspan=1 colspan=2>Charge Enable Configuration0 - Charge Disable1- Charge Enable (default)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SYS_MIN[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>0.4V</td><td rowspan=3 colspan=1>Minimum System Voltage LimitOffset: 3.0VRange 3.0V-3.7VDefault: 3.5V (101)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SYS_MIN[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>0.2V</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SYS_MIN[02]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by REG_RST</td><td rowspan=1 colspan=1>0.1V</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>byREG_RSTby Watchdog</td><td rowspan=1 colspan=2>Reserved (default = 0)</td></tr></table>

# 8.4.5 REG04

Figure 30. REG04   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 12. REG04   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>EN_PUMPX</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=2>Current pulse control Enable0 - Disable Current pulse control (default)1- Enable Current pulse control (PUMPX_UP and PUMPX_DN)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>ICHG[6]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>4096mA</td><td rowspan=7 colspan=1>Fast Charge Current LimitOffset: OmARange: 0mA (0000000)- 5056mA (1001111)Default: 2048mA (0100000)Note:ICHG=000000 (OmA) disables chargeICHG &gt;1001111 (5056mA) is clamped to register value1001111(5056mA）</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>ICHG[5]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>2048mA</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>ICHG[4]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>1024mA</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ICHG[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>512mA</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ICHG[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>256mA</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ICHG[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>128mA</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>ICHG[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mA</td></tr></table>

# 8.4.6 REG05

Figure 31. REG05   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 13. REG05   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>IPRECHG[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>512mA</td><td rowspan=4 colspan=1>Precharge Current LimitOffset: 64mARange: 64mA – 1024mADefault: 128mA (0001)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>IPRECHG[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>256mA</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>IPRECHG[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>128mA</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>IPRECHG[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mA</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ITERM[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>512mA</td><td rowspan=4 colspan=1>Termination Current LimitOffset:64mARange: 64mA-1024mADefault: 256mA (0011)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ITERM[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>256mA</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ITERM[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>128mA</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>ITERM[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mA</td></tr></table>

# 8.4.7 REG06

Figure 32. REG06   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 14. REG06   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>VREG[5]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>512mV</td><td rowspan=6 colspan=1>Charge Voltage LimitOffset: 3.840VRange: 3.840V-4.608V (110000)Default: 4.208V (010111)Note:VREG &gt; 110000 (4.608V) is clamped to register value110000 (4.608V)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>VREG[4]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>256mV</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VREG[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>128mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VREG[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VREG[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>32mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VREG[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>16mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>BATLOWV</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=2>Battery Precharge to Fast Charge Threshold0-2.8V1-3.0V (default)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>VRECHG</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=2>Battery Recharge Threshold Offset(below Charge Voltage Limit)0-100mV (VRECHG) belOwVREG (REG06[7:2) (default)1-200mV (VRECHG) below VREG (REG06[7:2])</td></tr></table>

# 8.4.8 REG07

Figure 33. REG07   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 15. REG07   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>EN_TERM</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Charging Termination Enable0- Disable1- Enable (default)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>STAT_DIS</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>STAT Pin Disable0 – Enable STAT pin function (default)1– Disable STAT pin function</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>WATCHDOG[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=2 colspan=1>I2C Watchdog Timer Seting00– Disable watchdog timer01-40s (default)1 -80s11-160s</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>WATCHDOG[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>EN_TIMER</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Charging Safety Timer Enable0- Disable1- Enable (default)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>CHG_TIMER[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=2 colspan=1>Fast Charge Timer Setting00-5hr01-8hrs10- 12 hrs (default)11-20 hrs</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>CHG_TIMER[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Reserved (Default = 1)</td></tr></table>

# 8.4.9 REG08

Figure 34. REG08   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 16. REG08   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>BAT_COMP[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>80mΩ</td><td rowspan=3 colspan=1>IR Compensation Resistor SettingRange: 0– 140mΩDefault: 0Q (000) (i.e. Disable IRComp)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>BAT_COMP[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>40mΩ</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BAT_COMP[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>20mΩ2</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VCLAMP[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>128mV</td><td rowspan=3 colspan=1>IR Compensation Voltage Clampabove VREG (REG06[7:2])Offset: 0mVRange: 0-224mVDefault: OmV (000)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VCLAMP[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VCLAMP[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>32mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>TREG[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=2 colspan=2>Thermal Regulation Threshold00-60℃01-80℃1 -100^℃$11-120°C(default)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>TREG[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td></tr></table>

# 8.4.10 REG09

Figure 35. REG09   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 17. REG09   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>FORCE_ICO</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Force Start Input Current Optimizer (ICO)0– Do not force ICO (default)1-Force ICONote:This bit is can only be set only and always returns to 0 after ICO starts</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>TMR2X_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Safety Timer Setting during DPM or Thermal Regulation0 – Safety timer not slowed by 2X during input DPM or thermalregulation1 − Safety timer slowed by 2X during input DPM or thermal regulation(default)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BATFET_DIS</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>Force BATFET off to enable ship mode0 – Allow BATFET turn on (default)1–Force BATFET off</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Reserved (Default = 0)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>BATFET_DLY</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>BATFET turn off delay control0 – BATFET turn off immediately when BATFET_DIS bit is set (default)1 – BATFET turn off delay by tsm_DLy when BATFET_DIS bit is set</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>BATFET_RST_EN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>BATFET full system reset enable0 – Disable BATFET full system reset1 – Enable BATFET full system reset (default)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>PUMPX_UP</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Current pulse control voltage up enable0- Disable (default)1-EnableNote:This bit is can only be set when EN_PUMPX bit is set and returns to 0after current pulse control sequence is completed</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>PUMPX_DN</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>Current pulse control voltage down enable0- Disable (default)1-EnableNote:This bit is can only be set when EN_PUMPX bit is set and returns to 0after current pulse control sequence is completed</td></tr></table>

# 8.4.11 REG0A

Figure 36. REG0A   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 18. REG0A   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>BOOSTV[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>512mV</td><td rowspan=4 colspan=1>Boost Mode Voltage RegulationOffset: 4.55VRange: 4.55V-5.51VDefault: 5.126V (1001)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>BOOSTV[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>256mV</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BOOSTV[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>128mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>BOOSTV[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwarebyby Watchdog</td><td rowspan=1 colspan=1>64mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby Watchdog</td><td rowspan=1 colspan=2>Reserved (default = 0)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>RW</td><td rowspan=1 colspan=1>by Softwareby Watchdog</td><td rowspan=1 colspan=2>Reserved (default = 0)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby Watchdog</td><td rowspan=1 colspan=2>Reserved (default = 1)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>RW</td><td rowspan=1 colspan=1>by Softwareby Watchdog</td><td rowspan=1 colspan=2>Reserved (default = 1)</td></tr></table>

# 8.4.12 REG0B

Figure 37. REG0B   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>X</td><td>x</td><td>X</td><td>x</td><td>X</td><td>x</td><td>x</td><td>X</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 19. REG0B   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>VBUS_STAT[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=3 colspan=1>VBUS Status registerbq25895000: No Input 001: USB Host SDP010: USB CDP (1.5A)011: USB DCP (3.25A)100: Adjustable High Voltage DCP (MaxCharge) (1.5A)101: Unknown Adapter (500mA)110: Non-Standard Adapter (1A/2A/2.1A/2.4A)111:OTGNote: Software current limit is reported in IINLIM register</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>VBUS_STAT[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VBUS_STAT[O]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CHRG_STAT[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=2 colspan=1>Charging Status00-Not Charging01-Pre-charge(&lt;VBATLow)10-Fast Charging11 – Charge Termination Done</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>CHRG_STAT[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>PG_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>Power Good Status0- Not Power Good1-Power Good</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SDP_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>USB Input Status0 – USB100 input is detected1– USB500 input is detectedNote: This bit always read 1 when VBUS_STAT is not 001</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>VSYS_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>VSYS Regulation Status0-Not in VSYSMIN regulation (BAT&gt;VSYSMIN)1 – In VSYSMIN regulation (BAT &lt; VSYSMIN)</td></tr></table>

# 8.4.13 REG0C

Figure 38. REG0C   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>×</td><td>X</td><td>x</td><td>X</td><td>x</td><td>x</td><td>x</td><td>X</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

# Table 20. REG0C

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>WATCHDOG_FAULT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Watchdog Fault StatusStatus 0 -Normal1- Watchdog timer expiration</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>BOOST_FAULT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Boost Mode Fault Status0- Normal1 – VBUS overloaded in OTG, or VBUS OVP, or battery is too low inboost mode</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>CHRG_FAULT[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=2 colspan=1>Charge Fault Status00-Normal01 − Input fault (VBUS &gt; VAcov or VBAT &lt; VBUS &lt; VvBusmin(typical 3.8V)10 - Thermal shutdown11- Charge Safety Timer Expiration</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CHRG_FAULT[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>BAT_FAULT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Battery Fault Status0-Normal1- BATOVP (VBAT &gt;VBATOVP)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>NTC_FAULT[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=3 colspan=1>NTC Fault StatusBuck Mode:000-Normal001-TS Cold010-TS HotBoost Mode:000 -Normal101-TS Cold110-TS Hot</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>NTC_FAULT[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>NTC_FAULT[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr></table>

# 8.4.14 REG0D

Figure 39. REG0D   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 21. REG0D   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>FORCE_VINDPM</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=2>VINDPM Threshold Setting Method0 – Run Relative VINDPM Threshold (default)1 – Run Absolute VINDPM Threshold</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>VINDPM[6]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>6400mV</td><td rowspan=7 colspan=1>Absolute VINDPM ThresholdOffset: 2.6VRange: 3.9V (0001101) – 15.3V (1111111)Default: 4.4V (0010010)Note:Value &lt; 0001101 is clamped to 3.9V (0001101)Register is read only when FORCE_ViINDPM=0 and canbe written by internal control based on relative VINDPMthreshold settingRegister can be read/write when FORCE_VINDPM = 1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VINDPM[5]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>3200mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VINDPM[4]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>1600mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VINDPM[3]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>800mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VINDPM[2]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>400mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>VINDPM[1]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>200mV</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>VINDPM[0]</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>by Softwareby</td><td rowspan=1 colspan=1>100mV</td></tr></table>

# 8.4.15 REG0E

Figure 40. REG0E   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 22. REG0E   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>THERM_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>Thermal Regulation Status0-Normal1 – In Thermal Regulation</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>BATV[6]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1280mV</td><td rowspan=7 colspan=1>ADC conversion of Battery Voltage (VBAT)Offset: 2.304VRange: 2.304V (0000000) - 4.848V (11111)Default: 2.304V (0000000)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>BATV[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>640mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>BATV[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>320mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>BATV[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>160mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>BATV[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>80mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>BATV[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>40mV</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>BATV[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>20mV</td></tr></table>

# 8.4.16 REG0F

Figure 41. REG0F   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 23. REG0F   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>Reserved: Always reads 0</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>SYSV[6]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1280mV</td><td rowspan=7 colspan=1>ADDC conversion of System Voltage (Vsys)Offset: 2.304VRange: 2.304V (0000000) – 4.848V (1111111)Default: 2.304V (0000000)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>SYSV[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>640mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SYSV[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>320mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SYSV[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>160mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SYSV[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>80mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SYSV[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>40mV</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>SYSV[O]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>20mV</td></tr></table>

# 8.4.17 REG10

Figure 42. REG10   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 24. REG10   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>Reserved: Always reads 0</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>TSPCT[6]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>29.76%</td><td rowspan=7 colspan=1>ADC conversion of TS Voltage (TS) as percentage of REGNOffset: 21%Range 21% (0000000)-80% (1111111)Default: 21% (0000000)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>TSPCT[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>14.88%</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>TSPCT[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>7.44%</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>TSPCT[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>3.72%</td><td rowspan=1 colspan=1>Offset: 21%Range 21% (0000000)-80% (1111111)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>TSPCT[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1.86%</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>TSPCT[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>0.93%</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>TSPCT[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>0.465%</td></tr></table>

# 8.4.18 REG11

Figure 43. REG11   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 25. REG11   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>VBUS_GD</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>VBUS Good Status0 - Not VBUS attached1- VBUS Attached</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>VBUSV[6]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>6400mV</td><td rowspan=7 colspan=1>ADC conversion of VBUS voltage (VBus)Offset: 2.6VRange 2.6V (0000000) – 15.3V (1111111)Default: 2.6V (000000)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VBUSV[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>3200mV</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>VBUSV[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1600mV</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VBUSV[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>800mV</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>VBUSV[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>400mV</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>VBUSV[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>200mV</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>VBUSV[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>100mV</td></tr></table>

# 8.4.19 REG12

Figure 44. REG12   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 26. REG12   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Unused</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>Always reads 0</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>ICHGR[6]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>3200mA</td><td rowspan=7 colspan=1>ADC conversion of Charge Current (lBAT) when VBAT &gt;VBATSHORTOffset: 0mARange 0mA (0000000) -6350mA (1111111)Default: 0mA (0000000)Note:This register returns 00000 for VBAT &lt; VBATsHORT</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>ICHGR[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1600mA</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>ICHGR[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>800mA</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ICHGR[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>400mA</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ICHGR[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>200mA</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ICHGR[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>100mA</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>ICHGR[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>50mA</td></tr></table>

# 8.4.20 REG13

Figure 45. REG13   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 27. REG13   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=2>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>VDPM_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>VINDPM Status0 –Not in VINDPM1-VINDPM</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>IDPM_STAT</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=2>IINDPM Status0-Not in IINDPM1-IINDPM</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>IDPM_LIM[5]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>1600mA</td><td rowspan=6 colspan=1>Input Current Limit in effect while Input Current Optimizer(ICO) is enabledOffset: 100mA (default)Range 100mA (0000000) – 3.25mA (1111111)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>IDPM_LIM[4]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>800mA</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>IDPM_LIM[3]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>400mA</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>IDPM_LIM[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>200mA</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>IDPM_LIM[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>100mA</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>IDPM_LIM[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>50mA</td></tr></table>

# 8.4.21 REG14

Figure 46. REG14   

<table><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>R/W</td><td>R/W</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr></table>

LEGEND: R/W = Read/Write; R = Read only; -n = value after reset

Table 28. REG14   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>Reset</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>REG_RST</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Register Reset0-Keep current register seting (default)1–Reset to default register value and reset safety timerNote:Reset to 0 after register reset is completed</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>ICO_OPTIMIZED</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>NA</td><td rowspan=1 colspan=1>Input Current Optimizer (ICO) Status0-Optimization is in progress1 - Maximum Input Current Detected</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>PN[2]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=3 colspan=1>Device Configuration111: bq25895</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>PN[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>PN[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>TS_PROFILE</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Temperature Profile0− Cold/Hot (default)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>DEV_REV[1]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td><td rowspan=2 colspan=1>Device Revision: 01</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>DEV_REV[0]</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>N/A</td></tr></table>

# 9 Application and Implementation

# NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

# 9.1 Application Information

A typical application consists of the device configured as an I2C controlled power path management device and a single cell battery charger for Li-Ion and Li-polymer batteries used in a wide range of smartphones and other portable devices. It integrates an input reverse-block FET (RBFET, Q1), high-side switching FET (HSFET, Q2), low-side switching FET (LSFET, Q3), and BATFET (Q4) between the system and battery. The device also integrates a bootstrap diode for the high-side gate drive.

# 9.2 Typical Application

![](images/94af3b32807acfae95cc897f1822833bb620c983fb3014417de2476659061067.jpg)  
Figure 47. bq25895 with D+/D- Interface and 2.4 A Boost Mode Output

# 9.2.1 Design Requirements

For this design example, use the parameters shown in Table 29.

Table 29. Design Parameter   

<table><tr><td rowspan=1 colspan=1>PARAMETERS</td><td rowspan=1 colspan=1>VALUES</td></tr><tr><td rowspan=1 colspan=1>Input voltage range</td><td rowspan=1 colspan=1>3.9 V to 14 V</td></tr><tr><td rowspan=1 colspan=1>Input current limit</td><td rowspan=1 colspan=1>1.5A</td></tr><tr><td rowspan=1 colspan=1>Fast charge current</td><td rowspan=1 colspan=1>5000 mA</td></tr><tr><td rowspan=1 colspan=1>Output voltage</td><td rowspan=1 colspan=1>4.352V</td></tr><tr><td rowspan=1 colspan=1>VReF system pullup voltage</td><td rowspan=1 colspan=1>1.8 V- 3.3 V</td></tr></table>

# 9.2.2 Detailed Design Procedure

# 9.2.2.1 Custom Design With WEBENCH® Tools

Click here to create a custom design using the bq25895 device with the WEBENCH® Power Designer.

1. Start by entering the input voltage (VIN), output voltage (VOUT), and output current (IOUT) requirements.   
2. Optimize the design for key parameters such as efficiency, footprint, and cost using the optimizer dial.   
3. Compare the generated design with other possible solutions from Texas Instruments.

The WEBENCH Power Designer provides a customized schematic along with a list of materials with real-time pricing and component availability.

In most cases, these actions are available:

Run electrical simulations to see important waveforms and circuit performance Run thermal simulations to understand board thermal performance Export customized schematic and layout into popular CAD formats Print PDF reports for the design, and share the design with colleagues

Get more information about WEBENCH tools at www.ti.com/WEBENCH.

# 9.2.2.2 Inductor Selection

The device has 1.5 MHz switching frequency to allow the use of small inductor and capacitor values. The Inductor saturation current should be higher than the charging current (ICHG) plus half the ripple current (IRIPPLE): I I + (1/2) I BAT CHG RIPPLE ³ (5)

The inductor ripple current depends on input voltage (VBUS), duty cycle (D = VBAT/VVBUS), switching frequency (fs) and inductance (L):

![](images/eb718d5f0683216e711e141b649d03cf034dc4fa4a04d94fd2e68fcbcb69c912.jpg)

The maximum inductor ripple current happens with D = 0.5 or close to 0.5. Usually inductor ripple is designed in the range of (20–40%) maximum charging current as a trade-off between inductor size and efficiency for a practical design.

# 9.2.2.3 Buck Input Capacitor

Input capacitor should have enough ripple current rating to absorb input switching ripple current. The worst case RMS ripple current is half of the charging current when duty cycle is 0.5. If the converter does not operate at 50% duty cycle, then the worst case capacitor RMS current IPMID occurs where the duty cycle is closest to 50% and can be estimated by Equation 7:

Low ESR ceramic capacitor such as X7R or X5R is preferred for input decoupling capacitor and should be placed to the drain of the high side MOSFET and source of the low side MOSFET as close as possible. Voltage rating of the capacitor must be higher than normal input voltage level. 25 V rating or higher capacitor is preferred for up to 14-V input voltage. 8.2-μF capacitance is suggested for typical of 3 A – 5 A charging current.