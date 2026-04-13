# TPS6123x 8-A Valley Current Synchronous Boost Converters with Constant Current Output Feature

# 1 Features

Up to 97% Efficiency Synchronous Boost Up to 3.5-A IOUT for 3.3-V to 5-V Conversion 10-A 14-mΩ/14-mΩ Internal Power Switches Programmable Constant Output Current Output Current Monitor 10-µA IQ under Light Load Condition Boost Status Indication True disconnection during shutdown Fixed 5.1-V Output Voltage (TPS61235P) or Adjustable Output Voltage from 2.9-V to-5.5 V (TPS61236P) 1-MHz Switching Frequency Softstart, Current Limit, Over Voltage and Ove Thermal Protections 2.5 mm x 2.5 mm VQFN Package

# 2 Applications

Power Banks, Battery Backup Units • USB Charging Port USB Type-C Battery Powered USB Hub Tablet PCs Battery Powered Products

# 3 Description

The TPS6123x is a high current, high efficiency synchronous boost converter with constant output current feature for single cell Li-Ion and Li-polymer battery powered products, in a wide range of power bank, tablet, and other portable devices. The IC integrates 14-mΩ/14-mΩ power switches and is capable of delivering up to a 3.5-A output current for 3.3-V to 5-V conversion with up to 97% high efficiency. The device supports a programmable constant output current to control power delivery, so to save power path components and lower total system thermal dissipation effectively.

The device only consumes a 10-µA quiescent current under a light load condition, and can report load status to the system, which make it very suitable for Always-On applications. With the TPS6123x, a simple and flexible system design can be achieved, eliminating external power path components, saving PCB space, and reducing BOM cost.

In shutdown, the output is completely disconnected from the input, and current consumption is reduced to less than 1 µA. Other features like soft start control, reverse current blocking, over voltage protection, and thermal shutdown protection are built-in for system safety.

The devices are available in a 2.5-mm x 2.5-mm VQFN package.

Device Information(1)   

<table><tr><td rowspan=1 colspan=1>PART NUMBER</td><td rowspan=1 colspan=1>PACKAGE</td><td rowspan=1 colspan=1>BODY SIZE (NOM)</td></tr><tr><td rowspan=1 colspan=1>TPS61235P</td><td rowspan=1 colspan=1>VQFN (9)</td><td rowspan=1 colspan=1>2.50mm ×2.50mm</td></tr><tr><td rowspan=1 colspan=1>TPS61236P</td><td rowspan=1 colspan=1>VQFN (9)</td><td rowspan=1 colspan=1>2.50mm ×2.50 mm</td></tr></table>

(1) For all available packages, see the orderable addendum at the end of the data sheet.

![](images/55107f8ae706e7222a3d9299b8a05af198062997db986a31c94ba07673b8d02c.jpg)  
TPS61235P Typical Application

![](images/d99569b40604128eac373c0961ef56882bff69e82ffd958e41f3cdf2e016ada4.jpg)  
Typical Application Efficiency (TPS61235P)

# Table of Contents

1 Features... 1   
2 Applications . 1   
3 Description .. 1   
4 Revision History... 2   
5 Device Comparison Table. 3   
6 Pin Configuration and Functions. 3   
7 Specifications... 4

#

7.1 Absolute Maximum Ratings . 4   
7.2 ESD Ratings.. 4   
7.3 Recommended Operating Conditions. 4   
7.4 Thermal Information. 4   
7.5 Electrical Characteristics.. 5   
7.6 Typical Characteristics.

# 8 Detailed Description . 9

8.1 Overview .. 9   
8.2 Functional Block Diagram .. 9   
8.3 Feature Description.. 10   
8.4 Device Functional Modes. 15

# 9 Applications and Implementation . 16

9.1 Application Information.. 16   
9.2 Typical Applications . 16

# 10 Power Supply Recommendations 26

# 11 Layout.. 27

11.1 Layout Guidelines .. 27   
11.2 Layout Example .. 27   
11.3 Thermal Considerations. 28

# 12 Device and Documentation Support .. 29

12.1 Device Support.. 29   
12.2 Documentation Support 29   
12.3 Related Links . 29   
12.4 Receiving Notification of Documentation Updates 29   
12.5 Community Resources. 29   
12.6 Trademarks. 29   
12.7 Electrostatic Discharge Caution. . 29   
12.8 Glossary .. 30

# 13 Mechanical, Packaging, and Orderable

Information . 30

# 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Original (September 2015) to Revision A

• Changed part numbers to TPS61235P and TPS61236P for Pb-free nomenclature .

# 5 Device Comparison Table

<table><tr><td rowspan=1 colspan=1>PART NUMBER</td><td rowspan=1 colspan=1>OUTPUT VOLTAGE</td></tr><tr><td rowspan=1 colspan=1>TPS61235P</td><td rowspan=1 colspan=1>5.1V</td></tr><tr><td rowspan=1 colspan=1>TPS61236P</td><td rowspan=1 colspan=1>Adjustable</td></tr></table>

# 6 Pin Configuration and Functions

![](images/efd22071ef0c2b1619427e824300fc83cd7aae86b03e2316f81f00911f7a7e1a.jpg)

Pin Functions   

<table><tr><td rowspan=1 colspan=2>PIN</td><td rowspan=2 colspan=1>10</td><td rowspan=2 colspan=1>DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>NAME</td><td rowspan=1 colspan=1>NUMBER</td></tr><tr><td rowspan=1 colspan=1>PGND</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>Power ground.</td></tr><tr><td rowspan=1 colspan=1>SW</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>The switch pin of the boost converter.It is connected to the drain of the internal Power MOsFETs.</td></tr><tr><td rowspan=1 colspan=1>VIN</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>IC power supply input.</td></tr><tr><td rowspan=1 colspan=1>CC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>Constant output current programming pin. Connect a resistor to this pin to program the constant outputcurrent. A capacitor should be connected in parall to stabilize the control loop. Connect this pin to theAGND pin to disable the constant output current function.</td></tr><tr><td rowspan=1 colspan=1>AGND</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Analog ground.</td></tr><tr><td rowspan=1 colspan=1>FB</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Voltage feedback pin of adjustable version (TPS61236P). Must be connected to VOUT pin on fixedoutput voltage version (TPS61235).</td></tr><tr><td rowspan=1 colspan=1>EN</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Enable logic input. Logic high enables the device. Logic low disables the device and puts it inshutdown mode. This pin must be terminated and cannot be lef floating. An external pull down resistorconnected to this pin is recommended.</td></tr><tr><td rowspan=1 colspan=1>INACT</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>o</td><td rowspan=1 colspan=1>Load status indication. Open drain output. Can be left float or connected to AGND pin if not used.</td></tr><tr><td rowspan=1 colspan=1>VOUT</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>Boost converter output.</td></tr></table>

# 7 Specifications

# 7.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted)(1)

<table><tr><td></td><td></td><td rowspan=1 colspan=1>MIN      MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=2 colspan=1>Voltage(2)</td><td rowspan=1 colspan=1>VIN, EN, VOUT, CC, INACT, FB</td><td rowspan=1 colspan=1>-0.3       6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>SW</td><td rowspan=1 colspan=1>-0.3       7</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Operating junction temperature, TJ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40      150</td><td rowspan=1 colspan=1>°℃</td></tr><tr><td rowspan=1 colspan=1>Storage temperature, Tstg</td><td></td><td rowspan=1 colspan=1>-65       150</td><td rowspan=1 colspan=1>℃</td></tr></table>

(1) Stresses beyond those listed under absolute maximum ratings may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under recommended operating conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods my affect device reliability.   
(2) All voltages are with respect to network ground terminal.

# 7.2 ESD Ratings

<table><tr><td></td><td></td><td rowspan=1 colspan=1>VALUE</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=2 colspan=1>V(ESD)        Electrostatic discharge</td><td rowspan=1 colspan=1>Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)</td><td rowspan=1 colspan=1>±4000</td><td rowspan=2 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Charged-device model (CDM), per JEDEC specification JESD22-C101(2))</td><td rowspan=1 colspan=1>±1500</td></tr></table>

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.   
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

# 7.3 Recommended Operating Conditions

<table><tr><td colspan="2"></td><td>MIN</td><td>NOM</td><td>MAX</td><td>UNIT</td></tr><tr><td colspan="2">$ViN(1)) Supply voltage at VIN pin</td><td>2.3</td><td colspan="2">VOUT-0.6</td><td>V</td></tr><tr><td rowspan="2">VOUT</td><td>Target output voltage (TPS61235P)</td><td></td><td>5.1</td><td></td><td>V</td></tr><tr><td>Target output voltage (TPS61236P)</td><td>2.9</td><td></td><td>5.5</td><td>V</td></tr><tr><td>L</td><td>Effective inductance</td><td>0.7</td><td>1</td><td>1.3</td><td>μH</td></tr><tr><td>$C_}$</td><td>Effective input capacitance(2)</td><td>4.7</td><td>10</td><td></td><td>μF</td></tr><tr><td>Co</td><td>Effective output capacitance(2)</td><td>20</td><td></td><td></td><td>μF</td></tr><tr><td>CRCC</td><td>Capacitor parallel with the RCC resistor connected at CC pin</td><td>1</td><td>10</td><td></td><td>nF</td></tr><tr><td>RINACT</td><td>INACT pin pull up resistance</td><td></td><td>1</td><td></td><td>MΩ</td></tr><tr><td>REN</td><td>EN pin pull down resistance</td><td></td><td>1</td><td></td><td>MΩ</td></tr><tr><td>d$</td><td>Operating junction temperature</td><td>-40</td><td></td><td>125</td><td>℃</td></tr></table>

(1) The maximum input voltage should be 0.6-V lower than the output voltage in Constant Voltage operation for the TPS6123x to function correctly. (2) Effective capacitance value. Ceramic capacitor’s derating effect under bias should be considered when selecting capacitors.

# 7.4 Thermal Information

<table><tr><td rowspan=3 colspan=1>THERMAL METRIC (1)</td><td rowspan=1 colspan=1>TPS61235PTPS61236P</td><td rowspan=3 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>RWL (VQFN)</td></tr><tr><td rowspan=1 colspan=1>9 PINS</td></tr><tr><td rowspan=1 colspan=1>ReJA        Junction-to-ambient thermal resistance</td><td rowspan=1 colspan=1>28.7</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=1 colspan=1>ReJc(top)    Junction-to-case(top) thermal resistance</td><td rowspan=1 colspan=1>24.1</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>ROJB        Junction-to-board thermal resistance</td><td rowspan=1 colspan=1>10.9</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=1 colspan=1>YJT        Junction-to-top characterization parameter</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>YJB         Junction-to-board characterization parameter</td><td rowspan=1 colspan=1>10.8</td><td rowspan=1 colspan=1>CN</td></tr><tr><td rowspan=1 colspan=1>ReJC(bottom) Junction-to-case(bottom) thermal resistance</td><td rowspan=1 colspan=1>1.6</td><td rowspan=1 colspan=1>CW</td></tr></table>

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

# 7.5 Electrical Characteristics

<table><tr><td colspan="7">Tj = –40°C to 125°C and Vin = 3.6 V. Typical values are at Ty = 25°C, unless otherwise noted. TEST CONDITIONS</td></tr><tr><td colspan="3">PARAMETER</td><td>MIN</td><td>TYP</td><td>MAX</td><td>UNIT</td></tr><tr><td colspan="3">POWER SUPPLY</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">ViN Input voltage</td><td>2.3</td><td></td><td>VOUT-0.6</td><td>V</td></tr><tr><td rowspan="2">VuvLO</td><td rowspan="2"> Input under voltage lockout</td><td>Vin rising</td><td></td><td>2.2</td><td>2.3</td><td>V</td></tr><tr><td>Hysteresis</td><td></td><td>125</td><td></td><td>mV</td></tr><tr><td></td><td>Quiescent current into VIN</td><td>IC enabled, No Load, No switching,</td><td></td><td>5</td><td>11</td><td>μA</td></tr><tr><td></td><td>Quiescent current into VOUT</td><td>VoUT = 5.1 V</td><td></td><td>5</td><td>30</td><td>μA</td></tr><tr><td>1sD</td><td>Shutdown current into VIN</td><td>IC disabled, Tj = −40°C to 85°℃</td><td></td><td>0.01</td><td>3</td><td>μA</td></tr><tr><td rowspan="4">OUTPUT</td><td>Output voltage range</td><td>TPS61236P</td><td>2.9</td><td></td><td></td><td></td></tr><tr><td></td><td>PWM mode,</td><td></td><td></td><td>5.5</td><td>V</td></tr><tr><td>Output voltage</td><td>TPS61235P PFM mode,</td><td>5.0</td><td>5.1</td><td>5.2</td><td>V</td></tr><tr><td></td><td>TPS61235 PWM mode,</td><td></td><td>5.2</td><td></td><td>V</td></tr><tr><td rowspan="2">VFB</td><td rowspan="2">Feedback voltage</td><td>TPS61236P</td><td>1.219</td><td>1.244</td><td>1.269</td><td>V</td></tr><tr><td>PFM mode, TPS61236P</td><td></td><td>1.256</td><td></td><td>V</td></tr><tr><td>VovP</td><td>Output over voltage protection threshold</td><td></td><td>5.60</td><td>5.80</td><td>5.93</td><td>V</td></tr><tr><td>LKG_FB</td><td>Leakage current into FB pin</td><td>TPS61235P, VFB = 5.1 V TPS61236P, VFB = 1.244 V</td><td></td><td></td><td>4000</td><td>nA</td></tr><tr><td>ILKG_SW</td><td>Leakage current into SW pin</td><td>IC disabled, Tj = −40°C to 85°C,</td><td></td><td>0.05</td><td>120</td><td>nA</td></tr><tr><td>LKG_VOUT</td><td>Leakage current into VOuT pin</td><td>VsW = 5.1V IC disabled, Tj =−40°C to 85°C,</td><td></td><td></td><td>2</td><td>μA</td></tr><tr><td rowspan="2"></td><td>Line regulation</td><td>VOUT =5.1V 1OUT= 2A,ViN=2.7VtO4.5V,</td><td></td><td>0.05</td><td>2</td><td>μA</td></tr><tr><td></td><td>VOUT = 5.1 V</td><td></td><td>0.06</td><td></td><td>%N</td></tr><tr><td></td><td>Load regulation</td><td>1oUT=0.5Ato3A, ViN=3.6V, VOUT =5.1 V</td><td></td><td>0.06</td><td></td><td>%/A</td></tr><tr><td>POWER STAGE</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RDs(on)</td><td>High side MOSFET on resistance Low side MOSFET on resistance</td><td>VOUT=5.1V VoUT =5.1V</td><td></td><td>14</td><td>30</td><td>mΩ</td></tr><tr><td>fsw</td><td>Switching frequency</td><td>VouT = 5.1 V, PWM mode</td><td>750</td><td>14 1000</td><td>30 1250</td><td>mΩ kHz</td></tr><tr><td></td><td></td><td>Rcc = 124 kΩ, T =25^c$</td><td>-15%</td><td></td><td></td><td></td></tr><tr><td rowspan="4"></td><td rowspan="4">Constant output current limit accuracy</td><td></td><td></td><td></td><td>15%</td><td></td></tr><tr><td>Rc = 61.9kΩ2 $Tj =25^℃C$</td><td>-10%</td><td></td><td>10%</td><td></td></tr><tr><td>Rcc = 61.9kΩ, Tj=-20^C to125°C</td><td>-15%</td><td></td><td>15%</td><td></td></tr><tr><td>T₁ = -20^C to 100°℃C</td><td>6.5</td><td>8</td><td>9.5</td><td>A</td></tr><tr><td>LiM_pre</td><td>Precharge mode current limit</td><td>VoUT = 0V, Tj = 0^C to^125°C</td><td>0.05</td><td>0.25</td><td>0.8</td><td>A</td></tr><tr><td rowspan="3">liNACT th</td><td rowspan="3"></td><td>VOUT =2V</td><td></td><td>1.3</td><td></td><td>A</td></tr><tr><td>VoUT= 3V</td><td></td><td>1.7</td><td></td><td>A</td></tr><tr><td>VOUT= 5.1V</td><td></td><td>50</td><td></td><td>mA</td></tr><tr><td>tINACT_delay</td><td>Deglitch delay</td><td>VoUT = 5.1 V</td><td></td><td>15</td><td></td><td>ms</td></tr><tr><td>TSD</td><td rowspan="2">Thermal shutdown threshold</td><td>TJ rising</td><td></td><td>140</td><td></td><td>C</td></tr><tr><td></td><td>Hysteresis</td><td></td><td>15</td><td></td><td>C</td></tr></table>

# Electrical Characteristics (continued)

TJ = –40°C to 125°C and VIN = 3.6 V. Typical values are at TJ = 25°C, unless otherwise noted.

<table><tr><td colspan="2">PARAMETER</td><td>TEST CONDITIONS</td><td>MIN</td><td>TYP</td><td>MAX</td><td>UNIT</td></tr><tr><td colspan="3">LOGIC INTERFACE</td><td></td><td></td><td></td><td></td></tr><tr><td>VENH</td><td>EN Logic high input voltage</td><td></td><td>1.0</td><td></td><td></td><td>V</td></tr><tr><td>VEN_L</td><td>EN Logic low input voltage</td><td></td><td></td><td></td><td>0.4</td><td>V</td></tr><tr><td>LKG EN</td><td>EN pin input leakage current</td><td>EN pin connected to GND or VIN</td><td></td><td>0.01</td><td>0.3</td><td>μA</td></tr><tr><td>VINACT</td><td>INACT pin output low level voltage</td><td>ISINK INACT = 80 μA</td><td></td><td></td><td>0.4</td><td>V</td></tr></table>

# 7.6 Typical Characteristics

VIN = 3.6 V, VOUT = 5.0 V, TJ = –40°C to 125 °C, unless otherwise noted.

![](images/6c3ff71759e075e95617a95855830c47b363cc7bdbd13582545effc411664ebb.jpg)  
Figure 1. Efficiency vs Output Current with Different Inputs

![](images/8782773739a401b511e8227ad6a5b0dd3e938a6f35c950d4052d4d1796a09733.jpg)  
Figure 3. Efficiency vs Output Current with Different Inputs

![](images/c01713e3717b7264e525962eee7fd0b81c39ae30fbebe6cd7e50dab10fe670d1.jpg)  
Figure 2. Efficiency vs Output Current with Different Inputs

![](images/99138f114e955806bc287e983c13a93e59f446ffa9e91972881e8bd1bf0462b5.jpg)  
Figure 5. No Load Supply Current vs Ambient Temperature

![](images/f2c1fa92f45597db44a4893d0ebbad96279692427ba56fe7e9fc756c45885e07.jpg)  
Figure 4. No Load Supply Current vs Input Voltage

![](images/b4580600ca7045ecc2d1ffbb30992cb6b35c74a0ccbef5bc235b730b32898a8b.jpg)  
Figure 6. DC Pre-Charge Current vs Output Voltage

# Typical Characteristics (continued)

VIN = 3.6 V, VOUT = 5.0 V, TJ = –40°C to 125 °C, unless otherwise noted.

![](images/e9a582bc9e12ec3a98bf41cd1b1f6a1a9403576e56a05c2e53d5a713ec123b4f.jpg)  
Figure 7. DC Pre-Charge Current vs Output Voltage

![](images/6f77b0914de349f9385132f6ba5f1dd83be450114fef0bd13cc1aabfde7a9861.jpg)  
Figure 9. Current Limit vs Input Voltage

![](images/51abb1971c2715658d6fa4ba22bc4ec7a9e23d6a7a313fc238ecf7dd8bb557be.jpg)  
Figure 8. Minimum Load Resistance at Startup

![](images/107f8e63a9586253f24bf5412f2440a1f57fcc4f1c9a2c446702d60fbfa15dcd.jpg)  
Figure 11. Constant Output Current vs Input Voltage

![](images/77d43c7a92b26446711692c0fe0339f58b3757b15b3b76a688e8a72626635252.jpg)  
Figure 10. Current Limit vs Ambient Temperature

![](images/d3e41bda1584942c04e15f33d190f457dd9dd5919e834025582b3cb90cddd007.jpg)  
Figure 12. Constant Output Current vs Ambient Temperature

# 8 Detailed Description

# 8.1 Overview

The TPS6123x is a high current, high efficiency synchronous boost converter with constant current output feature. It is optimized for single cell Li-Ion and Li-polymer battery powered products, in a wide range of power bank, tablet, and other portable devices. The converter integrates 14-mΩ /14-mΩ power switches and is capable of delivering more than 3.5-A output current for 3.3-V to 5-V conversion. The low Rds(on) of the internal power switches enables up to 97% power conversion efficiency.

The TPS6123x has two regulation loops, one is the output voltage regulation loop as the normal boost converters have, and the other is the output current regulation loop. An external resistor can be used to program the maximum output current, and once the output current reaches the programmed value, the current loop kicks in to regulate the output current. The TPS6123x can also indicate the load status. These features can simplify system design, eliminate external power path components like a load switch, and achieve much lower system thermal dissipation and improve the total power conversion effectively.

The TPS6123x also consumes only 10-µA quiescent current under a light load condition. This low quiescent current together with the load status indication function makes the device very suitable for Always-On applications. For example, for a power bank application, the TPS6123x can remain always on and report load status to the system controller.

# 8.2 Functional Block Diagram

![](images/ba5dc3de0c3c76d7b5a92a7b84528b5ae9d25c8d18a351bc5140b3498c3a0dd4.jpg)

(1) Internal FB resistor divider is implemented in TPS61235P only.

# 8.3 Feature Description

# 8.3.1 Boost Controller Operation

The TPS6123x synchronous boost converter typically operates at a quasi-constant 1-MHz frequency Pulse Width Modulation (PWM) at moderate to heavy load, which allows the use of small inductors and capacitors to achieve a small solution size. At light load, it operates in power-save mode with Pulse Frequency Modulation (PFM) for improved efficiency.

During PWM operation, the converter uses a quasi-constant on-time valley current mode control scheme to achieve excellent line/load regulation. Based on the VIN /VOUT ratio, a simple circuit predicts the required on-time. At the beginning of the switching cycle, the low-side NMOS switch is turned on and the inductor current ramps up to a peak current that is determined by the on-time and the inductance. Once the on-time has expired, the lowside switch is turned off and the rectifying NMOS switch is turned on. The inductor current decays until reaching the valley current threshold which is determined by internal control loops. Once this occurs, the on-time is set again to turn the low-side switch back on and the cycle is repeated. Internal loop compensation is implemented to simplify the design process while minimizing the number of external components. A bootstrap circuit is built in to drive the rectifying NMOS switch. Figure 13 illustrates the PWM mode operation.

![](images/3782216f6d31cf1278371e7488e92cf7210e81a1b8e4effdf9e53ca09803c591.jpg)  
Figure 13. PWM Mode Operation Illustration

Under a light load condition, the converter works in Pulse Frequency Modulation (PFM) mode. In this mode, the boost converter switches and ramps up the output voltage until VOUT reaches the PFM threshold. Then it stops switching and consumes less quiescent current. It resumes switching when the output voltage drops below the threshold. The converter exits PFM mode when the output current can no longer be supported in this mode. Refer to Figure 14 for PFM mode operation details.

![](images/4ed905661046c0512296cd95e27ea86c24320741b26cc9034ac1862f84ba0204.jpg)  
Figure 14. PFM Mode Operation Illustration

# 8.3.2 Soft Start

The TPS6123x integrates an internal soft start circuit which controls ramp up of the output voltage and prevents the converter from inrush current during start-up.

When the device is enabled, the rectifying switch is turned on to charge the output capacitor to the input voltage. This is called the pre-charge phase. During the phase, the output current is limited to the pre-charge current limit ILIM_pre, which is proportional to the output voltage. The pre-charge current increases when the output voltage gets higher.

# Feature Description (continued)

Once the output capacitor is charged close to the input voltage, the converter starts switching. This is called the start-up switching phase. During the phase, the converter steps up the voltage to its nominal output voltage by following an internal ramp up reference voltage, which ramps up in around 3 ms (typ.) to its final value. The current limit function is activated in this phase.

Because of the current limitation during the pre-charge phase, the TPS6123x may not be able to start up under a heavy load condition. It is recommended to apply no load or a light load during the startup process, and apply the full load only after the TPS6123x starts up successfully. Refer to Figure 8 for the recommended minimum load resistance.

# 8.3.3 Enable and Disable

An external logic signal at the EN pin can enable and disable the device.

The TPS6123x device starts operation when EN is set high and starts up with the soft-start process. For proper operation, the EN pin must be terminated and must not be left floating. Pulling EN low forces the device into shutdown, with a shutdown current of typically 0.01 µA. In shutdown mode, a true disconnection between input and output is implemented. It can prevent current from input to output, or reverse current from output to input.

# 8.3.4 Constant Output Voltage and Constant Output Current Operations

Normally a boost converter only regulates its output voltage, but for the TPS6123x, it is different. There are two regulation loops for the device. One loop regulates the output voltage, and it is called CV (Constant Voltage) operation; the other regulates the output current, and it is called CC (Constant Current) operation.

# 8.3.4.1 Constant Voltage Operation

Before the output current reaches the constant current value programmed by an external resistor at the CC pin, the voltage regulation loop dominates. The output voltage is monitored via external or internal feedback network resistors at the FB pin. An error amplifier compares the feedback voltage to an internal reference voltage VREF and adjusts the inductor current valley accordingly. In this way, the TPS6123x operates as a normal boost converter to regulate the output voltage.

During CV operation, the maximum VIN should be 0.6-V below VOUT to keep the output voltage well regulated. The TPS6123x may enter into pass-through operation prematurely when VIN is close to but still below VOUT, and exists when VIN is below the threshold with a hysteresis. When in pass-through operation, the boost converter stops switching and keeps the rectifying switch on, so the input voltage can pass through the external inductor and internal rectifying switch to the output. The output current capability becomes lower and is limited by the precharge current limit ILIM_pre of the rectifying switch. More than 0.4-V under-voltage of VOUT may occur due to the premature pass-through operation and the hysteresis of existing. If the under-voltage is not acceptable, the maximum VIN should be limited to 0.6-V below VOUT , which gives enough margin to avoid the pass-through operation.

# 8.3.4.2 Output Current Monitor

During the CV operation, the output current can be monitored at the CC pin. In the TPS6123x, the inductor current is sensed through the rectifying switch during the off-time of each switching cycle. The device then builds a current signal which is 1/K times the sensed current and feeds it to the CC pin during off-time. As a result, the CC pin voltage, VCC, is proportional to the average output current as Equation 1 shows.

![](images/d9e5344cd9b66ce9c11592cb615e12d054f748c47499681d334946a15a36dd41.jpg)

Where:

VCC is the voltage at the CC pin,   
IOUT is the output current,   
K is the coefficient between the output current and the internal built current signal, K = 100,000, RCC is the resistor connected at the CC pin.

A capacitor must be connected in parallel with RCC to average the CC pin voltage and also stabilize the control loop. Normally a 10-nF capacitor is recommended. A larger capacitor at the CC pin will smooth the CC voltage better, and also slow down the loop response.

# Feature Description (continued)

The CC pin can be connected to ground to disable the output current monitor function, and it will not affect the CV operation.

# 8.3.4.3 Constant Current Operation

As Equation 1 shows, the CC pin voltage is proportional to the output current. The TPS6123x monitors the CC pin voltage and compares it to an internal reference voltage VREF, which is 1.244 V typically. When VCC exceeds VREF, the CC regulation loop kicks in and pulls the inductor current valley to a lower value so to keep the CC pin voltage at VREF. Equally, the output current is regulated at the set value as Equation 2.

![](images/9131c49426f823e1441542013bf826f6dfb35ffc9a13172e0d7258f024310b3a.jpg)

# Where:

IOUT_CC is the set constant output current,   
VREF is the internal reference voltage, 1.244 V typically,   
RCC is the resistor connected at the CC pin,   
K is the coefficient between the output current and the internal built current signal, K = 100,000.

If the load current is higher than the CC setting, the output voltage drops. A balance can be achieved if the load decreases and matches the CC current before VOUT is pulled below input voltage. In the balance status, the TPS6123x can keep CC operation, output the constant current, and maintain the output voltage at the balanced level. If the output voltage is pulled below the input voltage by a strong load before the balance is achieved, the device exits CC operation and enters into start-up process, where the output current is limited by ILIM_pre instead of the CC value. If the load is still higher than ILIM_pre, the device will be stuck in the pre-charge phase; otherwise, the device can complete the pre-charge phase, but its output voltage will be pulled down again in the switching phase due to the limited output current, so an oscillation may happen.

In order to avoid the potential oscillation, the CC operation is only recommended for pure resistive loads or load devices with dynamic power management function. For a resistive load, its resistance should be higher than VIN / IOUT_CC; for a load device with dynamic power management function, which can regulate its input voltage to a set value, a higher set voltage than VIN of the TPS6123x is suggested. By doing this, a balance can be achieved before the output voltage is pulled below the input voltage, so to avoid the TPS6123x entering into the startup process.

For effective CC operation, a capacitor must be connected in parallel with RCC at CC pin, and the CC value should be set lower than the maximum output capability of the converter; otherwise, the TPS6123x will trigger the over current protection first and fail to regulate the output current. Refer to the Over Current Protection section for details.

The CC operation can be disabled by shorting the CC pin to ground. By doing so, the CC loop is disabled, so the TPS6123x works as a normal boost converter to regulate the output voltage, and its maximum output current capability is decided by the internal current limit.

# 8.3.5 Over Current Protection

To protect the device from over load condition, an internal cycle-by-cycle current limit is implemented. Once the inductor valley current reaches the internal current limit, the protection is triggered and it clamps the valley current at the limit ILIM until next cycle comes.

Figure 15 illustrates the valley current limit scheme. The average of the rectifier ripple current equals the output current, IOUT(DC). When the load current increases, the loop increases the valley current accordingly. If the valley current is increased above ILIM, the off-time will be extended until the valley drops to ILIM. Then the next cycle begins.

# Feature Description (continued)

![](images/64558fb87dae5974d66fe5cffb05cc6fd02b5c79659c0bb26fe88ea544a3e565.jpg)  
Figure 15. Current Limit Operation

The maximum output current, IOUT_MAX, before the device enters into over current protection is decided by its operation condition and the switch current limit threshold. It can be calculated by using the following equations.

)2II 1( I()D LOUT _ MAX LIM '  ò    
INL V DI ò' swfL ò   
D 1  INV Kò OUTV

Where:

D is the duty cycle of the boost converter,   
ILIM is the switch valley current limit threshold,   
ΔIL is the inductor current ripple,   
L is the inductor value,   
fSW is the switching frequency,   
η is the conversion efficiency under the operation condition.

To estimate the maximum output current capability in the worst case, the minimum input voltage value, highest fSW value, and minimum ILIM value should be used for the calculation. And η should be the efficiency under this minimum VIN operation condition.

When the current limit is reached, the output voltage decreases during further load increases. If the output voltage drops below the input voltage, the device enters into the start-up process.

# 8.3.6 Load Status Indication

The TPS6123x can indicate load status by the INACT pin. The INACT pin is an open drain output and should be connected to a pull-up resistor. The INACT pin outputs high impedance when the boost converter works under inactive status (no load or light load status), and it outputs low logic when the boost converter works under active status (moderate load or heavy load status).

# Feature Description (continued)

Load status is defined by operation mode and output current. When the converter works in PFM mode with IOUT lower than the threshold IINACT_th for 16 PFM cycles, the boost enters inactive status. One PFM cycle is defined from the time the boost starts switching to ramp up the output voltage to the time it resumes switching after the output voltage drops below the PFM threshold, as shown in Figure 14. Once the output current is detected higher than IINACT_th or the converter exits PFM mode, the boost enters active status. There is 10-ms typical deglitch time when the INACT pin changes its output.

This indication function can report load status to a system controller, like an MCU. For example, it can be used to realize the load insert detection in a power bank application, where the TPS6123x can be kept always on while consuming only 10-µA quiescent current. When a load is applied, the TPS6123x detects the load and pulls the INACT pin low to wake up the MCU. It eliminates the need for external load detection circuitry and simplifies the system design.

# 8.3.7 Under voltage Lockout

Under voltage lockout prevents operation of the device at input voltages below typical 2.1-V. When the input voltage is below the under voltage threshold, the device is shut down and the internal switch FETs are turned off. If the input voltage rises by under voltage lockout hysteresis, the IC restarts.

# 8.3.8 Over Voltage Protection and Reverse Current Block

When the device detects the output voltage above the threshold VOVP, the over voltage protection will be triggered. The device stops switching and turn off the low side switch and rectifying switch. The voltage at output is blocked to input, and there is no reverse current. When the output voltage falls below the OVP threshold, the device resumes normal operation.

# 8.3.9 Short Circuit Protection

If the output voltage is detected lower than the input voltage during operation, the TPS6123x will enter into the pre-charge phase of the startup process. The output current is limited to ILIM_pre by the rectifying switch, which is 0.25-A typical when VOUT is short to ground. When the short circuit event is removed, the TPS6123x will start up automatically.

Short circuit protection is only valid when the input voltage is below 4.5 V. If the input voltage is higher than 4.5 V, a long term short to ground event may damage the device.

# 8.3.10 Thermal Shutdown

The TPS6123x has a built-in temperature sensor which monitors the internal junction temperature, TJ. If the junction temperature exceeds the threshold (140°C typical), the device goes into thermal shutdown, and the highside and low-side MOSFETs are turned off. When the junction temperature falls below the thermal shutdown minus its hysteresis (15°C typical), the device resumes operation.

# 8.4 Device Functional Modes

# 8.4.1 PWM Mode

The TPS6123x boost converter operates at a quasi-constant 1-MHz frequency PWM mode at moderate to heavy load currents. Refer to the Boost Controller Operation section for details.

# 8.4.2 PFM Mode

The TPS6123x works in PFM mode under light load conditions to improve light load efficiency. Refer to the Boost Controller Operation section for details.

# 8.4.3 CV Mode and CC Mode

A resistor at the CC pin can program the maximum output current of the TPS6123x. Before the output current reaches the programmed value, the TPS6123x works in CV (Constant Voltage) mode as a normal boost converter. When the output current reaches the programmed value, the TPS6123x works in CC (Constant Current) mode. Refer to the Constant Output Voltage and Constant Output Current Operations section for details.

# 9 Applications and Implementation

# NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

# 9.1 Application Information

The TPS6123x family is designed to operate from an input voltage supply range from 2.3-V to (VOUT – 0.6)-V, and the maximum output voltage can be up to 5.5-V. The device operates in PWM mode under medium to heavy load conditions and in power save mode under light load condition. In PWM mode, the TPS6123x converter operates with 1-MHz switching frequency which provides a controlled frequency variation over the input voltage range. As load current decreases, the converter enters PFM mode, reducing switching frequency and minimizing IC quiescent current to achieve high efficiency over the entire load current range. The TPS6123x also supports a constant current output feature to limit the maximum output current at a programmed value.

# 9.2 Typical Applications

# 9.2.1 TPS61236P 3-V to 4.35-V Input, 5-V Output Voltage, 3-A Maximum Output Current

This example illustrates how to use the TPS61236P to generate a 5-V output voltage from a Li-ion battery input and how to use the CC function to limit maximum output current to 3-A for the entire input voltage range.

![](images/5c420978d5bd6cf5d418cdd6834dd1fd19cdaa7cda3ebbf2e43ef895657f2960.jpg)  
Figure 16. TPS61236P 5-V Output with 3-A Constant Output Current

# 9.2.1.1 Design Requirements

The design parameters for the TPS61236P 5-V 3-A constant output current design are listed in Table 1.

Table 1. TPS61236P 5-V 3-A Constant Output Current Design Parameters   

<table><tr><td rowspan=1 colspan=1>DESIGN PARAMETERS</td><td rowspan=1 colspan=1>EXAMPLE VALUES</td></tr><tr><td rowspan=1 colspan=1>Input voltage range</td><td rowspan=1 colspan=1>3 V to 4.35V</td></tr><tr><td rowspan=1 colspan=1>Output voltage</td><td rowspan=1 colspan=1>5V</td></tr><tr><td rowspan=1 colspan=1>Output current limit</td><td rowspan=1 colspan=1>3A</td></tr><tr><td rowspan=1 colspan=1>Operating frequency</td><td rowspan=1 colspan=1>1 MHz</td></tr></table>

# 9.2.1.2 Detailed Design Procedure

The following sections describe the selection process of the external components. The following table summaries the final component selections.

Table 2. List of Components for TPS61236P 5-V Output with 3-A Constant Output Current Application   

<table><tr><td rowspan=1 colspan=1>REFERENCE</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>MANUFACTURER(1)</td></tr><tr><td rowspan=1 colspan=1>L1</td><td rowspan=1 colspan=1>1.0 μH, Power Inductor, XAL7030</td><td rowspan=1 colspan=1>Coilcrat</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=1>10 μF 6.3 V, 0603, X5R ceramic, GRM188R60J106ME84</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>$C2$</td><td rowspan=1 colspan=1>3 × 22 μF 10 V, 0805, X5R ceramic, GRM21BR61A226ME44</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C3</td><td rowspan=1 colspan=1>10 nF, 50 V, 0603, X5R ceramic, GRM188R61H103KA01D</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C4</td><td rowspan=1 colspan=1>1 μF, 6.3 V, 0402, X5R ceramic, GRM152R60J105ME15</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>R1</td><td rowspan=1 colspan=1>1 MΩ, Resistor, Chip, 1/10W, 1%</td><td rowspan=1 colspan=1>Rohm</td></tr><tr><td rowspan=1 colspan=1>R2</td><td rowspan=1 colspan=1>332 kΩ, Resistor, Chip, 1/10W, 0.5%</td><td rowspan=1 colspan=1>Rohm</td></tr><tr><td rowspan=1 colspan=1>R3</td><td rowspan=1 colspan=1>41.2 kΩ, Resistor, Chip, 1/10W, 0.5%</td><td rowspan=1 colspan=1>Rohm</td></tr><tr><td rowspan=1 colspan=1>R4</td><td rowspan=1 colspan=1>1 MΩ, Resistor, Chip, 1/10W, 1%</td><td rowspan=1 colspan=1>Rohm</td></tr><tr><td rowspan=1 colspan=1>R5</td><td rowspan=1 colspan=1>1 MΩ, Resistor, Chip, 1/10W, 1%</td><td rowspan=1 colspan=1>Rohm</td></tr></table>

# (1) See Third-party Products Disclaimer

# 9.2.1.2.1 Programming the Output Voltage

The TPS61236P's output voltage needs to be programmed via an external voltage divider at the FB pin, as shown in Figure 16.

By selecting R1 and R2, the output voltage is programmed to the desired value. When the output voltage is regulated, the typical voltage at the FB pin is VFB. The following equation can be used to calculate R1 and R2.

![](images/a4d7eb323f29e70077548d454166223d406b1e4755afbba0b4f2fe9297bc8dd2.jpg)

For the best accuracy, the current following through R2 should be 100 times larger than FB pin leakage current. Changing R2 towards a lower value increases the robustness against noise injection. Changing R2 towards higher values reduces the FB divider current for achieving the highest efficiency at low load currents.

For the fixed output voltage version, TPS61235P, the FB pin must be tied to the output directly.

In this example, 1-MΩ and 332-kΩ resistors are selected for R1 and R2. High accuracy like 0.5% resistors are recommended for better output voltage accuracy.

# 9.2.1.2.2 Program the Constant Output Current

The TPS6123x's constant output current can be programmed via an external resistor RCC at the CC pin.

Because the TPS6123x has an internal current limit function to protect the IC from over load situations, a user should make sure the constant output current is set within the device's maximum load capability. If the constant current is set too high, the output current will be limited by internal protection circuitry and cannot reach the set value.

The maximum output capability is determined by the input to output voltage ratio and the internal current limit ILIM. Refer to Equation 3, Equation 4, and Equation 5 for the maximum output current calculation. The minimum input voltage, minimum current limit value, and maximum switching frequency value shall be used for the worst case calculation.

In this example, the minimum input voltage is 3-V and output voltage is 5-V. The efficiency η can be estimated as 85% for the worst case condition. By checking the specification table, the minimum ILIM value is 6.5-A, and maximum switching frequency fSW is 1250-kHz, so the calculation result of the maximum output current under the worse case condition is 3.6-A.

After calculation, the 3-A constant current target is within the maximum output current range, so the user can set it. Equation 2 can be used to select RCC (R3 in Figure 16). In this example, the calculation result of R3 is 41.47- kΩ. A 1% accuracy 41.2-kΩ resistor is selected. By using it, the constant output current can be regulated at 3-A typically.

C3 must be connected in parallel with R3 to average the CC pin voltage and also stabilize the control loop. A larger capacitor can smooth the CC voltage better, and also slow down the loop response. Normally a 10-nF capacitor is recommended.

If the Constant Current function is not needed, the user can simply connect the CC pin to ground to disable it. Under this configuration, the TPS6123x works as a normal boost converter, and its maximum output current is decided by the internal current limit circuitry.

# 9.2.1.2.3 Inductor and Capacitor Selection

A boost converter requires two main passive components for storing energy during the conversion, an inductor and an output capacitor. Please refer to the following sections to select the inductor and capacitor. Also refer to the Recommended Operating Conditions for operation recommendations.

# 9.2.1.2.3.1 Inductor Selection

Because a 1-µH inductor normally has a higher current rating and smaller form factor than inductors of higher values, the TPS6123x is optimized for 1-µH inductor operation. Inductors of other values may cause control loop instability and so are not recommended.

It is advisable to select an inductor with a saturation current ISAT higher than the possible peak current flowing through the inductor. The inductor's current rating IRMS should be higher than the average input current. The inductor peak current varies as a function of the load, the input and output voltages, and can be estimated by using Equation 7.

![](images/c67c36a9d7dfcb919ace6344f0d8c32c70f2317214a953a4d8070061acf3da96.jpg)

Where:

D is the duty cycle, and can be calculated by using Equation 5.

When estimating inductor peak current and average input current, the minimum input voltage, maximum output current, and minimum switching frequency in the application should be used for the worst case calculation. In this example, the minimum VIN is 3.0-V, maximum IOUT is 3-A, and minimum fsw is 750-kHz, so the inductor peak current result is 6.9-A, and the average input current is 5.9-A with an 85% efficiency estimation.

Selecting an inductor with insufficient saturation current can lead to excessive peak current in the converter. This could eventually harm the device and reduce reliability. To leave enough margin, it is recommended to choose saturation current 20% to 30% higher than IL_PEAK.

The following inductors are recommended to be used in designs if the current rating allows.

Table 3. List of Inductors   

<table><tr><td rowspan=1 colspan=1>INDUCTANCE [μH]</td><td rowspan=1 colspan=1>ISAT [A]</td><td rowspan=1 colspan=1>IRMS [A]</td><td rowspan=1 colspan=1>DC RESISTANCE [mΩ]</td><td rowspan=1 colspan=1>PART NUMBER</td><td rowspan=1 colspan=1>MANUFACTURER(1)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>21.8</td><td rowspan=1 colspan=1>4.55</td><td rowspan=1 colspan=1>XAL7030-102ME</td><td rowspan=1 colspan=1>Coilcraft</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>14.1</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>7.1</td><td rowspan=1 colspan=1>SPM6530T-1R0M120</td><td rowspan=1 colspan=1>TDK</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>FDSD0630-H-1R0M</td><td rowspan=1 colspan=1>TOKO</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>SPM5020T-1R0M</td><td rowspan=1 colspan=1>TDK</td></tr></table>

# (1) See Third-party Products Disclaimer

# 9.2.1.2.3.2 Output Capacitor Selection

For the output capacitor, it is recommended to use small X5R or X7R ceramic capacitors placed as close as possible to the VOUT and PGND pins of the IC. If, for any reason, the application requires the use of large capacitors which cannot be placed close to the IC, using a smaller ceramic capacitor of 1-µF or 0.1-µF in parallel to the large one is highly recommended. This small capacitor should be placed as close as possible to the VOUT and PGND pins of the IC.

The TPS6123x requires at least 20-µF effective capacitance at output for stability consideration. Care must be taken when evaluating a capacitor’s derating under bias. The bias can significantly reduce the effective capacitance. Ceramic capacitors can have losses of as much as 50% of their capacitance at rated voltage. Therefore, leave margin on the voltage rating to ensure adequate effective capacitance. In this example, three 22-µF capacitors of 10-V rating are used.

The ESR impact on the output ripple must be considered as well if tantalum or electrolytic capacitors are used. Assuming there is enough capacitance such that the ripple due to the capacitance can be ignored, the ESR needed to limit the VRipple is:

VRipple(ESR) = I (L PEAK) ´ ESR

# 9.2.1.2.3.3 Input Capacitor Selection

Multilayer X5R or X7R ceramic capacitors are an excellent choice for input decoupling of the step-up converter as they have extremely low ESR and are available in small footprints. Input capacitors should be located as close as possible to the device. The required minimum effective capacitance at input for the TPS6123x is 4.7-µF. Considering the capacitor’s derating under bias, a 10-µF input capacitor is recommended, and a 22-μF input capacitor should be sufficient for most applications. There is no limitation to use larger capacitors. It is recommended to put the input capacitor close to the VIN and PGND pins of the IC. If, for any reason, the input capacitor cannot be placed close to the IC, putting a small ceramic capacitor of 1-µF or 0.1-µF close to the IC's VIN pin and ground pin is recommended.

Take care when a ceramic capacitor is used at the input and the power is being supplied through long wires, such as from a wall adapter. A load step at the output may cause ringing at the VIN pin due to the inductance of the long wires. This ringing can couple to the output and be mistaken as loop instability or could even damage the part. Additional bulk capacitance (electrolytic or tantalum) should in this circumstance be placed between CIN and the power source to reduce ringing.

# 9.2.1.2.4 Loop Stability, Feed Forward Capacitor

One approach of stability evaluation is to look from a steady-state perspective at the following signals:

Switching node, SW Inductor current, IL Output ripple, VRipple(OUT)

When the switching waveform shows large duty cycle jitter or the output voltage or inductor current shows oscillations, the regulation loop may be unstable. This is often a result of board layout and/or L-C combination.

Load transient response is another approach to check loop stability. During the load transient recovery time, VOUT can be monitored for settling time, overshoot, or ringing that helps judge the converter’s stability. Without any ringing, the loop has usually more than 45° of phase margin.

To improve output voltage undershoot and overshoot performance during heavy load transient such as a 2-A load step transient, a feed forward capacitor Cff in parallel with R1 is recommended, as shown in Figure 17. The feed forward capacitor increases the loop bandwidth by adding a zero, so to achieve smaller output voltage undershoot, as shown in Figure 25. A 10-pF capacitor is suitable for most applications of the TPS6123x. See Application Note SLVA289 for more application notes of feed forward capacitor.

![](images/9845d5384a17f5b8e589f98626ca854059c6882d4727bf8aab250e13471155db.jpg)  
Figure 17. TPS61236P with Cff

# 9.2.1.2.5 INACT Pin Pull-up Resistor

The INACT pin can be used to report boost converter loading status to the MCU. It is an open drain output and should be connected with a pull up resistor. Normally a 1-MΩ resistor is recommended for the pull up resistor.

![](images/68a787f8d5cea0f452e17f8fdd799b3e67ad02452287fe09c3174b62e8cd4e9d.jpg)  
9.2.1.3 TPS61236P 5-V Output Application Curves

VIN = 3.6 V, VOUT = 5 V, IOUT = 3.1 A

![](images/8c7ea6a7b234cfeff6f374c8fdbae3d44c1d6bf3cb5a16302691e9867cf6bb8d.jpg)

![](images/4a5cd06e361c7838dc972a241e18f7cedc9fdfd1807e8252adfa1a37c843c2b3.jpg)

![](images/3309065033082e70e8a0cdda377917d46bb89d703bf8aa498071a97563d2c17e.jpg)  
Figure 18. Switching Waveforms in PWM Mode

VIN = 3.6 V, VOUT = 5 V, IOUT = 0 mA

![](images/f48aa216da351e56f189a28e24a7a496d6a1abc58291d451dc6ed7e88eaf69f6.jpg)  
Figure 19. Switching Waveforms in PFM Mode   
VIN = 3.6 V, VOUT = 5 V, RL = 2.5 Ω

![](images/cce5daa178bdf3f2134c5c999bace225ebbefc6b1386c560cf5d12a4ad69e938.jpg)  
Figure 20. Switching Waveforms in PFM Mode   
VIN = 3.6 V, VOUT = 5 V, RL = 2.5 Ω

![](images/526a50dd638bca955635791f6b79110da9dc28db055c26ca6b72aef8fa7d3fca.jpg)  
Figure 21. Startup   
Figure 22. Shutdown Waveforms   
Figure 23. Load Transient Response

VIN = 3.6 V, VOUT = 5 V, IOUT = 500 mA to 2 A

![](images/ba23ab03d9239a4f5d33507cf4bed30f2249f3d2f10990bc14e32cc7bb8d06a4.jpg)

VIN = 2.8 V to 3.3 V, VOUT = 5 V, IOUT = 2 A

![](images/1e96a8cfbfb746c47f8256bc2c7fe20ffd9b16e958439011ad989c71278664a5.jpg)  
VIN = 3.6 V, VOUT = 5 V, IOUT = 500 mA to 2 A, Cff = 10 pF

![](images/81f1f83db9097e0a54f46f79b881839c407fcc1f695aaf69a9f1c7cab2f20837.jpg)  
Figure 24. Line Transient Response   
VIN = 2.8 V to 3.3 V, VOUT = 5 V, IOUT = 2 A, Cff = 10 pF

![](images/658a0ae74d0f8973103524514c0ef42d614ddfefb08a95f0611bd9b27a4b2672.jpg)  
Figure 25. Load Transient Response with Cff   
VIN = 3.6 V, VOUT = 5.1 V, RCC = 41.2 kΩ, RL = 2.5 Ω to 1.5 Ω

![](images/6b9d71a695aa5948df17970f765c38c9871dc024f67b77780e836ebe5215011b.jpg)  
Figure 26. Line Transient Response with Cff   
Figure 28. Load Sweep

VIN = 3.6 V, VOUT = 5 V, CC = 3.0 A, IOUT from 0 mA to 3 A

![](images/f2c462efbe46e89637a2705b8341e73b0c46a3d995c854f669bef40cc145e11d.jpg)  
Figure 27. Constant Current Response   
Figure 29. CC Pin Voltage vs Output Current with Different Inputs

![](images/ef31542889cec8608ebcb3e47c8c879a0e1df53308e91e4c16b105c256fb714f.jpg)

![](images/927ede32a2762ae1a238406698a0a4b9c33276ce446cc1841c19f7e80edb6768.jpg)

![](images/230b402e9ca84d67ae63016f8ea95f4401a4bb08e826ff47fc406d4e0239fc75.jpg)  
Figure 30. CC Pin Voltage vs Output Current with Different Ambient Temperatures   
Figure 31. CC Pin Voltage vs Output Current with Different Inputs   
Figure 32. CC Pin Voltage vs Output Current with Different Ambient Temperatures

# 9.2.2 TPS61236P 2.3-V to 5-V Input, 5-V 2-A Output Converter

In this application, the TPS6123x is required to be used as a standard boost converter to output 5-V voltage and maximum 2-A current. The Constant Current function should be disabled, and the INACT function is not needed either.

![](images/6d1fa15bc9acc57bd2ef20f1165ff147d32f2bd4f1e0530c5310adeee795759f.jpg)  
Figure 33. TPS61236P 5-V 2-A Output Typical Application

# 9.2.2.1 Design Requirements

The design parameters for the TPS61236P 5-V output current design are listed in Table 4.

Table 4. TPS61236P 5-V Output Design Parameters   

<table><tr><td rowspan=1 colspan=1>DESIGN PARAMETERS</td><td rowspan=1 colspan=1>EXAMPLE VALUES</td></tr><tr><td rowspan=1 colspan=1>Input voltage range</td><td rowspan=1 colspan=1>2.3 V to 4.4 V</td></tr><tr><td rowspan=1 colspan=1>Output voltage</td><td rowspan=1 colspan=1>5V</td></tr><tr><td rowspan=1 colspan=1>Output current rating</td><td rowspan=1 colspan=1>2A</td></tr><tr><td rowspan=1 colspan=1>Operating frequency</td><td rowspan=1 colspan=1>1 MHz</td></tr></table>

# 9.2.2.2 Detailed Design Procedure

Refer to the Detailed Design Procedure section for the detailed design steps.

Because the CC function and the INACT function are not needed, the user can simply connect the two pins to ground to disable the functions as shown in Figure 33.

![](images/a57af265a8a09fed9733255d92bf8b81192ef4aec7f8c0a2322c76184d597e3d.jpg)  
9.2.2.3 TPS61236P 5-V Output Application Curves

![](images/631bc30e054c7f40a0e410da3a4868be0cd775ee468924e85c5a1fe3720c3e2d.jpg)  
Figure 34. Maximum Load Capability after Startup

![](images/3a77f61182b094049fc4ca1b758e1b5e73d02b313ab448b4fd7cabdd260b0243.jpg)  
Figure 35. Load Regulation

![](images/c93e60176961bef8e8adcadaa3ced390e55737b5259c4bbf4207e163607806bb.jpg)  
Figure 37. Load Regulation

![](images/af4b5e84dfb058a9c6a59d985aa34e6c50b2b1733c018688a8e244a4c13d5166.jpg)  
Figure 36. Load Regulation   
Figure 38. Load Sweep

# 10 Power Supply Recommendations

The device is designed to operate from an input voltage supply range between 2.3-V and (VOUT – 0.6)-V. This input supply must be well regulated. If the input supply is located more than a few inches from the converter, additional bulk capacitance may be required in addition to the ceramic bypass capacitors. An electrolytic or tantalum capacitor with a value of 47-μF is a typical choice in this circumstance.

# 11 Layout

# 11.1 Layout Guidelines

For all switching power supplies, layout is an important step in the design, especially at high peak currents and high switching frequencies. If the layout is not carefully done, the regulator could show stability problems as well as EMI problems. Therefore, use wide and short traces for the main current paths and the power ground tracks. The input capacitor, output capacitor, and the inductor should be placed as close as possible to the IC. Use a common ground node for power ground and a different one for control/analog ground to minimize the effects of ground noise. Connect these ground nodes near the ground pins of the IC. The most critical current path for all boost converters is from the switching FET, through the synchronous FET, the output capacitors, and back to the ground of the switching FET. Therefore, the output capacitors and their traces should be placed on the same board layer as the IC and as close as possible between the VOUT and PGND pins of the IC.

See Figure 39 for the recommended layout.

# 11.2 Layout Example

The bottom layer is a large GND plane connected by vias.

![](images/f9f276b601b270fa90b9aef735be068b28fc13322123dea582f18f5d7f19b48b.jpg)  
Figure 39. Layout Recommendation

# 11.3 Thermal Considerations

The maximum IC junction temperature should be restricted to 125°C under normal operating conditions. Calculate the maximum allowable dissipation, PD(max), and keep the actual power dissipation less than or equal to PD(max). The maximum power dissipation limit is determined using:

![](images/02501175bf9df75029072753c9ee827801fb8d659379d8b22019edbb03dc1972.jpg)

Where:

TA is the maximum ambient temperature for the application.

RθJA is the junction-to-ambient thermal resistance given in the Thermal Information table.

The TPS6123x handles high power conversion so requires special attention to the power dissipation. The junction-to-ambient thermal resistance of a package in an application greatly depends on the PCB type and layout, and many system-dependent factors such as thermal coupling, airflow, added heat sinks and convection surfaces, and the presence of other heat-generating components also affect the power-dissipation limits.

Two common basic approaches to enhancing thermal performance are listed below.

Increase the power dissipation capability of the PCB. It is necessary to have sufficient copper area as heat sinks. For DC voltage nodes like VIN, VOUT, and PGND, make the copper area as large as possible. Multiple vias are helpful in further reducing thermal stress. It is also a good practice to have thick copper layers in order to minimize the PCB conduction loss and thermal impedance.   
Introduce airflow in the system.

For more details on how to use the thermal parameters in the Thermal Information table, check the Thermal Characteristics Application Note (SZZA017) and the IC Package Thermal Metrics Application Note (SPRA953).

# 12 Device and Documentation Support

# 12.1 Device Support

# 12.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

# 12.2 Documentation Support

# 12.2.1 Related Documentation

For related documentation see the following:

Optimizing Transient Response of Internally Compensated dc-dc Converters With Feedforward Capacitor   
Application Report (SLVA289)   
Thermal Characteristics of Linear and Logic Packages Using JEDEC PCB Designs Application Report   
(SZZA017)   
Semiconductor and IC Package Thermal Metrics Application Report (SPRA953)

# 12.3 Related Links

The table below lists quick access links. Categories include technical documents, support and community resources, tools and software, and quick access to sample or buy.

Table 5. Related Links   

<table><tr><td rowspan=1 colspan=1>PARTS</td><td rowspan=1 colspan=1>PRODUCT FOLDER</td><td rowspan=1 colspan=1>SAMPLE &amp; BUY</td><td rowspan=1 colspan=1>TECHNICALDOCUMENTS</td><td rowspan=1 colspan=1>TOOLS&amp;SOFTWARE</td><td rowspan=1 colspan=1>SUPPORT &amp;COMMUNITY</td></tr><tr><td rowspan=1 colspan=1>TPS61235P</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td></tr><tr><td rowspan=1 colspan=1>TPS61236P</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td><td rowspan=1 colspan=1>Click here</td></tr></table>

# 12.4 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on Alert me to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

# 12.5 Community Resources

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

TI E2E™ Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.

Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and contact information for technical support.

# 12.6 Trademarks

E2E is a trademark of Texas Instruments.   
All other trademarks are the property of their respective owners.

# 12.7 Electrostatic Discharge Caution

![](images/b3e75cd2777deb8121bc36276c5f85e0ed1f6530223edea871e6c67650f1cfcb.jpg)

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

# 12.8 Glossary

SLYZ022 — TI Glossary.

This glossary lists and explains terms, acronyms, and definitions.

# 13 Mechanical, Packaging, and Orderable Information

The following pages include mechanical packaging and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

# PACKAGING INFORMATION

<table><tr><td rowspan="2">Orderable Device</td><td rowspan="2">Status Package Type</td><td colspan="4">Package Pins Package Qty</td><td rowspan="2">Eco Plan</td><td rowspan="2">Lead/Ball Finish (6)</td><td rowspan="2">MSL Peak Temp (3)</td><td rowspan="2">Op Temp (°℃)</td><td rowspan="2">Device Marking (4/5)</td><td rowspan="2">Samples</td></tr><tr><td>(1)</td><td>Drawing</td><td></td><td>(2) Green (RoHS</td></tr><tr><td>TPS61235PRWLR</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWL</td><td>9</td><td>3000</td><td>&amp; no Sb/Br)</td><td>CU NIPDAU CU NIPDAU</td><td>Level-1-260C-UNLIM</td><td>-40 to 85</td><td>ZGEI</td><td>Samples</td></tr><tr><td>TPS61235PRWLT</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWL</td><td>9</td><td>250</td><td>Green (RoHS &amp; no Sb/Br)</td><td>Level-1-260C-UNLIM</td><td>-40 to 85</td><td>ZGEI</td><td></td><td>Samples</td></tr><tr><td>TPS61236PRWLR</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWL</td><td>9</td><td>3000</td><td>Green (RoHS &amp; no Sb/Br)</td><td>CU NIPDAU</td><td>Level-1-260C-UNLIM</td><td>-40 to 85</td><td>ZGFI</td><td>Samples</td></tr><tr><td>TPS61236PRWLT</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWL</td><td>9</td><td>250</td><td>Green (RoHS &amp;no Sb/Br)</td><td>CU NIPDAU</td><td>Level-1-260C-UNLIM</td><td>-40 to 85 ZGFI</td><td></td><td>Samples</td></tr></table>

(1) The marketing status values are defined as follows: ACTIVE: Product device recommended for new designs. LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect. NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design. PREVIEW: Device has been announced but is not in production. Samples may or may not be available. OBSOLETE: TI h oti of tho

(2) Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS & no Sb/Br) - please check http://www.ti.com/productcontent for the latest availabilityinformation and additional product content details.

TBD: The Pb-Free/Green conversion plan has not been defined.

Pb-Free (RoHS): TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS requirements for all 6 substances, including the requirement that lead not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified lead-free processes. Pb-Free (RoHS Exempt): This component has a RoHS exemption for either 1) lead-based flip-chip solder bumps used between the die and package, or 2) lead-based die adhesive used between the die and leadframe. The component is otherwise considered Pb-Free (RoHS compatible) as defined above.

Green (RoHS & no Sb/Br): TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb) based flame retardants (Br or Sb do not exceed 0.1% by weight in homogeneous material)

(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

(5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "\~" will appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device Marking for that device.

(6) Lead/Ball Finish - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead/Ball Finish values may wrap to two lines if the finish value exceeds the maximum column width.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# TAPE AND REEL INFORMATION

![](images/99f7d8b533bde0f09ab142d03c5f35ee87ecc99bdeaf88c4213c1f58b9c95c08.jpg)

![](images/40a02343d10819e4ba2f6fe1ccf93c9e84f039125bbd471581af7845f3edf7cc.jpg)

<table><tr><td rowspan=1 colspan=1>AO</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component width</td></tr><tr><td rowspan=1 colspan=1>B0</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component length</td></tr><tr><td rowspan=1 colspan=1>KO</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component thickness</td></tr><tr><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>Overall width of the carrier tape</td></tr><tr><td rowspan=1 colspan=1>P1</td><td rowspan=1 colspan=1>Pitch between successive cavity centers</td></tr></table>

# QUADRANT ASSIGnMENTs FOR PIN 1 ORIEnTATION IN TAPE

![](images/e8d8f22d440d62bb5e1648050816f8d111c36c2be6f606e45901004351d26986.jpg)

\*All dimensions are nominal   

<table><tr><td rowspan=1 colspan=1>Device</td><td rowspan=1 colspan=1>PackageType</td><td rowspan=1 colspan=1>PackageDrawing</td><td rowspan=1 colspan=1>Pins</td><td rowspan=1 colspan=1>SPQ</td><td rowspan=1 colspan=1>ReelDiameter(mm)</td><td rowspan=1 colspan=1>ReelWidthW1 (mm)</td><td rowspan=1 colspan=1>A0(mm)</td><td rowspan=1 colspan=1>B0(mm)</td><td rowspan=1 colspan=1>K0(mm)</td><td rowspan=1 colspan=1>P1(mm)</td><td rowspan=1 colspan=1>W(mm)</td><td rowspan=1 colspan=1>Pin1Quadrant</td></tr><tr><td rowspan=1 colspan=1>TPS61235PRWLR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr><tr><td rowspan=1 colspan=1>TPS61235PRWLT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr><tr><td rowspan=1 colspan=1>TPS61236PRWLR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr><tr><td rowspan=1 colspan=1>TPS61236PRWLT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr></table>

![](images/1e6032ad1371580f020949e8951592650612d99bef8dca5d3fa444790b38e953.jpg)

\*All dimensions are nominal   

<table><tr><td rowspan=1 colspan=1>Device</td><td rowspan=1 colspan=1>Package Type</td><td rowspan=1 colspan=1>Package Drawing</td><td rowspan=1 colspan=1>Pins</td><td rowspan=1 colspan=1>SPQ</td><td rowspan=1 colspan=1>Length (mm)</td><td rowspan=1 colspan=1>Width (mm)</td><td rowspan=1 colspan=1>Height (mm)</td></tr><tr><td rowspan=1 colspan=1>TPS61235PRWLR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>20.0</td></tr><tr><td rowspan=1 colspan=1>TPS61235PRWLT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>20.0</td></tr><tr><td rowspan=1 colspan=1>TPS61236PRWLR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>20.0</td></tr><tr><td rowspan=1 colspan=1>TPS61236PRWLT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWL</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>182.0</td><td rowspan=1 colspan=1>20.0</td></tr></table>

QUAD FLAT PACK - NO LEAD

![](images/08cf85d70062632a804c2ea24b028c3481acad44e6a12c4f82770b500315d1d2.jpg)

4221609/A 08/2014

# NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.   
2. This drawing is subject to change without notice.

QUAD FLAT PACK - NO LEAD

![](images/359ad7e21fe0a751a017f321c1412df0f573ad02ed73ae6b097905bbb47aaab5.jpg)  
NOTES: (continued)

4221609/A 08/2014

3. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).

QUAD FLAT PACK - NO LEAD

![](images/c1f95cd7513ca2fd86d57e134de56cfef7bcbf0d6be6815739a400f3d5356126.jpg)  
NOTES: (continued)

4221609/A 08/2014

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

# IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, or other requirements. These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI’s products are provided subject to TI’s Terms of Sale (www.ti.com/legal/termsofsale.html) or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for TI products.