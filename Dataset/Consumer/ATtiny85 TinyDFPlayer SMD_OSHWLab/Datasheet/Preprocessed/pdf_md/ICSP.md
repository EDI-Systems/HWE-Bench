# In-Circuit Serial Programming™ (ICSP™) Guide

# Note the following details of the code protection feature on Microchip devices:

Microchip products meet the specification contained in their particular Microchip Data Sheet.   
Microchip believes that its family of products is one of the most secure families of its kind on the market today, when used in the intended manner and under normal conditions.   
There are dishonest and possibly illegal methods used to breach the code protection feature. All of these methods, to our knowledge, require using the Microchip products in a manner outside the operating specifications contained in Microchip's Data Sheets. Most likely, the person doing so is engaged in theft of intellectual property.   
Microchip is willing to work with the customer who is concerned about the integrity of their code.   
Neither Microchip nor any other semiconductor manufacturer can guarantee the security of their code. Code protection does not mean that we are guaranteeing the product as “unbreakable.”

Code protection is constantly evolving. We at Microchip are committed to continuously improving the code protection features of our products. Attempts to break microchip’s code protection feature may be a violation of the Digital Millennium Copyright Act. If such acts allow unauthorized access to your software or other copyrighted work, you may have a right to sue for relief under that Act.

Information contained in this publication regarding device applications and the like is intended through suggestion only and may be superseded by updates. It is your responsibility to ensure that your application meets with your specifications. No representation or warranty is given and no liability is assumed by Microchip Technology Incorporated with respect to the accuracy or use of such information, or infringement of patents or other intellectual property rights arising from such use or otherwise. Use of Microchip’s products as critical components in life support systems is not authorized except with express written approval by Microchip. No licenses are conveyed, implicitly or otherwise, under any intellectual property rights.

# Trademarks

The Microchip name and logo, the Microchip logo, KEELOQ, MPLAB, PIC, PICmicro, PICSTART, PRO MATE and PowerSmart are registered trademarks of Microchip Technology Incorporated in the U.S.A. and other countries.

FilterLab, microID, MXDEV, MXLAB, PICMASTER, SEEVAL and The Embedded Control Solutions Company are registered trademarks of Microchip Technology Incorporated in the U.S.A.

Accuron, Application Maestro, dsPIC, dsPICDEM, dsPICDEM.net, ECONOMONITOR, FanSense, FlexROM, fuzzyLAB, In-Circuit Serial Programming, ICSP, ICEPIC, microPort, Migratable Memory, MPASM, MPLIB, MPLINK, MPSIM, PICC, PICkit, PICDEM, PICDEM.net, PowerCal, PowerInfo, PowerMate, PowerTool, rfLAB, rfPIC, Select Mode, SmartSensor, SmartShunt, SmartTel and Total Endurance are trademarks of Microchip Technology Incorporated in the U.S.A. and other countries.

Serialized Quick Turn Programming (SQTP) is a service mark of Microchip Technology Incorporated in the U.S.A.

All other trademarks mentioned herein are property of their respective companies.

© 2003, Microchip Technology Incorporated, Printed in the U.S.A., All Rights Reserved.

Printed on recycled paper.

# Table of Contents

PAGE

# SECTION 1 INTRODUCTION

In-Circuit Serial Programming™ (ICSP™) Guide . .. 1-1

# SECTION 2 TECHNICAL BRIEFS

How to Implement ICSP™ Using PIC12C5XX OTP MCUs .. 2-1   
How to Implement ICSP™ Using PIC16CXXX OTP MCUs ........ .... 2-9   
How to Implement ICSP™ Using PIC17CXXX OTP MCUs .. 2-15   
How to Implement ICSP™ Using PIC16F8X FLASH MCUs ... 2-21

# SECTION 3 PROGRAMMING SPECIFICATIONS

In-Circuit Serial Programming for PIC12C5XX OTP MCUs .. 3-1   
In-Circuit Serial Programming for PIC12C67X and PIC12CE67X OTP MCUs ... 3-15   
In-Circuit Serial Programming for PIC14000 OTP MCUs . .. 3-27   
In-Circuit Serial Programming for PIC16C55X OTP MCUs . .. 3-39   
Programming Specifications for PIC16C6XX/7XX/9XX OTP MCUs ... 3-51   
In-Circuit Serial Programming for PIC17C7XX OTP MCUs .... 3-75   
In-Circuit Serial Programming for PIC18CXXX OTP MCUs . 3-101   
PIC16F8X EEPROM Memory Programming Specification . 3-147   
PIC16F62X EEPROM Memory Programming Specification .. 3-161   
PIC16F87X EEPROM Memory Programming Specification .... .. 3-181

# SECTION 4 APPLICATION NOTES

# NOTES:

# Section 1 – Introduction

IN-CIRCUIT SERIAL PROGRAMMING™ (ICSP™) GUIDE .. 1-1

# In-Circuit Serial Programming™ (ICSP™) Guide

# WHAT IS IN-CIRCUIT SERIAL WHAT IS IN-CIRCUIT SE

In-System Programming (ISP) is a technique where a programmable device is programmed after the device is placed in a circuit board.

In-Circuit Serial Programming (ICSP) is an enhanced ISP technique implemented in Microchip’s PICmicro® One-Time-Programmable (OTP) and FLASH RISC microcontrollers (MCU). Use of only two I/O pins to serially input and output data makes ICSP easy to use and less intrusive on the normal operation of the MCU.

Because they can accommodate rapid code changes in a manufacturing line, PICmicro OTP and FLASH MCUs offer tremendous flexibility, reduce development time and manufacturing cycles, and improve time to market.

In-Circuit Serial Programming enhances the flexibility of the PICmicro even further.

# WHAT CAN I DO WITH IN-CIRCUITWHAT CAN I DO WITH IN-

This In-Circuit Serial Programming Guide is designed to show you how you can use ICSP to get an edge over your competition. Microchip has helped its customers implement ICSP using PICmicro MCUs since 1992. Contact your local Microchip sales representative today for more information on implementing ICSP in your product.

# PICmicro MCUs MAKE IN-CIRCUIT PICmicro MCUs MAKE IN-CIRCUIT

Unlike many other MCUs, most PICmicro MCUs offer a simple serial programming interface using only two I/O pins (plus power, ground and VPP). Following very simple guidelines, these pins can be fully utilized as I/O pins during normal operation and programming pins during ICSP.

ICSP can be activated through a simple 5-pin connector and a standard PICmicro programmer supporting Serial Programming mode such as Microchip’s PRO MATE® II.

No other MCU has a simpler and less intrusive Serial Programming mode to facilitate your ICSP needs.

ICSP is truly an enabling technology that can be used in a variety of ways including:

# • Reduce Cost of Field Upgrades

The cost of upgrading a system’s code can be dramatically reduced using ICSP. With very little effort and planning, a PICmicro OTP- or FLASHbased system can be designed to have code updates in the field.

For PICmicro FLASH devices, the entire code memory can be rewritten with new code. In PICmicro OTP devices, new code segments and parameter tables can be easily added in program memory areas left blank for update purpose. Often, only a portion of the code (such as a key algorithm) requires update.

# • Reduce Time to Market

In instances where one product is programmed with different customer codes, generic systems can be built and inventoried ahead of time. Based on actual mix of customer orders, the PICmicro MCU can be programmed using ICSP, then tested and shipped. The lead-time reduction and simplification of finished goods inventory are key benefits.

# • Calibrate Your System During Manufacturing

Many systems require calibration in the final stages of manufacturing and testing. Typically, calibration parameters are stored in Serial EEPROM devices. Using PICmicro MCUs, it is possible to save the additional system cost by programming the calibration parameters directly into the program memory.

# • Add Unique ID Code to Your System During Manufacturing

Many products require a unique ID number or a serial number. An example application would be a remote keyless entry device. Each transmitter has a unique “binary key” that makes it very easy to program in the access code at the very end of the manufacturing process and prior to final test.

Serial number, revision code, date code, manufacturer ID and a variety of other useful information can also be added to any product for traceability. Using ICSP, you can eliminate the need for DIP switches or jumpers.

In fact, this capability is so important to many of our customers that Microchip offers a factory programming service called Serialized Quick Turn Programming (SQTPSM), where each PICmicro MCU device is coded with up to 16 bytes of unique code.

# • Calibrate Your System in the Field

Calibration need not be done only in the factory. During installation of a system, ICSP can be used to further calibrate the system to actual operating environment.

In fact, recalibration can be easily done during periodic servicing and maintenance. In OTP parts, newer calibration data can be written to blank memory locations reserved for such use.

# • Customize and Configure Your System in the Field

Like calibration, customization need not be done in the factory only. In many situations, customizing a product at installation time is very useful. A good example is home or car security systems where ID code, access code and other such information can be burned in after the actual configuration is determined. Additionally, you can save the cost of DIP switches and jumpers, which are traditionally used.

# • Program Dice When Using Chip-On-Board (COB)

If you are using COB, Microchip offers a comprehensive die program. You can get dice that are preprogrammed, or you may want to program the die once the circuit board is assembled. Programming and testing in one single step in the manufacturing process is simpler and more cost effective.

# PROGRAMMING TIME PROGRAMMING TI

Programming time can be significantly different between OTP and FLASH MCUs. OTP (EPROM) bytes typically program with pulses in the order of several hundred microseconds. FLASH, on the other hand, require several milliseconds or more per byte (or word) to program.

Figure 1 and Figure 2 below illustrate the programming time differences between OTP and FLASH MCUs. Figure 1 shows programming time in an ideal programmer or tester, where the only time spent is actually programming the device. This is only important to illustrate the minimum time required to program such devices, where the programmer or the tester is fully optimized.

Figure 2 is a more realistic programming time comparison, where the “overhead” time for programmer or a tester is built in. The programmer often requires 3 to 5 times the “theoretically” minimum programming time.

# FIGURE 1: PROGRAMMING TIME FOR FLASH AND OTP MCUS (THEORETICAL MINIMUM TIMES)

![](images/d49aed7907e89caf49f4eaa4f7ed9d3db338b55dcf687ba2b4ce8fdfadc7befe.jpg)

Note 1: The programming times shown here only include the total programming time for all memory. Typically, a programmer will have quite a bit of overhead over this “theoretical minimum” programming time.

2: In the PIC16CXX MCU (used here for comparison) each word is 14-bits wide. For the sake of simplicity, each word is viewed as “two bytes”.

# FIGURE 2: PROGRAMMING TIME FOR FLASH AND OTP MCUS (TYPICAL PROGRAMMING TIMES ON A PROGRAMMER)

![](images/d71e42963b6a43e2065655a4428058ebfe655ea9221ee0a6dd46631769120ef0.jpg)  
Note 1: The programming times shown are actual programming times on vendor supplied programmers   
2: Microchip OTP programming times are based on PRO MATE II programmer.

# Ramifications

The programming time differences between FLASH and OTP MCUs are not particular material for prototyping quantities. However, its impact can be significant in large volume production.

# MICROCHIP PROVIDES A COMPLETE MICROCHIP PROVIDE

# Products

Microchip offers the broadest line of ICSP-capable MCUs:

• PIC12C5XX OTP, 8-pin Family • PIC12C67X OTP, 8-pin Family • PIC12CE67X OTP, 8-pin Family • PIC16C6XX OTP, Mid-Range Family • PIC17C7XX OTP High-End Family • PIC18CXXX OTP, High-End Family • PIC16F62X FLASH, Mid-Range Family • PIC16F8X FLASH, Mid-Range Family • PIC6F8XX FLASH, Mid-Range Family

All together, Microchip currently offers over 40 MCUs capable of ICSP.

# Development Tools

Microchip offers a comprehensive set of development tools for ICSP that allow system engineers to quickly prototype, make code changes and get designs out the door faster than ever before.

PRO MATE II Production Programmer – a production quality programmer designed to support the Serial Programming mode in MCUs up to midvolume production. PRO MATE II runs under DOS in a Command Line mode, Microsoft® Windows® 3.1, Windows® 95/98, and Windows NT®. PRO MATE II is also capable of Serialized Quick Turn ProgrammingSM (SQTPSM), where each device can be programmed with up to 16 bytes of unique code.

Microchip offers an ICSP kit that can be used with the Universal Microchip Device Programmer, PRO MATE II. Together these two tools allow you to implement ICSP with minimal effort and use the ICSP capability of Microchip's PICmicro MCUs.

# Technical support

Microchip has been delivering ICSP capable MCUs since 1992. Many of our customers are using ICSP capability in full production. Our field and factory application engineers can help you implement ICSP in your product.

# NOTES:

# Section 2 – Technical Briefs

HOW TO IMPLEMENT ICSP™ USING PIC12C5XX OTP MCUS .... ... 2-1

HOW TO IMPLEMENT ICSP™ USING PIC16CXXX OTP MCUS ..... 2-9

HOW TO IMPLEMENT ICSP™ USING PIC17CXXX OTP MCUS .... 2-15

HOW TO IMPLEMENT ICSP™ USING PIC16F8X FLASH MCUS . .. 2-21

# How to Implement ICSP™ Using PIC12C5XX OTP MCUs

Author: Thomas Schmidt Microchip Technology Inc.

# INTRODUCTION

The technical brief describes how to implement in-circuit serial programming™ (ICSP) using the PIC12C5XX OTP PICmicro® MCU.

ICSP is a simple way to manufacture your board with an unprogrammed PICmicro MCU and program the device just before shipping the product. Programming the PIC12C5XX MCU in-circuit has many advantages for developing and manufacturing your product.

• Reduces inventory of products with old firmware. With ICSP, the user can manufacture product without programming the PICmicro MCU. The PICmicro MCU will be programmed just before the product is shipped. ICSP in production. New software revisions or additional software modules can be programmed during production into the PIC12C5XX MCU. ICSP in the field. Even after your product has been sold, a service man can update your program with new program modules.   
One hardware with different software. ICSP allows the user to have one hardware, whereas the PIC12C5XX MCU can be programmed with different types of software.   
Last minute programming. Last minute programming can also facilitate quick turnarounds on custom orders for your products.

# IN-CIRCUIT SERIAL PROGRAMMING

To implement ICSP into an application, the user needs to consider three main components of an ICSP system: Application Circuit, Programmer and Programming Environment.

# Application Circuit

During the initial design phase of the application circuit, certain considerations have to be taken into account. Figure 1 shows and typical circuit that addresses the details to be considered during design. In order to implement ICSP on your application board you have to put the following issues into consideration:

1. Isolation of the GP3/MCLR/VPP pin from the rest of the circuit.   
2. Isolation of pins GP1 and GP0 from the rest of the circuit.   
3. Capacitance on each of the VDD, GP3/MCLR/ VPP, GP1, and GP0 pins.   
4. Interface to the programmer.   
5. Minimum and maximum operating voltage for VDD.

# FIGURE 1: TYPICAL APPLICATION CIRCUIT

![](images/ebfd314bb2494a3a1d26095cab3701d0f5116f2d3e12b94d416488e2022d407f.jpg)  
PICmicro, PRO MATE and PICSTART are registered trademarks of Microchip Technology Inc. In-Circuit Serial Programming and ICSP are trademarks of Microchip Technology Inc.

# Isolation of the GP3/MCLR/VPP Pin from the Rest of the Circuit

PIC12C5XX devices have two ways of configuring the MCLR pin:

• MCLR can be connected either to an external RC circuit or   
• MCLR is tied internally to VDD

When GP3/MCLR/VPP pin is connected to an external RC circuit, the pull-up resistor is tied to VDD, and a capacitor is tied to ground. This circuit can affect the operation of ICSP depending on the size of the capacitor.

Another point of consideration with the GP3/MCLR/VPP pin, is that when the PICmicro MCU is programmed, this pin is driven up to 13V and also to ground. Therefore, the application circuit must be isolated from the voltage coming from the programmer.

When MCLR is tied internally to VDD, the user has only to consider that up to 13V are present during programming of the GP3/MCLR/VPP pin. This might affect other components connected to that pin.

For more information about configuring the GP3/ MCLR/VPP internally to VDD, please refer to the PIC12C5XX data sheet (DS40139).

# Isolation of Pins GP1 and GP0 from the Rest of the Circuit

Pins GP1 and GP0 are used by the PICmicro MCU for serial programming. GP1 is the clock line and GP0 is the data line.

GP1 is driven by the programmer. GP0 is a bidirectional pin that is driven by the programmer when programming and driven by the PICmicro MCU when verifying. These pins must be isolated from the rest of the application circuit so as not to affect the signals during programming. You must take into consideration the output impedance of the programmer when isolating GP1 and GP0 from the rest of the circuit. This isolation circuit must account for GP1 being an input on the PICmicro MCU and for GP0 being bidirectional pin.

For example, PRO MATE® II has an output impedance of 1 kW. If the design permits, these pins should not be used by the application. This is not the case with most designs. As a designer, you must consider what type of circuitry is connected to GP1 and GP0 and then make a decision on how to isolate these pins.

# Total Capacitance on VDD, GP3/MCLR/VPP, GP1, and GP0

The total capacitance on the programming pins affects the rise rates of these signals as they are driven out of the programmer. Typical circuits use several hundred microfarads of capacitance on VDD, which helps to dampen noise and improve electromagnetic interference. However, this capacitance requires a fairly strong driver in the programmer to meet the rise rate timings for VDD.

# Interface to the Programmer

Most programmers are designed to simply program the PICmicro MCU itself and don’t have strong enough drivers to power the application circuit.

One solution is to use a driver board between the programmer and the application circuit. The driver board needs a separate power supply that is capable of driving the VPP, VDD, GP1, and GP0 pins with the correct ramp rates and also should provide enough current to power-up the application circuit.

The cable length between the programmer and the circuit is also an important factor for ICSP. If the cable between the programmer and the circuit is too long, signal reflections may occur. These reflections can momentarily cause up to twice the voltage at the end of the cable, that was sent from the programmer. This voltage can cause a latch-up. In this case, a termination resistor has to be used at the end of the signal line.

# Minimum and Maximum Operating Voltage for VDD

The PIC12C5XX programming specification states that the device should be programmed at 5V. Special considerations must be made if your application circuit operates at 3V only. These considerations may include totally isolating the PICmicro MCU during programming. The other point of consideration is that the device must be verified at minimum and maximum operation voltage of the circuit in order to ensure proper programming margin.

For example, a battery driven system may operate from three 1.5V cells giving an operating voltage range of 2.7V to 4.5V. The programmer must program the device at 5V and must verify the program memory contents at both 2.7V and 4.5V to ensure that proper programming margins have been achieved.

# THE PROGRAMMER

PIC12C5XX MCUs only use serial programming and, therefore, all programmers supporting these devices will support the ICSP. One issue with the programmer is the drive capability. As discussed before, it must be able to provide the specified rise rates on the ICSP signals and also provide enough current to power the application circuit. It is recommended that you buffer the programming signals.

Another point of consideration for the programmer is what VDD levels are used to verify the memory contents of the PICmicro MCU. For instance, the PRO MATE II verifies program memory at the minimum and maximum VDD levels for the specified device and is therefore considered a production quality programmer. On the other hand, the PICSTART® Plus only verifies at 5V and is for prototyping use only. The PIC12C5XX programming specifications state that the program memory contents should be verified at both the minimum and maximum VDD levels that the application circuit will be operating. This implies that the application circuit must be able to handle the varying VDD voltages.

There are also several third-party programmers that are available. You should select a programmer based on the features it has and how it fits into your programming environment. The Microchip Development Systems Ordering Guide (DS30177) provides detailed information on all our development tools. The Microchip Third Party Guide (DS00104) provides information on all of our third party development tool developers. Please consult these two references when selecting a programmer. Many options exist including serial or parallel PC host connection, stand-alone operation, and single or gang programmers.

# PROGRAMMING ENVIRONMENT

The programming environment will affect the type of programmer used, the programmer cable length, and the application circuit interface. Some programmers are well suited for a manual assembly line while others are desirable for an automated assembly line. A gang programmer should be chosen for programming multiple MCUs at one time. The physical distance between the programmer and the application circuit affects the load capacitance on each of the programming signals. This will directly affect the drive strength needed to provide the correct signal rise rates and current. Finally, the application circuit interface to the programmer depends on the size constraints of the application circuit itself and the assembly line. A simple header can be used to interface the application circuit to the programmer. This might be more desirable for a manual assembly line where a technician plugs the programmer cable into the board.

A different method is the uses spring loaded test pins (often referred as pogo-pins). The application circuit has pads on the board for each of the programming signals. Then there is a movable fixture that has pogo pins in the same configuration as the pads on the board. The application circuit is moved into position and the fixture is moved such that the spring loaded test pins come into contact with the board. This method might be more suitable for an automated assembly line.

After taking into consideration the issues with the application circuit, the programmer, and the programming environment, anyone can build a high quality, reliable manufacturing line based on ICSP.

# OTHER BENEFITS

ICSP provides several other benefits such as calibration and serialization. If program memory permits, it would be cheaper and more reliable to store calibration constants in program memory instead of using an external serial EEPROM.

# Field Programming of PICmicro OTP MCUs

An OTP device is not normally capable of being reprogrammed, but the PICmicro MCU architecture gives you this flexibility provided the size of your firmware is less than half that of the desired device.

This method involves using jump tables for the reset and interrupt vectors. Example 1 shows the location of a main routine and the reset vector for the first time a device with 0.5K-words of program memory is programmed. Example 2 shows the location of a second main routine and its reset vector for the second time the same device is programmed. You will notice that the GOTO Main that was previously at location 0x0002 is replaced with an NOP. An NOP is a program memory location with all the bits programmed as 0s. When the reset vector is executed, it will execute an NOP and then a GOTO Main1 instruction to the new code.

![](images/fb7f5de83b95974ed3d8e51f1634990e3f454bf261bebaac4984409af9999e6c.jpg)  
LEGEND: XX = CALIBRATION VALUE

EXAMPLE 2: LOCATION OF THE SECOND MAIN ROUTINE AND IT INTERRUPT VECTOR (AFTER SECOND PROGRAMMING)   

<table><tr><td colspan="3">PROGRAM MEMORY</td></tr><tr><td rowspan="3">0X000 0X001 0X002</td><td>MOVWF OSCAL</td><td rowspan="3">RESET VECTOR</td></tr><tr><td>NOP</td></tr><tr><td>GOTO MAIN2</td></tr><tr><td rowspan="2">0X040</td><td>UNPROGRAMMED MAIN1</td><td rowspan="2">MAIN1 ROUTINE</td></tr><tr><td></td></tr><tr><td rowspan="2">0X10E 0X136</td><td>UNPROGRAMMED</td><td></td></tr><tr><td>MAIN2</td><td>MAIN2 ROUTINE</td></tr><tr><td rowspan="2">0X1FF</td><td></td><td rowspan="2">CALIBRATION VALUE</td></tr><tr><td>MOVLW XX</td></tr></table>

Since the program memory of the PIC12C5XX devices is organized in 256 x 12 word pages, placement of such information as look-up tables and CALL instructions must be taken into account. For further information, please refer to application note AN581, Implementing Long Calls and application note AN556, Implementing a Table Read.

# CONCLUSION

Microchip Technology Inc. is committed to supporting your ICSP needs by providing you with our many years of experience and expertise in developing in-circuit system programming solutions. Anyone can create a reliable in-circuit system programming station by coupling our background with some forethought to the circuit design and programmer selection issues previously mentioned. Your local Microchip representative is available to answer any questions you have about the requirements for ICSP.

# APPENDIX A: SAMPLE DRIVER BOARD SCHEMATIC

![](images/ee0d5e0a80bee4fb965224f9cd9d62b4eae19ad4595c244989ccafe1a43a3d7c.jpg)

# NOTES:

# How to Implement ICSP™ Using PIC16CXXX OTP MCUs

Author: Rodger Richey Microchip Technology Inc.

# INTRODUCTION

In-Circuit Serial Programming™ (ICSP) is a great way to reduce your inventory overhead and time-to-market for your product. By assembling your product with a blank Microchip microcontroller (MCU), you can stock one design. When an order has been placed, these units can be programmed with the latest revision of firmware, tested, and shipped in a very short time. This method also reduces scrapped inventory due to old firmware revisions. This type of manufacturing system can also facilitate quick turnarounds on custom orders for your product.

Most people would think to use ICSP with PICmicro® OTP MCUs only on an assembly line where the device is programmed once. However, there is a method by which an OTP device can be programmed several times depending on the size of the firmware. This method, explained later, provides a way to field upgrade your firmware in a way similar to EEPROM- or Flash-based devices.

# HOW DOES ICSP WORK?

Now that ICSP appeals to you, what steps do you take to implement it in your application? There are three main components of an ICSP system: Application Circuit, Programmer and Programming Environment.

# FIGURE 1: TYPICAL APPLICATION CIRCUIT

# Application Circuit

The application circuit must be designed to allow all the programming signals to be directly connected to the PICmicro MCU. Figure 1 shows a typical circuit that is a starting point for when designing with ICSP. The application must compensate for the following issues:

1. Isolation of the MCLR/VPP pin from the rest of the circuit.   
2. Isolation of pins RB6 and RB7 from the rest of the circuit.   
3. Capacitance on each of the VDD, MCLR/VPP, RB6, and RB7 pins.   
4. Minimum and maximum operating voltage for VDD.   
5. PICmicro Oscillator.   
6. Interface to the programmer.

The MCLR/VPP pin is normally connected to an RC circuit. The pull-up resistor is tied to VDD and a capacitor is tied to ground. This circuit can affect the operation of ICSP depending on the size of the capacitor. It is, therefore, recommended that the circuit in Figure 1 be used when an RC is connected to MCLR/VPP. The diode should be a Schottky-type device. Another issue with MCLR/VPP is that when the PICmicro MCU device is programmed, this pin is driven to approximately 13V and also to ground. Therefore, the application circuit must be isolated from this voltage provided by the programmer.

![](images/9e8e6a9071631cd74e8818c7350324a18dea9ab3bbcbd8c7a617962fa2b2a0a9.jpg)

Pins RB6 and RB7 are used by the PICmicro MCU for serial programming. RB6 is the clock line and RB7 is the data line. RB6 is driven by the programmer. RB7 is a bidirectional pin that is driven by the programmer when programming, and driven by the PICmicro MCU when verifying. These pins must be isolated from the rest of the application circuit so as not to affect the signals during programming. You must take into consideration the output impedance of the programmer when isolating RB6 and RB7 from the rest of the circuit. This isolation circuit must account for RB6 being an input on the PICmicro MCU, and for RB7 being bidirectional (can be driven by both the PICmicro MCU and the programmer). For instance, PRO MATE® II has an output impedance of 1k¾. If the design permits, these pins should not be used by the application. This is not the case with most applications so it is recommended that the designer evaluate whether these signals need to be buffered. As a designer, you must consider what type of circuitry is connected to RB6 and RB7 and then make a decision on how to isolate these pins. Figure 1 does not show any circuitry to isolate RB6 and RB7 on the application circuit because this is very application dependent.

The total capacitance on the programming pins affects the rise rates of these signals as they are driven out of the programmer. Typical circuits use several hundred microfarads of capacitance on VDD which helps to dampen noise and ripple. However, this capacitance requires a fairly strong driver in the programmer to meet the rise rate timings for VDD. Most programmers are designed to simply program the PICmicro MCU itself and don’t have strong enough drivers to power the application circuit. One solution is to use a driver board between the programmer and the application circuit. The driver board requires a separate power supply that is capable of driving the VPP and VDD pins with the correct rise rates and should also provide enough current to power the application circuit. RB6 and RB7 are not buffered on this schematic but may require buffering depending upon the application. A sample driver board schematic is shown in Appendix A.

Note: The driver board design MUST be tested in the user's application to determine the effects of the application circuit on the programming signals timing. Changes may be required if the application places a significant load on VDD, VPP, RB6 OR RB7.

The Microchip programming specification states that the device should be programmed at 5V. Special considerations must be made if your application circuit operates at 3V only. These considerations may include totally isolating the PICmicro MCU during programming. The other issue is that the device must be verified at the minimum and maximum voltages at which the application circuit will be operating. For instance, a battery operated system may operate from three 1.5V cells giving an operating voltage range of 2.7V to 4.5V.

The programmer must program the device at 5V and must verify the program memory contents at both 2.7V and 4.5V to ensure that proper programming margins have been achieved. This ensures the PICmicro MCU option over the voltage range of the system.

This final issue deals with the oscillator circuit on the application board. The voltage on MCLR/VPP must rise to the specified program mode entry voltage before the device executes any code. The crystal modes available on the PICmicro MCU are not affected by this issue because the Oscillator Start-up Timer waits for 1024 oscillations before any code is executed. However, RC oscillators do not require any startup time and, therefore, the Oscillator Startup Timer is not used. The programmer must drive MCLR/VPP to the program mode entry voltage before the RC oscillator toggles four times. If the RC oscillator toggles four or more times, the program counter will be incremented to some value X. Now when the device enters programming mode, the program counter will not be zero and the programmer will start programming your code at an offset of X. There are several alternatives that can compensate for a slow rise rate on MCLR/VPP. The first method would be to not populate the R, program the device, and then insert the R. The other method would be to have the programming interface drive the OSC1 pin of the PICmicro MCU to ground while programming. This will prevent any oscillations from occurring during programming.

Now all that is left is how to connect the application circuit to the programmer. This depends a lot on the programming environment and will be discussed in that section.

# Programmer

The second consideration is the programmer. PIC16CXXX MCUs only use serial programming and therefore all programmers supporting these devices will support ICSP. One issue with the programmer is the drive capability. As discussed before, it must be able to provide the specified rise rates on the ICSP signals and also provide enough current to power the application circuit. Appendix A shows an example driver board. This driver schematic does not show any buffer circuitry for RB6 and RB7. It is recommended that an evaluation be performed to determine if buffering is required. Another issue with the programmer is what VDD levels are used to verify the memory contents of the PICmicro MCU. For instance, the PRO MATE II verifies program memory at the minimum and maximum VDD levels for the specified device and is therefore considered a production quality programmer. On the other hand, the PICSTART® Plus only verifies at 5V and is for prototyping use only. The Microchip programming specifications state that the program memory contents should be verified at both the minimum and maximum VDD levels that the application circuit will be operating. This implies that the application circuit must be able to handle the varying VDD voltages.

There are also several third party programmers that are available. You should select a programmer based on the features it has and how it fits into your programming environment. The Microchip Development Systems Ordering Guide (DS30177) provides detailed information on all our development tools. The Microchip Third Party Guide (DS00104) provides information on all of our third party tool developers. Please consult these two references when selecting a programmer. Many options exist including serial or parallel PC host connection, stand-alone operation, and single or gang programmers. Some of the third party developers include Advanced Transdata Corporation, BP Microsystems, Data I/O, Emulation Technology and Logical Devices.

# Programming Environment

The programming environment will affect the type of programmer used, the programmer cable length, and the application circuit interface. Some programmers are well suited for a manual assembly line while others are desirable for an automated assembly line. You may want to choose a gang programmer to program multiple systems at a time.

The physical distance between the programmer and the application circuit affects the load capacitance on each of the programming signals. This will directly affect the drive strength needed to provide the correct signal rise rates and current. This programming cable must also be as short as possible and properly terminated and shielded, or the programming signals may be corrupted by ringing or noise.

Finally, the application circuit interface to the programmer depends on the size constraints of the application circuit itself and the assembly line. A simple header can be used to interface the application circuit to the programmer. This might be more desirable for a manual assembly line where a technician plugs the programmer cable into the board. A different method is the use of spring loaded test pins (commonly referred to as pogo pins). The application circuit has pads on the board for each of the programming signals. Then there is a fixture that has pogo pins in the same configuration as the pads on the board. The application circuit or fixture is moved into position such that the pogo pins come into contact with the board. This method might be more suitable for an automated assembly line.

After taking into consideration the issues with the application circuit, the programmer, and the programming environment, anyone can build a high quality, reliable manufacturing line based on ICSP.

# Other Benefits

ICSP provides other benefits, such as calibration and serialization. If program memory permits, it would be cheaper and more reliable to store calibration constants in program memory instead of using an external serial EEPROM. For example, your system has a thermistor which can vary from one system to another. Storing some calibration information in a table format allows the microcontroller to compensate in software for external component tolerances. System cost can be reduced without affecting the required performance of the system by using software calibration techniques. But how does this relate to ICSP? The PICmicro MCU has already been programmed with firmware that performs a calibration cycle. The calibration data is transferred to a calibration fixture. When all calibration data has been transferred, the fixture places the PICmicro MCU in programming mode and programs the PICmicro MCU with the calibration data. Application note AN656, In-Circuit Serial Programming of Calibration Parameters Using a PICmicro Microcontroller, shows exactly how to implement this type of calibration data programming.

The other benefit of ICSP is serialization. Each individual system can be programmed with a unique or random serial number. One such application of a unique serial number would be for security systems. A typical system might use DIP switches to set the serial number. Instead, this number can be burned into program memory, thus reducing the overall system cost and lowering the risk of tampering.

# Field Programming of PICmicro OTP MCUs

An OTP device is not normally capable of being reprogrammed, but the PICmicro MCU architecture gives you this flexibility provided the size of your firmware is at least half that of the desired device and the device is not code protected. If your target device does not have enough program memory, Microchip provides a wide spectrum of devices from 0.5K to 8K program memory with the same set of peripheral features that will help meet the criteria.

The PIC16CXXX microcontrollers have two vectors, reset and interrupt, at locations 0x0000 and 0x0004. When the PICmicro MCU encounters a reset or interrupt condition, the code located at one of these two locations in program memory is executed. The first listing of Example 1 shows the code that is first programmed into the PICmicro MCU. The second listing of Example 1 shows the code that is programmed into the PICmicro MCU for the second time.

EXAMPLE 1: PROGRAMMING CYCLE LISTING FILES  

<table><tr><td></td><td></td><td colspan="3">First Program Cycle</td><td></td><td colspan="2">Second Program Cycle</td></tr><tr><td>Prog</td><td></td><td colspan="2">Opcode Assembly</td><td>|Prog</td><td>Opcode</td><td colspan="2">Assembly</td></tr><tr><td>Mem</td><td></td><td colspan="2">Instruction</td><td>|Mem</td><td colspan="2">Instruction</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td colspan="2"></td></tr><tr><td>0000</td><td>2808</td><td>goto Main</td><td>; Main loop ;at 0x0008</td><td>10000 0000 0001</td><td>nop goto1</td><td></td></tr><tr><td>0001</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>2860 0002</td><td>Main ;Main now</td><td></td></tr><tr><td>0002</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>3FFF</td><td>&lt;blank&gt;</td><td>;at0x0060</td></tr><tr><td>0003</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>0003 3FFF</td><td>&lt;blank&gt;</td><td></td></tr><tr><td>0004</td><td>2848</td><td>goto ISR</td><td>;ISR at</td><td>0004 0000</td><td>nop</td><td></td></tr><tr><td>0005</td><td>3FFF</td><td>&lt;blank&gt;</td><td>;0x0048</td><td>0005 28A8</td><td colspan="2">goto ISR ;ISR now at</td></tr><tr><td>0006</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>0006 3FFF</td><td colspan="2">&lt;blank&gt; ;0x00A8</td></tr><tr><td>0007</td><td>3FFF</td><td>&lt;blank&gt;</td><td>0007</td><td>3FFF</td><td colspan="2">&lt;blank&gt; STATUS, RP0</td></tr><tr><td>0008</td><td>1683</td><td>bsf STATUS, RP0</td><td></td><td>0008</td><td colspan="2">1683 bsf</td></tr><tr><td>0009</td><td>3007</td><td>movlw0x07</td><td>0009</td><td>3007 009F</td><td>movlw0x07</td><td rowspan="2"></td></tr><tr><td>000A ·</td><td>009F</td><td>movwf ADCON1</td><td>000A</td><td>movwf ADCON1</td></tr><tr><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0048</td><td>1C0C</td><td>btfss PIR1, RBIF goto EndISR</td><td></td><td>0048 0049 284E</td><td>1C0C goto</td><td>EndISR</td><td>btfss PIR1, RBIF</td></tr><tr><td>0049 004A</td><td>284E 1806</td><td>btfsc PORTB, 0</td><td></td><td>004A 1806</td><td></td><td>btfsc PORTB, 0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>&lt;blank&gt;</td><td></td><td>· 0060</td><td>bsf</td><td>STATUS, RP0</td><td></td></tr><tr><td>0060</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>1683 0061 3005</td><td></td><td>movlw0x05</td><td></td></tr><tr><td>0061</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>0062 009F</td><td></td><td></td><td></td></tr><tr><td>0062</td><td>3FFF</td><td></td><td></td><td></td><td></td><td>movwf ADCON1</td><td></td></tr><tr><td>·</td><td></td><td></td><td></td><td>.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td></td><td>&lt;blank&gt;</td><td></td><td></td><td></td><td>btfss PIR1,RBIF</td><td></td></tr><tr><td>00A8</td><td>3FFF</td><td></td><td></td><td>00A8 1C0C</td><td></td><td></td><td></td></tr><tr><td>00A9</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>00A9 28AE</td><td>goto</td><td>EndISR</td><td></td></tr><tr><td>00AA</td><td>3FFF</td><td>&lt;blank&gt;</td><td></td><td>00AA 1806</td><td></td><td>btfsc PORTB,0</td><td></td></tr><tr><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The example shows that to program the PICmicro MCU a second time the memory location 0x0000, originally goto Main (0x2808), is reprogrammed to all 0’s which happens to be a nop instruction. This location cannot be reprogrammed to the new opcode (0x2860) because the bits that are 0’s cannot be reprogrammed to 1’s, only bits that are 1’s can be reprogrammed to 0’s. The next memory location 0x0001 was originally blank (all 1’s) and now becomes a goto Main (0x2860). When a reset condition occurs, the PICmicro MCU executes the instruction at location 0x0000 which is the nop, a completely benign instruction, and then executes the goto Main to start the execution of code. The example also shows that all program memory locations after 0x005A are blank in the original program so that the second time the PICmicro MCU is programmed, the revised code can be programmed at these locations. The same descriptions can be given for the interrupt vector at location 0x0004.

This method changes slightly for PICmicro MCUs with >2K words of program memory. Each of the goto Main and goto ISR instructions are replaced by the following code segments due to paging on devices with >2K words of program memory.

movlw <page> movlw <page> movwf PCLATH movwf PCLATH goto Main goto ISR

Now your one time programmable PICmicro MCU is exhibiting more EEPROM- or Flash-like qualities.

# CONCLUSION

Microchip Technology Inc. is committed to supporting your ICSP needs by providing you with our many years of experience and expertise in developing ICSP solutions. Anyone can create a reliable ICSP programming station by coupling our background with some forethought to the circuit design and programmer selection issues previously mentioned. Your local Microchip representative is available to answer any questions you have about the requirements for ICSP.

![](images/eb72f606928e956e542a545f2f9d2554be9cdabf1deaecd15b02305f33e26675.jpg)  
APPENDIX A:  SAMPLE DRIVER BOARD SCHEMATIC

# How to Implement ICSP™ Using PIC17CXXX OTP MCUs

Author: Stan D’Souza Microchip Technology Inc.

# INTRODUCTION

PIC17CXXX microcontroller (MCU) devices can be serially programmed using an RS-232 or equivalent serial interface. As shown in Figure 1, using just three pins, the PIC17CXXX can be connected to an external interface and programmed. In-Circuit Serial Programming (ICSP™) allows for a greater flexibility in an application as well as a faster time to market for the user's product.

This technical brief will demonstrate the practical aspects associated with ICSP using the PIC17CXXX. It will also demonstrate some key capabilities of OTP devices when used in conjunction with ICSP.

# Implementation

The PIC17CXXX devices have special instructions, which enables the user to program and read the PIC17CXXX's program memory. The instructions are TABLWT and TLWT which implement the program memory write operation and TABLRD and TLRD which perform the program memory read operation. For more details, please check the In-Circuit Serial Programming for PIC17CXXX OTP Microcontrollers Specification (DS30273), PIC17C4X data sheet (DS30412) and PIC17C75X data sheet (DS30264).

When doing ICSP, the PIC17CXXX runs a boot code, which configures the USART port and receives data serially through the RX line. This data is then programmed at the address specified in the serial data string. A high voltage (about 13V) is required for the EPROM cell to get programmed, and this is usually supplied by the programming header as shown in Figure 1 and Figure 2. The PIC17CXXX's boot code enables and disables the high voltage line using a dedicated I/O line.

![](images/19438f930ab20282b82587a2948c00bcb36b734913ace6564d785878629de357.jpg)  
PIC17CXXX IN-CIRCUIT SERIAL PROGRAMMING USING TABLE WRITE INSTRUCTIONS

![](images/acd028eb312b3ee3fcc42b40be382084d88950e53cb7f3532c479619030d1937.jpg)  
FIGURE 2:   
PIC17CXXX IN-CIRCUIT SERIAL PROGRAMMING SCHEMATIC

# ICSP Boot Code

The boot code is normally programmed, into the PIC17CXX device using a PRO MATE® or PICSTART® Plus or any third party programmer. As depicted in the flowchart in Figure 4, on power-up, or a reset, the program execution always vectors to the boot code. The boot code is normally located at the bottom of the program memory space e.g. 0x700 for a PIC17C42A (Figure 3).

Several methods could be used to reset the PIC17CXXX when the ICSP header is connected to the system board. The simplest method, as shown in Figure 2, is to derive the system 5V, from the 13V supplied by the ICSP header. It is quite common in manufacturing lines, to have system boards programmed with only the boot code ready and available for testing, calibration or final programming. The ICSP header would thus supply the 13V to the system and this 13V would then be stepped down to supply the 5V required to power the system. Please note that the 13V supply should have enough drive capability to supply power to the system as well as maintain the programming voltage of 13V.

The first action of the boot code (as shown in flowchart Figure 4) is to configure the USART to a known baud rate and transmit a request sequence to the ICSP host system. The host immediately responds with an acknowledgment of this request. The boot code then gets ready to receive ICSP data. The host starts sending the data and address byte sequences to the PIC17CXXX. On receiving the address and data information, the 16-bit address is loaded into the TBLPTR registers and the 16-bit data is loaded into the TABLAT registers. The RA2 pin is driven low to enable 13V at MCLR. The PIC17CXXX device then executes a table write instruction. This instruction in turn causes a long write operation, which disables further code execution. Code execution is resumed when an internal interrupt occurs. This delay ensures that the programming pulse width of 1 ms (max.) is met. Once a location is written, RA2 is driven high to disable further writes and a verify operation is done using the Table read instruction. If the result is good, an acknowledge is sent to the host. This process is repeated till all desired locations are programmed.

In normal operation, when the ICSP header is not connected, the boot code would still execute and the PIC17CXXX would send out a request to the host. However it would not get a response from the host, so it would abort the boot code and start normal code execution.

![](images/1d107fef756b6c028b066ea1672b548a9e2d92754bc1af19fd68df5cb8858727.jpg)  
FIGURE 3: BOOT CODE EXAMPLE FOR PIC17C42A

# FIGURE 4: FLOWCHART FOR ICSP BOOT CODE

![](images/ffbdc586613dbf37beddc40ae0175038b7710da9342f1f5b3363a37e9ae55883.jpg)

# USING THE ICSP FEATURE ON USING THE ICSP FEATUR

The ICSP feature is a very powerful tool when used in conjunction with OTP devices.

# Saving Calibration Information Using ICSP

One key use of ICSP is to store calibration constants or parameters in program memory. It is quite common to interface a PIC17CXXX device to a sensor. Accurate, pre-calibrated sensors can be used, but they are more expensive and have long lead times. Un-calibrated sensors on the other hand are inexpensive and readily available. The only caveat is that these sensors have to be calibrated in the application. Once the calibration constants have been determined, they would be unique to a given system, so they have to be saved in program memory. These calibration parameters/constants can then be retrieved later during program execution and used to improve the accuracy of low cost un-calibrated sensors. ICSP thus offers a cost reduction path for the end user in the application.

# Saving Field Calibration Information Using ICSP

Sensors typically tend to drift and lose calibration over time and usage. One expensive solution would be to replace the sensor with a new one. A more cost effective solution however, is to re-calibrated the system and save the new calibration parameter/constants into the PIC17CXXX devices using ICSP. The user program however has to take into account certain issues:

1. Un-programmed or blank locations have to be reserved at each calibration constant location in order to save new calibration parameters/constants.   
2. The old calibration parameters/constants are all programmed to 0, so the user program will have to be "intelligent" and differentiate between blank (0xFFFF), zero (0x0000), and programmed locations.

Figure 5 shows how this can be achieved.

# Programming Unique Serial Numbers Using ICSP

There are applications where each system needs to have a unique and sometimes random serial number. Example: security devices. One common solution is to have a set of DIP switches which are then set to a unique value during final test. A more cost effective solution however would be to program unique serial numbers into the device using ICSP. The user application can thus eliminate the need for DIP switches and subsequently reduce the cost of the system.

![](images/3a0cd81568f569a1bab83a4e8e0e1330611e12c74dd5f4b82138a88f7c3dede6.jpg)

# Code Updates in the Field Using ICSP

With fast time to market it is not uncommon to see application programs which need to be updated or corrected for either enhancements or minor errors/bugs. If ROM parts were used, updates would be impossible and the product would either become outdated or recalled from the field. A more cost effective solution is to use OTP devices with ICSP and program them in the field with the new updates. Figure 6 shows an example where the user has allowed for one field update to his program.

Here are some of the issues which need to be addressed:

1. The user has to reserve sufficient blank memory to fit his updated code.   
2. At least one blank location needs to be saved at the reset vector as well as for all the interrupts.   
3. Program all the old "goto" locations (located at the reset vector and the interrupts vectors) to 0 so that these instructions execute as NOPs.   
4. Program new "goto" locations (at the reset vector and the interrupt vectors) just below the old "goto" locations.   
5. Finally, program the new updated code in the blank memory space.

# FIGURE 6: CODE UPDATES USING ICSP

# CONCLUSION

ICSP is a very powerful feature available on the PIC17CXXX devices. It offers tremendous design flexibility to the end user in terms of saving calibration constants and updating code in final production as well as in the field, thus helping the user design a low-cost and fast time-to-market product.

![](images/79ee42deef74208292511ddaefcac1517bff060d03970b6276f99dcbf78861cd.jpg)

# NOTES:

# How to Implement ICSP™ Using PIC16F8X FLASH MCUs

Author: Rodger Richey Microchip Technology Inc.

# INTRODUCTION

In-Circuit Serial Programming™ (ICSP) with PICmicro® FLASH microcontrollers (MCU) is not only a great way to reduce your inventory overhead and timeto-market for your product, but also to easily provide field upgrades of firmware. By assembling your product with a Microchip FLASH-based MCU, you can stock the shelf with one system. When an order has been placed, these units can be programmed with the latest revision of firmware, tested, and shipped in a very short time. This type of manufacturing system can also facilitate quick turnarounds on custom orders for your product. You don’t have to worry about scrapped inventory because of the FLASH-based program memory. This gives you the advantage of upgrading the firmware at any time to fix those “features” that pop up from time to time.

# HOW DOES ICSP WORK?

Now that ICSP appeals to you, what steps do you take to implement it in your application? There are three main components of an ICSP system.

These are the: Application Circuit, Programmer and Programming Environment.

# FIGURE 1: TYPICAL APPLICATION CIRCUIT

# Application Circuit

The application circuit must be designed to allow all the programming signals to be directly connected to the PICmicro MCUs. Figure 1 shows a typical circuit that is a starting point for when designing with ICSP. The application must compensate for the following issues:

1. Isolation of the MCLR/VPP pin from the rest of the circuit.   
2. Isolation of pins RB6 and RB7 from the rest of the circuit.   
3. Capacitance on each of the VDD, MCLR/VPP, RB6, and RB7 pins.   
4. Minimum and maximum operating voltage for VDD.   
5. PICmicro Oscillator.   
6. Interface to the programmer.

The MCLR/VPP pin is normally connected to an RC circuit. The pull-up resistor is tied to VDD and a capacitor is tied to ground. This circuit can affect the operation of ICSP depending on the size of the capacitor. It is, therefore, recommended that the circuit in Figure 1 be used when an RC is connected to MCLR/VPP. The diode should be a Schottky-type device. Another issue with MCLR/VPP is that when the PICmicro MCU device is programmed, this pin is driven to approximately 13V and also to ground. Therefore, the application circuit must be isolated from this voltage provided by the programmer.

![](images/40a217e1a23f7020c097eef5cc8ba100f6c0fe8af14c809c10af0acccadf63be.jpg)

Pins RB6 and RB7 are used by the PICmicro MCU for serial programming. RB6 is the clock line and RB7 is the data line. RB6 is driven by the programmer. RB7 is a bidirectional pin that is driven by the programmer when programming, and driven by the PICmicro MCU when verifying. These pins must be isolated from the rest of the application circuit so as not to affect the signals during programming. You must take into consideration the output impedance of the programmer when isolating RB6 and RB7 from the rest of the circuit. This isolation circuit must account for RB6 being an input on the PICmicro MCU and for RB7 being bidirectional (can be driven by both the PICmicro MCU and the programmer). For instance, PRO MATE® II has an output impedance of 1k¾. If the design permits, these pins should not be used by the application. This is not the case with most applications so it is recommended that the designer evaluate whether these signals need to be buffered. As a designer, you must consider what type of circuitry is connected to RB6 and RB7 and then make a decision on how to isolate these pins. Figure 1 does not show any circuitry to isolate RB6 and RB7 on the application circuit because this is very application dependent.

The total capacitance on the programming pins affects the rise rates of these signals as they are driven out of the programmer. Typical circuits use several hundred microfarads of capacitance on VDD which helps to dampen noise and ripple. However, this capacitance requires a fairly strong driver in the programmer to meet the rise rate timings for VDD. Most programmers are designed to simply program the PICmicro MCU itself and don’t have strong enough drivers to power the application circuit. One solution is to use a driver board between the programmer and the application circuit. The driver board requires a separate power supply that is capable of driving the VPP and VDD pins with the correct rise rates and should also provide enough current to power the application circuit. RB6 and RB7 are not buffered on this schematic but may require buffering depending upon the application. A sample driver board schematic is shown in Appendix A.

Note: The driver board design MUST be tested in the user's application to determine the effects of the application circuit on the programming signals timing. Changes may be required if the application places a significant load on Vdd, VPP, RB6 or RB7.

The Microchip programming specification states that the device should be programmed at 5V. Special considerations must be made if your application circuit operates at 3V only. These considerations may include totally isolating the PICmicro MCU during programming. The other issue is that the device must be verified at the minimum and maximum voltages at which the application circuit will be operating. For instance, a battery operated system may operate from three 1.5V cells giving an operating voltage range of 2.7V to 4.5V. The programmer must program the device at 5V and must verify the program memory contents at both 2.7V and 4.5V to ensure that proper programming margins have been achieved. This ensures the PICmicro MCU option over the voltage range of the system.

This final issue deals with the oscillator circuit on the application board. The voltage on MCLR/VPP must rise to the specified program mode entry voltage before the device executes any code. The crystal modes available on the PICmicro MCU are not affected by this issue because the Oscillator Start-up Timer waits for 1024 oscillations before any code is executed. However, RC oscillators do not require any startup time and, therefore, the Oscillator Startup Timer is not used. The programmer must drive MCLR/VPP to the program mode entry voltage before the RC oscillator toggles four times. If the RC oscillator toggles four or more times, the program counter will be incremented to some value X. Now when the device enters programming mode, the program counter will not be zero and the programmer will start programming your code at an offset of X. There are several alternatives that can compensate for a slow rise rate on MCLR/VPP. The first method would be to not populate the R, program the device, and then insert the R. The other method would be to have the programming interface drive the OSC1 pin of the PICmicro MCU to ground while programming. This will prevent any oscillations from occurring during programming.

Now all that is left is how to connect the application circuit to the programmer. This depends a lot on the programming environment and will be discussed in that section.

# Programmer

The second consideration is the programmer. PIC16F8X MCUs only use serial programming and therefore all programmers supporting these devices will support ICSP. One issue with the programmer is the drive capability. As discussed before, it must be able to provide the specified rise rates on the ICSP signals and also provide enough current to power the application circuit. Appendix A shows an example driver board. This driver schematic does not show any buffer circuitry for RB6 and RB7. It is recommended that an evaluation be performed to determine if buffering is required. Another issue with the programmer is what VDD levels are used to verify the memory contents of the PICmicro MCU. For instance, the PRO MATE II verifies program memory at the minimum and maximum VDD levels for the specified device and is therefore considered a production quality programmer. On the other hand, the PICSTART® Plus only verifies at 5V and is for prototyping use only. The Microchip programming specifications state that the program memory contents should be verified at both the minimum and maximum VDD levels that the application circuit will be operating. This implies that the application circuit must be able to handle the varying VDD voltages.

There are also several third party programmers that are available. You should select a programmer based on the features it has and how it fits into your programming environment. The Microchip Development Systems Ordering Guide (DS30177) provides detailed information on all our development tools. The Microchip Third Party Guide (DS00104) provides information on all of our third party tool developers. Please consult these two references when selecting a programmer. Many options exist including serial or parallel PC host connection, stand-alone operation, and single or gang programmers. Some of the third party developers include Advanced Transdata Corporation, BP Microsystems, Data I/O, Emulation Technology and Logical Devices.

# Programming Environment

The programming environment will affect the type of programmer used, the programmer cable length, and the application circuit interface. Some programmers are well suited for a manual assembly line while others are desirable for an automated assembly line. You may want to choose a gang programmer to program multiple systems at a time.

The physical distance between the programmer and the application circuit affects the load capacitance on each of the programming signals. This will directly affect the drive strength needed to provide the correct signal rise rates and current. This programming cable must also be as short as possible and properly terminated and shielded or the programming signals may be corrupted by ringing or noise.

Finally, the application circuit interface to the programmer depends on the size constraints of the application circuit itself and the assembly line. A simple header can be used to interface the application circuit to the programmer. This might be more desirable for a manual assembly line where a technician plugs the programmer cable into the board. A different method is the use of spring loaded test pins (commonly referred to as pogo pins). The application circuit has pads on the board for each of the programming signals. Then there is a fixture that has pogo pins in the same configuration as the pads on the board. The application circuit or fixture is moved into position such that the pogo pins come into contact with the board. This method might be more suitable for an automated assembly line.

After taking into consideration the issues with the application circuit, the programmer, and the programming environment, anyone can build a high quality, reliable manufacturing line based on ICSP.

# Other Benefits

ICSP provides other benefits, such as calibration and serialization. If program memory permits, it would be cheaper and more reliable to store calibration constants in program memory instead of using an external serial EEPROM. For example, your system has a thermistor which can vary from one system to another. Storing some calibration information in a table format allows the microcontroller to compensate in software for external component tolerances. System cost can be reduced without affecting the required performance of the system by using software calibration techniques. But how does this relate to ICSP? The PICmicro MCU has already been programmed with firmware that performs a calibration cycle. The calibration data is transferred to a calibration fixture. When all calibration data has been transferred, the fixture places the PICmicro MCU in programming mode and programs the PICmicro MCU with the calibration data. Application note AN656, In-Circuit Serial Programming of Calibration Parameters Using a PICmicro Microcontroller, shows exactly how to implement this type of calibration data programming.

The other benefit of ICSP is serialization. Each individual system can be programmed with a unique or random serial number. One such application of a unique serial number would be for security systems. A typical system might use DIP switches to set the serial number. Instead, this number can be burned into program memory thus reducing the overall system cost and lowering the risk of tampering.

# Field Programming of FLASH PICmicro MCUs

With the ISP interface circuitry already in place, these FLASH-based PICmicro MCUs can be easily reprogrammed in the field. These FLASH devices allow you to reprogram them even if they are code protected. A portable ISP programming station might consist of a laptop computer and programmer. The technician plugs the ISP interface cable into the application circuit and downloads the new firmware into the PICmicro MCU. The next thing you know the system is up and running without those annoying “bugs”. Another instance would be that you want to add an additional feature to your system. All of your current inventory can be converted to the new firmware and field upgrades can be performed to bring your installed base of systems up to the latest revision of firmware.

# CONCLUSION

Microchip Technology Inc. is committed to supporting your ICSP needs by providing you with our many years of experience and expertise in developing ICSP solutions. Anyone can create a reliable ICSP programming station by coupling our background with some forethought to the circuit design and programmer selection issues previously mentioned. Your local Microchip representative is available to answer any questions you have about the requirements for ICSP.

![](images/60a6307af61ac6145d1e7f21d8a7ed242d44c49ef4b30db1f2b54542de9d002c.jpg)  
APPENDIX A:  SAMPLE DRIVER BOARD SCHEMATIC

# Section 3 – Programming Specifications

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC12C5XX OTP MCUs ....... .... 3-1

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC12C67X AND PIC12CE67X OTP MCUs ................. 3-15

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC14000 OTP MCUs ...... .. 3-27

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC16C55X OTP MCUs .... 3-39

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC16C6XX/7XX/9XX OTP MCUs .. ... 3-51

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC17C7XX OTP MCUs .... .. 3-71

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC18CXXX OTP MCUs .... .. 3-97

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC16F62X FLASH MCUs .... ... 3-135

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC16F8X FLASH MCUs ..... ... 3-149

IN-CIRCUIT SERIAL PROGRAMMING FOR PIC16F8XX FLASH MCUs .... ... 3-165

# In-Circuit Serial Programming™ for PIC12C5XX OTP MCUs

# This document includes the programming specifications for the following devices:

• PIC12C508 • PIC12C508A • PIC12CE518 • PIC12C509 • PIC12C509A • PIC12CE519 • rfPIC12C509AG   
• rfPIC12C509AF

# 1.0 PROGRAMMING THE PROGRAM

The PIC12C5XX can be programmed using a serial method. Due to this serial programming, the PIC12C5XX can be programmed while in the user’s system, increasing design flexibility. This programming specification applies to PIC12C5XX devices in all packages.

# 1.1 Hardware Requirements

The PIC12C5XX requires two programmable power supplies, one for VDD (2.0V to 6.5V recommended) and one for VPP (12V to 14V). Both supplies should have a minimum resolution of 0.25V.

# 1.2 Programming Mode

The Programming mode for the PIC12C5XX allows programming of user program memory, special locations used for ID, and the configuration word for the PIC12C5XX.

# Pin Diagram

![](images/0cf235a9ee90a08c29b8f5e55f030b862bc81f0dec6d839bcff3340da1efd32a.jpg)

![](images/055f3d046f20e5462467a10d8c0d40567e296a3793a88b7af2cdd3772c2a809a.jpg)

# 2.0 PROGRAM MODE ENTRY

The Program/Verify Test mode is entered by holding pins DB0 and DB1 low, while raising MCLR pin from VIL to VIHH. Once in this Test mode, the user program memory and the test program memory can be accessed and programmed in a serial fashion. The first selected memory location is the fuses. GP0 and GP1 are Schmitt Trigger inputs in this mode.

Incrementing the PC once (using the increment address command), selects location 0x000 of the regular program memory. Afterwards, all other memory locations from 0x001-01FF (PIC12C508/CE518), 0x001-03FF (PIC12C509/CE519) can be addressed by incrementing the PC.

If the program counter has reached the last user program location and is incremented again, the on-chip special EPROM area will be addressed. (See Figure 2- 2 to determine where the special EPROM area is located for the various PIC12C5XX devices.)

# 2.1 Programming Method

The programming technique is described in the following section. It is designed to ensure good programming margins. It does, however, require a variable power supply for VCC.

# 2.1.1 PROGRAMMING METHOD DETAILS

Essentially, this technique includes the following steps:

1. Perform blank check at VDD = VDDMIN. Report failure. The device may not be properly erased.   
2. Program location with pulses and verify after each pulse at VDD = VDDP: where VDDP = VDD range required during programming (4.5V - 5.5V).   
a) Programming condition: VPP = 13.0V to 13.25V VDD = VDDP = 4.5V to 5.5V VPP must be ≥ VDD + 7.25V to keep “Programming mode” active.   
b) Verify condition: VDD = VDDP VPP ≥ VDD + 7.5V but not to exceed 13.25V If location fails to program after “N” pulses (suggested maximum program pulses of 8), then report error as a programming failure.

<table><tr><td>Note:</td><td>Device must be verified at minimum and maximum specified operating voltages as</td></tr></table>

3. Once location passes “Step 2", apply 11X over programming (i.e., apply 11 times the number of pulses that were required to program the location). This will insure a solid programming margin. The over programming should be made “software programmable” for easy updates.

4. Program all locations.

5. Verify all locations (using Speed Verify mode) at VDD = VDDMIN.   
6. Verify all locations at VDD = VDDMAX. VDDMIN is the minimum operating voltage spec. for the part. VDDMAX is the maximum operating voltage spec. for the part.

# 2.1.2 SYSTEM REQUIREMENTS

Clearly, to implement this technique, the most stringent requirements will be that of the power supplies:

VPP: VPP can be a fixed 13.0V to 13.25V supply. It must not exceed 14.0V to avoid damage to the pin and should be current limited to approximately 100 mA.

VDD: 2.0V to 6.5V with 0.25V granularity. Since this method calls for verification at different VDD values, a programmable VDD power supply is needed.

# Current Requirement: 40 mA maximum

Microchip may release devices in the future with different VDD ranges, which make it necessary to have a programmable VDD.

It is important to verify an EPROM at the voltages specified in this method to remain consistent with Microchip's test screening. For example, a PIC12C5XX specified for 4.5V to 5.5V should be tested for proper programming from 4.5V to 5.5V.

Note: Any programmer not meeting the programmable VDD requirement and the verify at VDDMAX and VDDMIN requirement, may only be classified as a “prototype” or “development” programmer, but not a production programmer.

# 2.1.3 SOFTWARE REQUIREMENTS

Certain parameters should be programmable (and therefore, easily modified) for easy upgrade.

a) Pulse width.   
b) Maximum number of pulses, present limit 8.   
c) Number of over-programming pulses: should be = (A • N) + B, where N = number of pulses required in regular programming. In our current algorithm A = 11, B = 0.

# 2.2 Programming Pulse Width

Program Memory Cells: When programming one word of EPROM, a programming pulse width (TPW) of 100 µs is recommended.

The maximum number of programming attempts should be limited to 8 per word.

After the first successful verify, the same location should be over-programmed with 11X over-programming.

Configuration WordW= qÜÉ= ÅçåÑáÖìê\~íáçå= ïçêÇ= Ñçê çëÅáää\~íçê= ëÉäÉÅíáçåI= taq= Et\~íÅÜÇçÖ= qáãÉêF= Çáë\~ÄäÉ \~åÇ= ÅçÇÉ= éêçíÉÅíáçåI= \~åÇ= j\`io= Éå\~ÄäÉI= êÉèìáêÉë= \~ éêçÖê\~ããáåÖ=éìäëÉ=ïáÇíÜ=EqmtcF=çÑ=NM=ãëK=^=ëÉêáÉë=çÑ NMM=µë=éìäëÉë=áë=éêÉÑÉêêÉÇ=çîÉê=\~=ëáåÖäÉ=NM=ãë=éìäëÉK

![](images/f484be2cc1366d50e2ef8642eba33b27d51154e9291c62d868e75a6c8616301a.jpg)  
FIGURE 2-1: PROGRAMMING METHOD FLOW CHART

# FIGURE 2-2: PIC12C5XX SERIES PROGRAM MEMORY MAP IN PROGRAM/VERIFY MODE

![](images/02ed70cc50369bf22034700ab91a3aec594d252eca7f820c0f23e7fe14f64c84.jpg)

NNN Highest normal EPROM memory address. NNN = 0x1FF for PIC12C508/CE518. NNN = 0x3FF for PIC12C509/CE519. Note that some versions will have an oscillator calibration value programmed at NNN.   
TTT Start address of special EPROM area and ID locations.

# 2.3 Special Memory Locations

The highest address of program memory space is reserved for the internal RC oscillator calibration value. This location should not be overwritten except when this location is blank, and it should be verified, when programmed, that it is a MOVLW XX instruction.

The ID Locations area is only enabled if the device is in Programming/Verify mode. Thus, in normal operation mode, only the memory location 0x000 to 0xNNN will be accessed and the Program Counter will just rollover from address 0xNNN to 0x000 when incremented.

The configuration word can only be accessed immediately after MCLR going from VIL to VHH. The Program Counter will be set to all '1's upon MCLR = VIL. Thus, it has the value “0xFFF” when accessing the configuration EPROM. Incrementing the Program Counter once causes the Program Counter to rollover to all '0's. Incrementing the Program Counter 4K times after RESET (MCLR = VIL) does not allow access to the configuration EPROM.

# 2.3.1 CUSTOMER ID CODE LOCATIONS

Per definition, the first four words (address TTT to TTT + 3) are reserved for customer use. It is recommended that the customer use only the four lower order bits (bits 0 through 3) of each word and filling the eight higher order bits with '0's.

A user may want to store an identification code (ID) in the ID locations and still be able to read this code after the code protection bit was programmed.

# EXAMPLE 2-1: CUSTOMER CODE 0xD1E2

The Customer ID code “0xD1E2” should be stored in the ID locations 0x200-0x203 like this (PIC12C508/ 508A/CE518):

200: 0000 0000 1101   
201: 0000 0000 0001   
202: 0000 0000 1110   
203: 0000 0000 0010

Reading these four memory locations, even with the code protection bit programmed, would still output on GP0 the bit sequence “1101”, “0001”, “1110”, “0010” which is “0xD1E2”.

Note: All other locations in PICmicro® MCU configuration memory are reserved and should not be programmed.

# 2.4 Program/Verify Mode

The Program/Verify mode is entered by holding pins GP1 and GP0 low, while raising MCLR pin from VIL to VIHH (high voltage). Once in this mode, the user program memory and the configuration memory can be accessed and programmed in serial fashion. The mode of operation is serial. GP0 and GP1 are Schmitt Trigger inputs in this mode.

The sequence that enters the device into the Programming/Verify mode places all other logic into the RESET state (the MCLR pin was initially at VIL). This means that all I/O are in the RESET state (High impedance inputs).

Note: The MCLR pin should be raised from VIL to VIHH within 9 ms of VDD rise. This is to ensure that the device does not have the PC incremented while in valid operation range.

# 2.4.1 PROGRAM/VERIFY OPERATION

The GP1 pin is used as a clock input pin, and the GP0 pin is used for entering command bits and data input/ output during serial operation. To input a command, the clock pin (GP1) is cycled six times. Each command bit is latched on the falling edge of the clock with the Least Significant bit (LSb) of the command being input first. The data on pin GP0 is required to have a minimum setup and hold time (see AC/DC specs), with respect to the falling edge of the clock. Commands that have data associated with them (read and load) are specified to have a minimum delay of 1 µs between the command and the data. After this delay, the clock pin is cycled 16 times with the first cycle being a START bit and the last cycle being a STOP bit. Data is also input and output LSb first. Therefore, during a read operation, the LSb will be transmitted onto pin GP0 on the rising edge of the second cycle, and during a load operation, the LSb will be latched on the falling edge of the second cycle. A minimum 1 µs delay is also specified between consecutive commands.

All commands are transmitted LSb first. Data words are also transmitted LSb first. The data is transmitted on the rising edge and latched on the falling edge of the clock. To allow for decoding of commands and reversal of data pin configuration, a time separation of at least 1 µs is required between a command and a data word (or another command).

The commands that are available are listed in Table 2-1.

TABLE 2-1: COMMAND MAPPING   

<table><tr><td>Command</td><td colspan="6">Mapping (MSb .. LSb)</td><td>Data</td></tr><tr><td>Load Data</td><td>0</td><td>0 0</td><td></td><td>0 1</td><td>0</td><td>0, data(14), 0</td></tr><tr><td>Read Data</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0 0</td><td>0, data(14), 0</td></tr><tr><td>Increment Address</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1 0</td><td></td></tr><tr><td>Begin programming</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0 0</td><td></td></tr><tr><td>End Programming</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1 0</td><td></td></tr></table>

Note: The clock must be disabled during in-circuit programming.

# 2.4.1.1 Load Data

After receiving this command, the chip will load in a 14-bit “data word” when 16 cycles are applied, as described previously. Because this is a 12-bit core, the two MSb’s of the data word are ignored. A timing diagram for the load data command is shown in Figure 5-1.

# 2.4.1.2 Read Data

After receiving this command, the chip will transmit data bits out of the memory currently accessed, starting with the second rising edge of the clock input. The GP0 pin will go into Output mode on the second rising clock edge, and it will revert back to Input mode (hi-impedance) after the 16th rising edge. Because this is a 12- bit core, the two MSb’s of the data are unused and read as’0’. A timing diagram of this command is shown in Figure 5-2.

# 2.4.1.3 Increment Address

The PC is incremented when this command is received. A timing diagram of this command is shown in Figure 5-3.

# 2.4.1.4 Begin Programming

A load data command must be given before every begin programming command. Programming of the appropriate memory (test program memory or user program memory) will begin after this command is received and decoded. Programming should be performed with a series of 100 µs programming pulses. A programming pulse is defined as the time between the begin programming command and the end programming command.

# 2.4.1.5 End Programming

After receiving this command, the chip stops programming the memory (configuration program memory or user program memory) that it was programming at the time.

# 2.5 Programming Algorithm Requires Variable VDD

The PIC12C5XX uses an intelligent algorithm. The algorithm calls for program verification at VDDMIN, as well as VDDMAX. Verification at VDDMIN guarantees good “erase margin”. Verification at VDDMAX guarantees good “program margin”.

The actual programming must be done with VDD in the VDDP range (4.75 - 5.25V).

VDDP = VCC range required during programming.

VDDMIN = minimum operating VDD spec for the part.

VDDMAX = maximum operating VDD spec for the part.

Programmers must verify the PIC12C5XX at its specified VDDMAX and VDDMIN levels. Since Microchip may introduce future versions of the PIC12C5XX with a broader VDD range, it is best that these levels are user selectable (defaults are ok).

Note: Any programmer not meeting these requirements may only be classified as a “prototype” or “development” programmer, but not a “production” quality programmer.

# 3.0 CONFIGURATION WORD

The PIC12C5XX family members have several configuration bits. These bits can be programmed (reads '0'), or left unprogrammed (reads '1'), to select various device configurations. Figure 3-1 provides an overview of configuration bits.

# FIGURE 3-1: CONFIGURATION WORD BIT MAP

<table><tr><td colspan="10"></td></tr><tr><td>Bit Number:</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PIC12C5XX</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>MCLRE</td><td>CP</td><td>WDTE</td><td>FOSC1</td><td>FOSCO</td></tr></table>

Äáí=11-5: Reserved: Write as '0' for mf\`NO\`Ruu

Äáí=4: MCLRE: Master Clear Enable bit 1 = j\`io pin enabled 0 = j\`io internally connected to saa

Äáí=3: CP: Code Protect Enable bit 1 = Code memory unprotected 0 = Code memory protected

Äáí=2: WDTE, WDT Enable bit 1 = WDT enabled 0 = WDT disabled

Äáí=1-0: FOSC<1:0>, Oscillator Selection Bit 11 = External RC oscillator 10 = Internal RC oscillator 01 = XT oscillator 00 = LP oscillator

# 4.0 CODE PROTECTION

The program code written into the EPROM can be protected by writing to the CP bit of the configuration word.

In PIC12C5XX, it is still possible to program and read locations 0x000 through 0x03F, after code protection. Once code protection is enabled, all protected segments read '0's (or “garbage values”) and are prevented from further programming. All unprotected segments, including ID locations and configuration word, read normally. These locations can be programmed.

Once code protection is enabled, all code protected locations read 0’s. All unprotected segments, including the internal oscillator calibration value, ID, and configuration word read as normal.

# 4.1 Embedding Configuration Word and ID Information in the HEX File

To allow portability of code, the programmer is required to read the configuration word and ID locations from the HEX file when loading the HEX file. If configuration word information was not present in the HEX file, then a simple warning message may be issued. Similarly, while saving a HEX file, configuration word and ID information must be included. An option to not include this information may be provided.

Microchip Technology Inc. feels strongly that this feature is important for the benefit of the end customer.

# TABLE 4-1: CODE PROTECTION

PIC12C508 To code protect:

√ (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0x40:0x1FF]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0x200 : 0x203)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# PIC12C508A

# To code protect:

√ (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×40:0x1FE]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>0x1FF Oscillator Calibration Value</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0x200 : 0x203)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# PIC12C509

# To code protect:

√ (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0x40:0x3FF]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0x400 : 0×403)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# PIC12C509A

# To code protect:

√ (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×40:0x3FE]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>0x3FF Oscillator Calibration Value</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0x400 : 0x403)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# PIC12CE518

To code protect:

• (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0x40:0x1FE]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>0x1FF Oscillator Calibration Value</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0x200 : 0x203)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# PIC12CE519 To code protect:

• (CP enable pattern: XXXXXXXX0XXX)

<table><tr><td rowspan=1 colspan=1>Program Memory Segment</td><td rowspan=1 colspan=1>R/W in Protected Mode</td><td rowspan=1 colspan=1>R/W in Unprotected Mode</td></tr><tr><td rowspan=1 colspan=1>Configuration Word (OxFFF)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0×00:0x3F]</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>[0x40:0x3FF]</td><td rowspan=1 colspan=1>Read Disabled (all O&#x27;s), Write Disabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr><tr><td rowspan=1 colspan=1>ID Locations (0×400 : 0x403)</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td><td rowspan=1 colspan=1>Read Enabled, Write Enabled</td></tr></table>

# 4.2 Checksum

# 4.2.1 CHECKSUM CALCULATIONS

Checksum is calculated by reading the contents of the PIC12C5XX memory locations and adding up the opcodes up to the maximum user addressable location (not including the last location which is reserved for the oscillator calibration value), e.g., 0x1FE for the PIC12C508/CE518. Any carry bits exceeding 16 bits are neglected. Finally, the configuration word (appropriately masked) is added to the checksum. Checksum computation for each member of the PIC12C5XX family is shown in Table 4-2.

The checksum is calculated by summing the following:

• The contents of all program memory locations • The configuration word, appropriately masked • Masked ID locations (when applicable)

The Least Significant 16 bits of this sum are the checksum.

The following table describes how to calculate the checksum for each device. Note that the checksum calculation differs depending on the code protect setting. Since the program memory locations read out differently depending on the code protect setting, the table describes how to manipulate the actual program memory values to simulate the values that would be read from a protected device. When calculating a checksum by reading a device, the entire program memory can simply be read and summed. The configuration word and ID locations can always be read.

The oscillator calibration value location is not used in the above checksums.

TABLE 4-2: CHECKSUM COMPUTATION   

<table><tr><td rowspan=1 colspan=1>Device</td><td rowspan=1 colspan=1>CodeProtect</td><td rowspan=1 colspan=1>Checksum*</td><td rowspan=1 colspan=1>BlankValue</td><td rowspan=1 colspan=1>0x723 at0 and MaxAddress</td></tr><tr><td rowspan=1 colspan=1>PIC12C508</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x1FE] + CFGW &amp; 0x01FSUM[0x000:0×03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EE20EDF7</td><td rowspan=1 colspan=1>DC68D363</td></tr><tr><td rowspan=1 colspan=1>PIC12C508A</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x1FE] + CFGW &amp; 0x01FSUM[0x000:0x03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EE20EDF7</td><td rowspan=1 colspan=1>DC68D363</td></tr><tr><td rowspan=1 colspan=1>PIC12C509</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0×000:0x3FE] + CFGW &amp; 0x01FSUM[0x000:0×03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EC20EBF7</td><td rowspan=1 colspan=1>DA68D163</td></tr><tr><td rowspan=1 colspan=1>PIC12C509A</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x3FE] + CFGW &amp; 0x01FSUM[0x000:0x03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EC20EBF7</td><td rowspan=1 colspan=1>DA68D163</td></tr><tr><td rowspan=1 colspan=1>PIC12CE518</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x1FE] + CFGW &amp; 0x01FSUM[0x000:0×03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EE20EDF7</td><td rowspan=1 colspan=1>DC68D363</td></tr><tr><td rowspan=1 colspan=1>PIC12CE519</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x3FE] + CFGW &amp; 0x01FSUM[O×000:0x03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EC20EBF7</td><td rowspan=1 colspan=1>DA68D163</td></tr><tr><td rowspan=1 colspan=1>rfPIC12C509AG</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x3FE] + CFGW &amp; 0x01FSUM[O×000:0x03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EC20EBF7</td><td rowspan=1 colspan=1>DA68D163</td></tr><tr><td rowspan=1 colspan=1>rfPIC12C509AF</td><td rowspan=1 colspan=1>OFFON</td><td rowspan=1 colspan=1>SUM[0x000:0x3FE] + CFGW &amp; 0x01FSUM[0x000:0x03F] + CFGW &amp; 0x01F + SUM(IDS)</td><td rowspan=1 colspan=1>EC20EBF7</td><td rowspan=1 colspan=1>DA68D163</td></tr></table>

Legend: CFGW = Configuration Word SUM[a:b] = [Sum of locations a through b inclusive] SUM_ID = ID locations masked by 0xF then made into a 16-bit value with ID0 as the most significant nibble. For example, ID0 = 0x12, ID1 = 0x37, ID2 = 0x4, ID3 = 0x26, then SUM_ID = 0x2746. \*Checksum = [Sum of all the individual expressions] MODULO [0xFFFF] + = Addition & = Bitwise AND

# 5.0 PROGRAM/VERIFY MODE ELECTRICAL CHARACTERISTICS

TABLE 5-1: AC/DC CHARACTERISTICS TIMING REQUIREMENTS FOR PROGRAM/VERIFY MODE

<table><tr><td rowspan=1 colspan=8>Standard Operating ConditionsOperating Temperature: +10°C ≤ TA ≤ +40°C, unless otherwise stated, (20°C recommended)Operating Voltage:      4.5V ≤ VDD ≤ 5.5V, unless otherwise stated.</td></tr><tr><td rowspan=1 colspan=1>ParameterNo.</td><td rowspan=1 colspan=1>Sym.</td><td rowspan=1 colspan=1>Characteristic</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Conditions</td></tr><tr><td rowspan=1 colspan=8>General</td></tr><tr><td rowspan=1 colspan=1>PD1</td><td rowspan=1 colspan=1>VDDP</td><td rowspan=1 colspan=1>Supply voltage during programming</td><td rowspan=1 colspan=1>4.75</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>5.25</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PD2</td><td rowspan=1 colspan=1>IDDP</td><td rowspan=1 colspan=1>Supply current (from VDD)during programming</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>mA</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PD3</td><td rowspan=1 colspan=1>VDDV</td><td rowspan=1 colspan=1>Supply voltage during verify</td><td rowspan=1 colspan=1>VDDMIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDDMAX</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>(Note 1)</td></tr><tr><td rowspan=1 colspan=1>PD4</td><td rowspan=1 colspan=1>VIHH1</td><td rowspan=1 colspan=1>Voltage on MCLR/VpP duringprogramming</td><td rowspan=1 colspan=1>12.75</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13.25</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>(Note 2)</td></tr><tr><td rowspan=1 colspan=1>PD5</td><td rowspan=1 colspan=1>VIHH2</td><td rowspan=1 colspan=1>Voltage on MCLR/VPp during verify</td><td rowspan=1 colspan=1>VDD + 4.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PD6</td><td rowspan=1 colspan=1>IPP</td><td rowspan=1 colspan=1>Programming supply current(from VPP)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>mA</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PD9</td><td rowspan=1 colspan=1>VH1</td><td rowspan=1 colspan=1>(GP1, GPO) input high level</td><td rowspan=1 colspan=1>0.8 VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>Schmitt Trigger input</td></tr><tr><td rowspan=1 colspan=1>PD8</td><td rowspan=1 colspan=1>VIL1</td><td rowspan=1 colspan=1>(GP1, GP0) input low level</td><td rowspan=1 colspan=1>0.2 VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>Schmitt Trigger input</td></tr></table>

<table><tr><td rowspan=1 colspan=8>Serial Program Verify</td></tr><tr><td rowspan=1 colspan=1>P1</td><td rowspan=1 colspan=1>TR</td><td rowspan=1 colspan=1>MCLR/Vpp rise time (Vss to VHH)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>$P2$</td><td rowspan=1 colspan=1>Tf</td><td rowspan=1 colspan=1>MCLR fall time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P3</td><td rowspan=1 colspan=1>Tset1</td><td rowspan=1 colspan=1>Data in setup time before clock ↓</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P4</td><td rowspan=1 colspan=1>Thld1</td><td rowspan=1 colspan=1>Data in hold time after clock ↓</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P5</td><td rowspan=1 colspan=1>Tdly1</td><td rowspan=1 colspan=1>Data input not driven to next clockinput (delay required between com-mand/data or command/command)</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P6</td><td rowspan=1 colspan=1>Tdly2</td><td rowspan=1 colspan=1>Delay between clock ↓ to clock ↑ ofnext command or data</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P7</td><td rowspan=1 colspan=1>Tdly3</td><td rowspan=1 colspan=1>Clock ↑ to date out valid(during read data)</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P8</td><td rowspan=1 colspan=1>Thld0</td><td rowspan=1 colspan=1>Hold time after MCLR↑</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td><td rowspan=1 colspan=1></td></tr></table>

Note 1: Program must be verified at the minimum and maximum VDD limits for the part. 2: VIHH must be greater than VDD + 4.5V to stay in Programming/Verify mode.