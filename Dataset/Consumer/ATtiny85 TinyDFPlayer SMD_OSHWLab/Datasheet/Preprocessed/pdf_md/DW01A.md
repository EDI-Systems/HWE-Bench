# One Cell Lithium-ion/Polymer Battery Protection IC

# Description

The DW01A has built-in a high precision voltage detection circuit and delay circuit, by detecting the battery voltage、current, realize the battery overcharge, overdischarge, overcurrent protection and so on. Suitable for single section lithium-ion/lithium-polymer rechargeable battery protection circuit.

# Features

High precision voltage detection function: 1. Overcharge Protection Voltage 4.28V Accuracy: ±50mV 2. Overcharge Release Voltage 4.08V Accuracy: ±50mV 3. Overdischarge Protection Voltage 2.40V Accuracy: ±100mV 4. Overdischarge Release Voltage 3.00V Accuracy: ±100mV Discharge overcurrent detection function 1. Overcurrent Protection Voltage 160mV Accuracy: ±20mV 2. Short Current Protection Voltage 1.00V Accuracy: ±300mV Protection Delay Time 1. Overcharge Delay Time 80ms(Typ.) 2. Overdischarge Delay Time 40ms(Typ.) 3. Discharge overcurrent delay time 10ms(Typ.) 4. Charge overcurrent delay time 10ms(Typ.) 5. Load short circuit delay time 300µs(Typ.)   
⚫ Charge overcurrent detection voltage -0.150V   
Load detection function   
⚫ Allow to charge 0V battery function Low power consumption current 1. Operating state 1.5µA(Typ.), at T =25°C 2. Overdischarge state 0.7µA(Typ.), at TA=25°C   
⚫ The recommended capacity of lithium-ion batteries is 1000mA/h or less   
⚫ Operating temperature range：- 40℃\~+85℃ Available in SOT-23-6 Package

# Applications

⚫ Protection IC for One-Cell Lithium-Ion /Lithium-Polymer Battery Pack

# Typical Application Circuit

![](images/a892911d012e871368561ec7cd7a41a00f7a2556a9c12b4397944a8db1489b5a.jpg)

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Rating</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>R1</td><td rowspan=1 colspan=1>470</td><td rowspan=1 colspan=1>470~1500</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>R2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1~3</td><td rowspan=1 colspan=1>kΩ</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>≥0.1</td><td rowspan=1 colspan=1>μF</td></tr></table>

# Note：

1. R1, R2 cannot be omitted, and R1 must be greater than or equal to 470 ohms.

# Pin Distribution

![](images/aed12b1f9eca68201a531c25322466428a8b5cb77e91df2537b666a192425448.jpg)

# Functional Pin Description

<table><tr><td rowspan=1 colspan=1>Pin NO.</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Pin Description</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>OD</td><td rowspan=1 colspan=1>MOSFET gate connection pin for discharge control</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1> Input pin for current sense, charger detect</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>OC</td><td rowspan=1 colspan=1>MOSFET gate connection pin for charge control</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>NC</td><td rowspan=1 colspan=1>Not Connected</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>Power supply, through a resistor (R1)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>Ground pin</td></tr></table>

# Ordering Information

<table><tr><td rowspan=1 colspan=1>OrderableDevice</td><td rowspan=1 colspan=1>Package</td><td rowspan=1 colspan=1>Reel(inch)</td><td rowspan=1 colspan=1>Package Qty(PCS)</td><td rowspan=1 colspan=1>Eco Plan Note</td><td rowspan=1 colspan=1>MSL Level</td><td rowspan=2 colspan=1>Marking CodeDW01A</td></tr><tr><td rowspan=1 colspan=1>DW01A</td><td rowspan=1 colspan=1>SOT-23-6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>3000</td><td rowspan=1 colspan=1>RoHS &amp; Green</td><td rowspan=1 colspan=1>MSL3</td></tr></table>

Note: RoHS：TN defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance do not exceed 0.1% by weight in homogeneous materials. Green：TN defines "Green" to mean Halogen-Free and Antimony-Free.

# Block Diagram

![](images/4e300eb7e24441542a1afab84635e7772b60424f6420773c162a2c36728ba0f1.jpg)

# Product Name List

<table><tr><td rowspan=2 colspan=1>ParameterModel</td><td rowspan=1 colspan=1>OverchargeProtectVoltage</td><td rowspan=1 colspan=1>OverchargeReleaseVoltage</td><td rowspan=1 colspan=1>OverdischargeProtectVoltage</td><td rowspan=1 colspan=1>Overdischargereleasevoltage</td><td rowspan=1 colspan=1>OverdischargeCurrent</td><td rowspan=1 colspan=1>ShortCircuit</td><td rowspan=1 colspan=1>ChargingOvercurrent</td><td rowspan=1 colspan=1>OverchargeLock</td><td rowspan=1 colspan=1>OverdischargeLock</td></tr><tr><td rowspan=1 colspan=1>VOCP</td><td rowspan=1 colspan=1>VOCR</td><td rowspan=1 colspan=1>VODP</td><td rowspan=1 colspan=1>VODR</td><td rowspan=1 colspan=1>VEC1</td><td rowspan=1 colspan=1>VSHORT</td><td rowspan=1 colspan=1>VCHA</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>--</td></tr><tr><td rowspan=1 colspan=1>DW01A</td><td rowspan=1 colspan=1>4.280V</td><td rowspan=1 colspan=1>4.080V</td><td rowspan=1 colspan=1>2.400V</td><td rowspan=1 colspan=1>3.000V</td><td rowspan=1 colspan=1>0.160V</td><td rowspan=1 colspan=1>1.000V</td><td rowspan=1 colspan=1>-0.15V</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N</td></tr></table>

# Absolute Maximum Ratings

(TA=25℃ , unless otherwise noted.)

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Rating</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Power voltage</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>-0.3~6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>CS input pin voltage</td><td rowspan=1 colspan=1>VCS</td><td rowspan=1 colspan=1>VCC-15 to VCC+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Operating Temperature Range</td><td rowspan=1 colspan=1>TOPR</td><td rowspan=1 colspan=1>-40~85</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature Range</td><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1>-55~125</td><td rowspan=1 colspan=1>℃</td></tr></table>

Note: When the voltage exceeds the absolute maximum rating, the chip may be irreparable damage.

# Electrical Characteristics

(TA=25℃ , unless otherwise noted.)

<table><tr><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Test Conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=2>Operating Voltage</td><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=2>Supply Current</td><td rowspan=1 colspan=1>lvcc</td><td rowspan=1 colspan=1>VCC=3.5V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=2>Power-Down Current</td><td rowspan=1 colspan=1>IOPED</td><td rowspan=1 colspan=1>VCC =1.5V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=3 colspan=1>Overcharge</td><td rowspan=1 colspan=1>Protection Voltage</td><td rowspan=1 colspan=1>Voc</td><td rowspan=1 colspan=1>VCC =3.5→4.5V</td><td rowspan=1 colspan=1>4.230</td><td rowspan=1 colspan=1>4.280</td><td rowspan=1 colspan=1>4.330</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Release Voltage</td><td rowspan=1 colspan=1>VocR</td><td rowspan=1 colspan=1>VCC =4.5→3.5V</td><td rowspan=1 colspan=1>4.030</td><td rowspan=1 colspan=1>4.080</td><td rowspan=1 colspan=1>4.130</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Protection Delay Time</td><td rowspan=1 colspan=1>Toc</td><td rowspan=1 colspan=1>VCC =3.5→4.5V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>mS</td></tr><tr><td rowspan=3 colspan=1>Overdischarge</td><td rowspan=1 colspan=1>Protection Voltage</td><td rowspan=1 colspan=1>VoD</td><td rowspan=1 colspan=1>VC5=3.5→2.0V</td><td rowspan=1 colspan=1>2.300</td><td rowspan=1 colspan=1>2.400</td><td rowspan=1 colspan=1>2.500</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Release Voltage</td><td rowspan=1 colspan=1>VoDR</td><td rowspan=1 colspan=1>VCC =2.0→3.5V</td><td rowspan=1 colspan=1>2.900</td><td rowspan=1 colspan=1>3.000</td><td rowspan=1 colspan=1>3.100</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Protection Delay Time</td><td rowspan=1 colspan=1>ToD</td><td rowspan=1 colspan=1>VCC =3.5→2.0V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>mS</td></tr><tr><td rowspan=2 colspan=1>DischargeOvercurrent</td><td rowspan=1 colspan=1>Protection Voltage</td><td rowspan=1 colspan=1>VEC</td><td rowspan=1 colspan=1>VM-VSS=0→0.20V</td><td rowspan=1 colspan=1>0.140</td><td rowspan=1 colspan=1>0.160</td><td rowspan=1 colspan=1>0.180</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Protection Delay Time</td><td rowspan=1 colspan=1>TEc</td><td rowspan=1 colspan=1>VM-VSS=0→0.20V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>mS</td></tr><tr><td rowspan=2 colspan=1>ChargeOvercurrent</td><td rowspan=1 colspan=1>Protection Voltage</td><td rowspan=1 colspan=1>VCHA</td><td rowspan=1 colspan=1>VSS-VM=0→0.30V</td><td rowspan=1 colspan=1>-0.180</td><td rowspan=1 colspan=1>-0.150</td><td rowspan=1 colspan=1>-0.120</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Protection Delay Time</td><td rowspan=1 colspan=1>TCHA</td><td rowspan=1 colspan=1>VSS-VM=0→0.30V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>mS</td></tr><tr><td rowspan=2 colspan=1>Short-Circuit</td><td rowspan=1 colspan=1>Protection Voltage</td><td rowspan=1 colspan=1>VSHORT</td><td rowspan=1 colspan=1>VM -VSS=0→1.5V</td><td rowspan=1 colspan=1>0.700</td><td rowspan=1 colspan=1>1.000</td><td rowspan=1 colspan=1>1.300</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Protection Delay Time</td><td rowspan=1 colspan=1>TSHORT</td><td rowspan=1 colspan=1>VM -VSS=0→1.5V</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>600</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=2>Charger Starting Voltage(Allow Charging to OV Battery)</td><td rowspan=1 colspan=1>VovCH</td><td rowspan=1 colspan=1>Allow charging to OV battery</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>--</td><td rowspan=1 colspan=1>V</td></tr></table>

# Description of Operation

# 1. Overcharge Protection

When the battery voltage rises above VOC and lasts for a period of time TOC, the output of OC terminal will be reversed and the charging control MOSFET will be turned off to stop charging, which is called the overcharge state.When the battery voltage drops below the VOCR of overcharge release voltage and lasts for a period of timeTOCR, It will remove the overcharge state and return to normal state.

there are two ways to remove the overcharge state and return to the normal state:

1.1 Disconnect the charger, do not connect the load and VCHA<VCS<VEC. When the battery voltage drops below the VOCR of overcharge release voltage, the overcharge state will be released 1.2 Disconnect the charger and connect the load, if VCS>VEC. At this time, only VCC<VOC is required, and the overcharge state will be released. This function is called load detection function.attention, after detecting overcharge, if the charger is always connected, then even if the cell voltage drops to below VOCR , overcharging state can not be released. through disconnect the charger and VCS> VCHA to remove the overcharge and discharge state.

# 2. Overdischarge Protection

When the battery voltage drops below VOD and lasts for a period of timeTOD, the output of OD terminal will be reversed and the discharging control MOSFET will be turned off to stop discharging, which is called the overdischarge state.When the battery voltage rises above the VODR of overcharge release voltage and lasts for a period of timeTODR, It will remove the overdischarge state and return to normal state.

There are three ways to release the over-discharge state:

2.1 Connect the charger, if the CS terminal voltage is lower than the charger detection voltage (VCH), when the battery voltage is higher than the overdischarge detection voltage (VOD), the overdischarge state will be released and the charger will return to normal operating state. This function is called the charger detection function.

2.2 Connect the charger. If the CS terminal voltage is higher than the charger detection voltage (VCH), when the battery voltage is higher than the overdischarge discharge voltage (VODR), the overdischarge state will be released and return to normal operating state.

2.3 When disconnect the charger, if the battery voltage restores to higher than the over-discharge discharge voltage (VODR), the over-discharge state is released and the battery returns to normal operating state., that is, the over-discharge self-recovery function is available.

# 3. Discharge Overcurrent State

In Voltage of the battery are in a state of discharge, VCS increases with the increase of discharge current, when the voltage of the CS is higher than the VEC and lasted for a period of time(TEC) , The chip is thought to have a discharge overcurrent; when the voltage of the CS is higher than the VSHORT and lasted for a period of time(TSHORT), The chip is thought to short circuit . The above two kinds of any state, OD terminal output will be reversed, the discharge control MOSFET will be turned off to stop discharging

As long as the load equivalent resistance be increased or disconnect the load, make the VCS < VEC, can remove discharge overdischarge state, returned to normal state.

# 4. Charge Overcurrent Detection

Under normal operating state of the battery, in the process of charging, if CS terminal voltage is lower than charging overcurrent detection voltage (VCHA), and the state duration is over the delay time of charge overcurrent detection(TCHA), then close the charging control MOSFET, stop charging, the state is called charge overcurrent state. After charging into the overcurrent detection state, if broken charger to CS terminal voltage higher than over-current detection voltage (VCHA), charge overcurrent state was lifted, return to normal operating condition.

# 5. Allow to charge 0V battery function

This function is used to have self-discharge to 0V of rechargeable batteries. When the charger voltage connected to the positive (P+) and negative (P-) between the battery higher than the 0V battery charger starting voltage(V0VCH) , The gate of charging control MOSFET is the potential of VDD, Due to the charger voltage make the voltage between gate and the source of MOSFET higher than threshold voltage, the charge control MOSFET be turn on (OC terminal open), start charging. at this time, the discharge control MOSFET is still shut off, the charging current through its internal parasitic diodes. When the battery voltage is higher than the discharge detection voltage (VOD), IC into the normal operating condition.

# Package Outline

SOT-23-6 Dimensions in mm

![](images/23e9bb2cc8828cbd0cf54ebfc529e8a3bac83e2bf0de54dca15c6444a85ef6ca.jpg)

![](images/8bd86138b89f742241f5a36c26e1eaa05a1f7fa1a6eaff73b997b6198f2f8b07.jpg)

![](images/4fc240654ce2bd0a0a13cc6f268a2f4fef0d34a770b833cc685cf5bd06d40dbf.jpg)

# Contact Information

TANI website: http://www.tanisemi.com Email:tani@tanisemi.com

For additional information, please contact your local Sales Representative.

# ® is registered trademarks of TANI Corporation.

# Product Specification Statement

The product specification aims to provide users with a reference regarding various product parameters, performance, and usage. It presents certain aspects of the product's performance in graphical form and is intended solely for users to select product and make product comparisons, enabling users to better understand and evaluate the characteristics and advantages of the product. It does not constitute any commitment, warranty, or guarantee.

The product parameters described in the product specification are numerical values, characteristics, and functions obtained through actual testing or theoretical calculations of the product in an independent or ideal state. Due to the complexity of product applications and variations in test conditions and equipment, there may be slight fluctuations in parameter test values. TANI shall not guarantee that the actual performance of the product when installed in the customer's system or equipment will be entirely consistent with the product specification, especially concerning dynamic parameters. It is recommended that users consult with professionals for product selection and system design. Users should also thoroughly validate and assess whether the actual parameters and performance when installed in their respective systems or equipment meet their requirements or expectations. Additionally, users should exercise caution in verifying product compatibility issues, and TANI assumes no responsibility for the application of the product. TANI strives to provide accurate and up -to- date information to the best of our ability. However, due to technical, human, or other reasons, TANI cannot guarantee that the information provided in the product specification is entirely accurate and error-free. TANI shall not be held responsible for any losses or damages resulting from the use or reliance on any information in these product specifications.

TANI reserves the right to revise or update the product specification and the products at any time without prior notice, and the user's continued use of the product specification is considered an acceptance of these revisions and updates. Prior to purchasing and using the product, users should verify the above information with TANI to ensure that the prod uct specification is the most current, effective, and complete. If users are particularly concerned about product parameters, please consult TANI in detail or request relevant product test reports. Any data not explicitly mentioned in the product specification shall be subject to separate agreement.

Users are advised to pay attention to the parameter limit values specified in the product specification and maintain a certain margin in design or application to ensure that the produc does not exceed the parameter limit values defined in the product specification. This precaution should be taken to avoid exceeding one or more of the limit values, which may result i permanent irreversible damage to the product, ultimately affecting the quality and reliability of the system or equipment.

The design of the product is intended to meet civilian needs and is not guaranteed for use in harsh environments or precision equipment. It is not recommended for use in systems or equipment such as medical devices, aircraft, nuclear power, and similar systems, where failures in these systems or equipment could reasonably be expected to result in personal injury. TANI shall assume no responsibility for any consequences resulting from such usage.

Users should also comply with relevant laws, regulations, policies, and standards when using the product specification. Users are responsible for the risks and liabilities arising from th use of the product specification and must ensure that it is not used for illegal purposes. Additionally, users should respect the intellectual property rights related to the product specification and refrain from infringing upon any third- party legal rights. TANI shall assume no responsibility for any disputes or controv ersies arising from the above-mentioned issues in any form.