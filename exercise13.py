from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
amountmoved = 0

while True:
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        amountmoved += 1
        for x in range (amountmoved):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (amountmoved):
            robotArm.moveLeft()


    else:
        break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()