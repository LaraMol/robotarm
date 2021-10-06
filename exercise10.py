from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
positieHeen = 9
positieTerug = 8
for x in range (5):
    robotArm.grab()
    for x in range (positieHeen):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (positieTerug):
        robotArm.moveLeft()
    positieHeen -= 2
    positieTerug -= 2




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()