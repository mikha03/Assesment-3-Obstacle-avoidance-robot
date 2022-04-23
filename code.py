from roboticstoolbox import Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
Robot_initial=(input("Please enter the robot's start coordinates as x  y: "))
Robot_initial=Robot_initial.split()
Robot_initial_angle=(input("Please enter the robot's initial angle in radians: "))
Target_Coordinates=(input("Please enter the target coordinates as x  y: "))
Target_Coordinates=Target_Coordinates.split()
Num_of_obstacles=(input("Please input number of obstacles: "))

#option input
Target2=(input("Do you want two targets?. please input 'yes' or 'no': "))
if Target2 =="yes":
    Target_Coordinates2=(input("Please enter target 2 coordinates as x  y: "))
    Target_Coordinates2=Target_Coordinates2.split()

#Robot's place and design
anim = VehicleIcon('redcar.png', scale = 2)
veh = Bicycle(
animation = anim,
control = RandomPath,
x0 = (Robot_initial[0],Robot_initial[1],Robot_initial_angle),
)
print(veh.x)
veh.init(plot=True)
veh._animation.update(veh.x)

#Target design and coordinates
goal=[float(Target_Coordinates[0]),float(Target_Coordinates[1])];
goal_marker_style = {
'marker': 'X',
'markersize': 15,
'color': 'b',
}
plt.plot(goal[0],goal[1], **goal_marker_style)

#Target 2 design and coordinates
if Target2=="yes":
    goal2=[float(Target_Coordinates2[0]),float(Target_Coordinates2[1])];
    goal_marker_style = {
    'marker': 'X',
    'markersize': 15,
    'color': 'r',
    }
    plt.plot(goal2[0],goal2[1], **goal_marker_style)


#map and number of obsticles
map=LandmarkMap(int(Num_of_obstacles), 10)
map.plot()
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)

#Function that detects the obstacle near the car and direction that the car will choose to avoid it
def detect_obstacles(readings):
    for i in readings:
        if i[0]< 1.5 and i[1]<pi/3.6 and i[1]>=0:
            veh.step(2,-pi/2.8) #The robot will avoid the obstacle by moving to the right
            veh._animation.update(veh.x)
            plt.pause(0.005)
        elif i[0]< 1.5 and i[1]>-pi/3.6 and i[1]<0:
            veh.step(2,pi/2.8)   #The robot will avoid the obstacle by moving to the left
            veh._animation.update(veh.x)
            plt.pause(0.005)


#Function that moves the car to target 1 and update angle to goal
def ON():
    goal_heading=atan2(
    (goal[1]-veh.x[1]),(goal[0]-veh.x[0])
    )
    steer = goal_heading-veh.x[2]
    veh.step(2,steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)
    
    
#Funtion that checks that the car reached the first target
def reach_condtion():
    if ((abs(goal[0]-veh.x[0])<0.45) and (abs(goal[1] -veh.x[1])<0.45)): #distance between the robot and the target
        return True
    else:
        return False

#Function that moves the car to target 2
def ON2():
        goal_heading2=atan2(
        (goal2[1]-veh.x[1]),(goal2[0]-veh.x[0])
        )
        steer2 = goal_heading2-veh.x[2]
        veh.step(2,steer2)
        veh._animation.update(veh.x)
        plt.pause(0.005)

#Funtion that checks that the car reached the second target
def reach_condtion2():
        if ((abs(goal2[0]-veh.x[0])<0.45) and (abs(goal2[1] -veh.x[1])<0.45)):
            return True


run=True
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
