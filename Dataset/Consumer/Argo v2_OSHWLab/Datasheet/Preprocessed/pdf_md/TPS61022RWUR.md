# TPS61022 8-A Boost converter with 0.5-V ultra-low input voltage

# 1 Features

Input voltage range: 0.5 V to 5.5 V 1.8-V Minimum input voltage for start-up Output voltage setting range: 2.2 V to 5.5 V Two 12-mΩ (LS) / 18-mΩ (HS) MOSFETs 8-A Valley switching current limit   
94.7% Efficiency at VIN = 3.6 V, VOUT = 5 V and IOUT = 3 A 1-MHz Switching frequency when VIN > 1.5 V and 0.6-MHz switching frequency when VIN < 1 V ±2.5% Reference voltage accuracy over –40°C to +125°C Pin-selectable auto PFM operation mode or forced PWM operation mode at light load Pass-through mode when VIN > VOUT   
True disconnection between input and output during shutdown Output overvoltage and thermal shutdown protections Output short-circuit protection   
2-mm × 2-mm VQFN 7-pin package

# 3 Description

The TPS61022 provides a power supply solution for portable equipment and IoT devices powered by various batteries and super capacitors. The TPS61022 has minimum 6.5-A valley switch current limit over full temperature range. With a wide input voltage range of 0.5 V to 5.5 V, the TPS61022 supports supercapacitor backup power applications, which may deeply discharge the supercapacitor.

The TPS61022 operates at 1-MHz switching frequency when the input voltage is above 1.5 V. the switching frequency decreases gradually to 0.6 MHz when the input voltage is below 1.5 V down to 1 V. A MODE pin sets the TPS61022 operating either in power-save mode or forced PWM mode in light load condition. The TPS61022 only consumes a 26-µA quiescent current from VOUT in light load condition. During shutdown, the load is completely disconnected from the input power. The TPS61022 has 5.7-V output overvoltage protection, output short-circuit protection, and thermal shutdown protection.

The TPS61022 offers a very small solution size with its 2-mm × 2-mm VQFN package and minimum amount of external components.

# 2 Applications

USB port SuperCap backup GPRS power supply

Device Information(1)   

<table><tr><td rowspan=1 colspan=1>PART NUMBER</td><td rowspan=1 colspan=1>PACKAGE</td><td rowspan=1 colspan=1>BODY SIZE (NOM)</td></tr><tr><td rowspan=1 colspan=1>TPS61022</td><td rowspan=1 colspan=1>VQFN (7)</td><td rowspan=1 colspan=1>2.00 mm × 2.00 mm</td></tr></table>

(1) For all available packages, see the orderable addendum at the end of the data sheet.

# Typical Application Circuit

![](images/e46364f9fcca2b2456d4455a32d41b40639b004a934e6530d0dca9e9a67c3963.jpg)

# Layout Example

![](images/11cb1a0fc4180b942b6addc22b62f2b96de2b0e47b2c4fe501d10941c667c8cf.jpg)

Note: A ceramic output capacitor is needed and must be close to VOUT pin and GND pin of the TPS61022

# Table of Contents

# 1 Features..

# 5 Pin Configuration and Functions.. 3

# 6 Specifications.. 4

6.1 Absolute Maximum Ratings .. 4   
6.2 ESD Ratings.. 4   
6.3 Recommended Operating Conditions.. 4   
6.4 Thermal Information. 4   
6.5 Electrical Characteristics. 5   
6.6 Typical Characteristics .. 6

# 7 Detailed Description . 9

7.1 Overview . 9   
7.2 Functional Block Diagram .. 9   
7.3 Feature Description.. 10   
7.4 Device Functional Modes. 11

# 8 Application and Implementation 13

8.1 Application Information.. 13   
8.2 Typical Application . 13   
8.3 System Examples . 19

# 9 Power Supply Recommendations. 19

# 10 Layout.. 20

10.1 Layout Guidelines ... 20   
10.2 Layout Example . 20   
10.3 Thermal Considerations. 21

# 11 Device and Documentation Support .. 22

11.1 Device Support 22   
11.2 Receiving Notification of Documentation Updates 22   
11.3 Support Resources . 22   
11.4 Trademarks. 22   
11.5 Electrostatic Discharge Caution.. 22   
11.6 Glossary .. 22

# 12 Mechanical, Packaging, and Orderable

Information .. 22

# 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Revision A (March 2019) to Revision B

Added Layout Example image to front page

# Changes from Original (January 2019) to Revision A Page

First release of production-data data sheet ..

# 5 Pin Configuration and Functions

![](images/a36621b49bfc79767d9331fc9396400677ff25fdc631bab757b3648410383d51.jpg)

# Pin Functions

<table><tr><td rowspan=1 colspan=2>PIN</td><td rowspan=2 colspan=1>10</td><td rowspan=2 colspan=1>DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>NO.</td><td rowspan=1 colspan=1>NAME</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>Ground pin of the IC. The GND pad of output capacitor must be close to the GND pin.Layout example is shown in Figure 29.</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SW</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>The switch pin of the converter. It is connected to the drain of the internal low-side powerMOSFET and the source of the internal high-side power MOSFET.</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>VOUT</td><td rowspan=1 colspan=1>PWR</td><td rowspan=1 colspan=1>Boost converter output. The VOUT pad of output capacitor must be close to the VOUT pin.Layout example is shown in Figure 29.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>FB</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Voltage feedback of adjustable output voltage.</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>EN</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Enable logic input. Logic high voltage enables the device. Logic low voltage disables thedevice and turns it into shutdown mode.</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>MODE</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Operation mode selection in the light load condition. When it is connected to logic highvoltage, the device works in forced PWM mode. When it is connected to logic low voltage,the device works in auto PFM mode.</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>VIN</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>IC power supply input.</td></tr></table>

# 6 Specifications

# 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted)(1)

<table><tr><td></td><td></td><td>MIN</td><td>MAX</td><td>UNIT</td></tr><tr><td>Voltage range at terminals (2)</td><td>VIN, EN, FB, MODE, SW, VOUT</td><td>-0.3</td><td>7</td><td>V</td></tr><tr><td>Operating junction temperature, TJ</td><td></td><td>-40</td><td>150</td><td>℃</td></tr><tr><td>Storage temperature, Tstg</td><td></td><td>-65</td><td>150</td><td>℃</td></tr></table>

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.   
(2) All voltage values are with respect to network ground terminal.

# 6.2 ESD Ratings

<table><tr><td></td><td></td><td></td><td rowspan=1 colspan=1>VALUE</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=2 colspan=1>V(ESD)</td><td rowspan=2 colspan=1>Electrostatic discharge</td><td rowspan=1 colspan=1>Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)</td><td rowspan=1 colspan=1>±2000</td><td rowspan=2 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Charged-device model (CDM), per JEDEC specification JESD22-C101(2)</td><td rowspan=1 colspan=1>±500</td></tr></table>

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. Manufacturing with less than 500-V HBM is possible with the necessary precautions. Pins listed as ±2000 V may actually have higher performance.   
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. Manufacturing with less than 250-V CDM is possible with the necessary precautions. Pins listed as ±500 V may actually have higher performance.

# 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

<table><tr><td colspan="3"></td><td>MIN</td><td>NOM</td><td>MAX</td><td>UNIT</td></tr><tr><td rowspan="3">ViN</td><td rowspan="3">Input voltage range</td><td>Output voltage pre biased &lt; 0.7V before start- up</td><td>0.5</td><td></td><td>4.8</td><td>V</td></tr><tr><td>Output voltage pre biased &gt; 0.7V before start-</td><td>0.5</td><td></td><td>5.5</td><td>V</td></tr><tr><td>up</td><td>2.2</td><td></td><td>5.5</td><td>V</td></tr><tr><td>VoUT L</td><td>Output voltage setting range Effective inductance range</td><td></td><td>0.33</td><td>1.0</td><td>2.9</td><td>μH</td></tr><tr><td>CIN</td><td>Effective input capacitance range</td><td></td><td>4.7</td><td>10</td><td></td><td>μF</td></tr><tr><td rowspan="3">CouT</td><td rowspan="3">Effective output capacitance range</td><td>1oUT&gt;=3A</td><td>30</td><td>30</td><td>1000</td><td>μF</td></tr><tr><td>1.5A&lt; louT&lt; 3A</td><td>20</td><td>30</td><td>1000</td><td>μF</td></tr><tr><td>loUT &lt;=1.5A</td><td>10</td><td>30</td><td>1000</td><td></td></tr><tr><td>$Tf$</td><td>Operating junction temperature</td><td></td><td>-40</td><td></td><td>125</td><td>μF ℃</td></tr></table>

# 6.4 Thermal Information

<table><tr><td rowspan=3 colspan=2>THERMAL METRIC (1)</td><td rowspan=1 colspan=1>TPS61022</td><td rowspan=1 colspan=1>TPS61022</td><td rowspan=3 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>RWU (VQFN) - 7 PINS</td><td rowspan=1 colspan=1>RWU (VQFN) - 7 PINS</td></tr><tr><td rowspan=1 colspan=1>Standard</td><td rowspan=1 colspan=1>EVM(2)</td></tr><tr><td rowspan=1 colspan=1>RaJA</td><td rowspan=1 colspan=1>Junction-to-ambient thermal resistance</td><td rowspan=1 colspan=1>108.2</td><td rowspan=1 colspan=1>50.9</td><td rowspan=1 colspan=1>CW</td></tr><tr><td rowspan=1 colspan=1>RaJC</td><td rowspan=1 colspan=1>Junction-to-case thermal resistance</td><td rowspan=1 colspan=1>70.2</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>°CW</td></tr><tr><td rowspan=1 colspan=1>ROJB</td><td rowspan=1 colspan=1>Junction-to-board thermal resistance</td><td rowspan=1 colspan=1>37.1</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>°C/W</td></tr><tr><td rowspan=1 colspan=1>4JT</td><td rowspan=1 colspan=1>Junction-to-top characterization parameter</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>1.6</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>JB$</td><td rowspan=1 colspan=1>Junction-to-board characterization parameter</td><td rowspan=1 colspan=1>36.7</td><td rowspan=1 colspan=1>20.0</td><td rowspan=1 colspan=1>C/W</td></tr></table>

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report. (2) Measured on TPS61022EVM-034, 4-layer, 2oz copper 58mm×46mm PCB.

# 6.5 Electrical Characteristics

TJ = –40°C to 125°C, VIN = 3.6 V and VOUT = 5.0 V. Typical values are at TJ = 25°C (unless otherwise noted)   

<table><tr><td rowspan=1 colspan=2>PARAMETER</td><td rowspan=1 colspan=1>TEST CONDITIONS</td><td rowspan=1 colspan=1>MIN      TYP      MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=2>POWER SUPPLY</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ViN</td><td rowspan=1 colspan=1>Input voltage range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5                    5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>VIN_UWLO</td><td rowspan=2 colspan=1>Under-voltage lockout threshold</td><td rowspan=1 colspan=1>Vin rising</td><td rowspan=1 colspan=1>1.7       1.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vin fallingg</td><td rowspan=1 colspan=1>0.4       0.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>1Q</td><td rowspan=1 colspan=1>Quiescent current into VIN pin</td><td rowspan=1 colspan=1>IC enabled, No load, No switching ViN=1.8VtO5.5V, VFB = VREF + 0.1V, TJUPto85°℃</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Quiescent current into VOUT pin</td><td rowspan=1 colspan=1>IC enabled, No load, No switching VouT=2.2VtO5.5V,VFB=VREF+0.1V,TJup to 85℃</td><td rowspan=1 colspan=1>27        32</td><td rowspan=1 colspan=1>MA</td></tr><tr><td rowspan=2 colspan=1>IsD</td><td rowspan=2 colspan=1>Shutdown current into VIN and SW pin</td><td rowspan=1 colspan=1>IC disabled, ViN = 1.8V to5.5 V, Tj =25°℃</td><td rowspan=1 colspan=1>0.25       0.6</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>IC disabled, ViN = 1.8V to 5.5 V, TJ upto85°℃</td><td rowspan=1 colspan=1>0.25       3.0</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>OUTPUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VouT</td><td rowspan=1 colspan=1>Output voltage setting range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.2                    5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=2 colspan=1>VREF</td><td rowspan=2 colspan=1>Reference voltage at the FB pin</td><td rowspan=1 colspan=1>PWM mode</td><td rowspan=1 colspan=1>585       600       615</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>PFM mode</td><td rowspan=1 colspan=1>590       606</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>VOVP</td><td rowspan=1 colspan=1>Output over-voltage protection threshold</td><td rowspan=1 colspan=1>Vour rising</td><td rowspan=1 colspan=1>5.5       5.7       6.0</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOVP HYS</td><td rowspan=1 colspan=1>Over-voltage protection hysteresis</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>FB_LKG</td><td rowspan=1 colspan=1>Leakage current at FB pin</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>nA</td></tr><tr><td rowspan=1 colspan=1>IVOUT_LKG</td><td rowspan=1 colspan=1>Leakage current into VOUT pin</td><td rowspan=1 colspan=1>IC disabled, ViN=0V, Vsw =0V, VouT =5.5V,TJup to 85°C</td><td rowspan=1 colspan=1>1         3</td><td rowspan=1 colspan=1>MA</td></tr><tr><td rowspan=1 colspan=1>ts</td><td rowspan=1 colspan=1>Soft startup time</td><td rowspan=1 colspan=1>From active EN to VOUT regulation.ViN=2.5V, VOUT=5.0V,COUTEFF=30μF, IoUT = 0</td><td rowspan=1 colspan=1>700</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>POWER SWITCH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>RDs(on)</td><td rowspan=1 colspan=1>High-side MOSFET on resistance</td><td rowspan=1 colspan=1>VOUT = 5.0V</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>m2</td></tr><tr><td rowspan=1 colspan=1>Low-side MOSFET on resistance</td><td rowspan=1 colspan=1>VoUT = 5.0V</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>mΩ</td></tr><tr><td rowspan=2 colspan=1>fsw</td><td rowspan=2 colspan=1>Switching frequency</td><td rowspan=1 colspan=1>ViN = 3.6 V, VouT = 5.0 V, PWM mode</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>ViN = 1.0 V, VouT = 5.0 V, PWM mode</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>toFF_min</td><td rowspan=1 colspan=1>Minimum off time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>80       150</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>Lm sw</td><td rowspan=1 colspan=1>Valley current imit</td><td rowspan=1 colspan=1>ViN=3.6V, VoUT =5.0V</td><td rowspan=1 colspan=1>6.5         8        10</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>LIM CHG</td><td rowspan=1 colspan=1>Pre-charge current</td><td rowspan=1 colspan=1>ViN = 1.8 -4.8V, VouT &lt;0.4V</td><td rowspan=1 colspan=1>400       700</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>LIM CHG_max</td><td rowspan=1 colspan=1>Maximum pre-charge current</td><td rowspan=1 colspan=1>ViN = 2.4 V, VouT &gt;0.4V</td><td rowspan=1 colspan=1>2       2.4</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>LOGIC INTERFACE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VENH</td><td rowspan=1 colspan=1>EN logic high threshold</td><td rowspan=1 colspan=1>ViN&gt;1.8Vor VouT&gt;2.2 V</td><td rowspan=1 colspan=1>1.2</td><td rowspan=2 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VENL</td><td rowspan=1 colspan=1>EN logic low threshold</td><td rowspan=1 colspan=1>ViN &gt;1.8Vor VouT &gt;2.2 V</td><td rowspan=1 colspan=1>0.35      0.42      0.45</td></tr><tr><td rowspan=1 colspan=1>VMODE H</td><td rowspan=1 colspan=1>MODE logic high threshold</td><td rowspan=1 colspan=1>ViN &gt;1.8Vor VouT&gt;2.2V</td><td rowspan=1 colspan=1>1.2</td><td rowspan=2 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VMODEL</td><td rowspan=1 colspan=1>MODE logic low threshold</td><td rowspan=1 colspan=1>ViN &gt;1.8Vor VouT &gt;2.2 V</td><td rowspan=1 colspan=1>0.4</td></tr><tr><td rowspan=1 colspan=1>PROTECTION</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>TsD</td><td rowspan=1 colspan=1>Thermal shutdown threshold</td><td rowspan=1 colspan=1>Tu rising</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>TSD HYS</td><td rowspan=1 colspan=1>Thermal shutdown hysteresis</td><td rowspan=1 colspan=1>T falling below TsD</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>C</td></tr></table>

# 6.6 Typical Characteristics

VIN = 3.6 V, VOUT = 5 V, TJ = 25°C, unless otherwise noted

![](images/6720db2fb70948dfad854e94645c49683f4a4dde929e92ae38bae5865445b86e.jpg)

![](images/913202e7199720dd932d5d5168631aa8e5bd900242bc0f4f0f2760be182fa98a.jpg)

![](images/b763e8d04b72174a56126a072fd53e9ffdcaade824be233224b961cd20905245.jpg)  
Figure 1. Load Efficiency With Different Input in Auto PFM

![](images/2afdf80e5cdab912deaf4bb13522bae249945fc3bb330f8fbc663bc30936ce9e.jpg)  
Figure 3. Load Efficiency With Different Input in Forced PWM   
Figure 5. Load Regulation in Auto PFM

![](images/b6ff8abd6f2ebda34b1c3c0d75352b5bd17fa2b67a80303efb8013b32454c2c2.jpg)  
Figure 2. Load Efficiency With Different Output in Auto PFM

![](images/54f5dd5db2e3931fe04ee2c5b44156686c8468d67a201ed0ef992efa4da53b49.jpg)  
Figure 4. Load Efficiency With Different Output in Forced PWM   
Figure 6. Load Regulation in Forced PWM

# Typical Characteristics (continued)

V = 3.6 V, V = 5 V, T = 25°C, unless otherwise noted

![](images/63d049b70872bced11611ed0828afb0318d867a5373ba92af70f134e5fb0c5d8.jpg)

![](images/cbb7e0210ed30b8d3279d555108a6093d81d587b5d1ae0adb3dab05b0242b443.jpg)  
Figure 7. Pre-charge Current vs Output Voltage   
VIN = 1.8 V, 3.6 V 4.5 V; VOUT = 5 V, TJ = –40°C to +85°C, No switching

![](images/a23637ed2f2c7703867cb088ab74dc4890b8adf3a08459118c1c2ed6ac568fe3.jpg)  
Figure 9. Quiescent Current into VIN vs Temperature   
Figure 11. Shutdown Current vs Temperature

![](images/0b98bb8bd10a8c3b3d1fe5e81eace2f6dab072e31d532037881244b30ef300b8.jpg)

![](images/a1f80814bb91a202166b0adae200b9acb179b3c5f62e019b124305486481134a.jpg)  
Figure 8. Reference Voltage vs Temperature   
VIN = 1.8 V; VOUT = 2.2 V, 3.6 V, 5 V, TJ = –40°C to +85°C, No switching

![](images/44cf11fa5a907b6f8fa8a2cfbc6464f6096aa33a1c6f3c588ce4bdf4f4b8bcaa.jpg)  
Figure 10. Quiescent Current into VOUT vs Temperature   
Figure 12. Switching Frequency vs Input Voltage

# Typical Characteristics (continued)

V = 3.6 V, V = 5 V, T = 25°C, unless otherwise noted

![](images/81c6631bd861d8dc4097b9f3e5b530e5155fcfb1d37c3f86eeba2f75e2ada752.jpg)  
Figure 13. EN Rising Threshold vs Temperature

![](images/c5b30973d72069e59c36d61c8ad40a4be637bec8551715e3b5c408f90b9d866d.jpg)  
Figure 14. EN Falling Threshold vs Temperature

# 7 Detailed Description

# 7.1 Overview

The TPS61022 synchronous step-up converter is designed to operate from an input voltage supply range between 0.5 V and 5.5 V with 6.5-A (minimum) valley switch current limit. The TPS61022 typically operates at a quasi-constant frequency pulse width modulation (PWM) at moderate to heavy load currents. The switching frequency is 1 MHz when the input voltage is above 1.5 V. The switching frequency reduces down to 0.6 MHz gradually when the input voltage goes down from 1.5 V to 1 V and keeps at 0.6 MHz when the input voltage is below 1 V. The MODE pin sets the TPS61022 converter operating in power-save mode with pulse frequency modulation (PFM) or forced PWM mode in light load conditions. During PWM operation, the converter uses adaptive constant on-time valley current mode control scheme to achieve excellent line regulation and load regulation and allows the use of a small inductor and ceramic capacitors. Internal loop compensation simplifies the design process while minimizing the number of external components.

# 7.2 Functional Block Diagram

![](images/ce645b03fa864bbdc1c8816640e129e75c829973203e41ca360d8528f1311501.jpg)

# 7.3 Feature Description

# 7.3.1 Undervoltage Lockout

The TPS61022 has a built-in undervoltage lockout (UVLO) circuit to ensure the device working properly. When the input voltage is above the UVLO rising threshold of 1.8 V, the TPS61022 can be enabled to boost the output voltage. After the TPS61022 starts up and the output voltage is above 2.2 V, the TPS61022 works with input voltage as low as 0.5 V.

# 7.3.2 Enable and Soft Start

When the input voltage is above the UVLO rising threshold and the EN pin is pulled to a voltage above 1.2 V, the TPS61022 is enabled and starts up. At the beginning, the TPS61022 charges the output capacitors with a current of about 700 mA when the output voltage is below 0.4 V. When the output voltage is charged above 0.4 V, the output current is changed to having output current capability to drive 1-Ω resistance load. After the output voltage reaches the input voltage, the TPS61022 starts switching, and the output voltage ramps up further. The typical start-up time is 700 µs accounting from EN high to output reaching target voltage for the application with input voltage is 2.5 V, output voltage is 5 V, output effective capacitance is 30 µF and no load. When the voltage at the EN pin is below 0.4 V, the internal enable comparator turns the device into shutdown mode. In the shutdown mode, the device is entirely turned off. The output is disconnected from input power supply.

# 7.3.3 Switching Frequency

The TPS61022 switches at a quasi-constant 1-MHz frequency when the input voltage is above 1.5 V. When the input voltage is lower than 1.5 V, the switching frequency is reduced gradually to 0.6 MHz to improve the efficiency and get higher boost ratio. When the input voltage is below 1 V, the switching frequency is fixed at a quasi-constant 0.6 MHz.

# 7.3.4 Current Limit Operation

The TPS61022 uses a valley current limit sensing scheme. Current limit detection occurs during the off-time by sensing of the voltage drop across the synchronous rectifier.

When the load current is increased such that the inductor current is above the current limit within the whole switching cycle time, the off-time is increased to allow the inductor current to decrease to this threshold before the next on-time begins (so called frequency fold-back mechanism). When the current limit is reached, the output voltage decreases during further load increase.

The maximum continuous output current (IOUT(LC)), before entering current limit (CL) operation, can be defined by Equation 1.

![](images/03c5d9618c5d13c7c45b27e827938761ffec1a2deae89e9c737fcf2be3786be4.jpg)

where

• D is the duty cycle • ΔIL(P-P) is the inductor ripple current

The duty cycle can be estimated by Equation 2.

![](images/f3ce2ada8f4599ecd68c7ad3ee852784f0c9b3d9eed2d2b8776258bd1a9069e5.jpg)

# where

VOUT is the output voltage of the boost converter VIN is the input voltage of the boost converter η is the efficiency of the converter, use 90% for most applications

# Feature Description (continued)

The peak-to-peak inductor ripple current is calculated by Equation 3.

![](images/bce3cc5e55b4198664925aafeb1c0ff7f3e9cf555d232d63afc99de640265511.jpg)

# where

L is the inductance value of the inductor • fSW is the switching frequency D is the duty cycle VIN is the input voltage of the boost converter

# 7.3.5 Pass-Through Operation

When the input voltage is higher than the setting output voltage, the output voltage is higher than the target regulation voltage. When the output voltage is 101% of the setting target voltage, the TPS61022 stops switching and fully turns on the high-side PMOS FET. The device works in pass-through mode. The output voltage is the input voltage minus the voltage drop across the DCR of the inductor and the RDS(on) of the PMOS FET. When the output voltage drops below the 97% of the setting target voltage as the input voltage declines or the load current increases, the TPS61022 resumes switching again to regulate the output voltage.

# 7.3.6 Overvoltage Protection

The TPS61022 has an output overvoltage protection (OVP) to protect the device if the external feedback resistor divider is wrongly populated. When the output voltage is above 5.7 V typically, the device stops switching. Once the output voltage falls 0.1 V below the OVP threshold, the device resumes operating again.

# 7.3.7 Output Short-to-Ground Protection

The TPS61022 starts to limit the output current when the output voltage is below 1.8 V. The lower the output voltage reaches, the smaller the output current is. When the VOUT pin is short to ground, and the output voltage becomes less than 0.4 V, the output current is limited to approximate 700 mA. Once the short circuit is released, the TPS61022 goes through the soft start-up again to the regulated output voltage.

# 7.3.8 Thermal Shutdown

The TPS61022 goes into thermal shutdown once the junction temperature exceeds 150°C. When the junction temperature drops below the thermal shutdown recovery temperature, typically 130°C, the device starts operating again.

# 7.4 Device Functional Modes

The TPS61022 operates at a quasi-constant frequency pulse width modulation (PWM) in moderate-to heavy load condition. Based on the input voltage to output voltage ratio, a circuit predicts the required on-time of the switching cycle. At the beginning of each switching cycle, the low-side NMOS FET switch, shown in Functional Block Diagram, is turned on. The input voltage is applied across the inductor and the inductor current ramps up. In this phase, the output capacitor is discharged by the load current. When the on-time expires, the main switch NMOS FET is turned off, and the rectifier PMOS FET is turned on. The inductor transfers its stored energy to replenish the output capacitor and supply the load. The inductor current declines because the output voltage is higher than the input voltage. When the inductor current hits a value that is the error amplifier's output, the next switching cycle starts again. The error amplifier compares the feedback voltage of the output voltage with an internal reference voltage; its output determines the inductor valley current in every switching cycle.

In light load condition, the TPS61022 implements two operation modes (power-save mode with PFM and forced PWM mode) to meet different application requirements. The operation modes are set by the status of the MODE pin. When the MODE pin is connected to logic low, the device works in the PFM mode. When the MODE pin is connected to logic high, the device works in the forced PWM mode.

# Device Functional Modes (continued)

# 7.4.1 Forced PWM Mode

In the forced PWM mode, the TPS61022 keeps the switching frequency constant in light load condition. When the load current decreases, the output of the internal error amplifier decreases as well to keep the inductor current down and deliver less power from input to output. When the output current further reduces, the current through the inductor decreases to zero during the off-time. The high-side P-MOSFET is not turned off even if the current through the MOSFET is zero. Thus, the inductor current changes its direction after it runs to zero. The power flow is from output side to input side. The efficiency is low in this mode. But with the fixed switching frequency, there is no audible noise and other problems which might be caused by low switching frequency in light load condition.

# 7.4.2 Power-Save Mode

The TPS61022 integrates a power-save mode with PFM to improve efficiency at light load. When the load current decreases, the inductor valley current set by the output of the error amplifier no longer regulates the output voltage. When the inductor valley current hits the low limit of 150 mA, the output voltage exceeds the setting voltage as the load current decreases further. When the FB voltage hits the PFM reference voltage, the TPS61022 goes into the power-save mode. In the power-save mode, when the FB voltage rises and hits the PFM reference voltage, the device continues switching for several cycles because of the delay time of the internal comparator — then it stops switching. The load is supplied by the output capacitor, and the output voltage declines. When the FB voltage falls below the PFM reference voltage, after the delay time of the comparator, the device starts switching again to ramp up the output voltage.

![](images/5d2867917b293f1aaaeec8551fd757e1d42d8f4b9fb213da4299e315c94f5d92.jpg)  
Figure 15. Output Voltage in PWM Mode and PFM Mode

# 8 Application and Implementation

# NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

# 8.1 Application Information

The TPS61022 is a synchronous boost converter designed to operate from an input voltage supply range between 0.5 V and 5.5 V with a minimum 6.5-A valley switch current limit. The TPS61022 typically operates at a quasi-constant 1-MHz frequency PWM at moderate-to-heavy load currents when the input voltage is above 1.5 V. The switching frequency changes to 0.6 MHz gradually with the input voltage changing from 1.5 V to 1 V for better efficiency and high step-up ratio. When the input voltage is below 1 V, the switching frequency is fixed at a quasi-constant 0.6 MHz. At light load currents, when the MODE pin is set to low logic level, the TPS61022 converter operates in power-save mode with PFM to achieve high efficiency over the entire load current range. When the MODE pin is set to high logic level, the TPS61022 converter operates in forced PWM mode to keep the switching frequency constant.

# 8.2 Typical Application

The TPS61022 provides a power supply solution for portable devices powered by batteries or backup applications powered by super-capacitors. With minimum 6.5-A switch current capability, the TPS61022 can output 5 V and 3 A from a single-cell Li-ion battery.

![](images/d8386ab18f9ee7bafc22da1f09ccb7744ee2ce93a0861da60e9f61515c094f9a.jpg)  
Figure 16. Li-ion Battery to 5-V Boost Converter

# 8.2.1 Design Requirements

The design parameters are listed in Table 1.

Table 1. Design Parameters   

<table><tr><td rowspan=1 colspan=1>PARAMETERS</td><td rowspan=1 colspan=1>VALUES</td></tr><tr><td rowspan=1 colspan=1>Input voltage</td><td rowspan=1 colspan=1>2.7 V to 4.35 V</td></tr><tr><td rowspan=1 colspan=1>Output voltage</td><td rowspan=1 colspan=1>5V</td></tr><tr><td rowspan=1 colspan=1>Output current</td><td rowspan=1 colspan=1>3A</td></tr><tr><td rowspan=1 colspan=1>Output voltage ripple</td><td rowspan=1 colspan=1>±50 mV</td></tr></table>

# 8.2.2 Detailed Design Procedure

# 8.2.2.1 Setting the Output Voltage

The output voltage is set by an external resistor divider (R1, R2 in Figure 16). When the output voltage is regulated, the typical voltage at the FB pin is VREF. Thus the resistor divider is determined by Equation 4.

![](images/b89d484c66ad8eee293b3ac5bff8fc472ebbe838ef1a6e5effdee166114cf3c4.jpg)

# where

• VOUT is the regulated output voltage • VREF is the internal reference voltage at the FB pin

For best accuracy, keep R2 smaller than 300 kΩ to ensure the current flowing through R2 is at least 100 times larger than the FB pin leakage current. Changing R2 towards a lower value increases the immunity against noise injection. Changing the R2 towards a higher value reduces the quiescent current for achieving highest efficiency at low load currents.

# 8.2.2.2 Inductor Selection

Because the selection of the inductor affects steady-state operation, transient behavior, and loop stability, the inductor is the most important component in power regulator design. There are three important inductor specifications, inductor value, saturation current, and dc resistance (DCR).

The TPS61022 is designed to work with inductor values between 0.33 µH and 2.9 µH. Follow Equation 5 to Equation 7 to calculate the inductor peak current for the application. To calculate the current in the worst case, use the minimum input voltage, maximum output voltage, and maximum load current of the application. To have enough design margins, choose the inductor value with –30% tolerances, and low power-conversion efficiency for the calculation.

In a boost regulator, the inductor dc current can be calculated by Equation 5.

![](images/df2a02e55c1a5141dbf03b69054ca346efb35f67cd98fb853d0a1b7440deca41.jpg)

# where

VOUT is the output voltage of the boost converter IOUT is the output current of the boost converter VIN is the input voltage of the boost converter η is the power conversion efficiency, use 90% for most applications

The inductor ripple current is calculated by Equation 6.

![](images/4fbfbf867c1645418b7f57ec0a502da60f3f214e23fe824eccb3cf99ec83d5ab.jpg)

# where

D is the duty cycle, which can be calculated by Equation 2 ● L is the inductance value of the inductor fSW is the switching frequency VIN is the input voltage of the boost converter

Therefore, the inductor peak current is calculated by Equation 7.

![](images/4679932ed428053cefee00cb2bf0dfa1df1a4fda906a99f27b25c1238225e8ee.jpg)

Normally, it is advisable to work with an inductor peak-to-peak current of less than 40% of the average inductor current for maximum output current. A smaller ripple from a larger valued inductor reduces the magnetic hysteresis losses in the inductor and EMI. But in the same way, load transient response time is increased. The saturation current of the inductor must be higher than the calculated peak inductor current. Table 2 lists the recommended inductors for the TPS61022.

Table 2. Recommended Inductors for the TPS61022   

<table><tr><td>PART NUMBER</td><td>L (μH)</td><td>DCR MAX (m2)</td><td>SATURATION CURRENT (A)</td><td>SIZE (LxWxH)</td><td>VENDOR</td></tr><tr><td>XAL7030-102MEC</td><td>1</td><td>5.00</td><td>28</td><td>8×8×3.1</td><td>Coilcraft</td></tr><tr><td>XAL6030-102MEC</td><td>1</td><td>6.18</td><td>23</td><td>6.36×6.56×3.1</td><td>Coilcraft</td></tr><tr><td>XEL5030-102MEC</td><td>1</td><td>8.40</td><td>16.9</td><td>5.3×5.5×3.1</td><td>Coilcraft</td></tr><tr><td>744316100</td><td>1</td><td>5.23</td><td>11.5</td><td>5.6×5.3×4.3</td><td>Wurth Elecktronik</td></tr></table>

# 8.2.2.3 Output Capacitor Selection

The output capacitor is mainly selected to meet the requirements for output ripple and loop stability. The ripple voltage is related to capacitor capacitance and its equivalent series resistance (ESR). Assuming a ceramic capacitor with zero ESR, the minimum capacitance needed for a given ripple voltage can be calculated by Equation 8.

![](images/5eefe7a7966bb02750d49f54d107994aabb4622ea976c166fb6c6e7261647cfd.jpg)

# where

DMAX is the maximum switching duty cycle VRIPPLE is the peak-to-peak output ripple voltage IOUT is the maximum output current fSW is the switching frequency

The ESR impact on the output ripple must be considered if tantalum or aluminum electrolytic capacitors are used. The output peak-to-peak ripple voltage caused by the ESR of the output capacitors can be calculated by Equation 9.

V I R RIPPLE(ESR) L(P) ESR u

Take care when evaluating the derating of a ceramic capacitor under dc bias voltage, aging, and ac signal. For example, the dc bias voltage can significantly reduce capacitance. A ceramic capacitor can lose more than 50% of its capacitance at its rated voltage. Therefore, always leave margin on the voltage rating to ensure adequate capacitance at the required output voltage. Increasing the output capacitor makes the output ripple voltage smaller in PWM mode.

TI recommends using the X5R or X7R ceramic output capacitor in the range of 10-μF to 50-μF effective capacitance. The output capacitor affects the small signal control loop stability of the boost regulator. If the output capacitor is below the range, the boost regulator can potentially become unstable. Increasing the output capacitor makes the output ripple voltage smaller in PWM mode.

# 8.2.2.4 Loop Stability, Feedforward Capacitor Selection

When the switching waveform shows large duty cycle jitter or the output voltage or inductor current shows oscillations, the regulation loop may be unstable.

The load transient response is another approach to check the loop stability. During the load transient recovery time, VOUT can be monitored for settling time, overshoot or ringing that helps judge the stability of the converters. Without any ringing, the loop has usually more than 45° of phase margin.

A feedforward capacitor (C3 in the Figure 17) in parallel with R1 induces a pair of zero and pole in the loop transfer function. By setting the proper zero frequency, the feedforward capacitor can increase the phase margin to improve the loop stability. For large output capacitance more than 40 μF application, TI recommends a feedforward capacitor to set the zero frequency (fFFZ) to 2 kHz. As for the input voltage lower than 2-V application, TI recommends setting the zero frequency (fFFZ) to 20 kHz when the effective output capacitance is less than 40 μF. The value of the feedforward capacitor can be calculated by Equation 10.

![](images/46dbcc4634a2a71067b92f3fcae56d77a6bafc2004f98d3dee531b1bde4c81f6.jpg)

# where

• R1 is the resistor between the VOUT pin and FB pin • fFFZ is the zero frequency created by the feedforward capacitor

![](images/2edf6305a97238a57504d755431e93abb274c878b059a14900fa3862b622c8ce.jpg)  
Figure 17. TPS61022 Circuit With Feedforward Capacitor

# 8.2.2.5 Input Capacitor Selection

Multilayer X5R or X7R ceramic capacitors are excellent choices for input decoupling of the step-up converter as they have extremely low ESR and are available in small footprints. Input capacitors must be located as close as possible to the device. While a 10-μF input capacitor is sufficient for most applications, larger values may be used to reduce input current ripple without limitations. Take care when using only ceramic input capacitors. When a ceramic capacitor is used at the input and the power is being supplied through long wires, a load step at the output can induce ringing at the VIN pin. This ringing can couple to the output and be mistaken as loop instability or could even damage the part. In this circumstance, place additional bulk capacitance (tantalum or aluminum electrolytic capacitor) between ceramic input capacitor and the power source to reduce ringing that can occur between the inductance of the power source leads and ceramic input capacitor.

# 8.2.3 Application Curves

![](images/e796fc10286cb3b6f29505aaecc87f257e232420199f92bbc1345be44d853f7f.jpg)

![](images/a6adcabb666d9e46b080ee37afe41851833d8b25a429ada3aba54af28dd9e6b5.jpg)

![](images/041b7fb880c399d97dafd77efd2ec9831b27a5ea90e7ddc26b90db87efdad956.jpg)  
Figure 18. Switching Waveform at Heavy Load

![](images/f176eef272db92eaaacc543b6bfe5f5483a9f40e4c61c4d766a08b17b82018d4.jpg)  
Figure 19. Switching Waveform at Light Load

![](images/49539a1cecaf1d2473c740a9c4a0b6825c1d47b43245b9468f160f47e7761c20.jpg)  
Figure 20. Start-up Waveform   
Figure 22. Load Transient

VIN = 3.6 V, VOUT = 5 V, IOUT = 1 A to 3 A with 20-μs slew rate

![](images/4a4907507feaab518b0e8459b1bf8ef4823603023dea6f8fb147bc52b1d4ee54.jpg)  
Figure 21. Shutdown Waveform   
Figure 23. Line Transient

VIN = 2.7 V to 4.35 V with 50-μs slew rate, VOUT = 5 V, IOUT = 3 A

![](images/6ebfa2d073f6a0400eeee4140a3cb0d82ed85fb12af73baa454d0fee021e3a05.jpg)  
Figure 24. Load Sweep

![](images/4b19de8da2b068806959213e1da0e4528243162e55813d1ccfc93a4508e07254.jpg)  
Figure 25. Line Sweep

![](images/7c260364d388417ebbb0abb0c3119017da47ce699ca9d8396ae6b829225b2965.jpg)  
Figure 26. Output Short Protection (Entry)

![](images/919f84b7fb1b9ca3121b977302198b6b526e3b3fb35ff45a887f25290bfc9fb5.jpg)  
Figure 27. Output Short Protection (Recover)

# 8.3 System Examples

For those applications with input voltage higher than 4.8 V, TI suggests adding a diode between the VIN pin and the VOUT pin to pre-bias the output before the TPS61022 is enabled. As an example shown in Figure 28, the input voltage is from a USB port in the range of 4.5 V to 5.25 V. The target output voltage is 5 V to 5.25 V.

![](images/1c94d6bc739c0269e80feb86da0bf6ebb600fa9fbeee546509bbde3de7db4f92.jpg)  
Figure 28. TPS61022 Circuit for VIN > 4.8-V Application

# 9 Power Supply Recommendations

The device is designed to operate from an input voltage supply range between 0.5 V to 5.5 V. This input supply must be well regulated. If the input supply is located more than a few inches from the converter, additional bulk capacitance may be required in addition to the ceramic bypass capacitors. A typical choice is a tantalum or aluminum electrolytic capacitor with a value of 100 µF. Output current of the input power supply must be rated according to the supply voltage, output voltage, and output current of the TPS61022.

# 10 Layout

# 10.1 Layout Guidelines

As for all switching power supplies, especially those running at high switching frequency and high currents, layout is an important design step. If the layout is not carefully done, the regulator could suffer from instability and noise problems. To maximize efficiency, switch rise and fall time are very fast. To prevent radiation of high frequency noise (for example, EMI), proper layout of the high-frequency switching path is essential. Minimize the length and area of all traces connected to the SW pin, and always use a ground plane under the switching regulator to minimize interplane coupling. The input capacitor needs not only to be close to the VIN pin, but also to the GND pin in order to reduce input supply ripple.

The most critical current path for all boost converters is from the switching FET, through the rectifier FET, then the output capacitors, and back to ground of the switching FET. This high current path contains nanosecond rise and fall time and must be kept as short as possible. Therefore, the output capacitor not only must be close to the VOUT pin, but also to the GND pin to reduce the overshoot at the SW pin and VOUT pin.

# 10.2 Layout Example

![](images/12293d8bda0ea506ff4cfe38fd2971dd8b5afd16ea7b7c14235fea7b04547145.jpg)  
Figure 29. Layout Example

Note: A ceramic output capacitor is needed and must be close to VOUT pin and GND pin of the TPS61022

# 10.3 Thermal Considerations

Restrict the maximum IC junction temperature to 125°C under normal operating conditions. Calculate the maximum allowable dissipation, PD(max), and keep the actual power dissipation less than or equal to PD(max). The maximum-power-dissipation limit is determined using Equation 11.

![](images/91a8cefd61986dafe3ebb5b2ec18077c0991e254f19332a53087deb5242eea0b.jpg)

where

• TA is the maximum ambient temperature for the application • RθJA is the junction-to-ambient thermal resistance given in Thermal Information

The TPS61022 comes in a VQFN package. This package includes three power pads that improves the thermal capabilities of the package. The real junction-to-ambient thermal resistance of the package greatly depends on the PCB type, layout, and thermal pad connection. Using larger and thicker PCB copper for the power pads (GND, SW, and VOUT) to enhance the thermal performance. Using more vias connects the ground plate on the top layer and bottom layer around the IC without solder mask also improves the thermal capability.

# 11 Device and Documentation Support

# 11.1 Device Support

# 11.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

# 11.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on Alert me to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

# 11.3 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help — straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

# 11.4 Trademarks

E2E is a trademark of Texas Instruments.   
All other trademarks are the property of their respective owners.

# 11.5 Electrostatic Discharge Caution

![](images/9a457b4c6b1bc81ee97fb8271263712f610c97aed96777d9414dbb0c9410bcc2.jpg)

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

# 11.6 Glossary

SLYZ022 — TI Glossary.

This glossary lists and explains terms, acronyms, and definitions.

# 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

# PACKAGING INFORMATION

<table><tr><td>Orderable Device</td><td>Status (1)</td><td>Package Type Package</td><td>Drawing</td><td>PinsPackage</td><td>aty</td><td>Eco Plan (2)</td><td>Lead finish/ Ball material</td><td>MSL Peak Temp (3)</td><td>Op Temp (°℃)</td><td>Device Marking (4/5)</td><td>Samples</td></tr><tr><td>TPS61022RWUR</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWU</td><td>7</td><td>3000</td><td>RoHS &amp; Green</td><td>(6) Call TI|NIPDAU</td><td>Level-2-260C-1 YEAR</td><td>-40 to 125</td><td>1UNF</td><td>Samples</td></tr><tr><td>TPS61022RWUT</td><td>ACTIVE</td><td>VQFN-HR</td><td>RWU</td><td>7</td><td>250</td><td>RoHS &amp; Green</td><td>Call TI|NIPDAU</td><td>Level-2-260C-1 YEAR</td><td>-40 to 125</td><td>1UNF</td><td>Samples</td></tr></table>

(1) The marketing status values are defined as follows:

ACTIVE: Product device recommended for new designs.   
LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.   
NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.   
PREVIEW: Device has been announced but is not in production. Samples may or may not be available.   
OBSOLETE: TI has discontinued the production of the devic

(2) RoHS: TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may reference these types of products as "Pb-Free".

RoHS Exempt: TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.

Green: TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based flame retardants must also meet the <=1000ppm threshold requirement.

(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

(5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "\~" will appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device Marking for that device.

(6) Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# TAPE AND REEL INFORMATION

![](images/e4114b9d77a09f3e6df4cfe9c43cda75aaf0d5470a9f8d44b9869f32ab4525da.jpg)

![](images/61581525f1eae3bcb969ed9a7fe595ffa80ef78a4fdcb7c87551ee07978333b5.jpg)

<table><tr><td rowspan=1 colspan=1>AO</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component width</td></tr><tr><td rowspan=1 colspan=1>B0</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component length</td></tr><tr><td rowspan=1 colspan=1>KO</td><td rowspan=1 colspan=1>Dimension designed to accommodate the component thickness</td></tr><tr><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>Overall width of the carrier tape</td></tr><tr><td rowspan=1 colspan=1>P1</td><td rowspan=1 colspan=1>Pitch between successive cavity centers</td></tr></table>

# QUADRANT ASSIGnMENTs FOR PIN 1 ORIEnTATION IN TAPE

![](images/28eba3d8d7cf1584c07bfed6c3de0f0a6186b6e76fca75d5ecb091add9018ea2.jpg)

\*All dimensions are nominal   

<table><tr><td rowspan=1 colspan=1>Device</td><td rowspan=1 colspan=1>PackageType</td><td rowspan=1 colspan=1>PackageDrawing</td><td rowspan=1 colspan=1>Pins</td><td rowspan=1 colspan=1>SPQ</td><td rowspan=1 colspan=1>ReelDiameter(mm)</td><td rowspan=1 colspan=1>ReelWidthW1 (mm)</td><td rowspan=1 colspan=1>A0(mm)</td><td rowspan=1 colspan=1>B0(mm)</td><td rowspan=1 colspan=1>K0(mm)</td><td rowspan=1 colspan=1>P1(mm)</td><td rowspan=1 colspan=1>W(mm)</td><td rowspan=1 colspan=1>Pin1Quadrant</td></tr><tr><td rowspan=1 colspan=1>TPS61022RWUR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWU</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>1.15</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr><tr><td rowspan=1 colspan=1>TPS61022RWUT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWU</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>1.15</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q2</td></tr></table>

![](images/382679a312727e0b757c3f18e41a8483fe18090ba1bd03838745ba4c808a0fe6.jpg)

\*All dimensions are nominal   

<table><tr><td rowspan=1 colspan=1>Device</td><td rowspan=1 colspan=1>Package Type</td><td rowspan=1 colspan=1>Package Drawing</td><td rowspan=1 colspan=1>Pins</td><td rowspan=1 colspan=1>SPQ</td><td rowspan=1 colspan=1>Length (mm)</td><td rowspan=1 colspan=1>Width (mm)</td><td rowspan=1 colspan=1>Height (mm)</td></tr><tr><td rowspan=1 colspan=1>TPS61022RWUR</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWU</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>210.0</td><td rowspan=1 colspan=1>185.0</td><td rowspan=1 colspan=1>35.0</td></tr><tr><td rowspan=1 colspan=1>TPS61022RWUT</td><td rowspan=1 colspan=1>VQFN-HR</td><td rowspan=1 colspan=1>RWU</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>210.0</td><td rowspan=1 colspan=1>185.0</td><td rowspan=1 colspan=1>35.0</td></tr></table>

![](images/378a89ca1a8838d5cee7be42b39d3757e45df46409d499aad39186f62c84a58e.jpg)  
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.   
2. This drawing is subject to change without notice.

![](images/5de0592ac05870e772403ba1dd0a557df5dd17517b44e5913af826a9aea1a4b8.jpg)  
NOTES: (continued)

![](images/73f391996f246c12f908e981020c3e60d081969460a10433c96afbabdcf9342f.jpg)  
NOTES: (continued)

5. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

# IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, or other requirements. These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI’s products are provided subject to TI’s Terms of Sale (www.ti.com/legal/termsofsale.html) or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for TI products.