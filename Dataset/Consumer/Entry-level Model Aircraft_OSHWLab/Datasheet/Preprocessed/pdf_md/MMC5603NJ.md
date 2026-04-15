# ±30 Gauss, Monolithic, High Performance, Low Cost 3-axis Magnetic Sensor

# MMC5603NJ

# FEATURES

 Monolithic integrated 3-axis AMR magnetic sensor and electronic circuits requiring fewer external components

 Superior Dynamic Range and Accuracy:

±30 G FSR 20bits operation mode 0.0625mG per LSB resolution 2 mG total RMS noise Enables heading accuracy of 1º  Sensor true frequency response up to 1KHz  Ultra-Small Wafer Level Package 0.8x0.8x0.4 mm

 On-chip automatic degaussing with built-in SET/RESET function  Eliminates thermal variation induced offset error (Null field output) Clears the residual magnetization resulting from strong external fields

 On-chip sensitivity compensation   
On-chip temperature sensor Selftest signal available Data_ready Interrupt (I3C only) Low power consumption 1 µA power down current I 2C slave, FAST (≤400 KHz) mode I3C interface available   
 1.62V to 3.6V wide range single power supply   
1.2V logic IO   
 RoHS compliant

# APPLICATIONS

 Electronic Compass & GPS Navigation  Position Sensing

![](images/a8b47ac96e015e505ddfd5c13319511224f35ad5e47050d05454f418ddf30b2a.jpg)

# FUNCTIONAL BLOCK DIAGRAM

# DESCRIPTION

The MMC5603NJ is a monolithic complete 3-axis AMR magnetic sensor with on-chip signal processing and integrated digital bus (I2C fast mode and I3C interface), the device can be connected directly to a microprocessor, eliminating the need for A/D converters or timing resources.

It can measure magnetic fields within the full scale range of 30 Gauss (G), with up to 0.0625mG per LSB resolution at 20bits operation mode and 2mG total RMS noise level, enabling heading accuracy of 1º in electronic compass applications. Contact MEMSIC for access to advanced calibration and tilt-compensation algorithms.

An integrated SET/RESET function provides for the elimination of error due to Null Field output change with temperature. In addition it clears the sensors of any residual magnetic polarization resulting from exposure to strong external magnets. The SET/RESET function can be performed for each measurement or periodically as the specific application requires.

The MMC5603NJ is in wafer level package with an ultra-small size of 0.8x 0.8 x 0.4 mm and with an operating temperature range from -40 C to +85 C.

SPECIFICATIONS (Measurements @ 25 C, unless otherwise noted; VDD= 1.8 V, Auto_SR_en=1, unless otherwise specified)   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=1>Field Range (Each Axis)1</td><td rowspan=1 colspan=1>Total applied field</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±30</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>G</td></tr><tr><td rowspan=1 colspan=1>Supply Voltage</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>1.62</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VIO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Supply Voltage rise time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10.0</td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=4 colspan=1>Supply Current2,3(100 measurements/second)</td><td rowspan=1 colspan=1>BW=00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.4</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>BW=01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>BW=10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>1.6</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>BW=11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>Power Down Current3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Operating Temperature</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-55</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Linearity Error3(Best fit straight line)</td><td rowspan=1 colspan=1>FS=±30GHapplied=±15 G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>%FS</td></tr><tr><td rowspan=1 colspan=1>Hysteresis3</td><td rowspan=1 colspan=1>3 sweeps across ±30 G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>%FS</td></tr><tr><td rowspan=1 colspan=1>Repeatability Error3</td><td rowspan=1 colspan=1>3 sweeps across ±30 G</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>%FS</td></tr><tr><td rowspan=1 colspan=1>Alignment Error</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1.0</td><td rowspan=1 colspan=1>±3.0</td><td rowspan=1 colspan=1>Degrees</td></tr><tr><td rowspan=1 colspan=1>Transverse Sensitivity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+2.0</td><td rowspan=1 colspan=1>±5.0</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=4 colspan=1>Total RMS Noise3</td><td rowspan=1 colspan=1>BW=00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>mG</td></tr><tr><td rowspan=1 colspan=1>BW=01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>mG</td></tr><tr><td rowspan=1 colspan=1>BW=10</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>mG</td></tr><tr><td rowspan=1 colspan=1>BW=11</td><td rowspan=1 colspan=1>[b]</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>7.0</td><td rowspan=1 colspan=1>mG</td></tr><tr><td rowspan=1 colspan=1>Output resolution</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Bits</td></tr><tr><td rowspan=4 colspan=1>Max Output data rate4</td><td rowspan=1 colspan=1>BW=00</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>HZ</td></tr><tr><td rowspan=1 colspan=1>BW=01</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>BW=10</td><td rowspan=1 colspan=1>255</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>HZ</td></tr><tr><td rowspan=1 colspan=1>BW=11</td><td rowspan=1 colspan=1>255</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>Heading accuracy3,5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1.0</td><td rowspan=1 colspan=1>±3.0</td><td rowspan=1 colspan=1>Degrees</td></tr><tr><td rowspan=4 colspan=1>Sensitivity3,6,8</td><td rowspan=1 colspan=1>+30G</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>With16bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>counts/G</td></tr><tr><td rowspan=1 colspan=1>With18bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4096</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>counts/G</td></tr><tr><td rowspan=1 colspan=1>With 20bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16384</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>counts/G</td></tr><tr><td rowspan=1 colspan=1>Sensitivity Change OverTemperature3</td><td rowspan=1 colspan=1>-40~85°℃Delta from 25 C±30 G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±5</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=4 colspan=1>Null Field Output8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>G</td></tr><tr><td rowspan=1 colspan=1>With16bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>32768</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Counts</td></tr><tr><td rowspan=1 colspan=1>With18bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>131072</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Counts</td></tr><tr><td rowspan=1 colspan=1>With 20bits operation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>524288</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Counts</td></tr><tr><td rowspan=1 colspan=1>Null Field Output Change OverTemperature3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.2</td><td rowspan=1 colspan=1>±1.0</td><td rowspan=1 colspan=1>mG/C</td></tr><tr><td rowspan=1 colspan=1>Temperature Sensor Output3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>C/Count</td></tr><tr><td rowspan=1 colspan=1>Disturbing Field7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>G</td></tr><tr><td rowspan=1 colspan=1>Maximum Exposed Field</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10,000</td><td rowspan=1 colspan=1>G</td></tr><tr><td rowspan=1 colspan=1>Output Repeatability3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>mG</td></tr></table>

1. External magnetic field on each axis not continuously higher than 16G. 2. Supply current is proportional to how many measurements performed per second, 75Hz (maximum) for BW=00. 3. Based on 3lots characterization result. 4. The 1000 Hz ODR is available by writing 255 into Register ODR and setting hpower to 1. 5. MEMSIC product enables users to utilize heading accuracy to be 1.0 degree typical when using MEMSIC’s proprietary software or algorithm. 6. Sensitivity of the orthogonal axes is analytically derived from raw data and is subsequently processed by MEMSIC software drivers. 7. This is the magnitude of external field that can be tolerated without changing the sensor characteristics. If the disturbing field is exceeded, a SET/RESET operation is required to restore proper sensor operation. 8. Based on shipment test result.

# NOTES:

# I 2C INTERFACE I/O CHARACTERISTICS (VIO=1.8 V)

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Condition</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Logic Input Low Level</td><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3*V10</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Logic Input High Level</td><td rowspan=1 colspan=1>ViH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7*V10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Vio</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Hysteresis of Schmitt input</td><td rowspan=1 colspan=1>Vhys</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Logic Output Low Level</td><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1> Input Leakage Current</td><td rowspan=1 colspan=1>li</td><td rowspan=1 colspan=1>0.1Vio&lt;Vin&lt;0.9Vio</td><td rowspan=1 colspan=1>-10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>SCL Clock Frequency</td><td rowspan=1 colspan=1>fscL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>START Hold Time</td><td rowspan=1 colspan=1>tHD;STA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>START Setup Time</td><td rowspan=1 colspan=1>tSU,STA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>LOW period of SCL</td><td rowspan=1 colspan=1>tLow</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>HIGH period of SCL</td><td rowspan=1 colspan=1>tHIGH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Data Hold Time</td><td rowspan=1 colspan=1>tHD;DAT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Data Setup Time</td><td rowspan=1 colspan=1>tsU;DAT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Rise Time</td><td rowspan=1 colspan=1>tr</td><td rowspan=1 colspan=1>From ViL to ViH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Fall Time</td><td rowspan=1 colspan=1>tf</td><td rowspan=1 colspan=1>From ViH to ViL</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Bus Free Time Between STOP andSTART</td><td rowspan=1 colspan=1>tBUF</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>STOP Setup Time</td><td rowspan=1 colspan=1>tsU;STO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr></table>

![](images/aecbeb36085d970fe2b44a1d1a78714f6a65bf51f74f86c9c2f49db323f7ed4f.jpg)

# ABSOLUTE MAXIMUM RATINGS\*

Supply Voltage Storage Temperature Maximum Exposed Field

-0.5 to +5 V -55 C to +125 C 10000 G

Note: Stresses above those listed under Absolute Maximum Ratings may cause permanent damage to the device. This is a stress rating only; the functional operation of the device at these or any other conditions above those indicated in the operational sections of this specification is not implied. Exposure to absolute maximum rating conditions for extended periods may affect the device’s reliability.

Pin Description: WLP Package   

<table><tr><td rowspan=1 colspan=1>Pin</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Io</td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>VSA</td><td rowspan=1 colspan=1>Connect to Ground</td><td rowspan=1 colspan=1>P</td></tr><tr><td rowspan=1 colspan=1>A2</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>Serial Clock Line</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>Power Supply</td><td rowspan=1 colspan=1>P</td></tr><tr><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>Serial Data Line</td><td rowspan=1 colspan=1>O</td></tr></table>

All parts are shipped in tape and reel packaging with 10000pcs (or 5000pcs per requested) per 7” reel.

# Caution:

This is an Electro-static Discharge (ESD) sensitive device.

Ordering Guide:

Package type:

<table><tr><td>Code</td><td>Type</td></tr><tr><td>J</td><td>WLP package RoHS compliant</td></tr></table>

Performance Grade:

![](images/55b12afc31ac85a7459f1b214d05f340a2d4350ac0c2d6a2df6058167ec19e5c.jpg)

<table><tr><td>Code</td><td>Performance Grade</td></tr><tr><td>N</td><td>Temp compensated</td></tr></table>

# MARKING ILLUSTRATION

![](images/9881c1072c343f6af2c4e75ba9daeb9ea874d4a4ad7605ec6df843fb645a1d4f.jpg)

Note: “Number” (top-left character) is used to differentiate between similar devices. The black dot marks the location of pin one (1). The 2nd line represents the device’s Lot Number.

# THEORY OF OPERATION

The Anisotropic Magneto-Resistive (AMR) sensors are special resistors made of permalloy thin film deposited on a silicon wafer. During manufacturing, a strong magnetic field is applied to the film to orient its magnetic domains in the same direction, establishing a magnetization vector. Subsequently, an external magnetic field applied perpendicularly to the sides of the film causes the magnetization to rotate and change angle. This effect causes the film’s resistance to vary with the intensity of the applied magnetic field. The MEMSIC AMR sensor is incorporated into a Wheatstone bridge configuration to maximize Signal to Noise ratio. A change in magnetic field produces a proportional change in differential voltage across the Wheatstone bridge

However, the influence of a strong magnetic field (more than 30 G) in any direction could upset, or flip, the polarity of the film, thus changing the sensor characteristics. A strong restoring magnetic field must be applied momentarily to restore, or set, the sensor characteristics. The MEMSIC magnetic sensor has an on-chip magnetically coupled strap: a SET/RESET strap pulsed with a high current, to provide the restoring magnetic field.

# EXTERNAL CIRCUITRY CONNECTION

The MMC5603NJ can operate from a single 1.62V to 3.6V supply. The circuit connection diagrams below illustrate power supply connection options.

![](images/1077779380a01c1c110fc758d8e24aed92b371c4e80edd2c275ea8d28dd6d712.jpg)

<TOP VIEW> Connection Block Diagram

# PIN DESCRIPTIONS

VDD – This is the power supply pin. MEMSIC recommends a minimum bypass capacitor of 2.2 µF placed in close proximity to the VDD pin.

VSA – This is the ground pin for the magnetic sensor.   
SDA – This pin is the I3C/I2C serial data line.   
SCL– This pin is the I3C/I2C serial clock line.

# HARDWARE DESIGN CONSIDERATION

Provide adequate separation distance to devices that contain permanent magnets or generate magnetic fields (e.g. speakers, coils, inductors) The combined magnetic field to be measured and interference magnetic field should be less than the full scale range of the MMC5603NJ (±30 G).   
 Provide adequate separation distance to current carrying traces. Do not route current carrying traces under the sensor or on the other side of the PCB opposite the device.   
✓ Do not cover the sensor with magnetized material or material that may become magnetized, (e.g., shield box, LCD, battery, iron bearing material).   
Do not place the device opposite magnetized material or material that may become magnetized located on the other side of the PCB.

Details please refer to MEMSIC Magnetic Sensor Hardware Design Layout Guideline for Electronic Device.

# POWER CONSUMPTION

The power consumed by the device is proportional to the number of measurements taken per second. For example, when BW<1:0>=10, MMC5603NJ consumes 1.3mA (typical) at 1.8V with 100 measurements per second. If only 1 measurements are performed per second, the current will be 1300\*1/100=13µA.

# I2C INTERFACE DESCRIPTION

A slave mode I2C circuit has been implemented into the MEMSIC magnetic sensor as a standard interface for customer applications. The A/D converter functionality have been added to the MEMSIC sensor, thereby increasing ease-of-use, and lowering power consumption, footprint and total solution cost.

The I2C (or Inter IC bus) is an industry standard bidirectional two-wire interface bus. A master I2C device can operate READ/WRITE controls to 128 devices by device addressing. The MEMSIC magnetic sensor operates only in a slave mode, i.e. only responding to calls by a master device.

# I 2C BUS CHARACTERISTICS

![](images/98fc1009baf10b74098fc07c56fec4c0189f1f03dbbb72d1fc46b9dee8135906.jpg)

The two wires in the I2C bus are called SDA (serial data line) and SCL (serial clock line). In order for a data transfer to start, the bus has to be free, which is defined by both wires in a HIGH output state. Due to the opendrain/pull-up resistor structure and wired Boolean “AND” operation, any device on the bus can pull lines low and overwrite a HIGH signal. The data on the SDA line has to be stable during the HIGH period of the SCL line. In other words, valid data can only change when the SCL line is LOW.

Note: Rp selection guide: 2.7Kohm for a short I2C bus length (less than 10 cm), and 10Kohm for a bus length less than 5 cm.

REGISTER MAP   

<table><tr><td rowspan=1 colspan=1>Register Name</td><td rowspan=1 colspan=1>Address (HEX)</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Xouto</td><td rowspan=1 colspan=1>00H</td><td rowspan=1 colspan=1>Xout[19:12]</td></tr><tr><td rowspan=1 colspan=1>Xout1</td><td rowspan=1 colspan=1>01H</td><td rowspan=1 colspan=1>Xout[11:4]</td></tr><tr><td rowspan=1 colspan=1>Youto</td><td rowspan=1 colspan=1>02H</td><td rowspan=1 colspan=1>Yout[19:12]</td></tr><tr><td rowspan=1 colspan=1>Yout1</td><td rowspan=1 colspan=1>03H</td><td rowspan=1 colspan=1>Yout[11:4]</td></tr><tr><td rowspan=1 colspan=1>Zouto</td><td rowspan=1 colspan=1>04H</td><td rowspan=1 colspan=1>Zout[19:12]</td></tr><tr><td rowspan=1 colspan=1>Zout1</td><td rowspan=1 colspan=1>05H</td><td rowspan=1 colspan=1>Zout[11:4]</td></tr><tr><td rowspan=1 colspan=1>Xout2</td><td rowspan=1 colspan=1>06H</td><td rowspan=1 colspan=1>Xout[3:0]</td></tr><tr><td rowspan=1 colspan=1>Yout2</td><td rowspan=1 colspan=1>07H</td><td rowspan=1 colspan=1>Yout[3:0]</td></tr><tr><td rowspan=1 colspan=1>Zout2</td><td rowspan=1 colspan=1>08H</td><td rowspan=1 colspan=1>Zout[3:0]</td></tr><tr><td rowspan=1 colspan=1>Tout</td><td rowspan=1 colspan=1>09H</td><td rowspan=1 colspan=1>Temperature output</td></tr><tr><td rowspan=1 colspan=1>Status1</td><td rowspan=1 colspan=1>18H</td><td rowspan=1 colspan=1>Device status1</td></tr><tr><td rowspan=1 colspan=1>ODR</td><td rowspan=1 colspan=1>1AH</td><td rowspan=1 colspan=1>Output data rate</td></tr><tr><td rowspan=1 colspan=1>Internal control 0</td><td rowspan=1 colspan=1>1BH</td><td rowspan=1 colspan=1>Control register 0</td></tr><tr><td rowspan=1 colspan=1>Internal control 1</td><td rowspan=1 colspan=1>1CH</td><td rowspan=1 colspan=1>Control register 1</td></tr><tr><td rowspan=1 colspan=1>Internal control 2</td><td rowspan=1 colspan=1>1DH</td><td rowspan=1 colspan=1>Control register 2</td></tr><tr><td rowspan=1 colspan=1>ST X TH</td><td rowspan=1 colspan=1>1EH</td><td rowspan=1 colspan=1>X-axis selftest threshold</td></tr><tr><td rowspan=1 colspan=1>ST Y_TH</td><td rowspan=1 colspan=1>1FH</td><td rowspan=1 colspan=1>Y-axis selftest threshold</td></tr><tr><td rowspan=1 colspan=1>ST Z_TH</td><td rowspan=1 colspan=1>20H</td><td rowspan=1 colspan=1>Z-axis selftest threshold</td></tr><tr><td rowspan=1 colspan=1>ST X</td><td rowspan=1 colspan=1>27H</td><td rowspan=1 colspan=1>X-axis selftest set value</td></tr><tr><td rowspan=1 colspan=1>STY</td><td rowspan=1 colspan=1>28H</td><td rowspan=1 colspan=1>Y-axis selftest set value</td></tr><tr><td rowspan=1 colspan=1>ST Z</td><td rowspan=1 colspan=1>29H</td><td rowspan=1 colspan=1>Z-axis selftest set value</td></tr><tr><td rowspan=1 colspan=1>Product ID</td><td rowspan=1 colspan=1>39H</td><td rowspan=1 colspan=1>Product ID</td></tr></table>

# REGISTER DETAILS

Xout0, Xout1, Xout2

<table><tr><td rowspan=1 colspan=1>Xouto</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 00H</td><td rowspan=1 colspan=8>Xout[19:12]</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Xout1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 01H</td><td rowspan=1 colspan=8>Xout[11:4]</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Xout2</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 06H</td><td rowspan=1 colspan=4>Xout[3:0]</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

X-axis output, unsigned format.

<table><tr><td rowspan=1 colspan=1>X-axis output</td><td rowspan=1 colspan=1>Data</td></tr><tr><td rowspan=1 colspan=1>16bits operation mode</td><td rowspan=1 colspan=1>Xout[19:4]</td></tr><tr><td rowspan=1 colspan=1>18bits operation mode</td><td rowspan=1 colspan=1>Xout[19:2]</td></tr><tr><td rowspan=1 colspan=1>20bits operation mode</td><td rowspan=1 colspan=1>Xout[19:0]</td></tr></table>

Yout0, Yout1, Yout2   

<table><tr><td>Youto</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2 1</td><td></td><td>0</td></tr><tr><td>Addr: 02H</td><td colspan="6">Yout[19:12]</td><td></td><td></td></tr><tr><td>Mode</td><td colspan="9">Read-only</td></tr></table>

<table><tr><td>Yout1</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>Addr: 03H</td><td colspan="8">Yout[11:4]</td></tr><tr><td>Mode</td><td colspan="9">Read-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Yout2</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 07H</td><td rowspan=1 colspan=4>Yout[3:0]</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

Y-axis output, unsigned format.

<table><tr><td rowspan=1 colspan=1>Y-axis output</td><td rowspan=1 colspan=1>Data</td></tr><tr><td rowspan=1 colspan=1>16bits operation mode</td><td rowspan=1 colspan=1>Yout[19:4]</td></tr><tr><td rowspan=1 colspan=1>18bits operation mode</td><td rowspan=1 colspan=1>Yout[19:2]</td></tr><tr><td rowspan=1 colspan=1>20bits operation mode</td><td rowspan=1 colspan=1>Yout[19:0]</td></tr></table>

# Zout0, Zout1, Zout2

<table><tr><td rowspan=1 colspan=1>Zouto</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5            4            3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 04H</td><td rowspan=1 colspan=6>Zout[19:12]</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=6>Read-only</td></tr></table>

<table><tr><td>Zout1</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>Addr: 05H</td><td colspan="8">Zout[11:4]</td></tr><tr><td>Mode</td><td colspan="9">Read-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Zout2</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6           5           4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>Zout[3:0]</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 08H</td><td rowspan=2 colspan=6>Read-only</td></tr><tr><td rowspan=1 colspan=1>Mode</td></tr></table>

Z-axis output, unsigned format.   

<table><tr><td rowspan=1 colspan=1>Z-axis output</td><td rowspan=1 colspan=1>Data</td></tr><tr><td rowspan=1 colspan=1>16bitsoperation mode</td><td rowspan=1 colspan=1>Zout[19:4]</td></tr><tr><td rowspan=1 colspan=1>18bitsoperation mode</td><td rowspan=1 colspan=1>Zout[19:2]</td></tr><tr><td rowspan=1 colspan=1>20bitsoperation mode</td><td rowspan=1 colspan=1>Zout[19:0]</td></tr></table>

# Temperature Out

<table><tr><td rowspan=1 colspan=1>Temperature</td><td rowspan=1 colspan=1>7            6</td><td rowspan=1 colspan=1>5            4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 09H</td><td rowspan=1 colspan=6>Tout[7:0]</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=6>Read-only</td></tr></table>

Temperature output, unsigned format. The range is -75-125°C, about 0.8°C/LSB, 00000000 stands for -75°C

Status1   

<table><tr><td rowspan=1 colspan=1>Device Status1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 18H</td><td rowspan=1 colspan=1>Meas_tdone</td><td rowspan=1 colspan=1>Meas_mdone</td><td rowspan=1 colspan=1>Sat_sensor</td><td rowspan=1 colspan=1>OTP_readdone</td><td rowspan=1 colspan=1>ST_Fail</td><td rowspan=1 colspan=1>Mdt_flagint</td><td rowspan=1 colspan=1>Meas_t_doneint</td><td rowspan=1 colspan=1>Meas_mdone_int</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Bit Name</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Meas m done int</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>Meas t done int</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>Mdt flag int</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>ST Fail</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>OTP_read_done</td><td rowspan=1 colspan=1>This bit is an indicator of successfully reading its OTP memory either as part of its power upsequence, or after an I2C command that reloads the OTP memory, such as resetting the chipand refreshing the OTP registers.</td></tr><tr><td rowspan=1 colspan=1>Sat sensor</td><td rowspan=1 colspan=1>This bit is an indicator of the selftest signal, it keeps low once the device PASS selftest.</td></tr><tr><td rowspan=1 colspan=1>Meas_m_done</td><td rowspan=1 colspan=1>This bit indicates that a measurement of magnetic field is done and the data is ready to beread. This bit is reset only when any of the magnetic data registers is read.</td></tr><tr><td rowspan=1 colspan=1>Meas_t_done</td><td rowspan=1 colspan=1>This bit indicates that a measurement of temperature is done and the data is ready to be read.This bit is reset only when the temperature register is read.</td></tr></table>

ODR   

<table><tr><td rowspan=1 colspan=1>ODR</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1AH</td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=3>ODR[7:0]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=4>0            0           0           0</td><td rowspan=1 colspan=3>0          0            0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Bit Name</td><td rowspan=1 colspan=4>Description</td></tr><tr><td rowspan=6 colspan=1>ODR[7:0]</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>BW</td><td rowspan=1 colspan=1>Automatic SET/RESET</td><td rowspan=1 colspan=1>No SET/RESET</td><td rowspan=1 colspan=1>ODR range</td></tr><tr><td rowspan=1 colspan=1>00</td><td rowspan=1 colspan=1>75Hz</td><td rowspan=1 colspan=1>150Hz</td><td rowspan=1 colspan=1>1~75</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>150Hz</td><td rowspan=1 colspan=1>255 Hz</td><td rowspan=1 colspan=1>1~150</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>255 Hz</td><td rowspan=1 colspan=1>255 Hz</td><td rowspan=1 colspan=1>1~255</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>255Hz</td><td rowspan=1 colspan=1>hpower=0: 255 Hz;hpower=1: 1000 Hz</td><td rowspan=1 colspan=1>1~255</td></tr></table>

Internal Control 0   

<table><tr><td rowspan=1 colspan=1>ControlRegister 0</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1BH</td><td rowspan=1 colspan=1>Cmm_freqen</td><td rowspan=1 colspan=1>Auto_sten</td><td rowspan=1 colspan=1>Auto_SRen</td><td rowspan=1 colspan=1>Do Reset</td><td rowspan=1 colspan=1>Do Set</td><td rowspan=1 colspan=1>Start_MDT</td><td rowspan=1 colspan=1>Take_meas_T</td><td rowspan=1 colspan=1>Take_meas_M</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Bit Name</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Take_meas_M</td><td rowspan=1 colspan=1>Take Measure of Magnetic field, or TM_M bit. Writing a 1 into this location causes the chip toperform a magnetic measurement. This bit is self-clearing at the end of each measurement.</td></tr><tr><td rowspan=1 colspan=1>Take_meas_T</td><td rowspan=1 colspan=1>Take Measure of Temperature, or TM_T bit. Writing a 1 into this location causes the chip toperform a temperature measurement. This bit is self-clearing at the end of each measurement.</td></tr><tr><td rowspan=1 colspan=1>Start_MDT</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>Do Set</td><td rowspan=1 colspan=1>Writing a 1 into this location will cause the chip to do the Set operation, which will allow large setcurrent to flow through the sensor coils for 375ns. This bit is self-cleared at the end of Setoperation.</td></tr><tr><td rowspan=1 colspan=1>Do Reset</td><td rowspan=1 colspan=1>Writing a 1 into this location wil cause the chip to do the Reset operation, which will allow largereset current to flow through the sensor coils for 375ns. This bit is self-cleared at the end of Resetoperation.</td></tr><tr><td rowspan=1 colspan=1>Auto_SR_en</td><td rowspan=1 colspan=1>Writing a 1 into this location wil enable the function of automatic set/reset. This function appliesto both on-demand and continuous-time measurements. This bit must be set to 1 in order toactivate the feature of periodic set. This bit is recommended to set to &quot;1&quot; in the application.</td></tr><tr><td rowspan=1 colspan=1>Auto_st_en</td><td rowspan=1 colspan=1>Writing a 1 into this location will enable the function of automatic self-test. The threshold inregister 1EH, 1FH, 20H should be set before this bit is set to 1. This bit clears itself after theoperation is completed.</td></tr><tr><td rowspan=1 colspan=1>Cmm_freq_en</td><td rowspan=1 colspan=1>Writing a 1 into this location wil start the calculation of the measurement period according to theODR. This bit should be set before continuous-mode measurements are started. This bit is self-cleared after the measurement period is calculated by internal circuits.</td></tr></table>

# Internal Control 1

<table><tr><td rowspan=1 colspan=1>ControlRegister 1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1CH</td><td rowspan=1 colspan=1>Sw_reset</td><td rowspan=1 colspan=1>St_enm</td><td rowspan=1 colspan=1>St enp</td><td rowspan=1 colspan=1>Z-inhibit</td><td rowspan=1 colspan=1>Y-inhibit</td><td rowspan=1 colspan=1>X-inhibit</td><td rowspan=1 colspan=1>BW1</td><td rowspan=1 colspan=1>BWO</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

<table><tr><td colspan="1" rowspan="1">Bit Name</td><td colspan="3" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="6">BW0&amp;BW1</td><td colspan="3" rowspan="6">These bandwidth selection bits adjust the length of the decimation fiter. They control the durationof each measurement.BW1     BWO    Measurement Time0         0        6.6ms0          1        3.5ms1          0        2.0ms1         1        1.2msNote: X/YiZ channel measurements are taken sequentially. Delay Time among thosemeasurements is 1/3 of the Measurement Time defined in the table.</td></tr><tr><td colspan="1" rowspan="1">BW1</td><td colspan="1" rowspan="1">BWO</td><td colspan="1" rowspan="1">Measurement Time</td></tr><tr><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">6.6ms</td></tr><tr><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">3.5ms</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">2.0ms</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1.2ms</td></tr><tr><td colspan="1" rowspan="1">X-inhibit</td><td colspan="3" rowspan="3">Writing "1" will disable this channel, and reduce Measurement Time and total charge permeasurement.When a channel is disabled it is simply skipped during Take Measure routine. Itsoutput register is not reset and wil maintain the last value written to it when this channel wasactive. Note: Y/Z needs to be inhibited the same time in case needed.</td></tr><tr><td colspan="1" rowspan="1">Y-inhibit</td></tr><tr><td colspan="1" rowspan="1">Z-inhibit</td></tr><tr><td colspan="1" rowspan="1">St_enp</td><td colspan="3" rowspan="1">Writing 1 into this location will bring a DC current through the self-test coil of the sensor. Thiscurrent will cause an offset of the magnetic field. This function is used to check whether thesensor has been saturated.</td></tr><tr><td colspan="1" rowspan="1">St_enm</td><td colspan="3" rowspan="1">The function of this bit is similar to ST_ENP, but the offset of the magnetic field is of oppositepolarity.</td></tr><tr><td>Sw_reset</td><td colspan="3">Software Reset. Writing "1"will cause the part to reset, similar to power-up. lt willclear all registers and also re-read OTP as part of its startup routine. The power on time is 20mS.</td></tr></table>

# Internal Control 2

<table><tr><td rowspan=1 colspan=1>ControlRegister 2</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1DH</td><td rowspan=1 colspan=1>hpower</td><td rowspan=1 colspan=1>INT_measdone en</td><td rowspan=1 colspan=1>INT_mdten</td><td rowspan=1 colspan=1>Cmm_en</td><td rowspan=1 colspan=1>En_prd_set</td><td rowspan=1 colspan=3>Prd_set[2:0]</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Bit Name</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Prd_set[2:0]</td><td rowspan=1 colspan=1>These bits determine how many measurements are done before a set is executed, when thepart is in continuous mode and the automatic set/reset is enabled. From 000 to 111, the sensorwill do one set for every 1, 25, 75, 100, 250, 500, 1000, and 2000 samples. In order to enablethis feature, both En_prd_set and Auto_SR must be set to 1, and the part should work incontinuous mode. Please note that during this operation, the sensor will not be reset.</td></tr><tr><td rowspan=1 colspan=1>En prd set</td><td rowspan=1 colspan=1>Writing 1 into this location will enable the function of periodical set.</td></tr><tr><td rowspan=1 colspan=1>Cmm_en</td><td rowspan=1 colspan=1>The device will enter continuous mode, if ODR has been set to a non-zero value and a 1 hasbeen writen into Cmm_freq_en. The internal counter wil start counting as well since this bitis set.</td></tr><tr><td rowspan=1 colspan=1>INT_mdt en</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>INT_ meas done_en</td><td rowspan=1 colspan=1>Factory use only, reset value is 0.</td></tr><tr><td rowspan=1 colspan=1>hpower</td><td rowspan=1 colspan=1>If this bit is set to 1 to achieve 1000Hz ODR.</td></tr></table>

# ST_X_TH

<table><tr><td rowspan=1 colspan=1>ST X TH</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1EH</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>ST X TH[7:0]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=3>0            0           0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>0           0            0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

X-axis selftest threshold

# ST_Y_TH

<table><tr><td rowspan=1 colspan=1>ST Y_TH</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 1FH</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=4>0            0           0           0</td><td rowspan=1 colspan=4>0            0           0           0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Write-only</td></tr></table>

Y-axis selftest threshold

# ST_Z_TH

<table><tr><td>ST Z TH</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>Addr: 20H</td><td></td><td></td><td></td><td>ST Z TH[7:0]</td><td></td><td></td><td></td><td></td></tr><tr><td>Reset Value</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Mode</td><td colspan="8">Write-only</td></tr></table>

Z-axis selftest threshold

ST_X   

<table><tr><td rowspan=1 colspan=1>ST X</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 27H</td><td rowspan=1 colspan=8>ST_X[7:0]</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=8>Factory stored value</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read/Write</td></tr></table>

X-axis selftest set value

ST_Y   

<table><tr><td rowspan=1 colspan=1>ST Y</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6           5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1            0</td></tr><tr><td rowspan=1 colspan=1>Addr: 28H</td><td rowspan=1 colspan=6>ST_Y[7:0]</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=6>Factory stored value</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=6>Read/Write</td></tr></table>

Y-axis selftest set value

# ST_Z

<table><tr><td rowspan=1 colspan=1>ST Z</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6           5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 29H</td><td rowspan=1 colspan=7>ST Z[7:0]</td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=7>Factory stored value</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=7>Read/Write</td></tr></table>

Z-axis selftest set value

# Product ID 1

<table><tr><td rowspan=1 colspan=1>Product ID 1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Addr: 39H</td><td rowspan=1 colspan=4>Product ID1[7:0]</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>Reset Value</td><td rowspan=1 colspan=3>0            0           0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0           0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=8>Read-only</td></tr></table>

Product ID, used to recognize device.

# I 2C INTERFACE OPERATION:

# DATA TRANSFER

A data transfer is started with a “START” condition and ended with a “STOP” condition. A “START” condition is defined by a HIGH to LOW transition on the SDA line while SCL line is HIGH. A “STOP” condition is defined by a LOW to HIGH transition on the SDA line while the SCL line is held HIGH. All data transfer in I2C system are 8-bits long. Each byte has to be followed by an acknowledge bit. Each data transfer involves a total of 9 clock cycles. Data is transferred starting with the most significant bit (MSB).

After a START condition, the master device calls a specific slave device by sending its 7-bit address with the 8th bit (LSB) indicating that either a READ or WRITE operation will follow, [1] for READ and [0] for WRITE. The MEMSIC device 7-bit device address is [0110000] where the three LSB’s are pre-programmed into the MMC5603NJ by the factory.

Note: A total of 8 different addresses can be preprogrammed into MEMSIC device by the factory. This variation of I2C address avoids a potential address conflict, either by ICs from other manufacturers or by other MEMSIC devices on the same bus.

The initial addressing of the slave is always followed by the master writing the number of the slave register to be read or written, so this initial addressing always indicates a WRITE operation by sending [01100000]. After being addressed, the MEMSIC device being called should respond by an “Acknowledge” signal by pulling SDA line LOW. Subsequent communication bytes can either be

a) The data to be written to the device register, or   
b) Another START condition followed by the device address indicating a READ operation [01100001], and then the master reads the register data.

Multiple data bytes can be written or read to numerically sequential registers without the need of another START condition. Data transfer is terminated by a STOP condition or another START condition. Two detailed examples of communicating with the MEMSIC device are listed below for the actions of acquiring a magnetic field measurement and magnetizing the sensor.

# EXAMPLE OF MEASUREMENT

1st cycle: A START condition is established by the Master Device followed by a call to the slave address [0110000] with the eighth bit held low to indicate a WRITE request.

2nd cycle: After an acknowledge signal is received by the master device (MEMSIC device pulls SDA line low during 9th SCL pulse), the master device sends the address of Control Register 0 as the target register to be written. The MEMSIC device should acknowledge receipt of the address (9th SCL pulse, SDA pulled low).

3rd cycle: The Master device writes to the Internal Control Register 0 the code [00100001] (TM_M and Auto_SR_en high) to initiate data acquisition. The MEMSIC device should send an Acknowledge and internally initiate a measurement (collect x, y and z data). A STOP condition indicates the end of the write operation.

4th cycle: The Master device sends a START command followed by the MEMSIC device’s seven bit address, and finally the eighth bit set low to indicate a WRITE. An Acknowledge should be send by the MEMSIC device in response.

5th cycle: The Master device sends the MEMSIC Device Status Register1 as the address to read.

6th cycle: The Master device sends a START command followed by the MEMSIC device’s seven bit address, and finally the eighth bit set high to indicate a READ. An Acknowledge should be send by the MEMSIC device in response.

7th cycle: The Master device cycles the SCL line. This causes the Status Register data to appear on SDA line. Continuously read the Device Status Register1 until the Meas_M_Done bit (bit 1) is set to ‘1’. This indicates that data for the x, y, and z sensors is available to be read.

8th cycle: The Master device sends a START command followed by the MEMSIC device’s seven bit address, and finally the eighth bit set low to indicate a WRITE. An Acknowledge should be send by the MEMSIC device in response.

9th cycle: The Master device sends a [00000000] (Xout LSB register address) as the register address to read.

10th cycle: The Master device calls the MEMSIC device’s address with a READ (8th SCL cycle SDA line high). An Acknowledge should be send by the MEMSIC device in response.

11th cycle: Master device continues to cycle the SCL line, and each consecutive byte of data from the X, Y and Z registers should appear on the SDA line. The internal memory address pointer automatically moves to the next byte. The Master device acknowledges each. Thus:

12th cycle: Xout[19:12].

13th cycle: Xout[11:4].

14th cycle: Yout[19:12].

15th cycle: Yout[11:4].

16th cycle: Zout[19:12].

17th cycle: Zout[11:4].

18th cycle: Xout[3:2] for 18bits mode. Xout[3:0] for   
20bits mode   
19th cycle: Yout[3:2] for 18bits mode. Yout[3:0] for   
20bits mode   
20th cycle: Zout[3:2] for 18bits mode. Zout[3:0] for   
20bits mode:0].

Master ends communications by NOT sending an ‘Acknowledge’ and also follows with a ‘STOP’ command.

# EXAMPLE OF CONTINUOUS MODE

The MMC5603NJ is designed with an on-chip continuous mode, or CMM. When enabled, the part will periodically take a measurement and store the results in I2C register. The frequency of these measurements is controlled by a setting in I2C register. The results of the last measurement can be read by the host. This mode, while it consumes more current, eliminates the need for the host to request measurements every time.

First the user needs to write the desired number into ODR[7:0]. It should be a non-zero integer, otherwise the continuous mode will not be activated. Then Cmm_freq_en is set to 1 to let the internal circuitry to calculate the target number for the counter. After that Cmm_en is set to 1 and the continuous mode is started and the internal counter starts to count at the same time.

# EXAMPLE OF SET

1st cycle: A START condition is established by the Master Device followed by a call to the slave address [0110000] with the eighth bit held low to indicate a WRITE request.

2nd cycle: After an acknowledge signal is received by the master device (The MEMSIC device pulls the SDA line low during the 9th SCL pulse), the master device sends [00011011] as the target address (Internal Control Register 0). The MEMSIC device should acknowledge receipt of the address (9th SCL pulse).

3rd cycle: The Master device writes to the MEMSIC device’s Internal Control 0 register the code [00001000] (SET bit) to initiate a SET action. The MEMSIC device should send an Acknowledge.

# EXAMPLE OF RESET

1st cycle: A START condition is established by the Master Device followed by a call to the slave address [0110000] with the eighth bit held low to indicate a WRITE request.

2nd cycle: After an acknowledge signal is received by the master device (The MEMSIC device pulls the SDA line low during the 9th SCL pulse), the master device sends [00011011] as the target address (Internal Control Register 0). The MEMSIC device should acknowledge receipt of the address (9th SCL pulse).

3rd cycle: The Master device writes to the MEMSIC device’s Internal Control 0 register the code [00010000] (RESET bit) to initiate a RESET action. The MEMSIC device should send an Acknowledge.

At this point, the MEMSIC AMR sensors have been conditioned for optimum performance and data measurements can commence.

# Note:

 The RESET action can be skipped for most applications

# USING SET AND RESET TO REMOVE BRIDGE OFFSET

The integrated SET and RESET functions of the MMC5603NJ enables the user to remove the error associated with bridge Offset change as a function of temperature, thereby enabling more precise heading measurements over a wider temperature than competitive technologies. The SET and RESET functions effectively alternately flip the magnetic sensing polarity of the sensing elements of the device.

1) The most accurate magnetic field measurements can be obtained by using the protocol described as follows: Perform SET. This sets the internal magnetization of the sensing resistors in the direction of the SET field.   
2) Perform MEASUREMENT. This measurement will contain not only the sensors response to the external magnetic field, H, but also the Offset; in other words, Output1 = +H + Offset.   
3) Perform RESET. This resets the internal magnetization of the sensing resistors in the direction of the RESET field, which is opposite to the SET field (180o opposed).   
4) Perform MEASUREMENT. This measurement will contain both the sensors response to the external field and also the Offset. In other words, Output2 = -H + Offset.   
5) Finally, calculate H by subtracting the two measurements and dividing by 2. This procedure effectively eliminates the Offset from the measurement and therefore any changes in the Offset over temperature. H = (Output1-Ouput2)/2.

# Note:

To calculate and store the offset; add the two measurements and divide by 2. This calculated offset value can be subtracted from subsequent measurements to obtain H directly from each measurement.

# EXAMPLE OF SELFTEST

The MMC5603NJ is designed with an on-chip selftest signal to do self-diagnose of the sensor:

1) Read out the selftest signal stored at register 27H, 28H, and 29H.   
2) Calculate the selftest signal threshold with 80% of the data readout from above registers.   
3) Write the threshold in to the register 1EH, 1FH, and 20H.   
4) Write [01000001] (TM_M and auto_st_en high) to Internal Control Register 1BH to initiate a selftest.   
5) Read out value of Sat_sensor bit at the Device Status register 18H.   
6) Sat_sensor=0, PASS selftest.

![](images/fdbc6a74b27460987d24c42776e2015bdccd2c6add936248b448ff79503b5053.jpg)

# Operating Timing Diagram

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Time to operate device after VDD valid</td><td rowspan=1 colspan=1>top</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>Minimum time interval between SET or RESET toother operations</td><td rowspan=1 colspan=1>tSR</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=4 colspan=1></td><td rowspan=1 colspan=1>tTmBW=00</td><td rowspan=1 colspan=1>6.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tTm BW=01</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tTmBW=10</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>tTm BW=11</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr></table>

# SOLDERING RECOMMENDATIONS

MEMSIC magnetic sensor is capable of withstanding an MSL1 / 260 ºC solder reflow. Following is the reflow profile:

![](images/05a5197bd74f146c8e9a3ad62060846ef8bc810df0b6fa7688e4d54320fcc8ac.jpg)  
  
Time (S)

# Note:

The second reflow cycle should be applied after device has cooled down to 25 Ԩ (room temperature)  This is the reflow profile for Pb free process  The peak temperature on the sensor surface should be limited under 260 Ԩ for 10 seconds.  Solder paste’s reflow recommendation should be followed to get the best SMT quality.

If the part is mounted manually, please ensure the temperature could not exceed 260 Ԩ for 10 seconds.

![](images/f3eb63a0a1a58e49308c7796f0c8c2cd3a726b336188c5c0244efa9be1fe49d2.jpg)

(SIDE VIEW)

UNIT: mm

![](images/a6ea1551a434b0b444b318d39e4baa1531a04e3734272b250fc66b38cbe4cd33.jpg)

# RELATIONSHIP BETWEEN THE MAGNETIC FIELD AND OUTPUT CODE

The measurement data increases as the magnetic flux density increases in the arrow directions.

![](images/9f70883c078fc5f1deb070c7ab3be37f0125cb6b9a8f76233893f749114bbf8f.jpg)