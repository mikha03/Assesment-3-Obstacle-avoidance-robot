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
## Functionality
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
    Target_Coordinates2=Target_Coordinates2.split()
```
        
We also used the split function `Robot_initial=Robot_initial.split()` , `Target_Coordinates=Target_Coordinates.split()` to be able to use the coordinates seperately later on.

**Designing the robot,map and target**:

Firstly we setup the robot using the functions imported from RoboticsToolbox and downloaded a picture to be the design of the robot and we scaled it using the VehicleIcon function. and we defined the intial position of the robot according to the coordinates and angle input by the user.Then we plotted the robot and updated its position
```#Robot's place and design
anim = VehicleIcon('redcar.png', scale = 2)
veh = Bicycle(
animation = anim,
control = RandomPath,
x0 = (Robot_initial[0],Robot_initial[1],Robot_initial_angle),
)
print(veh.x)
veh.init(plot=True)
veh._animation.update(veh.x)
```
We then plotted the target with the specified coordinates entered by the user and we design the target as we like. We can change Its color,size,and shape.
```#Target design and coordinates
goal=[float(Target_Coordinates[0]),float(Target_Coordinates[1])];
goal_marker_style = {
'marker': 'X',
'markersize': 15,
'color': 'b',
}
plt.plot(goal[0],goal[1], **goal_marker_style)
```
Then we designed another target with different colour so if the user wants another target, it will be plotted with the chosen coordinates.
```#Target 2 design and coordinates
if Target2=="yes":
    goal2=[float(Target_Coordinates2[0]),float(Target_Coordinates2[1])];
    goal_marker_style = {
    'marker': 'X',
    'markersize': 15,
    'color': 'r',
    }
    plt.plot(goal2[0],goal2[1], **goal_marker_style)
```
After that we write the function that displays the map with the specified number of obstacles entered by the user in the input as well as the dimensions of the map. In this task we needed a 20x20 map.
```#map and number of obsticles
map=LandmarkMap(int(Num_of_obstacles), 10)
map.plot()
```
in the same part of the code we use the function rangebearingsensor to measure the distance and the angle between each obstacle and the car .
`sensor=RangeBearingSensor(robot=veh,map=map,animate=True)`

**Defining different functions**:

- Firstly we defined the **obstacle avoidance** `detect_obstacles()` function.This function detects the obstacles in the car’s path using the readings from the sensor and making the car choose the best route for it wheather to the right or to the left according to the angle between the car and the obstacle.If the distance between the car and the obstacle is less than 1.5 and the angle between them is greater than or equal 0 and less than pi/3.6 degrees (*between 0 and pi/3.6*),this means the obstacle is closer to the left side of car, then the robot will avoid the obstacle by moving to the right with a speed of 2 and an angle of pi/2.8 ,else if distance between the car and the obstacle is less than 1.5 and the angle between them is greater than -pi/3.6 degress and less than 0 degrees (*between -pi/3.6 and 0*), this means the obstacle is closer to the right side of the car, then the robot will avoid the obstacle by moving to the left with a speed of 2 and an angle of pi/2.8
```#Function that detects the obstacle near the car and direction that the car will choose
def detect_obstacles(readings):
    for i in readings:
        if i[0]< 1.5 and i[1]<pi/3.6 and i[1]>=0:
            veh.step(2,-pi/2.8) #The robot will avoid the obstacle from the right the direction
            veh._animation.update(veh.x)
            plt.pause(0.005)
        elif i[0]< 1.5 and i[1]>-pi/3.6 and i[1]<0:
            veh.step(2,pi/2.8)   #The robot will avoid the obstacle from the left the direction
            veh._animation.update(veh.x)
            plt.pause(0.005)
            
```
The selected angles are the optimum and are chosen after conducting several tests and trials.

- Second function is the `ON()`. This function moves the car to the target and update the angle between the car and the target .we calculate the angle between the target and the car by using `atan` function.We use the coordinates of the car that keeps changing while it's moving and the coordinates of the target. The car moves to the direction of the calculated angle (*angle to target*) with a speed of 2.
```#Function that moves the car to the target 1 and update angle to goal
def ON():
    goal_heading=atan2(
    (goal[1]-veh.x[1]),(goal[0]-veh.x[0])
    )
    steer = goal_heading-veh.x[2]
    veh.step(2,steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)
```

- Third function is `reach_condtion()`. This function checks if the car has reached the target. If the the difference between x coordinates of the car and the target less than the tolerance and the difference between the y coordinates of the car and the target also less than it. The function will return `True` (*which means the car has reached the target*),else the function will return `False` (*which means the car has not reached the target*)
```#Funtion that checks that the car reached the first target
def reach_condtion():
    if ((abs(goal[0]-veh.x[0])<0.05) or (abs(goal[1] -veh.x[1])<0.05)): #distance between the robot and the target
        return True
    else:
        return False
 ```
- Then we have `ON2()` and `reach_condtion2()` which are the same as `ON()` and `reach_condtion()` but for target 2

## Make use of the defined functions to perform the task:
Firstly we run a while loop for the robot to start functioning, then

if there is two targets. we will check if the robot reached target 1 or not. So when reach_condition is False (*as the robot still didn't move*). We open a while loop and the robot starts moving towards the first target using the `ON()` function and avoiding obstacles using `detect_obstacles()` function. It keeps moving untill it reaches the first target, once its reached the while loop for target 1 will break. Now the reach_condition is True. When its True another while loop will open that will make the robot move to target 2 using the functions ON2() and `detect_obstacles()`. Once target 2 is reached the loop breaks and the robot stops.

While if there is only one target, The robot will move to it using `ON()` function and avoid obstacles using `detect_obstacles` function untill the robot reaches the target, then the loop breaks and the robot stops.

** To sum up if there is two targets the robot will reach target 1 and then go to target 2, and if there is only 1 the car will move till it reaches the target and then stops**

```run=True
run_target1=True
run_target2=True
while(run):
    if Target2=="yes":
        if reach_condtion() is False:
            while (run_target1):
                ON()
                detect_obstacles(sensor.h(veh.x))
                if reach_condtion() is True:
                    run_target1=False
        else:
            while (run_target2):
                ON2()
                detect_obstacles(sensor.h(veh.x))
                if reach_condtion2() is True:
                    run_target2=False
    else:
        ON()
        detect_obstacles(sensor.h(veh.x))
        if reach_condtion() is True:
            run=False
        
plt.pause(1000)
```

  
            
