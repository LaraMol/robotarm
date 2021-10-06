from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for x in range (4):
    for x in range(4):
        robotArm.grab()
        for x in range(4):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (4):
            robotArm.moveLeft()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()