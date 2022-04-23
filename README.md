# Assesment 3 - Obstacle avoidance robot
This is our README git file for assesment 3. Youssef Elsayed 202000067 - Amr Hamdy 202000109

## What we used in this code
- In this code we used **Python 3.6.9** and we used **VS code** to run and test the code.
- We also used some libraries to import some functions
    - **Libraries used:**
        - RoboticsToolbox
        - Math
        - matplotlib.pyplot
    - **Functions imported**
        - Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap (*from RoboticsToolbox*)
        - pi , atan2 (*from Math*)
## User inputs and expected outputs
- **User Inputs**
  1. Firstly the user is asked to input the x and y coordinates of the intial position of the robot inwhich the robot will start moving from using the function `Robot_initial=(input("Please enter the robot's start coordinates as x  y: "))`
  2. Then the user asked to input the intial angle of the robot in radians using the function `Robot_initial_angle=(input("Please enter the robot's initial angle in radians: "))`
  3. After that the user is asked to input the coordinates of the target the robot will approach using the function `Target_Coordinates=(input("Please enter the target coordinates as x  y: "))`
  4. Then the user is asked to input the number of obsticales that will be displayed on the map using the function `Num_of_obstacles=(input("Please input number of obstacles: "))
  5. The user is then asked if he want to add an extra target so the robot can reach the first target and go to the second one. The user has to answer with 'yes' or 'no'. If the user inputs 'yes' the user will be asked to input the second target coordinates x and y uing `Target_Coordinates2=(input("Please enter target 2 coordinates as x  y: "))` and if the user inputs 'no' the code will start functioning.
- **Expected output**
  1. The robot will be dispaled on the map at the exact starting coordinates and angle that are input by the user
  2. The target is displayed on the map at the input coordinates
  3. Obsticales are generated randomly on the map with the exact number that was input by the user
  4. If the user input 'yes' , the second target will be displayed on the map at the input coordinates. If the user input is 'No', no target will be displayed
  5. Then the robot will start to function
## Funtionality
We divided the code into **four parts**:
- Inputs
- Designing the robot,map and target
- Defining different functions
- Make use of the defined functions to perform the task

**Inputs**:
The first part of the code is the inputs of the user that are discussed above (*robot's position, Target's position, number of obsticles*) and there is an if condition so that if the user want an extra target, he will input the cooedinates of the extra target 

```#option input
Target2=(input("Do you want two targets?. please input 'yes' or 'no': "))
if Target2 =="yes":
    Target_Coordinates2=(input("Please enter target 2 coordinates as x  y: "))
    Target_Coordinates2=Target_Coordinates2.split()```
    
We also used the split function `Robot_initial=Robot_initial.split()` , `Target_Coordinates=Target_Coordinates.split()` to be able to use the coordinates seperately later on.

  
            
