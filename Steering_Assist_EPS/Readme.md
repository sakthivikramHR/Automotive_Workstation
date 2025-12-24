# Steering Assist with EPS

## Description
This project simulates a steering assist with EPS by checking whether the Vehicle speed and Engine Torque is under the limits of Safety regulations.

## Functional Safety Goals

1. The Vehicle Speed should be below the limit of the Vehicle Speed mentioned in the EPS Logic.
2. The Driving Torque should be in the limit of 20Nm.
3. If at all the conditions 1 and 2 are satisfied, the assist current has to be calculated 

## How to run the file?

Use the command "pytest -v eps_safety.py" to run all the files.

## Information about the project

1. The Vehicle_Speed variable is taken into account for the test because when the Vehicle_speed goes beyond 250km/h, the vehicle should have zero assist so that the steering is stiff to ensure stability.
2. When the Vehicle speed is under the Safety limit, the torque given by the driver is multiplied with 2 so that we get the assist current. 
3. But when the Driving torque reaches the limit of 20, the assist has to be set to 0 so that it ensures stability.