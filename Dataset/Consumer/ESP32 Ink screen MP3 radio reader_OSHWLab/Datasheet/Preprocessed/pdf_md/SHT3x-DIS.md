# Datasheet SHT3x-DIS

Humidity and Temperature Sensor

Fully calibrated, linearized, and temperature   
compensated digital output   
Wide supply voltage range, from 2.15 V to 5.5 V   
I2C Interface with communication speeds up to 1   
MHz and two user selectable addresses   
Typical accuracy of  1.5 %RH and  0.1 °C for   
SHT35   
Very fast start-up and measurement time   
Tiny 8-Pin DFN package

![](images/98961341c03f9c8b36d331fd9fac3ad9dcdf2588bf610ee7634d1d00de417702.jpg)

# Product Summary

SHT3x-DIS is the next generation of Sensirion’s temperature and humidity sensors. It builds on a new CMOSens® sensor chip that is at the heart of Sensirion’s new humidity and temperature platform. The SHT3x-DIS has increased intelligence, reliability and improved accuracy specifications compared to its predecessor. Its functionality includes enhanced signal processing, two distinctive and user selectable I2C addresses and communication speeds of up to 1 MHz. The DFN package has a footprint of 2.5 x 2.5 mm2 while keeping a height of 0.9 mm. This allows for integration of the SHT3x-DIS into a great variety of applications. Additionally, the wide supply voltage range of 2.15 V to 5.5 V guarantees compatibility with diverse assembly situations. All in all, the SHT3x-DIS incorporates 15 years of knowledge of Sensirion, the leader in the humidity sensor industry.

# Benefits of Sensirion’s CMOSens® Technology

High reliability and long-term stability   
Industry-proven technology with a track record of   
more than 15 years   
Designed for mass production   
High process capability   
High signal-to-noise ratio

# Content

1 Sensor Performance...   
2 Specifications . .6   
3 Pin Assignment . .8   
4 Operation and Communication.. .9   
5 Packaging..... ..16   
6 Shipping Package . ..18   
7 Quality .. ..19   
8 Ordering Information.. ..19   
9 Further Information ... .19

![](images/0b6dd7906175ffa565f28a59b0edd01d6a144764e5ff9d6076371c599ffcc23b.jpg)  
Figure 1 Functional block diagram of the SHT3x-DIS. The sensor signals for humidity and temperature are factory calibrated, linearized and compensated for temperature and supply voltage dependencies.

# 1 Sensor Performance

# Humidity Sensor Specification

Table 1 Humidity sensor specification.   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=2 colspan=1>SHT30 Accuracy tolerance1</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 2</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=2 colspan=1>SHT31 Accuracy tolerance1</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 3</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=2 colspan=1>SHT35 Accuracy tolerance1</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>±1.5</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 4</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=3 colspan=1>Repeatability2</td><td rowspan=1 colspan=1>Low, typ.</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Medium, typ.</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>High, typ.</td><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Resolution</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Hysteresis</td><td rowspan=1 colspan=1>at25°℃</td><td rowspan=1 colspan=1>±0.8</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Specified range3</td><td rowspan=1 colspan=1>extended4</td><td rowspan=1 colspan=1>0 to 100</td><td rowspan=1 colspan=1>%RH</td></tr><tr><td rowspan=1 colspan=1>Response time5</td><td rowspan=1 colspan=1>T63%</td><td rowspan=1 colspan=1>86</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>Long-term drift</td><td rowspan=1 colspan=1>Typ.7</td><td rowspan=1 colspan=1>&lt;0.25</td><td rowspan=1 colspan=1>%RH/yr</td></tr></table>

# Temperature Sensor Specification

Table 2 Temperature sensor specification.   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=2 colspan=1>SHT30 Accuracy tolerance1</td><td rowspan=1 colspan=1>typ., 0°C to 65°C</td><td rowspan=1 colspan=1>±0.2</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 8</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=2 colspan=1>SHT31 Accuracy tolerance1</td><td rowspan=1 colspan=1>typ., 0°C to 90°℃</td><td rowspan=1 colspan=1>±0.2</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 9</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=2 colspan=1>SHT35 Accuracy tolerance1</td><td rowspan=1 colspan=1>typ., 20°C to 60°℃</td><td rowspan=1 colspan=1>±0.1</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Figure 10</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=3 colspan=1>Repeatability2</td><td rowspan=1 colspan=1>Low, typ.</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Medium, typ.</td><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>High, typ.</td><td rowspan=1 colspan=1>0.04</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Resolution</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Specified Range</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-40 to 125</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Response time 8</td><td rowspan=1 colspan=1>T63%</td><td rowspan=1 colspan=1>&gt;2</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>Long Term Drift</td><td rowspan=1 colspan=1>max</td><td rowspan=1 colspan=1>&lt;0.03</td><td rowspan=1 colspan=1>Clyr</td></tr></table>

# Humidity Sensor Performance Graphs

![](images/84999a0ee4bd35898c6d1b4e914644f7d0b4bee93389ffbce966b5fc1370d74a.jpg)  
Figure 2 Tolerance of RH at 25°C for SHT30.

![](images/72227788ef2a13256648083e13911ccc3623c6ec3b5e4d7cec3bc1a9c1bfcd6d.jpg)  
Figure 3 Tolerance of RH at 25°C for SHT31.

![](images/52f496fc5cdd723552040412f03b3a4c1feb9540dbd9dd1dd0eff2a1368bcb6b.jpg)  
Figure 4 Tolerance of RH at 25°C for SHT35.

![](images/65a21d2dc867145daa8ca16b7b742eea0267bbc4825a2e3233d1209ae3cf5d8e.jpg)  
Figure 5 Typical tolerance of RH over T for SHT30.

![](images/0a9a9b60989838a3543b3ed16bc5b24d67d6519d2e346b14f5b4cc712258623d.jpg)  
Figure 6 Typical tolerance of RH over T for SHT31.

![](images/ba5dba15a0078423c47e0b53af6523501813b907cdc1066cba3e33f897d580c6.jpg)  
Figure 7 Typical tolerance of RH over T for SHT35.

![](images/15432ab93c06c8138faba5ee13fcad8896690e956b293afb1b35abab2a768b4f.jpg)  
Temperature Sensor Performance Graphs SHT30

![](images/9385a2b3e9c0c4b94041a2cdeeffe0d8e6eceedb6be5cb4253a65059cbe9771b.jpg)  
Figure 8 Temperature accuracy of the SHT30 sensor.   
Figure 9 Temperature accuracy of the SHT31 sensor.

![](images/0bc0877a66036b6d6c482e918726e4c91d4178b9ef8cd087cba11e83b8fb44d2.jpg)  
Figure 10 Temperature accuracy of the SHT35 sensor.

# 1.1 Recommended Operating Condition

The sensor shows best performance when operated within recommended normal temperature and humidity range of 5 °C – 60 °C and 20 %RH – 80 %RH, respectively. Long-term exposure to conditions outside normal range, especially at high humidity, may temporarily offset the RH signal (e.g. +3%RH after 60h kept at >80%RH). After returning into the normal temperature and humidity range the sensor will slowly come back to calibration state by itself. Prolonged exposure to extreme conditions may accelerate ageing. To ensure stable operation of the humidity sensor, the conditions described in the document “SHTxx Assembly of SMD Packages”, section “Storage and Handling Instructions” regarding exposure to volatile organic compounds have to be met. Please note as well that this does apply not only to transportation and manufacturing, but also to operation of the SHT3x-DIS.

# 2 Specifications

# 2.1 Electrical Specifications

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>Supply voltage</td><td rowspan=1 colspan=1>VD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.15</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Power-up/down level</td><td rowspan=1 colspan=1>VPOR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>2.10</td><td rowspan=1 colspan=1>2.15</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Slew rate change of thesupply voltage</td><td rowspan=1 colspan=1>VDD,slew</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>V/ms</td><td rowspan=1 colspan=1>Voltage changes on theVDD line betweenVDD,min and VDD,maxshould be slower thanthe maximum slew rate;faster slew rates maylead to reset;</td></tr><tr><td rowspan=5 colspan=1>Supply current</td><td rowspan=5 colspan=1>IDD</td><td rowspan=1 colspan=1>idle state(single shot mode)T=25°C$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>2.0</td><td rowspan=2 colspan=1>μA</td><td rowspan=2 colspan=1>Current when sensor isnot performing ameasurement duringsingle shot mode</td></tr><tr><td rowspan=1 colspan=1>idle state(single shot mode)$T=125°℃</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>6.0</td></tr><tr><td rowspan=1 colspan=1>idle state(periodic dataacquisition mode)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td><td rowspan=1 colspan=1>Current when sensor isnot performing ameasurement duringperiodic data acquisitionmode</td></tr><tr><td rowspan=1 colspan=1>Measuring</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>600</td><td rowspan=1 colspan=1>1500</td><td rowspan=1 colspan=1>μA</td><td rowspan=1 colspan=1>Current consumptionwhile sensor ismeasuring</td></tr><tr><td rowspan=1 colspan=1>Average</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td><td rowspan=1 colspan=1>Current consumption(operation with onemeasurement persecond at lowestrepeatability, single shotmode)</td></tr><tr><td rowspan=1 colspan=1>Alert Output drivingstrength</td><td rowspan=1 colspan=1>IOH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.5xVDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td><td rowspan=1 colspan=1>See also section 3.5</td></tr><tr><td rowspan=1 colspan=1>Heater power</td><td rowspan=1 colspan=1>PHeater</td><td rowspan=1 colspan=1>Heater running</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>Depending on thesupply voltage</td></tr></table>

Table 3 Electrical specifications, typical values are valid for T=25°C, min. & max. values for T=-40°C … 125°C

# 2.2 Timing Specification for the Sensor System

Table 4 System timing specification, valid from -40 °C to 125 °C and 2.4 V … 5.5 V.   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>Power-up time</td><td rowspan=1 colspan=1>tPu</td><td rowspan=1 colspan=1>After hard reset,VDD ≥VPOR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ms</td><td rowspan=1 colspan=1>Time between Voo reachingVpoR and sensor entering idlestate</td></tr><tr><td rowspan=1 colspan=1>Soft reset time</td><td rowspan=1 colspan=1>tsR</td><td rowspan=1 colspan=1>After soft reset.</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>ms</td><td rowspan=1 colspan=1>Time between ACK of softreset command and sensorentering idle state</td></tr><tr><td rowspan=1 colspan=1>Duration of reset pulse</td><td rowspan=1 colspan=1>tRESETN</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μs</td><td rowspan=1 colspan=1>See section 3.6</td></tr><tr><td rowspan=3 colspan=1>Measurement duration</td><td rowspan=1 colspan=1>tMEAS,</td><td rowspan=1 colspan=1>Low repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>ms</td><td rowspan=3 colspan=1>The three repeatability modesdiffer with respect tomeasurement duration, noiselevel and energy consumption.</td></tr><tr><td rowspan=1 colspan=1>tMEAS,m</td><td rowspan=1 colspan=1>Medium repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tMEAS,h</td><td rowspan=1 colspan=1>High repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>12.5</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>ms</td></tr></table>

<table><tr><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=2>Power-up time</td><td rowspan=1 colspan=1>tpu</td><td rowspan=1 colspan=1>After hard reset,VD ≥ VPOR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>ms</td><td rowspan=1 colspan=1>Time between VoD reachingVpoR and sensor entering idlestate</td></tr><tr><td rowspan=3 colspan=2>Measurement duration</td><td rowspan=1 colspan=1>tMEAS,</td><td rowspan=1 colspan=1>Low repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>ms</td><td rowspan=3 colspan=1>The three repeatability modesdiffer with respect tomeasurement duration, noiselevel and energy consumption.</td></tr><tr><td rowspan=1 colspan=1>con</td><td rowspan=1 colspan=1>tMEAS,m</td><td rowspan=1 colspan=1>Medium repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>6.5</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tMEAS,h</td><td rowspan=1 colspan=1>High repeatability</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>12.5</td><td rowspan=1 colspan=1>15.5</td><td rowspan=1 colspan=1>ms</td></tr></table>

Table 5 System timing specification, valid from -40 °C to 125 °C and 2.15 V … < 2.4V.

# 2.3 Absolute Minimum and Maximum Ratings

Stress levels beyond those listed in Table 6 may cause permanent damage to the device or affect the reliability of the sensor. These are stress ratings only and functional operation of the device at these conditions is not guaranteed. Ratings are only tested each at a time.

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Rating</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=1>Supply voltage VDD</td><td rowspan=1 colspan=1>-0.3 to 6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Max Voltage on pins (pin 1 (SDA); pin 2 (ADDR); pin 3 (ALERT); pin 4 (SCL); pin 6(nRESET))</td><td rowspan=1 colspan=1>-0.3 to VDD+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Input current on any pin</td><td rowspan=1 colspan=1>±100</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1>-40 to 125</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Storage temperature range</td><td rowspan=1 colspan=1>-40 to 150</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>ESD HBM (human body model)9</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>kV</td></tr><tr><td rowspan=1 colspan=1>ESD CDM (charge device model)10</td><td rowspan=1 colspan=1>750</td><td rowspan=1 colspan=1>V</td></tr></table>

Table 6 Minimum and maximum ratings; voltages may only be applied for short time periods.

# 3 Pin Assignment

The SHT3x-DIS comes in a 8-pin DFN package – see Table 7.

<table><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>Serial data; input / output</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ADDR</td><td rowspan=1 colspan=1>Address pin; input; connect to eitherlogic high or low, do not leave floating</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ALERT</td><td rowspan=1 colspan=1>Indicates alarm condition; output; mustbe left fl oating if unused</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>Serial clock; input /output</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>Supply voltage; input</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>nRESET</td><td rowspan=1 colspan=1>Reset pin active low; input; if not used itis recommended to be left fl oating; canbe connected to VDD with a seriesresistor of R ≥2 kΩ</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>No electrical function; to be connectedto VSS</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>VSS</td><td rowspan=1 colspan=1>Ground</td></tr><tr><td rowspan=1 colspan=3>1                       82                        73                      ]4                     5]</td></tr></table>

# 3.1 Power Pins (VDD, VSS)

The electrical specifications of the SHT3x-DIS are shown in Table 3. The power supply pins must be decoupled with a 100 nF capacitor that shall be placed as close to the sensor as possible – see Figure 11 for a typical application circuit.

# 3.2 Serial Clock and Serial Data (SCL, SDA)

SCL is used to synchronize the communication between microcontroller and the sensor. The clock frequency can be freely chosen between 0 to 1000 kHz. Commands with clock stretching according to I2C Standard11 are supported.

The SDA pin is used to transfer data to and from the sensor. Communication with frequencies up to 400 kHz must meet the I2C Fast Mode11 standard.

Communication frequencies up to 1 Mhz are supported following the specifications given in Table 21.

Both SCL and SDA lines are open-drain I/Os with diodes to VDD and VSS. They should be connected to external pull-up resistors (please refer to Figure 11). A device on the I2C bus must only drive a line to ground. The external pull-up resistors (e.g. Rp=10 kΩ) are required to pull the signal high. For dimensioning resistor sizes please take bus capacity and communication frequency into account (see for example Section 7.1 of NXPs I2C Manual for more details11). It should be noted that pull-up resistors may be included in I/O circuits of microcontrollers. It is recommended to wire the sensor according to the application circuit as shown in Figure 11.

![](images/16dd1ae115e659e69831394e80e5a8444a162072963392c8949b03316d5704b7.jpg)  
Table 7 SHT3x-DIS pin assignment (transparent top view). Dashed lines are only visible if viewed from below. The die pad is internally connected to VSS.   
Figure 11 Typical application circuit. Please note that the positioning of the pins does not reflect the position on the real sensor. This is shown in Table 7.

# 3.3 Die Pad (center pad)

The die pad or center pad is visible from below and located in the center of the package. It is electrically connected to VSS. Hence electrical considerations do not impose constraints on the wiring of the die pad. However, due to mechanical reasons it is recommended to solder the center pad to the PCB. For more information on design-in, please refer to the document “SHTxx_STSxx Design Guide”.

# 3.4 ADDR Pin

Through the appropriate wiring of the ADDR pin the I2C address can be selected (see Table 8 for the respective addresses). The ADDR pin can either be connected to logic high or logic low. The address of the sensor can be changed dynamically during operation by switching the level on the ADDR pin. The only constraint is that the level has to stay constant starting from the I2C start condition until the communication is finished. This allows to connect more than two SHT3x-DIS onto the same bus.

# Datasheet SHT3x-DIS

The dynamical switching requires individual ADDR lines to the sensors.

Please note that the I2C address is represented through the 7 MSBs of the I2C read or write header. The LSB switches between read or write header. The wiring for the default address is shown in Table 8 and Figure 11. The ADDR pin must not be left floating. Please note that only the 7 MSBs of the I2C Read/Write header constitute the I2C Address.

Table 8 I2C device addresses.   

<table><tr><td rowspan=1 colspan=1>SHT3x-DIS</td><td rowspan=1 colspan=1>I2C Address in Hex.representation</td><td rowspan=1 colspan=1>Condition</td></tr><tr><td rowspan=1 colspan=1>I2C address A</td><td rowspan=1 colspan=1>0×44 (default)</td><td rowspan=1 colspan=1>ADDR (pin 2)connected to logiclow</td></tr><tr><td rowspan=1 colspan=1>I2C address B</td><td rowspan=1 colspan=1>0x45</td><td rowspan=1 colspan=1>ADDR (pin 2)connected to logichigh</td></tr></table>

# 3.5 ALERT Pin

The alert pin may be used to connect to the interrupt pin of a microcontroller. The output of the pin depends on the value of the RH/T reading relative to programmable limits. Its function is explained in a separate application note. If not used, this pin must be left floating. The pin switches high, when alert conditions are met. The maximum driving loads are listed in Table 3. Be aware that self-heating might occur, depending on the amount of current that flows. Self-heating can be prevented if the Alert Pin is only used to switch a transistor.

# 3.6 nRESET Pin

The nReset pin may be used to generate a reset of the sensor. A minimum pulse duration of 1 µs is required to reliably trigger a reset of the sensor. Its function is explained in more detail in section 4. If not used it is recommended to leave the pin floating or to connect it to VDD with a series resistor of R ≥2 kΩ. However, the nRESET pin is internally connected to VDD with a pull up resistor of R = 50 kΩ (typ.).

# 4 Operation and Communication

The SHT3x-DIS supports I2C fast mode (and frequencies up to 1000 kHz). Clock stretching can be enabled and disabled through the appropriate user command. For detailed information on the I2C protocol, refer to NXP I2C-bus specification12.

After sending a command to the sensor a minimal waiting time of 1ms is needed before another command can be received by the sensor.

All SHT3x-DIS commands and data are mapped to a 16- bit address space. Additionally, data and commands are protected with a CRC checksum. This increases communication reliability. The 16 bits commands to the sensor already include a 3 bit CRC checksum. Data sent from and received by the sensor is always succeeded by an 8 bit CRC.

In write direction it is mandatory to transmit the checksum, since the SHT3x-DIS only accepts data if it is followed by the correct checksum. In read direction it is left to the master to read and process the checksum.

# 4.1 Power-Up and Communication Start

The sensor starts powering-up after reaching the powerup threshold voltage VPOR specified in Table 3. After reaching this threshold voltage the sensor needs the time tPU to enter idle state. Once the idle state is entered it is ready to receive commands from the master (microcontroller).

Each transmission sequence begins with a START condition (S) and ends with a STOP condition (P) as described in the I2C-bus specification. Whenever the sensor is powered up, but not performing a measurement or communicating, it automatically enters idle state for energy saving. This idle state cannot be controlled by the user.

# 4.2 Starting a Measurement

A measurement communication sequence consists of a START condition, the I2C write header (7-bit I2C device address plus 0 as the write bit) and a 16-bit measurement command. The proper reception of each byte is indicated by the sensor. It pulls the SDA pin low (ACK bit) after the falling edge of the 8th SCL clock to indicate the reception. A complete measurement cycle is depicted in Table 9.

With the acknowledgement of the measurement command, the SHT3x-DIS starts measuring humidity and temperature.

# 4.3 Measurement Commands for Single Shot Data Acquisition Mode

In this mode one issued measurement command triggers the acquisition of one data pair. Each data pair consists of one 16 bit temperature and one 16 bit humidity value (in this order). During transmission each data value is always followed by a CRC checksum, see section 4.4.

In single shot mode different measurement commands can be selected. The 16 bit commands are shown in Table 9. They differ with respect to repeatability (low, medium and high) and clock stretching (enabled or disabled).

The repeatability setting influences the measurement duration and thus the overall energy consumption of the sensor. This is explained in section 2.

<table><tr><td rowspan=1 colspan=2>Condition</td><td rowspan=1 colspan=2>Hex. code</td></tr><tr><td rowspan=1 colspan=1>Repeatability</td><td rowspan=1 colspan=1>Clockstretching</td><td rowspan=1 colspan=1>MSB</td><td rowspan=1 colspan=1>LSB</td></tr><tr><td rowspan=1 colspan=1>High</td><td rowspan=3 colspan=1>enabled</td><td rowspan=3 colspan=1>0x2C</td><td rowspan=1 colspan=1>06</td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=1>OD</td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>High</td><td rowspan=3 colspan=1>disabled</td><td rowspan=3 colspan=1>0x24</td><td rowspan=1 colspan=1>00</td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=1>OB</td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=4>e.g. 0x2C06: high repeatability measurement with clock</td></tr></table>

![](images/ad08006225fd397d51fa8dd679f2ddbb9fc2b2d9b1057d945ab54bd11000654f.jpg)  
stretching enabled   
Table 9 Measurement commands in single shot mode. The first “SCL free” block indicates a minimal waiting time of 1ms. (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

# 4.4 Readout of Measurement Results for Single Shot Mode

After the sensor has completed the measurement, the master can read the measurement results (pair of RH& T) by sending a START condition followed by an I2C read header. The sensor will acknowledge the reception of the read header and send two bytes of data (temperature) followed by one byte CRC checksum and another two bytes of data (relative humidity) followed by one byte CRC checksum. Each byte must be acknowledged by the microcontroller with an ACK condition for the sensor to continue sending data. If the sensor does not receive an ACK from the master after any byte of data, it will not continue sending data.

The sensor will send the temperature value first and then the relative humidity value. After having received the checksum for the humidity value a NACK and stop condition should be sent (see Table 9).

The I2C master can abort the read transfer with a NACK condition after any data byte if it is not interested in subsequent data, e.g. the CRC byte or the second measurement result, in order to save time.

In case the user needs humidity and temperature data but does not want to process CRC data, it is recommended to read the two temperature bytes of data with the CRC byte (without processing the CRC data); after having read the two humidity bytes, the read transfer can be aborted with a with a NACK.

# No Clock Stretching

When a command without clock stretching has been issued, the sensor responds to a read header with a not acknowledge (NACK), if no data is present.

# Clock Stretching

When a command with clock stretching has been issued, the sensor responds to a read header with an ACK and subsequently pulls down the SCL line. The SCL line is pulled down until the measurement is complete. As soon as the measurement is complete, the sensor releases the SCL line and sends the measurement results.

# 4.5 Measurement Commands for Periodic Data Acquisition Mode

In this mode one issued measurement command yields a stream of data pairs. Each data pair consists of one 16 bit temperature and one 16 bit humidity value (in this order).

In periodic mode different measurement commands can be selected. The corresponding 16 bit commands are shown in Table 10. They differ with respect to repeatability (low, medium and high) and data acquisition frequency (0.5, 1, 2, 4 & 10 measurements per second, mps). Clock stretching cannot be selected in this mode.

The data acquisition frequency and the repeatability setting influences the measurement duration and the current consumption of the sensor. This is explained in section 2 of this datasheet.

If a measurement command is issued, while the sensor is busy with a measurement (measurement durations see Table 4), it is recommended to issue a break command first (see section 4.8). Upon reception of the break command the sensor abort the ongoing measurement and enter the single shot mode.

<table><tr><td rowspan=1 colspan=4>Condition</td><td rowspan=1 colspan=2>Hex. code</td></tr><tr><td rowspan=1 colspan=3>Repeatability</td><td rowspan=1 colspan=1>mps</td><td rowspan=1 colspan=1>MSB</td><td rowspan=1 colspan=1>LSB</td></tr><tr><td rowspan=1 colspan=3>High</td><td rowspan=3 colspan=1>0.5</td><td rowspan=3 colspan=1>0x20</td><td rowspan=1 colspan=1>32</td></tr><tr><td rowspan=1 colspan=3>Medium</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=3>Low</td><td rowspan=1 colspan=1>2F</td></tr><tr><td rowspan=1 colspan=3>High</td><td rowspan=3 colspan=1>1</td><td rowspan=3 colspan=1>0x21</td><td rowspan=1 colspan=1>30</td></tr><tr><td rowspan=1 colspan=3>Medium</td><td rowspan=1 colspan=1>26</td></tr><tr><td rowspan=1 colspan=3>Low</td><td rowspan=1 colspan=1>2D</td></tr><tr><td rowspan=1 colspan=3>High</td><td rowspan=3 colspan=1>2</td><td rowspan=3 colspan=1>0x22</td><td rowspan=1 colspan=1>36</td></tr><tr><td rowspan=1 colspan=3>Medium</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=3>Low</td><td rowspan=1 colspan=1>2B</td></tr><tr><td rowspan=1 colspan=3>High</td><td rowspan=3 colspan=1>4</td><td rowspan=3 colspan=1>0x23</td><td rowspan=1 colspan=1>34</td></tr><tr><td rowspan=1 colspan=3>Medium</td><td rowspan=1 colspan=1>22</td></tr><tr><td rowspan=1 colspan=3>Low</td><td rowspan=1 colspan=1>29</td></tr><tr><td rowspan=1 colspan=3>High</td><td rowspan=3 colspan=1>10</td><td rowspan=3 colspan=1>0x27</td><td rowspan=1 colspan=1>37</td></tr><tr><td rowspan=1 colspan=3>Medium</td><td rowspan=1 colspan=1>21</td></tr><tr><td rowspan=1 colspan=3>Low</td><td rowspan=1 colspan=1>2A</td></tr><tr><td rowspan=1 colspan=6>e.g. 0x2130: 1 high repeatability mps - measurement persecond</td></tr><tr><td rowspan=2 colspan=6>1 2 3 5 6789  23  5 6 7 8 9 10 11 12 13 14 15 16 17 18S 12C Address $WCommand MSB Command LSB </td></tr><tr><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>12C Address</td><td rowspan=1 colspan=1>$W</td><td rowspan=1 colspan=2>Command MSB</td><td rowspan=1 colspan=1>Command LSB</td></tr><tr><td rowspan=1 colspan=6>-I2C write header                 -16-bitcommand</td></tr></table>

Table 10 Measurement commands for periodic data acquisition mode (Clear blocks are controlled by the microcontroller, grey blocks by the sensor). N.B.: At the highest mps setting self-heating of the sensor might occur.

# 4.6 Readout of Measurement Results for Periodic Mode

Transmission of the measurement data can be initiated through the fetch data command shown in Table 11. If no measurement data is present the I2C read header is responded with a NACK (Bit 9 in Table 11) and the communication stops. After the read out command fetch data has been issued, the data memory is cleared, i.e. no measurement data is present.

![](images/5bd462bcfd62c8b96eb0c537f205ea4b3833067dd2e4f1e254984d968fface5d.jpg)

Table 11 Fetch Data command (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

# 4.7 ART Command

The ART (accelerated response time) feature can be activated by issuing the command in Table 12. After issuing the ART command the sensor will start acquiring data with a frequency of 4Hz.

The ART command is structurally similar to any other command in Table 10. Hence section 4.5 applies for starting a measurement, section 4.6 for reading out data and section 4.8 for stopping the periodic data acquisition.

The ART feature can also be evaluated using the Evaluation Kit EK-H5 from Sensirion.

<table><tr><td colspan="3">Command</td><td colspan="5">Hex Code</td></tr><tr><td colspan="5">Periodic Measurement with ART</td><td colspan="7">0x2B32</td></tr><tr><td colspan="18">1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18</td></tr><tr><td rowspan="2">S</td><td colspan="9">I2CAddress W</td><td rowspan="2">Command LSB</td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>-I2C write header-</td><td colspan="4">Command MSB</td><td></td><td colspan="3">-16-bitcommand-</td><td></td></tr></table>

Table 12 Command for a periodic data acquisition with the ART feature (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

# 4.8 Break command / Stop Periodic Data Acquisition Mode

The periodic data acquisition mode can be stopped using the break command shown in Table 13. It is recommended to stop the periodic data acquisition prior to sending another command (except Fetch Data command) using the break command. Upon reception of the break command the sensor will abort the ongoing measurement and enter the single shot mode. This takes 1ms.

![](images/9ef27d516362ed2bba4167fd93db9ea33970a7315760f4087f6c2e59344e1552.jpg)  
Table 13 Break command (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

# 4.9 Reset

A system reset of the SHT3x-DIS can be generated externally by issuing a command (soft reset) or by sending a pulse to the dedicated reset pin (nReset pin). Additionally, a system reset is generated internally during power-up. During the reset procedure the sensor will not process commands.

In order to achieve a full reset of the sensor without removing the power supply, it is recommended to use the nRESET pin of the SHT3x-DIS.

# Interface Reset

If communication with the device is lost, the following signal sequence will reset the serial interface: While leaving SDA high, toggle SCL nine or more times. This must be followed by a Transmission Start sequence preceding the next command. This sequence resets the interface only. The status register preserves its content.

# Soft Reset / Re-Initialization

The SHT3x-DIS provides a soft reset mechanism that forces the system into a well-defined state without removing the power supply. When the system is in idle state the soft reset command can be sent to the SHT3xDIS. This triggers the sensor to reset its system controller and reloads calibration data from the memory. In order to start the soft reset procedure the command as shown in Table 14 should be sent.

It is worth noting that the sensor reloads calibration data prior to every measurement by default.

![](images/213e202c672d7eb3784b1c2e08511eb5790c789521756d047f0554d2b5eb52bd.jpg)  
Table 14 Soft reset command (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).   
Table 15 Reset through the general call address (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

# Reset through General Call

Additionally, a reset of the sensor can also be generated using the “general call” mode according to I2C-bus specification12. This generates a reset which is functionally identical to using the nReset pin. It is important to understand that a reset generated in this way is not device specific. All devices on the same I2C bus that support the general call mode will perform a reset. Additionally, this command only works when the sensor is able to process I2C commands. The appropriate command consists of two bytes and is shown in Table 15.

<table><tr><td>Command</td><td colspan="2">Code</td></tr><tr><td colspan="2">Address byte</td><td>0x00</td></tr><tr><td colspan="2">Second byte</td><td>0x06</td></tr><tr><td colspan="2">Reset command using the general all ddress</td><td colspan="2">0x0006</td></tr><tr><td colspan="4">1  2 3 4 6 7 8 9 1 2 3 4 5 6 7 8 9</td></tr><tr><td rowspan="2">S</td><td>General Call Address</td><td></td><td>Reset Command</td></tr><tr><td>General Call st byte</td><td></td><td>General Call 2nd byte</td></tr></table>

# Reset through the nReset Pin

Pulling the nReset pin low (see Table 7) generates a reset similar to a hard reset. The nReset pin is internally connected to VDD through a pull-up resistor and hence active low. The nReset pin has to be pulled low for a minimum of 1 µs to generate a reset of the sensor.

# Hard Reset

A hard reset is achieved by switching the supply voltage to the VDD Pin off and then on again. In order to prevent powering the sensor over the ESD diodes, the voltage to pins 1 (SDA), 4 (SCL) and 2 (ADDR) also needs to be removed.

# 4.10 Heater

The SHT3x is equipped with an internal heater, which is meant for plausibility checking only. The temperature increase achieved by the heater depends on various parameters and lies in the range of a few degrees centigrade. It can be switched on and off by command, see table below. The status is listed in the status register. After a reset the heater is disabled (default condition).

<table><tr><td rowspan=2 colspan=1>Command</td><td rowspan=1 colspan=2>Hex Code</td></tr><tr><td rowspan=1 colspan=1>MSB</td><td rowspan=1 colspan=1>LSB</td></tr><tr><td rowspan=1 colspan=1>Heater Enable</td><td rowspan=2 colspan=1>0x30</td><td rowspan=1 colspan=1>6D</td></tr><tr><td rowspan=1 colspan=1>Heater Disabled</td><td rowspan=1 colspan=1>66</td></tr><tr><td rowspan=1 colspan=3>1 2 3 4 5 6 7 8 9 1 2 34 5 6 7 8 9 10 11 12 13 14 15 16 17 18S 12CAddress  W Command MSB Command LSB EP</td></tr><tr><td rowspan=1 colspan=3>-I2C write header-                -16-bitcommand-</td></tr></table>

# 4.11 Status Register

The status register contains information on the operational status of the heater, the alert mode and on the execution status of the last command and the last write sequence. The command to read out the status register is shown in Table 17 whereas a description of the content can be found in Table 18.

![](images/836c362d858a1cdf30a6ec3a75c5ea0655b6c0497f46375081792b615c599f55.jpg)  
Table 16 Heater command (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).   
Table 17 Command to read out the status register (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).   
Table 19 Command to clear the status register (Clear blocks are controlled by the microcontroller, grey blocks by the sensor).

Table 18 Description of the status register.   

<table><tr><td rowspan=1 colspan=1>Bit</td><td rowspan=1 colspan=1>Field description</td><td rowspan=1 colspan=1>Defaultvalue</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>Alert pending status&#x27;O&#x27;: no pending alerts&#x27;1&#x27;: at least one pending alert</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>0&#x27;</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>Heater status&#x27;0&#x27;: Heater OFF1&#x27;: Heater ON</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>0&#x27;</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>RH tracking alert0&#x27;:no alert1&#x27;.alert</td><td rowspan=1 colspan=1>&#x27;0</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>T tracking alert0&#x27;:no alert1&#x27;.alert</td><td rowspan=1 colspan=1>0&#x27;</td></tr><tr><td rowspan=1 colspan=1>9:5</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>&#x27;XXXxX&#x27;</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>System reset detected&#x27;0&#x27;: no reset detected since last &#x27;clearstatus register&#x27; command&#x27;1&#x27;: reset detected (hard reset, soft resetcommand or supply fail)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>3:2</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>00&#x27;</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Command status&#x27;0&#x27;: last command executed successfully&#x27;1&#x27;: last command not processed. It waseither invalid, failed the integratedcommand checksum</td><td rowspan=1 colspan=1>0&#x27;</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Write data checksum status&#x27;0&#x27;: checksum of last write transfer wascorrect&#x27;1&#x27;: checksum of last write transfer failed</td><td rowspan=1 colspan=1>“0&#x27;</td></tr></table>

# Clear Status Register

All flags (Bit 15, 11, 10, 4) in the status register can be cleared (set to zero) by sending the command shown in Table 19.

<table><tr><td>Command</td></tr><tr><td>Clear status register 0x3041</td></tr><tr><td>1 23 7 8 9 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18</td></tr><tr><td>$ S I2C Address Command MSB Command LSB P</td></tr></table>

# 4.12 Checksum Calculation

The 8-bit CRC checksum transmitted after each data word is generated by a CRC algorithm. Its properties are displayed in Table 20. The CRC covers the contents of the two previously transmitted data bytes. To calculate

# Datasheet SHT3x-DIS

the checksum only these two previously transmitted data bytes are used.

<table><tr><td rowspan=1 colspan=1>Property</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>CRC-8</td></tr><tr><td rowspan=1 colspan=1>Width</td><td rowspan=1 colspan=1>8 bit</td></tr><tr><td rowspan=1 colspan=1>Protected data</td><td rowspan=1 colspan=1>read and/or write data</td></tr><tr><td rowspan=1 colspan=1>Polynomial</td><td rowspan=1 colspan=1>0x31 (x8 +x5 +x4 + 1)</td></tr><tr><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>0xFF</td></tr><tr><td rowspan=1 colspan=1>Reflect input</td><td rowspan=1 colspan=1>False</td></tr><tr><td rowspan=1 colspan=1>Reflect output</td><td rowspan=1 colspan=1>False</td></tr><tr><td rowspan=1 colspan=1>Final XOR</td><td rowspan=1 colspan=1>0x00</td></tr><tr><td rowspan=1 colspan=1>Examples</td><td rowspan=1 colspan=1>CRC (0xBEEF) = 0x92</td></tr></table>

Table 20 I2C CRC properties.

# 4.13 Conversion of Signal Output

Measurement data is always transferred as 16-bit values (unsigned integer). These values are already linearized

and compensated for temperature and supply voltage effects. Converting those raw values into a physical scale can be achieved using the following formulas.

Relative humidity conversion formula (result in %RH):

![](images/23d3c893ce319aff42ae8e8d96c1c2a8edd33f7b401711961526d7cc689ceb22.jpg)

Temperature conversion formula (result in °C & °F):

![](images/1a399e0e4dae330702f84c8f7b64f8995b4d36501e8d7368b0f7095f225ae3d2.jpg)

SRH and ST denote the raw sensor output for humidity and temperature, respectively. The formulas work only correctly when SRH and ST are used in decimal representation.

# 4.14 Communication Timing

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>SCL clock frequency</td><td rowspan=1 colspan=1>fscL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>kHz</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Hold time (repeated) STARTcondition</td><td rowspan=1 colspan=1>tHD;STA</td><td rowspan=1 colspan=1>After this period, the firstclock pulse is generated</td><td rowspan=1 colspan=1>0.24</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μs</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>LOW period of the SCLclock</td><td rowspan=1 colspan=1>tLow</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.53</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μs</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>HIGH period of the SCLclock</td><td rowspan=1 colspan=1>tHIGH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μs</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>SDA hold time</td><td rowspan=2 colspan=1>tHD;DAT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1>Transmiting data</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1>Receiving data</td></tr><tr><td rowspan=1 colspan=1>SDA set-up time</td><td rowspan=1 colspan=1>tsU;DAT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SCL/SDA rise time</td><td rowspan=1 colspan=1>tr</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SCL/SDA fall time</td><td rowspan=1 colspan=1>tF</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SDA valid time</td><td rowspan=1 colspan=1>tVD;DAT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>us</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Set-up time for a repeatedSTART condition</td><td rowspan=1 colspan=1>tSU;STA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Set-up time for STOPcondition</td><td rowspan=1 colspan=1>tsU;STO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Capacitive load on bus line</td><td rowspan=1 colspan=1>CB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>pF</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Low level input voltage</td><td rowspan=1 colspan=1>Vi</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.3xVDD</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>High level input voltage</td><td rowspan=1 colspan=1>ViH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7xVDD</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>$1xVDD</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Low level output voltage</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>3 mA sink current</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr></table>

Table 21 Timing specifications for I2C communication, valid for T=-40°C … 125°C and VDD = VDDmin … VDDmax. The nomenclature above is according to the I2C (UM10204, Rev. 6, April 4, 2014).

![](images/029539fb79bb55a9ed0e43a2f488e7c674d82694bcf1662a8cb0735e7828793d.jpg)  
Figure 12 Timing diagram for digital input/output pads. SDA directions are seen from the sensor. Bold SDA lines are controlled by the sensor, plain SDA lines are controlled by the micro-controller. Note that SDA valid read time is triggered by falling edge of preceding toggle.

# 5 Packaging

SHT3x-DIS sensors are provided in an open-cavity DFN package. DFN stands for dual flat no leads. The humidity sensor opening is centered on the top side of the package.

The sensor chip is made of silicon and is mounted to a lead frame. The latter is made of Cu plated with Ni/Pd/Au. Chip and lead frame are overmolded by an epoxy-based mold compound leaving the central die pad and I/O pins exposed for mechanical and electrical connection. Please note that the side walls of the sensor are diced and therefore these diced lead frame surfaces are not covered with the respective plating.

The package (except for the humidity sensor opening) follows JEDEC publication 95, design registration 4.20, small scale plastic quad and dual inline, square and rectangular, No-LEAD packages (with optional thermal enhancements) small scale (QFN/SON), Issue D.01, September 2009.

SHT3x-DIS has a Moisture Sensitivity Level (MSL) of 1, according to IPC/JEDEC J-STD-020. At the same time, it is recommended to further process the sensors within 1 year after date of delivery.

# 5.1 Traceability

All SHT3x-DIS sensors are laser marked for easy identification and traceability. The marking on the sensor top side consists of a pin-1 indicator and two lines of text.

The top line consists of the pin-1 indicator which is located in the top left corner and the product name. The small letter x stands for the accuracy class.

The bottom line consists of 6 letters. The first two digits XY (=DI) describe the output mode. The third letter (A) represents the manufacturing year (4 = 2014, 5 = 2015, etc). The last three digits (BCD) represent an alphanumeric tracking code. That code can be decoded by Sensirion only and allows for tracking on batch level through production, calibration and testing – and will be provided upon justified request.

If viewed from below pin 1 is indicated by triangular shaped cut in the otherwise rectangular die pad. The dimensions of the triangular cut are shown in Figure 14 through the labels T1 & T2.

![](images/f2254f8f8cabfe9ab71019404d520b7a31335bd6ccfb27c819b15efd9d12702e.jpg)  
Figure 13 Top view of the SHT3x-DIS illustrating the laser marking.

# 5.2 Package Outline

![](images/07a2ecdbb3aea8f57dc7ffe36532f4c0edb95ec44078985eb69de142408156c5.jpg)  
Figure 14 Dimensional drawing of SHT3x-DIS sensor package

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Nom.</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>Package height</td><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Leadframe height</td><td rowspan=1 colspan=1>A3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pad width</td><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Package width</td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Center pad length</td><td rowspan=1 colspan=1>D2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Package length</td><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Center pad width</td><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pad pitch</td><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pad length</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.35</td><td rowspan=1 colspan=1>0.45</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Max cavity</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1>Only as guidance. This value includes al tolerances, including displacement tolerances. Typically the openingwill be smaller.</td></tr><tr><td rowspan=1 colspan=1>Center pad marking</td><td rowspan=1 colspan=1>T1xT2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.3×45°</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1>indicates the position of pin 1</td></tr></table>

Table 22 Package outline.

# 5.3 Land Pattern

Figure 15 shows the land pattern. The land pattern is understood to be the open metal areas on the PCB, onto which the DFN pads are soldered.

The solder mask is understood to be the insulating layer on top of the PCB covering the copper traces. It is recommended to design the solder pads as a NonSolder Mask Defined (NSMD) type. For NSMD pads, the solder mask opening should provide a 60 μm to 75 μm design clearance between any copper pad and solder mask. As the pad pitch is only 0.5 mm we recommend to have one solder mask opening for all 4 I/O pads on one side.

For solder paste printing it is recommended to use a laser-cut, stainless steel stencil with electro-polished trapezoidal walls and with 0.1 or 0.125 mm stencil thickness. The length of the stencil apertures for the I/O pads should be the same as the PCB pads. However, the position of the stencil apertures should have an offset of 0.1 mm away from the center of the package. The die pad aperture should cover about 70 – 90 % of the die pad area –thus it should have a size of about 0.9 mm x 1.6 mm.

For information on the soldering process and further recommendation on the assembly process please consult the Application Note HT_AN_SHTxx_Assembly_of_SMD_Packages , which can be found on the Sensirion webpage.

![](images/a7ec005eb4accbc801e3c678aaddc4ddc9ada2a5e734f5d43500313cb9e805c3.jpg)  
Figure 15 Recommended metal land pattern (left) and stencil apertures (right) for SHT3x-DIS. The dashed lines represent the outer dimension of the DFN package. The PCB pads (left) and stencil apertures (right) are indicated through the shaded areas.

![](images/a53bd8dde31f0889e1e975db47daaf8c4c5d17281057036e6b1b47dd393e34f9.jpg)

# 6 Shipping Package

![](images/cb6dbfdf46e3cb515d46e8c047d53bacde2dbd2bc13d5bd6c1018039a61e81b6.jpg)  
Figure 16 Technical drawing of the packaging tape with sensor orientation in tape. Header tape is to the right and trailer tape to the left on this drawing. Dimensions are given in millimeters.

# 7 Quality

Qualification of the SHT3x-DIS is performed based on the JEDEC JESD47 qualification test method.

# 7.1 Material Contents

The device is fully RoHS and WEEE compliant, e.g.   
free of Pb, Cd, and Hg.

# 8 Ordering Information

The SHT3x-DIS can be ordered in tape and reel packaging with different sizes, see Table 23. The reels are sealed into antistatic ESD bags. The document “SHT3x shipping package” that shows the details about the shipping package is available upon request.

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Quantity</td><td rowspan=1 colspan=1>Order Number</td></tr><tr><td rowspan=1 colspan=1>SHT30-DIS-B2.5kS</td><td rowspan=1 colspan=1>2500</td><td rowspan=1 colspan=1>1-101400-01</td></tr><tr><td rowspan=1 colspan=1>SHT30-DIS-B10kS</td><td rowspan=1 colspan=1>10000</td><td rowspan=1 colspan=1>1-101173-01</td></tr><tr><td rowspan=1 colspan=1>SHT31-DIS-B2.5kS</td><td rowspan=1 colspan=1>2500</td><td rowspan=1 colspan=1>1-101386-01</td></tr><tr><td rowspan=1 colspan=1>SHT31-DIS-B10kS</td><td rowspan=1 colspan=1>10000</td><td rowspan=1 colspan=1>1-101147-01</td></tr><tr><td rowspan=1 colspan=1>SHT35-DIS-B2.5kS</td><td rowspan=1 colspan=1>2500</td><td rowspan=1 colspan=1>1-101388-01</td></tr><tr><td rowspan=1 colspan=1>SHT35-DIS-B10kS</td><td rowspan=1 colspan=1>10000</td><td rowspan=1 colspan=1>1-101479-01</td></tr></table>

Table 23 SHT3x-DIS ordering options.

# 9 Further Information

For more in-depth information on the SHT3x-DIS and its application please consult the documents in Table 24. Parameter values specified in the datasheet overrule possibly conflicting statements given in references cited in this datasheet.

Table 24 Documents containing further information relevant for theSHT3x-DIS.   

<table><tr><td rowspan=1 colspan=1>Document Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Source</td></tr><tr><td rowspan=1 colspan=1>SHT3x Shipping Package</td><td rowspan=1 colspan=1>Information on Tape, Reel nd shipping bag(technical drawing and dimensions)</td><td rowspan=1 colspan=1>Available upon request</td></tr><tr><td rowspan=1 colspan=1>SHTxx_STSxx Assembly ofSMD Packages</td><td rowspan=1 colspan=1>Assembly Guide (Soldering Instructions)</td><td rowspan=1 colspan=1>Available for download at the Sensirionhumidity sensors download center:www.sensirion.com/humidity-download</td></tr><tr><td rowspan=1 colspan=1>SHTxx_STSxx Design Guide</td><td rowspan=1 colspan=1>Design guidelines for designing SHTxxhumidity sensors into applications</td><td rowspan=1 colspan=1>Available for download at the Sensirionhumidity sensors download center:www.sensirion.com/humidity-download</td></tr><tr><td rowspan=1 colspan=1>SHTxx Handling Instructions</td><td rowspan=1 colspan=1>Guidelines for proper handling of SHTxxhumidity sensors</td><td rowspan=1 colspan=1>Available for download at the Sensirionhumidity sensors download center:www.sensirion.com/humidity-download</td></tr><tr><td rowspan=1 colspan=1>Sensirion Humidity SensorSpecification Statement</td><td rowspan=1 colspan=1>Definition of sensor specifications.</td><td rowspan=1 colspan=1>Available for download at the Sensirionhumidity sensors download center:www.sensirion.com/humidity-download</td></tr></table>

# Revision History

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=2>Version</td><td rowspan=1 colspan=1>Page(s)</td><td rowspan=1 colspan=1>Changes</td></tr><tr><td rowspan=1 colspan=1>October 2015</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>June 2016</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>2-461117</td><td rowspan=1 colspan=1>Specifications for SHT35 addedESD specifications updatedTable 7 &quot;Comments&quot; section updatedFigure 11 updated according to Table 7Updated information about data memory to: &quot;After the read out command&quot;fetch data&quot; has been issued, the data memory is reset,ie. no measurementdata is present.Ordering information in Table 23 updated</td></tr><tr><td rowspan=1 colspan=1>August 2016</td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=1>6884</td><td rowspan=1 colspan=1>Updated Table 3Updated Table 4Updated information on ESD testing normUpdated Table 7Figure 11 and Table 7 updatedFigure 7 updated</td></tr><tr><td rowspan=3 colspan=1>March 2017</td><td rowspan=1 colspan=2>4</td><td rowspan=1 colspan=1>2-59681517</td><td rowspan=3 colspan=1>Updated RH&amp;T accuracy specifications, see Table 1, Table 2, Figure 2,Figure 5, Figure 8, Figure 9 and Figure 10Table 8 updatedTable 3 updatedFigure 11 updatedTable 21 updatedTable 22 updatedFigure 15 land pattern drawing simplified (no parameter changed)Inlcuded: &quot;Parameter values specified in the datasheet overrule possiblyconflicting statements given in references cited in this datasheet.&quot;</td></tr><tr><td rowspan=2 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>19</td></tr></table>

<table><tr><td>22 May 2018</td><td></td><td>multiple</td><td>VDDmin=2.15V</td></tr><tr><td></td><td></td><td>multiple 2</td><td>Typo &amp; formatting correction Updated RH repeatability values in Table 1</td></tr><tr><td></td><td></td><td></td><td>Updated T repeatability and resolution in Table 2</td></tr><tr><td></td><td></td><td></td><td>Table 3</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Updated VDDmin and POR levels</td></tr><tr><td></td><td></td><td></td><td>Updated supply current values</td></tr><tr><td></td><td></td><td></td><td>Updated specification range Updated soft reset time in Table 4</td></tr><tr><td></td><td></td><td></td><td>Introduced Table 5</td></tr><tr><td></td><td></td><td></td><td>Introduced &quot;Ratings are only tested each at a time.&quot; in section 2.3</td></tr><tr><td></td><td></td><td></td><td>Introduced &quot;After sending a command to the sensor a minimal waiting time of 1ms is needed before another command can be received by the sensor.&quot;</td></tr><tr><td></td><td></td><td>9</td><td>In section 4 Removed: &quot;The stop condition is optional.&quot; in section 4.1</td></tr><tr><td></td><td></td><td>10</td><td>Updated label of Table 9 with &quot;The first &quot;SCL free&quot; block indicates a minimal waiting time of 1ms.&quot;</td></tr><tr><td></td><td></td><td>10</td><td>Updated section 4.5 to “Upon reception of the break command the sensor abort the ongoing measurement and enter the single shot mode.&quot;</td></tr><tr><td></td><td></td><td>11</td><td>Updated section 4.8 to&quot;Upon reception of the break command the sensor will abort the ongoing measurement and enter the single shot mode. This takes 1ms.&quot;</td></tr><tr><td></td><td></td><td>14</td><td>Updated Table 21</td></tr><tr><td>February 2019</td><td>6</td><td>19</td><td>Revised qualification test method in section 7</td></tr></table>

# Important Notices

Warning, Personal Injury

Do not use this product as safety or emergency stop devices or in any other application where failure of the product could result in personal injury. Do not use this product for applications other than its intended and authorized use. Before installing, handling, using or servicing this product, please consult the data sheet and application notes. Failure to comply with these instructions could result in death or serious injury.

If the Buyer shall purchase or use SENSIRION products for any unintended or unauthorized application, Buyer shall defend, indemnify and hold harmless SENSIRION and its officers, employees, subsidiaries, affiliates and distributors against all claims, costs, damages and expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of personal injury or death associated with such unintended or unauthorized use, even if SENSIRION shall be allegedly negligent with respect to the design or the manufacture of the product.

# ESD Precautions

The inherent design of this component causes it to be sensitive to electrostatic discharge (ESD). To prevent ESD-induced damage and/or degradation, take customary and statutory ESD precautions when handling this product.

See application note “ESD, Latchup and EMC” for more information.

# Warranty

SENSIRION warrants solely to the original purchaser of this product for a period of 12 months (one year) from the date of delivery that this product shall be of the quality, material and workmanship defined in SENSIRION’s published specifications of the product. Within such period, if proven to be defective, SENSIRION shall repair and/or replace this product, in SENSIRION’S discretion, free of charge to the Buyer, provided that:

notice in writing describing the defects shall be given to SENSIRION within fourteen (14) days after their appearance;

such defects shall be found, to SENSIRION’s reasonable satisfaction, to have arisen from SENSIRION’s faulty design, material, or workmanship; the defective product shall be returned to SENSIRION’s factory at the Buyer’s expense; and  the warranty period for any repaired or replaced product shall be limited to the unexpired portion of the original period.

This warranty does not apply to any equipment which has not been installed and used within the specifications recommended by SENSIRION for the intended and proper use of the equipment. EXCEPT FOR THE WARRANTIES EXPRESSLY SET FORTH HEREIN, SENSIRION MAKES NO WARRANTIES, EITHER EXPRESS OR IMPLIED, WITH RESPECT TO THE PRODUCT. ANY AND ALL WARRANTIES, INCLUDING WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, ARE EXPRESSLY EXCLUDED AND DECLINED.

SENSIRION is only liable for defects of this product arising under the conditions of operation provided for in the data sheet and proper use of the goods. SENSIRION explicitly disclaims all warranties, express or implied, for any period during which the goods are operated or stored not in accordance with the technical specifications.

SENSIRION does not assume any liability arising out of any application or use of any product or circuit and specifically disclaims any and all liability, including without limitation consequential or incidental damages. All operating parameters, including without limitation recommended parameters, must be validated for each customer’s applications by customer’s technical experts. Recommended parameters can and do vary in different applications.

SENSIRION reserves the right, without further notice, (i) to change the product specifications and/or the information in this document and (ii) to improve reliability, functions and design of this product.

Copyright © 2019, by SENSIRION. CMOSens® is a trademark of Sensirion All rights reserved

# Headquarters and Subsidiaries

SENSIRION AG Laubisruetistr. 50 CH-8712 Staefa ZH Switzerland

phone: +41 44 306 40 00 fax: +41 44 306 40 30 info@sensirion.com www.sensirion.com

Sensirion Inc. USA phone: +1 312 690 5858 info-us@sensirion.com www.sensirion.com

Sensirion Japan Co. Ltd. phone: +81 3 3444 4940 info-jp@sensirion.com www.sensirion.co.jp

Sensirion Korea Co. Ltd. phone: +82 31 337 7700\~3 info-kr@sensirion.com www.sensirion.co.kr

Sensirion China Co. Ltd. phone: +86 755 8252 1501 info-cn@sensirion.com www.sensirion.com.cn/

Sensirion Taiwan Co. Ltd. phone: +41 44 306 40 00 info@sensirion.com