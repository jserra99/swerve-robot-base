import wpilib
import driveLogic

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        self.DriveLogic = driveLogic.DriveLogic()
        