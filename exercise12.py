from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
positie = 1
totaalposities = 10 

loop1 = 0
while loop1 <= 8:
    robotArm.grab()
    color = robotArm.scan()
    hoever = totaalposities - positie 
    hoeverTerug = hoever - 1
    if color == "red":
        for x in range(hoever):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(hoeverTerug):
            robotArm.moveLeft()
        positie += 1
        hoeverTerug -= 1
    else:
        robotArm.drop()
        robotArm.moveRight()
        positie = positie + 1
    loop1 += 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()