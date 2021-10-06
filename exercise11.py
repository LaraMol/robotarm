from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for x in range (9):
    robotArm.moveRight()
positie = 0
while positie < 9:
    robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        positie += 1

    

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()