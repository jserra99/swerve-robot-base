import math
import wpilib
from swerveModule import SwerveModule

# Constant values for the drivetrain
trackWidth = 0.60 # meters
trackLength = 0.70 # meters

class DriveLogic:
    def __init__(self):
        ''' Called when the robot starts up in any mode '''
        # Initializing the swerve modules
        self.frontLeft = SwerveModule(1, 2, 3, 0, "FrontLeft")
        self.frontRight = SwerveModule(4, 5, 6, 0, "FrontRight")
        self.rearLeft = SwerveModule(7, 8, 9, 0, "RearLeft")
        self.rearRight = SwerveModule(10, 11, 12, 0, "RearRight")