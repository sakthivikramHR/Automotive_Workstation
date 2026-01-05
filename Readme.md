# Vikram's Automotive Testing Projects/Experiments

## Description
A workstation filled with small automotive testing projects or experiments based on the knowledge I gathered from my working experience and combining it with the knowledge I have in Python Programming language 

## Contents of the Workstation

### Steering Assist in EPS: Torque to Current Mapping

1. A project to check whether the speed of the vehicle and the torque produced by the driver is very well under the defined limits. 

2. The assist current is also calculated and applied respectively based on the driver torque. 

3. Functional Safety: If the vehicle speed crosses the defined vehicle speed and the driving torque, the assist current which is provided by the motor is set to 0 Ampere. In this way, the steering wheel feels tighter and helps in the stability of higher speeds.

4. Provides better stability and vehicle control in both lower and higher speeds.

## Fault Identification in BMS: Unexpected Boundary Conditions

1. A project to develop a small state machine to manage the transitions between SHUTDOWN (High Temperature), OVERVOLTAGE, UNDERVOLTAGE, LOW TEMPERATURE based on the sensor inputs of Temperature and Voltage. 

2. Functional Safety: The above mentioned states in machine occurs when the temperature and voltage exceeds beyond the defined limits.

3. Maintaines the efficiency of the machine.

4. Handling unexpected boundary conditions by changing the states of the system notifying the machine requires further attention.

## Virtual HiL Architecture: 

1. A project to simulate network environment by implementing a virtual CAN. 

2. Designed and Implemented a .dbc file to define network communications.

3. Utilized Python-can and cantools libraries in Python for high level message encoding and decoding. 



## Error Injection: Communication Failure

1. A project where communication Failures like CRC Failure, Timeout Failure, Signal Jumps are induced manually to check whether the system reacts accordingly.

2. Used Defensive Programming techniques to prioritize error detection over functional processing.

3. Functions are created for the above mentioned Failures seperately to handle unexpected failures with respective error messages.

4. Improves the Robustness of the overall system.