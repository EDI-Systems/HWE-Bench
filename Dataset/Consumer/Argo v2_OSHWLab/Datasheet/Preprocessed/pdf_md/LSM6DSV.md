# 6-axis inertial measurement unit (IMU) and AI sensor with embedded sensor fusion, Qvar for high-end applications

![](images/d9f4e8270a3e32315794765dbf829a246bc56e9c9a63f4e50bbf6250b30f57f5.jpg)

# LGA-14L (2.5 × 3.0 × 0.83 mm) typ.

![](images/2bc97af14514bbc47a370817da92f7b1c2a1be8efdaae69e2ff9474ff73bcb2b.jpg)

<table><tr><td>Product status link</td></tr><tr><td>LSM6DSV16X</td></tr></table>

<table><tr><td rowspan=1 colspan=3>Product summary</td></tr><tr><td rowspan=1 colspan=1>Order code</td><td rowspan=1 colspan=1>LSM6DSV16X</td><td rowspan=1 colspan=1>LSM6DSV16XTR</td></tr><tr><td rowspan=1 colspan=1>Temp. range$[^C]</td><td rowspan=1 colspan=2>-40 to +85</td></tr><tr><td rowspan=1 colspan=1>Package</td><td rowspan=1 colspan=2>LGA-14L(2.5× 3.0 × 0.83 mm)</td></tr><tr><td rowspan=1 colspan=1>Packing</td><td rowspan=1 colspan=1>Tray</td><td rowspan=1 colspan=1>Tape and reel</td></tr></table>

<table><tr><td>Product resources</td></tr><tr><td>AN5763 (device application note) AN5882 (finite state machine) AN5804 (machine learning core) AN5755 (Qvar sensing)</td></tr></table>

![](images/47f773933087cbfa80df6da20ce7dccbbd1165490f28b8d2ed393bcdda6e2b93.jpg)

# Features

Triple-channel architecture for Ul, EIS, and OIS data processing   
"Always-on" experience with low power consumption for both accelerometer   
and gyroscope   
Smart FIFO up to 4.5 KB   
Android compliant   
±2/±4/±8/±16 g full scale   
±125/±250/±500/±1000/±2000/±4000 dps full scale   
SPI / I²C & MIPI 13C® v1.1 serial interface with main processor data   
synchronization   
Auxiliary SPI for OIS data output for gyroscope and accelerometer   
OIS configurable from aux. SPl, primary interface (SPI / I2C & MIPI 13C® v1.1)   
EIS dedicated channel on primary interface with dedicated fitering   
Advanced pedometer, step detector, and step counter   
Significant motion detection, tilt detection   
Standard interrupts: free-fall, wake-up, 6D/4D orientation, click and double   
click   
Programmable finite state machine for accelerometer, gyroscope, and external   
sensor data processing with high rate @ 960 Hz   
Machine learning core with exportable features and filters for Al applications   
Embedded adaptive self-configuration (ASC)   
Embedded Qvar (electrostatic sensor) for user interface functions (tap, double   
tap, triple tap, long press, L/R – R/L swipe)   
Embedded analog hub for ADC and processing analog input data   
Embedded sensor fusion low-power algorithm   
Embedded temperature sensor   
Analog supply voltage: 1.71 V to 3.6 V   
Independent IO supply (extended range: 1.08 V to 3.6 V)   
Power consumption: 0.65 mA in combo high-performance mode   
Compact footprint: 2.5 mm × 3 mm × 0.83 mm   
ECOPACK and RoHS compliant

# Applications

Motion tracking and gesture detection, augmented reality (AR) / virtual reality   
(VR) / mixed reality (MR) applications & metaverse applications   
Wearables   
Indoor navigation   
loT and connected devices   
Smartphones and handheld devices   
EIS and OIS for camera applications   
Vibration monitoring and compensation

# Description

The LSM6DSV16X is a high-performance, low-power 6-axis small IMU, featuring a 3-axis digital accelerometer and a 3-axis digital gyroscope, that fers the best IMU sensor with a triple-channel architecture for processing acceleration and angular rate data on three separate channels (user interface, OIS, and EIS) with dedicated configuration, processing, and filtering.

The LSM6DSV16X enables processes in edge computing, leveraging embedded advanced dedicated features such as a finite state machine (FSM) for configurable motion tracking and a machine learning core (MLC) for context awareness with exportable AI features for loT applications.

The LSM6DSV16X supports the adaptive self-configuration (ASC) feature, which allows the FSM to automatically reconfigure the device in real time based on the detection of a specific motion pattern or based on the output of a specific decision tree configured in the MLC, without any intervention from the host processor.

The LSM6DSV16X embeds Qvar (electric charge variation detection) for user interface functions like tap, double tap, triple tap, long press, or L/R – R/L swipe.

The LSM6DSV16X embeds an analog hub able to connect an external analog input and convertit to a digital signal for processing.

# 1 Overview

The LSM6DSV16X is a system-in-package featuring a high-performance 3-axis digital accelerometer and 3-axis digital gyroscope.

The LSM6DSV16X delivers best-in-class motion sensing that can detect orientation and gestures in order to empower application developers and consumers with features and capabilies that are more sophisticated than simply orienting their devices to portrait and landscape mode.

The event-detection interrupts enable ficient and rliable motion tracking and context awareness, implementing hardware recognition of free-fall events, 6D orientation, lick and double-click sensing, activity or inactivity, stationary/motion detection and wake-up events. Machine learning and finite state machine processing allow moving some algorithms from the application processor to the LSM6DSV16X sensor, enabling consistent reduction of power consumption.

The LSM6DSV16X supports the main OS requirements, offring real, virtual, and batch mode sensors. In addition, the LSM6DSV16X can eficiently run the sensor-related features specified in Android, saving power and enabling faster reaction time. In particular, the LSM6DSV16X has been designed to implement hardware features such as significant motion detection, stationary/motion detection, tit, pedometer functions, imestamping and to support the data acquisition of external sensors.

The LSM6DSV16X offers hardware flexibility to connect the pins with different mode connections to external sensors to expand functionalities such as adding a sensor hub, auxiliary SPl, and so forth.

The LSM6DSV16X offers advanced design flexibity for OIS and EIS applications. Both channels have a dedicated processing path with independent fitering and enhanced EIS channel gyroscope data are read over the primary interfaces |²C/ MIPI 13C® v1.1 / SPI.

Channel 1 has been designed for user interface data processing for motion tracking. Data are available on the primary output of 1C / SPI / 3c@ for the accelerometer and gyroscope with independent ODR and FS.

Channel 2 has been designed for OIS applications. Data are available on the aux SPI at 7.68 kHz with accelerometer/gyroscope processing with independent FS at ±2 g - ±16 g (accelerometer) / ±125 dps - ±2000 dps (gyroscope). The accelerometer is also available as standalone with dedicated fitering.

Channel 3 has been design for enhanced EIS. Data are available in freerun mode in the output registers or in FIFO with dedicated tag and timestamp.

Up to 4.5 KB of FiFO with compression and dynamic allocation of significant data (that is, external sensors, timestamp, and so forth) allows overall power' saving of the system.

The LSM6DSV16X embeds a sensor fusion low-power (SFLP) algorithm able to provide a 6-axis (accelerometer + gyroscope) game rotation vector represented as a quaternion. The X, Y, Z quaternion components are stored in FIFO.

Like the entire portfolio of MEMS sensor modules, the LSM6DSV16X leverages the robust and mature in-house manufacturing processes already used for the production of micromachined accelerometers and gyroscopes. The various sensing elements are manufactured using specialized micromachining processes, while the IC interfaces are developed using CMOS technology that allows the design of a dedicated circuit, which istrimmed to better match the characteristics of the sensing element.

The LSM6DSV16X embeds an analog hub, which is able to connect an external analog input and convert it to a digital signal for prcessing as wellas advanced dedicated features like a finite state machine and data fitering for Ois, EiS, and motion processing.

The LSM6DSV16X embeds Qvar functionality, which is an electrostatic sensor able to measure the variation of the quasi-electrostatic potential. The Qvar sensing channel can be used for user interface applications like tap, double tap, triple tap, long press, and L/R – R/L swipe.

The LSM6DSV16X is available in a small plastic land grid array (LGA) package of 2.5 × 3.0 × 0.83 mm to address ultracompact solutions.

# 2 Embedded low-power features

The LSM6DSV16X has been designed to be fully compliant with Android featuring the following on-chip functions:

4.5 KB FIFO data buffering, data can be compressed two or three times 100% efficiency with flexible configurations and partitioning Possibility to store timestamp

● Event-detection interrupts (fully configurable)

Free-fall   
Wake-up   
6D orientation   
Click and double-click sensing Activity/inactivity recognition Stationary/motion detection

Specific IP blocks (called "embedded functions") with negligible power consumption and high performance

Pedometer functions: step detector and step counters   
Tilt   
Significant motion detection   
Finite state machine (FSM)   
Machine learning core (MLC) with exportable features and filters for Al applications   
Adaptive self-configuration (ASC)   
Embedded sensor fusion low-power (SFLP) algorithm

Up to six total sensors: two internal (accelerometer and gyroscope) and four external sensors analog hub for processing external analog input data

Qvar: electric charge variation detection

# Pedometer functions: step detector and step counters

The LSM6DSV16X embeds an advanced pedometer with an algorithm running in an ultralow-power domain in order to ensure extensive battery life in battery-constrained applications.

Leveraging enhanced configurability the advanced embedded pedometer is suitable for a large range of applications from mobile to wearable devices.

The algorthm processes and analyzes the accelerometer waveform in order to count the user's steps during walking and running activities.

The pedometer works at 30 Hz and itis not affected by the selected device power mode (ultralow-power, lowpower, high-performance), thus guaranteeing an ultralow-power experience and extreme flexibity in conjunctio with other device functionalities.

The pedometer output can be batched in the device's FIFO buffer, in order to decrease overall system current consumption.

ST freely provides the support and the tools for easily configuring the device and tuning the algorithm configuration for a best-in-class user experience.

# 2.2

# Pedometer algorithm

The pedometer algorithm is composed of a cascade of four stages:

Computation of the acceleration magnitude signal in order to detect the signal independently from device orientation; 2. FIR filter to extract relevant frequency components and to smooth the signal by cuting of high frequencies; 3. Peak detector to find the maximum and minimum of the waveform and compute the peak-to-peak value; 4. Step count: if the peak-to-peak value is greater than the settled threshold, a step is counted.

![](images/6e83b8e6d7d2dc71151cd4230b7e2e476e0695e4421a83ca6337e1b57b90c3e3.jpg)  
Figure 1. Four-stage pedometer algorithm

The LSM6DSV16X embeds a dynamic internal threshold for step detection that is updated ater each peak-topeak evaluation: the internal threshold is increased with a configurable speed if a step is detected or decreased with a configurable speed if a step is not detected.

This approach ensures high accuracy when the user starts to walk and a false peak rejection when the user is walking or running.

An internal configurable debounce algorthm can be also set to fiter false walks: indeed, an accelerometer pattern is recognized as a walk or run only if a minimum number of steps are counted.

The LSM6DSV16X has been designed to reject a false-positive signal inside the algorithm core.

On top of the mechanisms detailed above, the LSM6DsV16X allows enabling and configuring a dedicated false-positive rejection block to further boost pedometer accuracy.

# 2.3 Tilt detection

The tit function helps to detect activity change and has been implemented in hardware using only the accelerometer to achieve targets of both ultralow power consumption and robustness during the short duration of dynamic accelerations.

The tilt function is based on a trigger of an event each time the device's tit changes and can be used with different scenarios, for example:

Triggers when a phone is in a front pants pocket and the user goes from siting to standing or standing to sitting; Does not trigger when a phone is in a front pants pocket and the user is walking, running, or going upstairs.

# Significant motion detection

The significant motion detection (SMD) function generates an interupt when a'significant motion', that could be due to a change in user location, is detected. In the LSM6DSV16X device this function has been implemented in hardware using only the accelerometer.

SMD functionality can be used in location-based applications in order to receive a notification indicating when the user is changing location.

# 2.5

# Finite state machine

The LSM6DSV16X can be configured to generate interupt signals activated by user-defined motion paterns. To do this, up to 8 embedded finite state machines can be programmed independently for motion detection such as glance gestures, absolute wrist tit, shake and double-shake detection.

# Definition of finite state machine

A state machine is a mathematical abstraction used to design logic connections. It is a behavioral model composed of a finite number of states and transitions between states, similar to a flow chart in which one can inspect the way logic runs when certain conditions are met. The state machine begins with a start state, goes to different states through transitions dependent on the inputs, and can finally end in a specific state (called stop state). The current state is determined by the past states of the system. The following figure shows a generic state machine.

![](images/290629d24b2a07d67ac02cc33e846c626dd5867dac98ced1d1d4462ff20f76e2.jpg)  
Figure 2. Generic state machine

# Finite state machine in the LSM6DSV16X

The LSM6DSV16X works as a combo accelerometer-gyroscope sensor, generating acceleration and angular rate output data. It is also possible to connect an external sensor like a magnetometer or pressure sensor by using the sensor hub feature (mode 2). These data can be used as input of up to 8 programs in the embedded finite state machine (Figure 3. State machine in the LSM6DSV16X).

AI1 inte state machines are independent: each one has its dedicated memory area and itis independently executed. An interrupt is generated when the end state is reached or when some specific command is performed.

![](images/5fe840bb745a2f99b8a366363b6ce1aff4d824842fd427e0c90371f6f7b7f2b8.jpg)  
Figure 3. State machine in the LSM6DsV16X

# 2.6 Machine learning core

The LSM6DSV16X embeds a dedicated core for machine learning processing that provides system flexibity, allowing some algorithms run in the application processor to be moved to the MEMS sensor with the advantage of consistent reduction in power consumption.

Machine learning core logic allows identifying if a data pattern (for example motion, pressure, temperature, magnetic data, and so forth) matches a user-defined set of classes. Typical examples of applications could be activity detection like running, walking, driving, and so forth.

The LSM6DSV16X machine learning core works on data patterns coming from the accelerometer and gyro sensors, but it s also possible to connect and process external sensor data (like magnetometer or pressure sensor) by using the sensor hub feature (mode 2).

The input data can be fitered using a dedicated configurable computation block containing fiters and features computed in a fixed time window defined by the user. Computed feature values and fitered data values can also be read through the FIFO buffer.

Machine learning processing is based on logical processing composed of a series of configurable nodes characterized by "ifthen-else" conditions where the "feature" values are evaluated against defined thresholds.

![](images/9e2776d7a9fd95fae51f4d1e3b5dc43bc220beb84fd21e0da60dcfa2c53d570a.jpg)  
Figure 4. Machine learning core in the LSM6DsV16X

The LSM6DSV16X can be configured to run up to 4 decision rees simultaneously and independently and every decision tree can generate up to 16 results. The total number of nodes can be up to 128.

The results of the machine learning processing are available in dedicated output registers readable from the application processor at any time.

The LSM6DSV16X machine learning core can be configured to generate an interrupt when a change in the result occurs.

# Adaptive self-configuration (ASC)

The LSM6DSV16X supports the adaptive self-configuration (ASC) feature, which allows the FSM to automatically reconfigure the device in real ime based on the detection of a specific motion paern or based on the output of a specific decision tree configured in the MLC, without any intervention from the host processor. The FSM can write a subset of the device registers using the SETR command, which allows indicating the register address and the new value to be written in such a register. The access to these device registers is mutually exclusive to the host.

# 2.8

# Sensor fusion low power

A sensor fusion low-power (SFLP) block is available in the LSM6DSV16X for generating the following data based on the accelerometer and gyroscope data processing:

Game rotation vector, which provides a quaternion representing the atitude of the device Gravity vector, which provides a three-dimensional vector representing the direction of gravity Gyroscope bias, which provides a three-dimensional vector representing the gyroscope bias

The SFLP block is enabled by setting the SFLP_GAME_EN bit to 1 of the EMB_FUNC_EN_A (04h) embedded functions register.

The SFLP block can be reinitialized by setting the SFLP_GAME_INIT bit to 1 of the EMB_FUNC_INIT_A (66h) embedded functions register.

Table 1. Sensor fusion performance   
1. Time required to reach steady state   

<table><tr><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=3 colspan=1>Static accuracy</td><td rowspan=1 colspan=1>heading /yaw</td><td rowspan=1 colspan=1>0.5 deg. / 5 minutes</td></tr><tr><td rowspan=1 colspan=1>pitch</td><td rowspan=1 colspan=1>1.5 deg.</td></tr><tr><td rowspan=1 colspan=1>roll</td><td rowspan=1 colspan=1>1.5 deg.</td></tr><tr><td rowspan=3 colspan=1>Low dynamic accuracy</td><td rowspan=1 colspan=1>heading / yaw</td><td rowspan=1 colspan=1>0.7 deg. / 5 minutes</td></tr><tr><td rowspan=1 colspan=1>pitch</td><td rowspan=1 colspan=1>0.5 deg.</td></tr><tr><td rowspan=1 colspan=1>roll</td><td rowspan=1 colspan=1>0.5 deg.</td></tr><tr><td rowspan=3 colspan=1>High dynamic accuracy</td><td rowspan=1 colspan=1>heading / yaw</td><td rowspan=1 colspan=1>5.9 deg. 15 minutes</td></tr><tr><td rowspan=1 colspan=1>pitch</td><td rowspan=1 colspan=1>1.6 deg.</td></tr><tr><td rowspan=1 colspan=1>roll</td><td rowspan=1 colspan=1>1.2 deg.</td></tr><tr><td rowspan=1 colspan=1>Calibration time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8 seconds(1)</td></tr><tr><td rowspan=1 colspan=1>Orientation stabilization time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7 seconds</td></tr></table>

# 3 Pin description

![](images/de69001976df311a8e0d8ef2f3a61958ff2f312a4989c5ec23c09093512d81ab.jpg)  
Figure 5. Pin connections

Direction of detectable angular rate (top view)

# 3.1 Pin connections

The LSM6DSV16X offers flexibility to connect the pins in order to have three diferent mode connections and functionalities. In detail:

Mode 1: IC / MIPI I3C® slave interface or SPI (3- and 4-wire) serial interface is available. The analog hub and Qvar functionalities are available in mode i with I²C interface only.   
Mode 2: IC / MIPI I3C® slave interface or SPI (3- and 4-wire) serial interface and I²C interface master for external sensor connections are available.   
Mode 3: ²C / MIPl 13C® slave interface or SPI (3- and 4-wire) serial interface is available for the applicatior processor interface while an auxiliary SPI (3- and 4-wire) serial interface for external sensor connections is available for the accelerometer and gyroscope.

# Note:

Refer to the product aplication note for the details regarding operatingpower mode configurations, sttings, turn-on/off time and on-the-fly changes.

![](images/c59a1082c9b20966bfbceaed047d73a39d2ecf5ebf81d8671aef4f80370af3b5.jpg)  
Figure 6. LSM6DSV16X connection modes

In the following table, each mode is described for the pin connections and function.

Table 2. Pin description   

<table><tr><td rowspan=1 colspan=1>Pin#</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Mode 1 function</td><td rowspan=1 colspan=1> Mode 2 function</td><td rowspan=1 colspan=1>Mode 3 function</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SDO/SA0(1)</td><td rowspan=1 colspan=1>SPI 4-wire interface serial data output(SDO)I²C least significant bit of the deviceaddress (SAO)</td><td rowspan=1 colspan=1>SPI 4-wire interface serial dataoutput (SDO)I²C least significant bit of the deviceaddress (SA0)</td><td rowspan=1 colspan=1>SPI 4-wire interface serial data output(SDO)I²C least significant bit of the deviceaddress (SAO)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SDx/AH1/Qvar1</td><td rowspan=1 colspan=1>Connect to Vdd_IO or GND i the analoghub and Qvar are disabled.AH input 1 (or Qvar electrode 1) isconnected ifthe analog hub (or Qvarfunctionality) is enabled.</td><td rowspan=1 colspan=1>IC serial data master (MSDA)</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire interface serialdata input (SDl_Aux)and SPI 3-wire serial data output(SDO_Aux)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCx/AH2/Qvar2</td><td rowspan=1 colspan=1>Connect to Vdd_IO or GND if the analoghub and Qvar are disabled.AH input 2 (or Qvar electrode 2) isconnected if the analog hub (or Qvarfunctionality) is enabled.</td><td rowspan=1 colspan=1>I²C serial clock master (MSCL)</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire interface serialport clock (SPC_Aux)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>INT1</td><td rowspan=1 colspan=3>Programmable interrupt in ²C and SPI</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Vdd_10(2)</td><td rowspan=1 colspan=3>Power supply for I/O pins</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=3>0 V supply</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=3>o V supply</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Vdd(2)</td><td rowspan=1 colspan=3>Power supply</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>INT2</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2) / Data enable (DEN)</td><td rowspan=1 colspan=1>Programmable interrupt 2 (INT2) /Data enable (DEN) /I²C master external synchronizationsignal (MDRDY)</td><td rowspan=1 colspan=1>Programmable interrupt 2 (INT2) /Data enable (DEN)</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>OCS_Aux</td><td rowspan=1 colspan=1>Connect to Vdd_I0 orleave unconnected(3)</td><td rowspan=1 colspan=1>Connect to Vdd_10 orleave unconnected(3)</td><td rowspan=1 colspan=1>Enable auxiliary SPl 3/4-wire interface</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>SDO_Aux</td><td rowspan=1 colspan=1>Connect to Vdd_I0 orleave unconnected(3)</td><td rowspan=1 colspan=1>Connect to Vdd_I0 orleave unconnected(3)</td><td rowspan=1 colspan=1>Auxiliary SPI 3-wire interface: leaveunconnected(3)Auxiliary SPI 4-wire interface: serialdata output (SDO_Aux)</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>CS(1)</td><td rowspan=1 colspan=1>²C / MIPI 3C®/ SPI mode selection(1: SPl ide mode / ²C /MIP| 13C©communication enabled;0: SPI communication mode / I²C / MIPI13C®disabled)</td><td rowspan=1 colspan=1>²C /MIPI 13C@/SPI modeselection(1: SPl idle mode / ?C / MIPI 13C®communication enabled;0: SPI communication mode / I²C /MIPI 13C@ disabled)</td><td rowspan=1 colspan=1>|C / MIPI 3C® / SPI mode selection(1: SPl idle mode / ²C /MIPI 3C©communication enabled;0: SPI communication mode / 1C /MIPI I3C® disabled)</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>SCL(1)</td><td rowspan=1 colspan=1>|2C / MIPl |3C® serial clock (SCL)SPI serial port clock (SPC)</td><td rowspan=1 colspan=1>|²C / MIPI 3C® serial clock (SCL)SPI serial port clock (SPC)</td><td rowspan=1 colspan=1>|²C / MIPl I3C® serial clock (SCL)SPI serial port clock (SPC)</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>SDA(1)</td><td rowspan=1 colspan=1>²C / MIPI 13C@ serial data (SDA)SPI serial data input (SDI)3-wire interface serial data output (SDO)</td><td rowspan=1 colspan=1>²C / MIPI I3C@ serial data (SDA)SPI serial data input (SDI)3-wire interface serial data output(SDO)</td><td rowspan=1 colspan=1>²C /MIPI 13C® serial data (SDA)SPI serial data input (SDI)3-wire interface serial dataoutput (SDO)</td></tr></table>

1. SPI 3/4-wire interface not available with the analog hub / Qvar functionality enabled. 2. Recommended 100 nF filter capacitor. 3. Leave pin electrically unconnected and soldered to PCB.

# 4 Module specifications

# 4.1 Mechanical characteristics

@ Vdd = 1.8 V, T = 25 ºC, unless otherwise noted.

Table 3. Mechanical characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=4 colspan=1>LA_FS</td><td rowspan=4 colspan=1>Linear acceleration measurement range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>g</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±8</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±16</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=6 colspan=1>G_FS</td><td rowspan=6 colspan=1>Angular rate measurement range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±125</td><td rowspan=1 colspan=1></td><td rowspan=6 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±250</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±500</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1000</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±2000</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±4000</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=4 colspan=1>LA_So</td><td rowspan=4 colspan=1>Linear acceleration sensitivity</td><td rowspan=1 colspan=1>FS =±2g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.061</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>mg/LSB</td></tr><tr><td rowspan=1 colspan=1>$FS= ±4g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.122</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS=±8g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.244</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS =±16g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.488</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=6 colspan=1>G_So</td><td rowspan=6 colspan=1>Angular rate sensitivity(2)</td><td rowspan=1 colspan=1>FS = ±125 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.375</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS = ±250 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8.75</td><td rowspan=1 colspan=1></td><td rowspan=5 colspan=1>mdps/LSB</td></tr><tr><td rowspan=1 colspan=1>FS = ±500 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>17.50</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS = ±1000 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS = ±2000 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS = ±4000 dps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>140</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>G_S0%</td><td rowspan=1 colspan=1>Sensitivit tolerance(2)</td><td rowspan=1 colspan=1>at component level</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>LA_SODr</td><td rowspan=1 colspan=1>Linear acceleration sensitivity change vs. temperature(3)</td><td rowspan=1 colspan=1>from -40°to +85°</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%1°℃c</td></tr><tr><td rowspan=1 colspan=1>G_SoDr</td><td rowspan=1 colspan=1>Angular rate sensitity change vs. temperature(3)</td><td rowspan=1 colspan=1>from -40°to +85°</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.007</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%1°℃</td></tr><tr><td rowspan=1 colspan=1>LA_TyOff</td><td rowspan=1 colspan=1>Linear acceleration zero-g level offset accuracy(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mg</td></tr><tr><td rowspan=1 colspan=1>G_TyOff</td><td rowspan=1 colspan=1>Angular rate zero-rate level(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1>LA_OffDr</td><td rowspan=1 colspan=1>Linear acceleration zero-g level change vs. temperature(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.07</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mg/°℃</td></tr><tr><td rowspan=1 colspan=1>G_OffDr</td><td rowspan=1 colspan=1>Angular rate typical zero-rate level change vs. temperature(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.006</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dps/°℃C</td></tr><tr><td rowspan=1 colspan=1>Rn</td><td rowspan=1 colspan=1>Rate noise density in high-performance mode(5)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mdps/VHz</td></tr><tr><td rowspan=1 colspan=1>RnRMS</td><td rowspan=1 colspan=1>Gyroscope RMS noise in low-power mode(6)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mdps RMS</td></tr><tr><td rowspan=2 colspan=1>An</td><td rowspan=1 colspan=1>Acceleration noise density in high-performance mode(7</td><td rowspan=1 colspan=1>FS=±2g-±16g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>μg/Hz</td></tr><tr><td rowspan=1 colspan=1>Acceleration noise densit in normal mode(8)9)</td><td rowspan=1 colspan=1>FS =±2g-±16g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>RMS</td><td rowspan=3 colspan=1>Accelerometer RMS noise in low-power mode</td><td rowspan=1 colspan=1>LPM1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>LPM2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>mg RMS</td></tr><tr><td rowspan=1 colspan=1>LPM3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=3 colspan=1>Symbol</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=2 colspan=1>Parameter</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=2>Test conditions</td><td rowspan=1 colspan=2>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=12 colspan=1>LA_ODR</td><td rowspan=12 colspan=1>Linear acceleration output data rate</td><td rowspan=2 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1.875(10)</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=10 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1></td><td rowspan=20 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=2></td><td rowspan=1 colspan=1>240</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>480</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>960</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1.92k</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=2></td><td rowspan=1 colspan=1>3.84k</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.68k</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=11 colspan=1></td><td rowspan=11 colspan=1>G_ODR Angular rate output data rate</td><td rowspan=11 colspan=2></td><td rowspan=2 colspan=2></td><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>15</td><td rowspan=2 colspan=1></td></tr><tr><td></td><td></td></tr><tr><td rowspan=3 colspan=2></td><td></td><td></td></tr><tr><td rowspan=4 colspan=2></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td rowspan=2 colspan=2></td><td rowspan=2 colspan=1>2404809601.92k3.84k7.68k</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>HAODR</td><td rowspan=2 colspan=1>ODR variation over temperature and supply range in high-accuracymode(1))</td><td rowspan=1 colspan=2>Gyro on</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1</td><td rowspan=2 colspan=1>%</td></tr><tr><td rowspan=1 colspan=2>Gyro off</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±3</td></tr><tr><td rowspan=3 colspan=1>Vst</td><td rowspan=1 colspan=1>Linear acceleration slf-test output change(12)(13)(14)</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>50</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1700</td><td rowspan=1 colspan=1>mg</td></tr><tr><td rowspan=2 colspan=1>Angular rate self-test output change(15)(16)</td><td rowspan=1 colspan=2>FS = ±250 dps</td><td rowspan=1 colspan=2>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=2>FS = ±2000 dps</td><td rowspan=1 colspan=2>150</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>700</td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr></table>

1. Typical specifications are not guaranteed.   
2. Sensitivity tolerance for FS up to ±2000 dps.   
3. Measurements are performed in a uniform teerature setup and they are basedon characterization data in lited umber of saple. Not measured during final test for production.   
4. Value after calibration.   
5. Gyroscope rate noise density in high-performance mode is independent of the ODR and FS setting up to ±2000 dps.   
6. Gyroscope RMS noise in low-power mode is independent of the ODR and FS setting up to ±2000 dps.   
7. Accelerometer noise density in high-performance mode is independent of the selected ODR and FS. Valid whenL_DualC_EN = 0 in register CTRL8 (17h) .   
8. Accelerometer noise densit in normal mode is independent of the ODR and FS seting.Valid whenXL_Dual_EN = 0 in registerCTRL (17h).   
9. Noise RMS related to BW = ODR/2.   
10. This ODR is available when the accelerometer is in low-power mode.   
11. Values specified by design.   
12. The sign of te linear acceleration self-test output change is defined by the ST_XL_[1:0] bits in a dedicated register for llaxes.   
13.The liear acceleration slftest utut change is defind with the evice instationary condition as the absolute valu of UPUT (self-test enabled) - OUTPUT[LSb] (self-test disabled). 1LSb = 0.061 mg at ±2 g full scale.

14. Accelerometer self-test limits are full-scale independent.

15. The sign of the angula rate sef-test output change is defined by the ST_G_[1:0] bits in a dedicated register for allaxes.

16.The angularrate elftest outut change is defined with the evic i stationary condition as the asolute valu of UUb (elf-tet enabled) - OUTPUT[L Sb] (self-test disabled). 1LSb = 70 mdps at ±2000 dps full scale.

# 4.2 Electrical characteristics

@ Vdd = 1.8 V, T = 25 ºC, unless otherwise noted.

Table 4. Electrical characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Vdd</td><td rowspan=1 colspan=1>Supply voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vdd_10</td><td rowspan=1 colspan=1>Power supply for /O</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.08</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IddHP</td><td rowspan=1 colspan=1>Gyroscope and accelerometer current consumption in high-performancemode</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.65</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>LA_IddHP</td><td rowspan=1 colspan=1>Accelerometer current consumption in high-performance mode</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>190</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>LA_IddNM</td><td rowspan=1 colspan=1>Accelerometer current consumption in normal mode</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>LA_IddLPM2</td><td rowspan=1 colspan=1>Accelerometer current consumption in low-power mode (LPM2)</td><td rowspan=1 colspan=1>ODR = 60 HzODR = 1.875 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>204.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>LA_IddLPM1</td><td rowspan=1 colspan=1>Accelerometer current consumption in low-power mode (LPM1)</td><td rowspan=1 colspan=1>ODR = 60 HzODR= 1.875 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>174.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>IddPD</td><td rowspan=1 colspan=1>Gyroscope and accelerometer current consumption during power-down</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Ton</td><td rowspan=1 colspan=1>Turn-on time - gyroscope</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>VH</td><td rowspan=1 colspan=1>Digital high-level input voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7*vdd_10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VIL</td><td rowspan=1 colspan=1>Digital low-level input voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3*vdd_10</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>High-level output voltage</td><td rowspan=1 colspan=1>10H = 4 mA(2)</td><td rowspan=1 colspan=1>Vdd _10-0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VoL</td><td rowspan=1 colspan=1>Low-level output voltage</td><td rowspan=1 colspan=1>10L= 4 mA(2)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr></table>

1. Typical specifications are not guaranteed.

2. 4mA is the axi driving capability that is the maxiu DCcurent that can be sourcedsunk te digitl pin in orde to arante the correct digital output voltage levels VoH and VoL.

Table 5. Electrical parameters of Qvar (@Vdd = 1.8 V, T = 25 °C)   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Power consumption</td><td rowspan=1 colspan=1>15(2)</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Offset (shorted inputs)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=1 colspan=1>Noise (shorted inputs)</td><td rowspan=1 colspan=1>54</td><td rowspan=1 colspan=1>μV</td></tr><tr><td rowspan=1 colspan=1>Qvar gain</td><td rowspan=1 colspan=1>78</td><td rowspan=1 colspan=1>LSB/mV</td></tr><tr><td rowspan=1 colspan=1>CMRR</td><td rowspan=1 colspan=1>54</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>Input impedance</td><td rowspan=1 colspan=1>Configurable (from 235 M to 2.4 G)</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>Input range</td><td rowspan=1 colspan=1>±460</td><td rowspan=1 colspan=1>mV</td></tr></table>

Vdd_I0 = 1.8 V, Zin = 235 MOhm. Typical values are based on characterization and are not guarantee

2. Extra power consumption when only the analog hub /Qvar functin is enabled. In this condion the accelerometer must be set to high-performance mode or normal mode.

# 4.3 Temperature sensor characteristics

@ Vdd = 1.8 V, T = 25 ºC unless otherwise noted.

Table 6. Temperature sensor characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test condition</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>TODR(2)</td><td rowspan=1 colspan=1>Temperature refresh rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>$Hz$</td></tr><tr><td rowspan=1 colspan=1>Toff</td><td rowspan=1 colspan=1>Temperature offset(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+15</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>TSen</td><td rowspan=1 colspan=1>Temperature sensitivity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LSB/°C</td></tr><tr><td rowspan=1 colspan=1>TST</td><td rowspan=1 colspan=1>Temperature stabization time(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>us</td></tr><tr><td rowspan=1 colspan=1>T_ADC_res</td><td rowspan=1 colspan=1>Temperature ADC resolution</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>bit</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr></table>

2. When the accelerometer isin low-power mode and the gyroscope part s turned of the TODR value is equal to the accelerometer ODR.   
3. The output of the temperature sensor is 0 LSB (typ.) at 25 \*C.   
4. Time from power ON to valid data based on characterization data.

# 4.4

# Communication interface characteristics

# 4.4.1

# SPI - serial peripheral interface

Subject to general operating conditions for Vdd and Top. @ Vdd_IO = 1.8 V, T = 25 \*C unless otherwise noted.

Table 7. sPI slave timing values   

<table><tr><td rowspan=2 colspan=1>Symbol</td><td rowspan=2 colspan=1>Parameter</td><td rowspan=1 colspan=3>Value(1)</td><td rowspan=2 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>fc(SPC)</td><td rowspan=1 colspan=1>SPI clock frequency</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>tc(SPC)</td><td rowspan=1 colspan=1>SPl clock period</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=11 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>thigh(SPC)</td><td rowspan=1 colspan=1>SPI clock high</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tow(SPC)</td><td rowspan=1 colspan=1>SPI clock low</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>tsu(CS)</td><td rowspan=1 colspan=1>CS setup time (mode 3)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>CS setup time (mode 0)</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>th(CS)</td><td rowspan=1 colspan=1>CS hold time (mode 3)</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>CS hold time (mode 0)</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(S1)</td><td rowspan=1 colspan=1>SDl input setup time</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>th(s1)</td><td rowspan=1 colspan=1>SDl input hold time</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tu(so)</td><td rowspan=1 colspan=1>SDO valid output time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>25</td></tr><tr><td rowspan=1 colspan=1>tis(S)</td><td rowspan=1 colspan=1>SDO output disable time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>Cload</td><td rowspan=1 colspan=1>Bus capacitance</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>pF</td></tr></table>

1. Values are evaluated at 10 MHz clock frequency for SPI with both 4 and 3 wires, based on characterization results, not tested in production

![](images/abc8b89457e94acee91733417c41f71298ac1b71dd6a7e4ab5b50ff176c48c51.jpg)  
Figure 7. SPI slave timing in mode 0

![](images/9bf974545a7c260f85c88778b8e5bdeae27b1d258e338b09d447b97061e687d8.jpg)  
Figure 8. SPI slave timing in mode 3

Note:

Measurement points are done at 0.3·Vdd_10 and 0.7·Vdd_10 for both input and output ports.

# 4.4.2

# ²C - inter-IC control interface

Subject to general operating conditions for Vdd and Top.

Table 8. I²C slave timing values   

<table><tr><td rowspan=2 colspan=1>Symbol</td><td rowspan=2 colspan=1>Parameter</td><td rowspan=1 colspan=2>²C fast mode(1)(2)</td><td rowspan=1 colspan=2> I²C fast mode plus(1)(2)</td><td rowspan=2 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>f(SCL)</td><td rowspan=1 colspan=1>SCL clock frequency</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>KHz</td></tr><tr><td rowspan=1 colspan=1>tw(SCLL)</td><td rowspan=1 colspan=1>SCL clock low time</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>μs</td></tr><tr><td rowspan=1 colspan=1>tw(SCLH)</td><td rowspan=1 colspan=1>SCL clock high time</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(SDA)</td><td rowspan=1 colspan=1>SDA setup time</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>th(SDA)</td><td rowspan=1 colspan=1>SDA data hold time</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=7 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>th(ST)</td><td rowspan=1 colspan=1>START/REPEATED START condition hold time</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(SR)</td><td rowspan=1 colspan=1>REPEATED START condition setup time</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(SP)</td><td rowspan=1 colspan=1>STOP condition setup time</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tw(SP:SR)</td><td rowspan=1 colspan=1>Bus free time between STOP and START condition</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Data valid time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.45</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Data valid acknowledge time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.45</td></tr><tr><td rowspan=1 colspan=1>CB</td><td rowspan=1 colspan=1>Capacitive load for each bus line</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>pF</td></tr></table>

1. Data based on standard I2C protocol requirement, not tested in production. 2. Data for ²C fast mode and I?C fast mode plus have been validated by characterization, not tested in production.

![](images/34e8c444d837e6d447f71998d8fedd8b90f6bc9795e3eb7951f0ab62c56bdece.jpg)  
Figure 9. IC slave timing diagram

Note:

Measurement points are done at 0.3·Vdd_10 and 0.7·Vdd_I1O for both ports.

# 4.5

# Absolute maximum ratings

Stresses above those listed as absolute maximum ratings" may cause permanent damage to the device. This is a stress rating only and functional operation of the device under these conditions is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability.

Table 9. Absolute maximum ratings   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Ratings</td><td rowspan=1 colspan=1>Maximum value</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Vdd</td><td rowspan=1 colspan=1>Supply voltage</td><td rowspan=1 colspan=1>-0.3 to 4.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1>Storage temperature range</td><td rowspan=1 colspan=1>-40 to +125</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Sg</td><td rowspan=1 colspan=1>Acceleration g for 0.2 ms</td><td rowspan=1 colspan=1>20,000</td><td rowspan=1 colspan=1>g</td></tr><tr><td rowspan=1 colspan=1>ESD</td><td rowspan=1 colspan=1>Electrostatic discharge protection (HBM)</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>kV</td></tr><tr><td rowspan=1 colspan=1>Vin</td><td rowspan=1 colspan=1>Input voltage on any control pin(including CS, SCL/SPC, SDA/SDI/SDO, SDO/SA0)</td><td rowspan=1 colspan=1>-0.3 to Vdd_1O +0.3</td><td rowspan=1 colspan=1>V</td></tr></table>

# Note:

# Supply voltage on any pin should never exceed 4.8 V.

This device is sensitive to mechanical shock, improper handling can cause permanent damage to the part.

This device is sensitive to electrostatic discharge (EsD), improper handling can cause permanent damage to the part.

# 4.6 Terminology

# 4.6.1 Sensitivity

Linear acceleration sensitivity can be determined, for example, by applying 1 g acceleration to the device. Because the sensor can measure DC accelerations, this can be done easily by pointing the selected axis towards the ground, noting the output value, rotating the sensor 180 degrees (pointing towards the sky) and noting the output value again. By doing so, ±1 g acceleration is applied to the sensor. Subtracting the larger output value from the smalle one, and dividing the result by 2, leads to the actual sensitivity of the sensor. This value changes very itle over temperature and over time. The sensitity tolerance describes the range of sensitivities of a large number of sensors (see Table 3).

An angular rate gyroscope is a device that produces a positive-going digital output for counterclockwise rotation around the axis considered. Sensitivity describes the gain of the sensor and can be determined by applying a defined angular velocity to it. This value changes very litle over temperature and time (see Table 3).

# 4.6.2 Zero-g and zero-rate level

Linear acceleration zero-g level fet (TyOff) describes the deviation of an actual output signal from the ideal output signal if no acceleration is present. A sensor in a steady state on a horizontal surface measures 0 g on both the X-axis and Y-axis, whereas the Z-axis measures 1 g. Ideally, the output is in the midle of the dynamic range of the sensor (content of OUT registers 0h, data expressed as two's complement number). A deviation from the ideal value in this case is called zero-g ofset.

Offset is to some extent a result of stress to the MEMS sensor and therefore the offset can slightly change after mounting the sensor onto a printed circuit board or exposing it to extensive mechanical stress. Offset changes Iitle over temperature, see “Linear acceleration zero-g level change vs. temperature" in Table 3. The zero-g level tolerance (TyOff) describes the standard deviation of the range of zero-g levels of a group of sensors.

Zero-rate level describes the actual output signal if there is no angular rate present. The zero-rate level of precise MEMS sensors is, to some extent, a result of stress to the sensor and therefore the zero-rate level can slightly change after mounting the sensor onto a printed circuit board or after exposing it to extensive mechanical stress. This value changes very little over temperature and time (see Table 3).

# 5 Digital interfaces

# 5.1

# |²C/SPl interface

The registers embedded inside the LSM6DSV16X may be accessed through both the I²C and SPI serial interfaces. The latter may be software configured to operate either in 3-wire or 4-wire interface mode. The device is compatible with SPI modes 0 and 3.

The serial interfaces are mapped to the same pins. To select/exploit the IC interface, the CS line must be tied high (that is, connected to Vdd_IO).

Table 10. Serial interface pin description   

<table><tr><td>Pin name</td><td>Pin description</td></tr><tr><td rowspan="4">CS</td><td>Enables SPI</td></tr><tr><td>|²C/SPI mode selection</td></tr><tr><td>(1: SPl idle mode / I?C communication enabled;</td></tr><tr><td>0: SPI communication mode / I²C disabled)</td></tr><tr><td>SCL/SPC</td><td>|²C serial clock (SCL) SPI serial port clock (SPC)</td></tr><tr><td>SDASDI/SDO</td><td>I²C serial data (SDA) SPI serial data input (SDI) 3-wire interface serial data output (SDO)</td></tr><tr><td>SDO/SAO</td><td>SPI serial data output (SDO) |²C less significant bit of the device address</td></tr></table>

# 5.1.1

# I²C serial interface

The LSM6DSV16X IC is a bus slave. The IC is employed to write the data to the registers, whose content can also be read back.

The relevant I?C terminology is provided in the table below.

Table 11. IC terminology   

<table><tr><td rowspan=1 colspan=1>Term</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Transmitter</td><td rowspan=1 colspan=1>The device that sends data to the bus</td></tr><tr><td rowspan=1 colspan=1>Receiver</td><td rowspan=1 colspan=1>The device that receives data from the bus</td></tr><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>The device that initiates a transfer, generates clock signals, and terminates a transfer</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1>The device addressed by the master</td></tr></table>

There are two signals associated with the ²C bus: the serial clock line (SCL) and the serial data line (SDA). The latter is a bidirectional line used for sending and receiving the data to/from the interface. Both the lines must be connected to Vdd_IO through external pull-up resistors. When the bus is free, both the lines are high.

The IC interface is implemented with fast mode (400 kHz) I?C standards as wellas with fast mode plus (1000 kHz).

In order to disable the ²C block, 12C_I3C_disable = 1 must be written in IF_CFG (03h).

# 5.1.2 I²C operation

The transaction on the bus is started through a start (ST) signal. A start condition is defined as a high to low transition on the data line while the SCL line is held high. After this has been transmitted by the master, the bus is considered busy. The next byte of data transmited ater the start condition contains the address of the slave in the first 7 bits and the eighth bit tells whether the master is receiving data from the slave or transmiting data to the slave. When an address is sent, each device in the system compares the first seven bits after a start condition with its address. If they match, the device considers itself addressed by the master.

The slave address (SAD) associated to the LSM6DSV16X is 110101xb. The SDO/SA0 pin can be used to modify the less significant bit of the device address.If the SDO/SA0 pin is connected to the supply voltage, LSb is 1 (address 1101011b); else if the SDO/SA0 pin is connected to ground, the LSb value is 0 (address 1101010b). This solution permits to connect and address two different inertial modules to the same I?C bus.

Data transfer with acknowledge is mandatory. The transmiter must release the SDA line during the acknowledge pulse. The receiver must then pul the data line low so that it remains stable low during the high period of the acknowledge clock pulse. A receiver that has been addressed is obliged to generate an acknowledge ater each byte of data received.

The ²C embedded inside the LSM6DSV16X behaves like a slave device and the following protocol must be adhered to. After the start condition (ST) a slave address is sent, once a slave acknowledge (SAK) has been returned, an 8-bit subaddress (SUB) is transmitted. The increment of the address is configured by the CTRL3 (12h) (IF_INC).

The slave address is completed with a read/write bit.If the bit is 1 (read), a repeated start (SR) condition must be issued after the two subaddress bytes; if the bit is 0 (write) the master transmits to the slave with direction unchanged. Table 12 explains how the SAD+read/write bit pattern is composed, isting all the possible configurations.

Table 12. SAD+read/write patterns   

<table><tr><td rowspan=1 colspan=1>Command</td><td rowspan=1 colspan=1>SAD[6:1]</td><td rowspan=1 colspan=1>SAD[0] = SA0</td><td rowspan=1 colspan=1>RW</td><td rowspan=1 colspan=1>SAD+R/W</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>11010101 (D5h)</td></tr><tr><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>11010100(D4h)</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1101011(D7h)</td></tr><tr><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>11010110 (D6h)</td></tr></table>

Table 13. Transfer when master is writing one byte to slave   

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td></tr></table>

Table 14. Transfer when master is writing multiple bytes to slave   

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td></tr></table>

# Table 15. Transfer when master is receiving (reading) one byte of data from slave

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SR</td><td rowspan=1 colspan=1>SAD + R</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NMAK</td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Table 16. Transfer when master is receiving (reading) multiple bytes of data from slave   

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD+W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SR</td><td rowspan=1 colspan=1>SAD+R</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NMAK</td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Data are transmited in byte format (DATA). Each data transfer contains 8 bits. The number of bytes transferred per transfer is unlimited. Data is transferred with the most significant bit (MSb) first.If a slave receiver does not acknowledge the slave address (that is, t is not able to receive because it is performing some real-time function) the data line must be lef high by the slave. The master can then abort the transfer. A low to high transition on the SDA Iine while the SCL line is high is defined as a stop condition. Each data transfer must be terminated by the generation of a stop (SP) condition.

In the presented communication format, MAK is master acknowledge and NMAK is no master acknowledge.

# 5.1.3

# SPI bus interface

The SPl on the LSM6DSV16X is a bus slave which allows writing and reading the registers of the device.

![](images/3fde6df3763609a50e1f2b345bb7ba3fe2a985368ec405e1122e091ce681f59f.jpg)  
Figure 10. Read and write protocol (in mode 3)

CS enables the serial port and it is controlled by the SPI master It goes low at the start of the transmission and goes back high at the end. SPC is the serial port clock and it is controlled by the SPI master.It is stopped high when Cs is high (no transmission). SDI and sDO are, respectively, the serial port data input and output. Those lines are driven at the falling edge of sPC and should be captured at the rising edge of sPC.

Both the read register and write register commands are completed in 16 clock pulses or in multiples of 8 in case of multiple read/write bytes. Bit duration is the time between two faling edges of sPC. The first bit (bit 0) starts at the first falling ede of sPC after the falling edge ofCs whil the last bit (bit 15, bit 23, …) starts at the last falling edge of SPC just before the rising edge of cs.

bit 0: RW bit. When 0, the data DI(7:0) is writen into the device. When 1, the data DO(7:0) from the device is read. In latter case, the chip drives sDo at the start of bit 8.

bit 1-7: address AD(6:0). This is the address field of the indexed register.

it 8-15: data DI(7:0) (write mode). This is the data that is written into the device (MSb first).

bit 8-15: data DO(7:0) (read mode). This is the data that is read from the device (MSb first).

In multiple read/write commands further blocks of 8 clock periods are added. When the CTRL3 (12h) (IF_INC) bit is 0, the address used to read/wrte data remains the same for every block. When the CTRL3 (12h) (IF_iNC) bit is 1, the address used to read/write data is increased at every block.

The function and the behavior of sDI and sDo remain unchanged.

# 5.1.3.1 SPI read

![](images/eaa06a7ad4df25be3cbac9173bdb898d8c99619616eee9675c7b32e85897ca4d.jpg)  
Figure 11. SPI read protocol (in mode 3)

The SPl read command is performed with 16 clock pulses. A multiple byte read command is performed by ading blocks of 8 clock pulses to the previous one.

bit 0: READ bit. The value is 1.   
bit 1-7: address AD(6:0). This is the address field of the indexed register.   
bit 8-15: data DO(7:0) (read mode). This is the data that is read from the device (MSb first).   
bit 16-.: data DO(.-8). Further data in multiple byte reads.

![](images/3fdc8c0fcc9a1ad9538957c17b137066b67775588f6ad5eee373cba3b204325f.jpg)  
Figure 12. Multiple byte SPI read protocol (2-byte example) (in mode 3)

# 5.1.3.2 SPI write

![](images/5a2bf506ffee648d59e598c776aab7b8099f4b94da7725482da9c44d65581025.jpg)  
Figure 13. SPI write protocol (in mode 3)

The SPI write command is performed with 16 clock pulses. A multiple byte write command is performed by adding blocks of 8 clock pulses to the previous one.

bit 0: WRITE bit. The value is 0.   
bit 1 -7: address AD(6:0). This is the address field of the indexed register.   
bit 8-15: data DI(7:0) (write mode). This is the data that is written inside the device (MSb first).   
bit 16-. : data DI(.-8). Further data in multiple byte writes.

![](images/d198b176a526da1f74f91d4fb3c2d3df0faa7461546aba6cc17c8556c55a6a03.jpg)  
Figure 14. Multiple byte SPI write protocol (2-byte example) (in mode 3)

# 5.1.3.3 SPI read in 3-wire mode

3-wire mode is entered by seting the IF_CFG (03h) (SiM) bit equal to 1 (SPI serial interface mode selection).

![](images/4e509f794a27bf5421d4563066323e0054509d2e200cb9a8d255a51772166d46.jpg)  
Figure 15. SPI read protocol in 3-wire mode (in mode 3)

The SPI read command is performed with 16 clock pulses: bit 0: READ bit. The value is 1.   
bit 1-7: address AD(6:0). This is the address field of the indexed register.   
bit 8-15: data DO(7:0) (read mode). This is the data that is read from the device (MSb first).   
A multiple read command is also available in 3-wire mode.

# 5.2

# MIPI I3C® interface

# 5.2.1 MIPI I3C® slave interface

The LSM6DSV16X interface includes an MIPl I3C® sDR only slave interface (compliant with release 1.1 of the specification) with MIPl 13C® SDR embedded features:

中 CCC command Direct CCC communication (SET and GET) Broadcast CCC communication Private communications Private read and write for single byte Multiple read and write In-band interrupt request Slave reset pattern Group address Full range Vdd_IO support Asynchronous modes 0 and 1 Synchronous mode Error detection and recovery methods (S0-S6)

In order to disable the MIPI I3C® block, 12C_I3C_disable = 1 must be written in IF_CFG (03h).

# 5.2.2 MIPl I3c® ccC supported commands

The list of MIPl l3C® CCC commands supported by the device is detailed in the follwing table.

Table 17. MIPl I3c® ccC commands   

<table><tr><td colspan="1" rowspan="1">Command</td><td colspan="1" rowspan="1">Command code</td><td colspan="1" rowspan="1">Default</td><td colspan="2" rowspan="2">DescriptionDAA procedure</td></tr><tr><td colspan="1" rowspan="1">ENTDAA</td><td colspan="1" rowspan="1">0×07</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">SETDASA</td><td colspan="1" rowspan="1">0×87</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Assign dynamic address using static address 0x6B/0x6A depending on SDO pin</td></tr><tr><td colspan="1" rowspan="1">ENEC</td><td colspan="1" rowspan="1">0×80/0×00</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Slave activity control (direct and broadcast)</td></tr><tr><td colspan="1" rowspan="1">DISEC</td><td colspan="1" rowspan="1">0×81/0x01</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Slave activity control (direct and broadcast)</td></tr><tr><td colspan="1" rowspan="1">ENTASO</td><td colspan="1" rowspan="1">0×82/0×02</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Enter activity state (direct and broadcast)</td></tr><tr><td colspan="1" rowspan="1">SETXTIME</td><td colspan="1" rowspan="1">0×98/0x28</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Timing information exchange</td></tr><tr><td colspan="1" rowspan="1">GETXTIME</td><td colspan="1" rowspan="1">0x99</td><td colspan="1" rowspan="1">0x070x000x050x92</td><td colspan="2" rowspan="1">Timing information exchange</td></tr><tr><td colspan="1" rowspan="1">RSTDAA</td><td colspan="1" rowspan="1">0x06</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Reset the assigned dynamic address (broadcast only)</td></tr><tr><td colspan="1" rowspan="1">SETMWL</td><td colspan="1" rowspan="1">0x89 /0×08</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Define maximum write length during private write (direct and broadcast)</td></tr><tr><td colspan="1" rowspan="1">SETMRL</td><td colspan="1" rowspan="1">0x8A/0x09</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Define maximum read length during private read (direct and broadcast)</td></tr><tr><td colspan="1" rowspan="1">SETNEWDA</td><td colspan="1" rowspan="1">0×88</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Change dynamic address</td></tr><tr><td colspan="1" rowspan="1">GETMWL</td><td colspan="1" rowspan="1">0x8B</td><td colspan="1" rowspan="1">0x000x08(2 byte)</td><td colspan="2" rowspan="1">Get maximum write length during private write</td></tr><tr><td colspan="1" rowspan="1">GETMRL</td><td colspan="1" rowspan="1">0x8C</td><td colspan="1" rowspan="1">0x000x100x09(3 byte)</td><td colspan="2" rowspan="1">Get maximum read length during private read</td></tr><tr><td colspan="1" rowspan="2">GETPID</td><td colspan="1" rowspan="2">0x8D</td><td colspan="1" rowspan="1">0x020x080x000×700x920x0B</td><td colspan="2" rowspan="1">SDO = 1</td></tr><tr><td colspan="1" rowspan="1">0x020x080x000×700x120x0B</td><td colspan="2" rowspan="1">SDO = 0</td></tr><tr><td colspan="1" rowspan="1">GETBCR</td><td colspan="1" rowspan="1">0x8E</td><td colspan="1" rowspan="1">0x07(1 byte)</td><td colspan="2" rowspan="1">Bus characteristics register</td></tr><tr><td colspan="1" rowspan="1">GETDCR</td><td colspan="1" rowspan="1">0x8F</td><td colspan="1" rowspan="1">0x44 default</td><td colspan="2" rowspan="1">MIPI |3C@device characteristics register</td></tr><tr><td colspan="1" rowspan="1">GETSTATUS</td><td colspan="1" rowspan="1">0x90</td><td colspan="1" rowspan="1">0x000x00(2 byte)</td><td colspan="2" rowspan="1">Status register</td></tr><tr><td colspan="1" rowspan="1">Command</td><td colspan="1" rowspan="1">Command code</td><td colspan="1" rowspan="1">Default</td><td colspan="2" rowspan="2">DescriptionReturn max write and read speed</td></tr><tr><td colspan="1" rowspan="1">GETMXDS</td><td colspan="1" rowspan="1">0x94</td><td colspan="2" rowspan="1">0x080x60</td></tr><tr><td colspan="1" rowspan="1">GETCAPS</td><td colspan="1" rowspan="1">0x95</td><td colspan="1" rowspan="1">0x000x110x180x00</td><td colspan="2" rowspan="1">Provide information about device capabities and supported extended features</td></tr><tr><td colspan="1" rowspan="1">SETGRPA</td><td colspan="1" rowspan="1">0x9B</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Group address assignment command</td></tr><tr><td colspan="1" rowspan="1">RSTGRPA</td><td colspan="1" rowspan="1">0x2C/0x9C</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Reset the group address</td></tr><tr><td colspan="1" rowspan="1">RSTACT</td><td colspan="1" rowspan="1">0x9A/0x2A</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">Configure slave reset action</td></tr></table>

# 5.2.3

# Overview of anti-spike filter management

The device acts as a standard IC target as long as it has an I²C static address. The device is capable of detecting and disabling the IC anti-spike fiter ater detecting the broadcast address (7'h7E/W). In order to guarantee proper behavior of the device, the I3C master must emit the first START, 7h7E/W at open-drain speed using IC fast mode plus reference timing.

After detecting the broadcast address, the device can receive the I3C dynamic address following the I3C pushpulltiming. If the device is not assigned a dynamic address, then the device continues to operate as an IC device with no anti-spike fiter. For the case in which the host decides to keep the device as IC with anti-spike filter, there is a configuration required to keep the anti-spike filter active. This configuration is done by writing the ASF_CTRL bit to 1 in the IF_CFG (03h) register. This configuration forces the anti-spike fiter to always be turned on instead of being managed by the communication on the bus.

# 5.3 Master I²C interface

If the LSM6DSV16X is configured in mode 2, a master 1C line is available. The master serial interface is mapped to the following dedicated pins.

Table 18. Master IC pin details   

<table><tr><td rowspan=1 colspan=1>Pin name</td><td rowspan=1 colspan=1>Pin description</td></tr><tr><td rowspan=1 colspan=1>MSCL</td><td rowspan=1 colspan=1>I²C serial clock master</td></tr><tr><td rowspan=1 colspan=1>MSDA</td><td rowspan=1 colspan=1>I²C serial data master</td></tr><tr><td rowspan=1 colspan=1>MDRDY</td><td rowspan=1 colspan=1>I²C master external synchronization signal</td></tr></table>

# 5.4

# Auxiliary SPI interface

If the LSM6DSV16X is configured in mode 3, the auxiliary SPl is available. The auxiary SPlinterface is mapped to the follwing dedicated pins.

Table 19. Auxiliary SPI pin details   

<table><tr><td rowspan=1 colspan=1>Pin name</td><td rowspan=1 colspan=1>Pin description</td></tr><tr><td rowspan=1 colspan=1>OCS_Aux</td><td rowspan=1 colspan=1>Enables auxiliary SPl 3/4-wire</td></tr><tr><td rowspan=1 colspan=1>SDx/AH1/Qvar1</td><td rowspan=1 colspan=1>Auxiliary SPl 3/4-wire data input (SD_Aux) and SPl 3-wire data output (SDO_Aux)</td></tr><tr><td rowspan=1 colspan=1>SCx/AH2/Qvar2</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire interface serial port clock</td></tr><tr><td rowspan=1 colspan=1>SDO_Aux</td><td rowspan=1 colspan=1>Auxiliary SPI 4-wire data output (SDO_Aux)</td></tr></table>

When the LSM6DSV16X is configured in mode 3, the auxiliary SPI can be connected to a camera module for OIs support.

# 6 Functionality

This section describes all the operating modes and power modes of the LSM6DSV16X.

# Note:

Refer to the product application note for the details regarding operating/power mode configurations, settings, turn-on/off time and on-the-fly changes.

# 6.1

# Operating modes

In the LSM6DSV16X, the accelerometer and the gyroscope can be turned on/of independently of each other and are allowed to have diferent ODRs and power modes.

The LSM6DSV16X has three operating modes available:

Only accelerometer active and gyroscope in power-down   
Only gyroscope active and accelerometer in power-down   
Both accelerometer and gyroscope sensors active with independent ODR and power mode

The accelerometer is activated from power-down by writing ODR_XL_[3:0] in CTRL1 (10h) while the gyroscope is activated from power-down by writing ODR_G_[3:0] in CTRL2 (11h). For combo mode, the ODRs are totally independent.

# 6.2

# Accelerometer power modes

In the LSM6DSV16X, the accelerometer can be configured in five diferent operating modes: power-down mode, low-power mode (1, 2, 3), normal mode, high-performance mode and high-accuracy ODR mode.

The operating mode selected depends on the value of the OP_MODE_XL_[2:0] bits in CTRL1 (10h).

If the value of the OP_MODE_XL_[2:0] bits is 000 (default), high-performance mode is valid for al ODRs (from 7.5 Hz up to 7.68 kHz).

Normal mode is available for ODR values from 7.5 Hz to 1.92 kHz and it is enabled by setting the OP_MODE_XL_[2:0] bits to 111. Normal mode cannot be used in mode 3 connection mode.

In high-performance mode and in normal mode the analog anti-aliasing fiter is active.

_oW-power mode is available for lower ODRs (1.875 Hz, 15 Hz, 30 Hz, 60 Hz, 120 Hz, 240 Hz). The three ow-power modes are enabled by setting OP_MODE_XL_[2:0] to 100 (LPM1), 101 (LPM2), 10 (LPM3).

High-accuracy ODR mode is available for ODR values from 15 Hz up to 7.68 kHz and it is enabled by setting the OP_MODE_XL_[2:0] bits to 001. Refer to Section 6.5 High-accuracy ODR mode for more details.

The embedded functions based on accelerometer data (free-fall, 6D/4D, tap/double-tap, wake-up, activity inactivity, stationary/motion, step counter, step detection, significant motion, tit) and the FiFO batching functionality are supported in all modes.

# 6.3

# Accelerometer dual-channel mode

The LSM6DSV16X accelerometer block has a dual-channel architecture able to work with two different ful scales simultaneously. By default, the device operates in single-channel mode supporting FS scale values from ±2 g through ±16 g and different power modes, as described in Section 6.2 Accelerometer power modes. The block diagrams in the following figures show the configuration of acceleration data processing in the two diferent modes.

![](images/d3a81f0fd64663151f21c624b10cca906c5f8454dc5d230f24565aaf17ca673a.jpg)  
Figure 16. Single-channel mode (XL_DualC_EN = 0)

![](images/cf3f4d03f3c581a07376a8deeff9dd3fa8f375c41af403a12dd46b20c8425c29.jpg)  
Figure 17. Dual-channel mode (XL_DualC_EN = 1)

The dual-channel functionality can be enabled/disabled by configuring the bit XL_DualC_EN to 1 (enable) or to 0 (disable) in CTRL8 (17h).

Referring to Figure 17. Dual-channel mode (XL_DualC_EN = 1), when the dual-channel mode has been activated:

Channel 1 supports user-selectable ful-scale acceleration range of ±2/±4/±8/±16 g based on the value of the FS_XL_[1:0] bits in the CTRL8 (17h) register. 2 Channel 2 full scale is set to ±16 g. Acceleration data are available in the output registers from UI_OUTX_L_A_OIS_DualC (34h) and Ul_OUTX_H_A_OIS_DualC (35h) through UI_OUTZ_L_A_OIs_DualC (38h) and UI_OuTZ_H_A_OIs_DualC (39h)).

# 6.4 Gyroscope power modes

In the LSM6DSV16X, the gyroscope can be configured in five diferent operating modes: power-down mode, sleep mode, low-power mode, high-performance mode and high-accuracy ODR mode.

The operating mode selected depends on the value of the OP_MODE_G_[2:0] bits in CTRL2 (11h).

If the value of the OP_MODE_G_[2:0] bits is 000 (default), high-performance mode is valid for all ODRs (from 7.5 Hz up to 7.68 kHz).

Low-power mode is available for lower ODRs (7.5 Hz, 15 Hz, 30 Hz, 60 Hz, 120 Hz, 240 Hz) and it is enabled by setting the the OP_MODE_G_[2:0] bits to 101.

High-accuracy ODR mode is available for ODR values from 15 Hz up to 7.68 kHz and it is enabled by setting the OP_MODE_G_[2:0] bits to 001. Refer to Section 6.5 High-accuracy ODR mode for more details.

# 6.5 High-accuracy ODR mode

High-accuracy ODR (HAODR) mode can be enabled to reduce the part-to-part output data rate variation. It supports accelerometer only, gyroscope only, and combo (accelerometer and gyroscope) modes. When this mode is used for one sensor (accelerometer or gyroscope), the other sensor also has to be configured in high-accuracy ODR (HAODR) mode.

The main high-accuracy ODR features are:

Noise level is aligned with high-performance mode   
Power consumption increase of 20 μA (typical) vs. the corresponding high-performance mode configuration selected   
The UI channel bandwidth can be selected through the gyroscope LPF1 and accelerometer HPF/LPF2 filters.   
When HAODR mode is enabled, it is applied to the Ul accelerometer, UI gyroscope, EIS gyroscope, and temperature. It is not applied to OIS accelerometer/gyroscope channels.

# Note:

HAODR mode has to be enabled / disabled when the device is in power-down mode.

When HAODR mode is enabled, two different sets of ODRs are supported based on the configuration of the HAODR_SEL_[1:0] bitfield in the HAODR_CFG (62h) register, as shown in the table below.

# Note:

High-accuracy ODR mode is not compatible with the analog hub / Qvar functionality and the activityinactivity functionality (motion/stationary can be used).

Table 20. Accelerometer and gyroscope ODR selection in high-accuracy ODR mode   

<table><tr><td rowspan=1 colspan=1>ODR_XL _[3:0]ODR_G_[3:0]</td><td rowspan=1 colspan=1>ODR [Hz]HAODR_SEL_[1:0]= 00</td><td rowspan=1 colspan=1>ODR [Hz]HAODR_SEL_[1:0] = 01</td><td rowspan=1 colspan=1>ODR [Hz]HAODR_SEL_[1:0] = 10</td></tr><tr><td rowspan=1 colspan=1>0000</td><td rowspan=1 colspan=1>Power-down</td><td rowspan=1 colspan=1>Power-down</td><td rowspan=1 colspan=1>Power-down</td></tr><tr><td rowspan=1 colspan=1>0001</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td></tr><tr><td rowspan=1 colspan=1>0010</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td></tr><tr><td rowspan=1 colspan=1>0011</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>15.625</td><td rowspan=1 colspan=1>12.5</td></tr><tr><td rowspan=1 colspan=1>0100</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>31.25</td><td rowspan=1 colspan=1>25</td></tr><tr><td rowspan=1 colspan=1>0101</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>62.5</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>0110</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>100</td></tr><tr><td rowspan=1 colspan=1>0111</td><td rowspan=1 colspan=1>240</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>200</td></tr><tr><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>480</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>400</td></tr><tr><td rowspan=1 colspan=1>1001</td><td rowspan=1 colspan=1>960</td><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>800</td></tr><tr><td rowspan=1 colspan=1>1010</td><td rowspan=1 colspan=1>1920</td><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>1600</td></tr><tr><td rowspan=1 colspan=1>1011</td><td rowspan=1 colspan=1>3840</td><td rowspan=1 colspan=1>4000</td><td rowspan=1 colspan=1>3200</td></tr><tr><td rowspan=1 colspan=1>1100</td><td rowspan=1 colspan=1>7680</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>6400</td></tr><tr><td rowspan=1 colspan=1>Others</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1>Reserved</td></tr></table>

# 6.6

# ODR-triggered mode

When ODR-triggered mode is enabled, a reference signal must be provided to the INT2 pin, and the device then automatically aligns (in frequency and phase) the data generation to the edges of the reference signal.

It supports accelerometer only, gyroscope only, and combo (accelerometer and gyroscope) modes. When both the accelerometer and gyroscope are enabled, the user must configure the same ODR on both the accelerometer and gyroscope.It is not possible to select different ODRs for the accelerometer and gyroscope; f different output data rate values are set, the ODR configured for the gyroscope data is also applied to the accelerometer data.

The full-scale configurations are totally independent between the accelerometer and gyroscope and they can be set in any combination.

# Note:

ODR-triggered mode has to be enabled / disabled when the device is in power-down mode.

Note:

When ODR-triggered mode is enabled, the 1100 configuration of the ODR_XL_[3:0] bits in register CTRL1 (10h) and the 1100 configuration of the ODR_ G_[3:0] bits in register CTRL2 (11h) cannot be used.

Note:

ODR-triggered mode is not compatible with the analog hub /Qvar functionality nor the EIS functionality

# 6.7

# Analog hub functionality

The LSM6DSV16X embeds an analog hub sensing functionality which is able to connect an analog input and ;onvert it to a digital signal for embedded processing.

In the LSM6DSV16X, the analog hub has a dedicated channel that can be activated by seting the AH_QVAR_EN bit to 1 in the CTRL7 (16h) register.

The accelerometer sensor must be set in high-performance mode or in normal mode when the analog hub channel is enabled.

The analog hub data-ready signal s represented by the AH_QVARDA bit of the STATUS_REG (1Eh) register. This signal can be driven to the INT2 pin by setting the INT2_ DRDY_AH_QVAR bit to 1 in the CTRL7 (16h) register.

Analog hub data are available as a 16-bit word in two's complement in the AH_QVAR_OUT_L (3Ah) and AH_QVAR_OUT_H (3Bh) registers at a fixed rate of 240 Hz (typical).

Analog signal data can be also processed by MLC/FSM logic.

The analog hub functionality is available in mode 1 connection mode for the IC interface only. The external analog lines have to be connected to pin 2 (SDx/AH1/Qvar1) and/or pin 3 (SCx/AH2/Qvar2), so the I²C-master interface (mode 2) and the auxiliary SPI (mode 3) are not available when the analog hub is used.

The equivalent input impedance of the analog hub buffers can be selected by properly setting the AH_QVAR_C_ZIN_[1:0] bits in the CTRL7 (16h) register.

# 6.8 Qvar functionality

The LSM6DSV16X embeds a Qvar sensor which is able to detect electric charge variations in the proximity of the external electrodes connected to the device.

In the LSM6DSV16X, Qvar has a dedicated channel that can be activated by setting the AH_QVAR_EN bit to 1 in the CTRL7 (16h) register.

The accelerometer sensor must be set in high-performance mode or in normal mode when the Qvar channel is enabled.

The Qvar data-ready signal is represented by the AH_QVARDA bit of the STATUS_REG (1Eh) register. This signal can be driven to the INT2 pin by seting the INT2_ DRDY_AH_QVAR bit to 1 in the CTRL7 (16h) register.

Qvar data are available as a 16-bit word in two's complement in the AH_QVAR_OUT_L (3Ah) and AH_QVAR_OUT_H (3Bh) registers at a fixed rate of 240 Hz (typical).

Qvar data can also be processed by MLC/FSM logic.

The Qvar functionality is available in mode 1 connection mode for the IC interface only. The external electrodes have to be connected to pin 2 (SDx/AH1/Qvar1) and/or pin 3 (SCx/AH2/Qvar2), so the IC-master interface (mode 2) and the auxiliary SPI (mode 3) are not available when Qvar is used.

The equivalent input impedance of the Qvar buffers can be selected by properly setting the AH_QVAR_C_ZIN_[1:0] bits in the CTRL7 (16h) register.

# 6.9 Block diagram of filters

![](images/87e282f5530ac7b1371489460d4b315aafce074c41c58077f89ed9fd110cc9c9.jpg)  
Figure 18. Block diagram of filters

# 6.9.1

# Block diagrams of the accelerometer filters

In the LSM6DSV16X, the filtering chain for the accelerometer part is composed of the following:

Digital fiter (LPF1) Composite filter

Details of the block diagram appear in the following figure.

![](images/95194c12c29c08ce76189de84ef82c3879e16a3ce2e2a51562e7ededc827ecc2.jpg)  
Figure 19. Accelerometer UI chain

![](images/84de4bf06762b437e82794ba35357ecbec55a3ec955ffa089d4b53eef8872ba8.jpg)  
Figure 20. Accelerometer composite filter

1. The cutoff value of the LPF1 output is ODR/2 when the accelerometer is in high-performance mode, high-accuracy ODR mode, or normal mode. This value is equal to 2300 Hz when the accelerometer is in low-power mode 1 (2 mean), 912 Hz in low-power mode 2 (4 mean) or 431 Hz in low-power mode 3 (8 mean).

Embedded functions include finte state machine, machine learning core, pedometer,step detector and step counter, significant motion detection, and tit functions.

The acceleromete fitering chain when mode 3 is enabled i illustrated in the following figure.

![](images/fce5f4665e431a069d08de3f1f581475b251956fa9b71fe89d15240211c58e91.jpg)  
Figure 21. Accelerometer chain with mode 3 enabled

# Note:

The accelerometer OIS chain is enabled by setting the OIS_XL_EN bit to 1 in the UI_CTRL1_OIS (70h) / SPI2_CTRL1_OIS (70h) register.

The configuration of the accelerometer UI chain is not affected by enabling/disabling the accelerometer OIS chain, with one exception: accelerometer normal operating mode (OP_MODE_XL_I2:0] = 111 in the CTRL1 (10h) register) cannot be used when the accelerometer Ois chain is enabled.

Accelerometer output values are available in the following registers with ODR at 7.68 kHz:

UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h) through   
Ul_OuTZ_L_A_OIS_DualC (38h) and UI_OuTZ_H_A_OIs_DualC (39h)   
SPI2_OUTx_L_A_OIS (28h) and SPI2_OUTX_H_A_OIS (29h) through SPI2_OUTZ_L_A_OIS (2Ch) and   
SPI2_OUTZ_H_A_OIS (2Dh)

# Note:

When the accelerometer OIs is used, refer to the product application note for the power mode configuration and settings.

# 6.9.2

# Block diagrams of the gyroscope filters

In the LSM6DSV16X, the gyroscope filtering chain depends on the mode configuration:

Mode 1 (for user interface (UI) and electronic image stabizatio (EiS) functionalit through the primary interface) and mode 2

![](images/9cf01b579b1deb63c9dbd26ee9161ced845d3089cf490f544a2a3ce0b599aae5.jpg)  
Figure 22. Gyroscope digital chain - mode 1 (Ul/EiS) and mode 2

When the gyroscope OIS or EIS chain is enabled, the LPF1 fiter is not available in the gyroscope UI chain. It is recommended to avoid using the LPF1 fiter in the gyroscope UI chain when the gyroscope OIS or EIS is used.

2. The LPF1 fiter is available in high-performance mode only. If the gyroscope is configured in low-power mode, the LPF1 filter is bypassed.

In this configuration, the gyroscope ODR is selectable from 7.5 Hz up to 7.68 kHz. A low-pass fiter (LPF1) is available, for more details about the filter characteristics see Table 64. Gyroscope LPF1 + LPF2 bandwidth selection.

The digitl LPF2 fite's cutof frequency depends on the selected gyroscope ODR, as indicated in the following table.

Table 21. Gyroscope LPF2 bandwidth selection   

<table><tr><td rowspan=1 colspan=1>Gyroscope ODR [Hz]</td><td rowspan=1 colspan=1>LPF2 cutoff HZz]</td></tr><tr><td rowspan=1 colspan=1>7.5</td><td rowspan=1 colspan=1>3.4</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>6.6</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>13.0</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>24.6</td></tr><tr><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>49.4</td></tr><tr><td rowspan=1 colspan=1>240</td><td rowspan=1 colspan=1>96</td></tr><tr><td rowspan=1 colspan=1>480</td><td rowspan=1 colspan=1>187</td></tr><tr><td rowspan=1 colspan=1>960</td><td rowspan=1 colspan=1>342</td></tr><tr><td rowspan=1 colspan=1>1.92 kHz</td><td rowspan=1 colspan=1>491</td></tr><tr><td rowspan=1 colspan=1>3.84 KHz</td><td rowspan=1 colspan=1>528</td></tr><tr><td rowspan=1 colspan=1>7.68 KHz</td><td rowspan=1 colspan=1>537</td></tr></table>

# Note:

Data can be acquired from the output registers and FIFO over the primary IC/MIP 3c®/SPl interface.

Mode 3 (for OIS functionality)

![](images/ee2e715a9baa7c5aa9f36f0db2eef1dbe65f440336692c6d5b6a4d71236aae82.jpg)  
Figure 23. Gyroscope digital chain - mode 3 (OIs)

1. When the gyroscope OIS or EIS chain is enabled, the LPF1 filter is not available in the gyroscope UI chain. 2. It is recommended to avoid using the LPF1 fiter in mode 1/2 when the gyroscope OIS or EIS chain is used. 3. When the gyroscope OIs is used, refer to the product application note for the power mode configuration and settings.

The auxiliary interface needs to be enabled in UI_CTRL1_OIS (70h) / SPI2_CTRL1_OIS (70h). In mode 3 configuration, there are two paths:

The chain for user interface (UI) where the ODR is selectable from 7.5 Hz up to 7.68 kHz The chain for OIS where the ODR is at 7.68 kHz and the LPF1 is available. The LPF1 configuration depends on the setting of the LPF1_G_OIS_BW_[1:0] bits in register UI_CTRL2_OIS (71h) / SPI2_CTRL2_OIS (71h); for more details about the fiter characteristics see UI_CTRL2_OIS (71h). Gyroscope output values are in registers 22h to 27h if read from the Auxi_SPl or in registers 2Eh to 33h if read from the primary interface with the selected full scale FS_G_OiS_[1:0] bits in UIl_CTRL2_OIS (71h) / SPI2_CTRL2_OIS (71h).

# 6.10 Enhanced EIS

The LSM6DSV16X offers advanced desig flexibit for EIS applications: enhanced EIS functionality has a dedicated channel and processing with independent filtering.

Enhanced EIS main features:

Enhanced EIS channel gyroscope data can be read over the primary interfaces through ²C / MiPl 13c®/ SPI.

EIS data are available in free-run mode in the output registers (Ul_OUTX_L_G_OIS_EIS (2Eh) and UI_OUTX_H_G_OIS_EIS (2Fh) through UI_OUTZ_L_G_OIS_EIS (32h) and UI_OUTZ_H_G_OIS_EIS (33h)) by Setting the G EIS_ON G_OIS_OUT REG bit to 1 in the CTRL EIS (6Bh) register r in FIFO (by setting the G_EiS_FIFO_EN bit to T in the FIFO_CTRL4 (OAh) register) with dedicated TAG and timestamp configurable using FIFO_CTRL4 (0Ah).

Enhanced EIS option is compatible with mode 3 selection. When EIS data-out are read from the output registers (seting G_EIS_ON_G_OIS_OUT_REG bit), data from the gyroscope OIS chain can be only read from the auxiliary SPl interface.

![](images/5557f913d468f4e5df215e422c676e76cc7913b8f8dc162cf1c64034b1ec10bd.jpg)  
Figure 24. LSM6DsV16X supports Ul, enhanced EIS, and OIS processing simultaneously

![](images/19df31c809073749f9be54751948e497b313f3aba40a57ff5f8758a3a517f6ce.jpg)  
Figure 25. Gyroscope enhanced EIS and UI block diagram

When enhanced EIS mode is activated through the ODR_EIS_[1:0] bits in the CTRL_EIS (6Bh) register:

Gyroscope UI can be configured only in power-down mode, high-performance mode, or high-accuracy ODR mode.   
Gyroscope EIS full scale can be selected by using the FS_G_EIS_[2:0] bits in the CTRL_ EIS (6Bh) register.   
Gyroscope EIS data rate selectable at 1.92 kHz or 960 Hz configurable through the ODR_G_EIS_[1:0] bits in the CTRL_EIS (6Bh) register.   
LPF_EiS low-pass fiter (refer to Figure 25) bandwidth selection can be configured through the   
LPF_G_EIS_BW bit in the CTRL_EIS (6Bh) register.

# 6.11 OIS

This section describes OIS functionality. There is a dedicated gyroscope and accelerometer DSP for OIS.   
The device also supports self-test functionality on the OIs side.

# 6.11.1

# Enabling OIs functionality and connection schemes

There are two diferent ways in order to enable and configure OIS functionality:

Auxiliary SPI full control: Enabling and configuration done from the auxiliary SPI

Primary interface full control: Enabling and configuration done from the primary interface

The configurations that allow selecting these two different options are done using the OIS_CTRL_FROM_U bit in the FUNC_CFG_ACCESS (01h) register as described in the following table.

Table 22. OIS configurations   

<table><tr><td rowspan=1 colspan=1>OIS_CTRL_FROM_UI</td><td rowspan=1 colspan=1>Ois configuration option</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Auxiliary SPl full control</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Primary interface ful control</td></tr></table>

# 6.11.1.1

# Auxiliary SPI full control

This is the default condition of the device. The camera module is completely independent from the application processor as shown in Figure 26.

The auxiary SPI can configure OIS functionality through SPI2_INT_OIS (6Fh), SPI2_CTRL1_OIS (70h), SPI2_CTRL2_OIS (71h), SPI2_CTRL3_OIS (72h).

Reading from the auxiliry SPl is enabled only when the SPI2_READ_EN bit n the SPI2_CTRL1_OIS (70h) register is set to 1.

The primary interface can access the OIS control registers (UI_NT_OIS (6Fh), UI_CTRL1_OIS (70h), UI_CTRL2_OIS (71h), UI_CTRL3_OIS (72h)) in read mode.

![](images/72d0a6ed22cf22ca79a343959a4dcc0d24a4762b2d32a2b4df80b51437e8f180.jpg)  
Figure 26. Auxiliary SPI full control

# 6.11.1.2 Primary interface full control

This option allows the application processor to configure all OIS functionalities from the primary interface. This option allows using embedded OlS data for both the main and front camera, connecting them to the application processor (eventually adding a context hub) as shown in Figure 27: the AP can also do some processing on the data before sending them to the cameras.

In order to place the device in this mode, the OIS_CTRL_ FROM_UI bit in the FUNC_CFG_ACCESS (01h) register must be set to 1 from the primary interface.

![](images/147434122a0ea19ee5d8d44c3fbea84744f2fc09f2433bc944d7b60f7ccbaee2.jpg)  
Figure 27. OIs Primary interface full control

Then, the AP can configure OIS functionalties through UI_INT_OIS (6Fh), UI_CTRL1_OIS (70h), UI_CTRL2_OIS (71h), UI_CTRL3_OIS (72h).

Reading from the auxiliary SPI can be enabled by setting the SPI2_ READ_EN bit in the UI_CTRL1_OIS (70h) register to 1 in order to directly read OIS data (as shown in Figure 27 (b). The auxiliary SPI can access the SPI2_INT_OIS (6Fh), SPI2_CTRL1_OIS (70h), SPI2_CTRL2_OIS (7ih), and SPI2_CTRL3_OIS (72h) registers in read-only mode.

Note:

The OIS_CTRL_FROM_ UI bit is reset by the software reset procedure.

# 6.12 FIFO

The presence of a FIFO allows consistent power saving for the system since the host processor does not need continuously polldata from the sensor, but t can wake up only when needed and burst the significant data out from the FIFO.

The LSM6DSV16X embeds 1.5 KB of data in FIFO (up to 4.5 KB with the compression feature enabled) to store the following data:

Gyroscope   
Accelerometer   
External sensors (up to 4)   
Step counter   
Timestamp   
Temperature   
MLC features and filters   
SFLP output data (quaternion, gyroscope bias, gravity vector)

Writing data in the FIFO can be configured to be triggered by the:

Accelerometer / gyroscope data-ready signal Sensor hub data-ready signal Step detection signal

The applications have maximum flexibility in choosing the rate of batching for physical sensors with FIFOdedicated configurations: accelerometer, gyroscope and temperature sensor batch rates can be selected by the user. External sensor writing in FIFO can be triggered by the accelerometer data-ready signal or by an external sensor interupt. The step counter can be stored in FIFO with associated timestamp each time a step is detected. It is possible to select decimation for timestamp batching in FiFO with a factor of 1, 8, or 32.

The reconstruction of a FIFO stream is a simple task thanks to the FIFO_DATA_OUT_TAG byte that lows recognizing the meaning of a word in FIFO.

FIFO allows correct reconstruction of the timestamp information for each sensor stored in FIFO. If a change in the ODR or BDR (batch data rate) configuration is performed, the application can correctly reconstruct the timestamp and know exactly when the change was applied without disabling FIFO batching. FIFO stores information of the new configuration and timestamp in which the change was applied in the device.

Finally, FIFO embeds a compression algorithm that the user can enable in order to have up to 4.5 KB data stored in FIFO and take advantage of interface communication length for FIFO flushing and communication power consumption.

The programmable FIFO watermark threshold can be set using the WTM[7:0] bits in the FIFO_CTRL1 (07h) register. To monitor the FIFO status, dedicated registers (FIFO_STATUS1 (1Bh), FIFO_STATUS2 (1Ch) can be read to detect FIFO overrun events, FiFO full status, FIFO empty status, FiFO watermark status and the number of unread samples stored in the FIFO. To generate dedicated interrupts on the INT1 and INT2 pins of these status events, the configuration can be set in INT1_CTRL (0Dh) and INT2_CTRL (0Eh).

The FIFO buffer can be configured according to seven different modes:

Bypass mode   
FIFO mode   
Continuous mode   
Continuous-to-FIFO mode   
ContinuousWTM-to-full mode   
Bypass-to-continuous mode   
Bypass-to-FIFO mode

Each mode is selected by the FIFO_MODE_[2:0] bits in the FIFO_CTRL4 (OAh) register.

# 6.12.1 Bypass mode

In bypass mode (FIFO_CTRL4 (OAh)(FIFO_MODE_[2:0] = 000), the FIFO is not operational and it remains empty.   
Bypass mode is also used to reset the FIFO when in FIFO mode.

# 6.12.2 FIFO mode

In FIFO mode (FIFO_CTRL4 (0OAh)(FIFO_MODE_[2:0] = 001) data from the output channels are stored in the FIFO untilit is full.

To reset FIFO content, bypass mode should be selected by writing FIFO_CTRL4 (0OAh)(FIFO_MODE_[2:0]) to 000. After this reset command, t is possible to restart FiFO mode by writing FIFO_CTRL4 (OAh) (FIFO_MODE_[2:0]) to 001.

The FIFO buffr memorizes up to 4.5 KB of data (with compression enabled) but the depth of the FIFO can be resized by setting the WTM[7:0] bits in FIFO_CTRL1 (07h).If the STOP_ON_WTM bit in FIFO_CTRL2 (08h) is set to 1, FIFO depth is limited up to the WTM[7:0] bits in the FIFO_CTRL1 (07h) register.

# j.12.3 Continuous mode

Continuous mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 110) provides a continuous FIFO update: as new data arrives, the older data is discarded.

A FIFO threshold flag FIFO_STATUS2 (1Ch)(FIFO_WTM_IA) is asserted when the number of unread samples in FIFO is greater than or equal to FIFO_CTRL1 (07h) (WTM[7:0]).

It is possible to route the FIFO_WTM_IA flag to the INT1 pin by writing in register INT1_CTRL (ODh) (INT1_FIFO_TH) = 1 or to the INT2 pin by writing in register INT2_CTRL (OEh)(INT2_FiFO_TH) = 1.

A ful-flag interrupt can be enabled, INT1_CTRL (ODh)(INT1_FIFO_FULL) = 1 or INT2_CTRL (0Eh) (INT2_FiFO_FULL) = 1, in order to indicate FIFO saturation and eventually read its content all at once

If an overrun ocurs, at least one of the oldest samples in FiFO has been overwriten and the FIFO_OVR_IA flag in FIFO_STATUS2 (1Ch) is asserted.

In order to empty the FlFO before i is full i is also possible to pul rom FlFO the number of unread samples available in FIFO_STATUS1 (1Bh) and FIFO_STATUS2 (1Ch)(DIFF_FIFO_[8:0]).

# 6.12.4 Continuous-to-FIFO mode

In continuous-to-FIFO mode (FIFO_CTRL4 (OAh)(FIFO_MODE_[2:0] = 011), FIFO behavior changes according to the trigger event detected in one of the following interrupt events:

Single tap Double tap Wake-up Free-fall D6D

When the selected trigger bit is equal to 1, FIFO operates in FIFO mode.   
When the selected trigger bit is equal to 0, FIFO operates in continuous mode.

# 6.12.5 ContinuousWTM-to-full mode

In continuousWTM-to-ful mode (FIFO_CTRL4 (OAh)(FIFO_MODE_[2:0] = 010), FIFO behavior changes according to the trigger event detected in one of the following interrupt events:

Single tap Double tap Wake-up Free-fall D6D

When the selected trigger bit is equal to 0, FIFO operates in continuous mode with the FIFO size limited to the FIFO watermark level (defined by the WTM[7:0] bits in the FIFO_CTRL1 (07h) register).

When the selected trigger bit is equal to 1, FIFO continues to store data until it is full.

# 6.12.6 Bypass-to-continuous mode

In bypass-to-continuous mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 100), data measurement storage inside FiFO operates in Continuous mode when selected triggers are equal to 1, otherwise FIFO content is reset (bypass mode).

FIFO behavior changes according to the trigger event detected in one of the following interrupt events:

Single tap Double tap Wake-up Free-fall D6D

# 6.12.7 Bypass-to-FIFO mode

In bypass-to-FIFO mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 111), data measurement storage inside FIFO operates in FIFO mode when selected triggers are equal to 1, otherwise FIFO content is reset (bypass mode). FlFO behavior changes according to the trigger event detected in one of the following interrupt events:

Single tap Double tap Wake-up Free-fall D6D

# 6.12.8 FIFO reading procedure

The data stored in FIFO are accessible from dedicated registers and each FIFO word is composed of 7 bytes: one tag byte (FIFO_DATA_OUT_TAG (78h), in order to identify the sensor, and 6 bytes of fixed data (FIFO_DATA_OUT registers from (79h) to (7Eh)).

The DIFF_FIFO_[8:0] field in the FIFO_STATUS1 (1Bh) and FIFO_STATUS2 (1Ch) registers contains the number of words (1 byte TAG + 6 bytes DATA) collected in FIFO.

In adition, it is possible to configure a counter of the batch events of accelerometer or gyroscope sensors. The flag COUNTER_BDR_IA in FIFO_STATUS2 (1Ch) alerts that the counter reaches a selectable threshold (CNT_BDR_TH_[9:0j field in COUNTER_BDR_REG1 (OBh) and COUNTER_BDR_REG2 (OCh). This allows triggering the reading of FIFO with the desired latency of one single sensor. The sensor is selectable using the TRIG_COUNTER_BDR_[1:0] bits in COUNTER_BDR_REG1 (OBh). As for the other FIFO status events, the flag COUNTER_BDR_IA can be routed on the INT1 or INT2 pins by asserting the corresponding bits (INT1_CNT_BDR of INT1_CTRL (ODh) and INT2_CNT_BDR of iNT2_CTRL (OEh)).

In order to maximize the amount of accelerometer and gyroscope data in FIFO, the user can enable the compression algorithm by setting to 1 both the FIFO_COMPR_EN bit in EMB_FUNC_EN_B (05h) (embedded functions registers bank) and the FIFO_COMPR_RT_EN bit in FIFO_CTRL2 (08h). When compression is enabled, it is also possible to force writing noncompressed data at a selectable rate using the UNCOMPR_RATE_[1:0] field in FiFO_CTRL2 (08h).

Meta information about accelerometer and gyroscope sensor configuration changes can be managed by enabling the ODR_CHG_EN bit in FIFO_CTRL2 (08h).

# 7 Application hints

# 7.1 LSM6DsV16X electrical connections in mode 1

![](images/8629ed7d489e543a7624c602024777ef8b6a67d284a8d646014b2280fae24064.jpg)  
Figure 28. LSM6DsV16X electrical connections in mode 1

1. Leave pin electrically unconnected and soldered to PCB.

The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic should be placed as near as possible to the supply pin of the device (common design practice).

The functionality of the device and the measured acceleration/angular rate data is selectable and accessible through the SPi/²C/MIPI 13C® interface.

The functions, the threshold, and the timing of the two interupt pins for each sensor can be completely programmed by the user through the SPI/²C/MIPI I3C® interface.

![](images/7f9d8c62da24e4c67d0b535b147c30fbde437c7d351d3ad72acb1b775e143a76.jpg)  
Figure 29. Qvar external connections to pin 2, 3 (Qvar input)   
(1) ST ESDALCL5-1BM2 is referenced as an ST catalog product but similar features of other ESD diodes also can be used.

Figure 29 provides an example of a test circuit. For a specific application, refer to the related application note.

# 7.2 LSM6DSV16X electrical connections in mode 2

![](images/d7af108283ca47f9fb526f15fcda7d03b97e39c85a776f8307480f7fb72cad04.jpg)  
Figure 30. LSM6DsV16X electrical connections in mode 2

1. Leave pin electrically unconnected and soldered to PCB.

The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic) should be placed as near as possible to the supply pin of the device (common design practice).

The functionality of the device and the measured acceleration/angular rate data is selectable and accessible through the SPi/²C/MIPI I3C® primary interface.

The functions, the threshold, and the timing of the two interrupt pins for each sensor can be completely programmed by the user through the SPl/²C/MIPI 13C® primary interface.

# 7.3 LSM6DSV16X electrical connections in mode 3

![](images/2a2fa93b52c4ac665cb3f161cdfbe2c67e4ac69f6d24e75642b53c62fc2e975a.jpg)  
Figure 31. LSM6DsV16X electrical connections in mode 3 (auxiliary 3/4-wire SPI)

# Note:

When mode 3 is used, the pull-up on pins 10 and 1 can be enabled or disabled (refer to Table 23. Internal pin status). To avoid leakage current, it is not recommended to leave the SPl lines floating (or when the OIS system is off).

The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic) should be placed as near as possible to the supply pin of the device (common design practice).

The functionality of the device is selectable and accessible through the SPl/²C/MiPl I3C® primary interface.

Measured aceleration/angula rate data is selectable and acceibl through the SP/MiPl c@primary interface and auxiliary SPI.

The functions, the threshold, and the timing of the two interrupt pins for each sensor can be completely programmed by the user through the SPI/²C/MIPI I3C® interface.

Note:

When mode 3 is used, refer to the product application note for the power mode configuration and setings

Table 23. Internal pin status   

<table><tr><td rowspan=1 colspan=1>pin#</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Mode 1 function</td><td rowspan=1 colspan=1>Mode 2 function</td><td rowspan=1 colspan=1>Mode 3 function</td><td rowspan=1 colspan=1>Pin status mode 1</td><td rowspan=1 colspan=1>Pin status mode 2</td><td rowspan=1 colspan=1>Pin status mode 3(1)</td></tr><tr><td rowspan=2 colspan=1>1</td><td rowspan=1 colspan=1>SDO</td><td rowspan=1 colspan=1>SPI 4-wire interface serialdata output (SDO)</td><td rowspan=1 colspan=1>SPI 4-wire interface serialdata output (SDO)</td><td rowspan=1 colspan=1>SPI 4-wire interface serialdata output (SDO)</td><td rowspan=2 colspan=1>Default: input without pull-upPull-up is enabled if bitSDO_PU_EN= 1in registerPIN_CTRL (02h).</td><td rowspan=2 colspan=1>Default: input without pull-upPull-up is enabled if bitSDO_PU_EN=1in registerPIN_CTRL (02h).</td><td rowspan=2 colspan=1>Default: input without pull-upPull-up is enabled if bitSDO_PU_EN=1in registerPIN_CTRL (02h).</td></tr><tr><td rowspan=1 colspan=1>SAO</td><td rowspan=1 colspan=1>²C least significant bit ofthe device address (SA0)MIPI 13C@least significantbit of the static address(SAO0)</td><td rowspan=1 colspan=1>²C least significant bit ofthe device address (SA0)MIPI I3C@leas signifcantbit of the static address(SAO)</td><td rowspan=1 colspan=1>²C least significant bitofthe device address (SA0)MIPI 13C@least significantbit of the static adress(SA0)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SDx/AH1/Qvar1</td><td rowspan=1 colspan=1>Connect to Vdd_IO or GNDif the analog hub and/orQvar are disabled.Connect to the analog inputor Qvar electrode 1 if theQvar function is enabled.(2)</td><td rowspan=1 colspan=1>I²C serial data master(MSDA)</td><td rowspan=1 colspan=1>Auxiliary SP| 3/4-wireinterface serial datainput(SDI_Aux) and SPI 3-wire serial data output(SDO_Aux)</td><td rowspan=1 colspan=1>Default: input without pull-upPull-up is enabled if bitSHUB_PU_EN= 1in registerIF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input without pull-upPull-up is enabled if bitSHUB_PU EN = 1 in registerF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input without pull-upPull-up is enabled if bitSHUB_PU_EN=1in registerIF_CFG (03h).</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCx/AH2/Qvar2</td><td rowspan=1 colspan=1>Connect to Vdd_IO or GNDifthe analog hub and/orQvar are disabled.Connect t the analog inputor Qvar electrode2if eQvar function is enabled.2)</td><td rowspan=1 colspan=1>I²C serial clock master(MSCL)</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wireinterface serial port clock(SPC_Aux)</td><td rowspan=1 colspan=1>Default: input without pull-upPull-up is enabled if bitSHUB_PU EN = 1 in register−IF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input without pul-upPull-up is enabled if bitSHUB_PU_EN =1 in registerIF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input without pul-upPull-up is enabled if bitSHUB_PU EN = 1 in registerIF_CFG(03h)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>INT1</td><td rowspan=1 colspan=1>Programmable interrupt 1</td><td rowspan=1 colspan=1>Programmable interrupt 1</td><td rowspan=1 colspan=1>Programmable interrupt 1</td><td rowspan=1 colspan=1>Default: output forced to ground</td><td rowspan=1 colspan=1>Default: output forced to ground</td><td rowspan=1 colspan=1>Default: output forced to ground</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Vdd_10</td><td rowspan=1 colspan=1>Power supply for I/O pins</td><td rowspan=1 colspan=1>Power supply for VO pins</td><td rowspan=1 colspan=1>Power supply for IVO pins</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>oV supply</td><td rowspan=1 colspan=1>oV supply</td><td rowspan=1 colspan=1>o V supply</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>0V supply</td><td rowspan=1 colspan=1>oV supply</td><td rowspan=1 colspan=1>0V supply</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Vdd</td><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>INT2</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2)/ Data enabled(DEN)</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2) / Data enabled(DEN) / IC master externalsynchronization signal(MDRDY)</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2)/ Data enabled(DEN)</td><td rowspan=1 colspan=1>Default: output forced to ground</td><td rowspan=1 colspan=1>Default: output forced to ground</td><td rowspan=1 colspan=1>Default: output forced to ground</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>OCS_Aux</td><td rowspan=1 colspan=1>Connect to Vdd_10 orleave unconnected</td><td rowspan=1 colspan=1>Connect to Vdd_10 orleave unconnected</td><td rowspan=1 colspan=1>Auxiliary SPl 3/4-wireinterface enabled</td><td rowspan=1 colspan=1>Default: input with pull-upPull-up is disabled if bitOIS_PUDIS=1in registerPIN_CTRL (02h).</td><td rowspan=1 colspan=1>Default: input with pull-upPull-up is disabled if bitOIS_PU_DIS=1 in registerPIN_CTRL (02h).</td><td rowspan=1 colspan=1>Default: input without pullupregardss ofthevaeofitOIS_PU_DIS in register PIN_CTRL(02h)))</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>SDO_Aux</td><td rowspan=1 colspan=1>Connect to Vdd_10 orleave unconnected</td><td rowspan=1 colspan=1>Connect to Vdd_10 orleave unconnected</td><td rowspan=1 colspan=1>Auxiliary SPI 3-wire interface: leaveunconnected /AuxilirySPI4-wire interface: serial dataoutput (SDO_Aux)</td><td rowspan=1 colspan=1>Default input with pulupPull-up is disabled if bitOIS_PUDIS=1 in registerPIN_CTRL (02h).</td><td rowspan=1 colspan=1>Default: input with pullupPull-up is disabled if bitOIS_PU_DIS = 1in registerPIN_CTRL (02h).</td><td rowspan=1 colspan=1>Default: input without pull-upPull-up is enabled if bit SIM_OIS = 1(Aux_SPI 3-wire) in reg 70h andbitOIS_PU_DIS =0in registerPIN_CTRL (02h).</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>²C/SPI mode selection(1: SPl idle mode/ Ccommunication enabled;0: SPI communicationmode / C disabled)</td><td rowspan=1 colspan=1>I²C/SPI mode selection(1: SPl idle mode / 1Ccommunication enabled;0: SPI communicationmode / ²C disabled)</td><td rowspan=1 colspan=1>I²C/SPI mode selection(1: SPlidle mode / ?Ccommunication enabled;0:SPI communicationmode / ²C disabled)</td><td rowspan=1 colspan=1>Default: input with pull-upPull-up is disabled if bit12C_13Cdisable=1inregisterIF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input with pull-upPull-up is disabled if bit12C_13Cdisable=1inregisterF_CFG (03h).</td><td rowspan=1 colspan=1>Default: input with pull-upPull-up is disabled if bitI2C_I3C_isable =1 inregisterF_CFG (03h).</td></tr></table>