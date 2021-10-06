from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for i in range (7):
    robotArm.moveright()
    robotArm.grab()
    robotArm.left()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()