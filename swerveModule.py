import math
import wpilib
import ctre

countsPerRevolution = 2048 # encoder counts per revolution
turningingGearRatio = 12.8 # gear ratio for turning the wheels
drivingGearRatio = 8.14 # gear ratio for driving the wheels

class SwerveModule:
    def __init__(self, driveCAN, turnCAN, absoluteCAN, absoluteOffset, moduleName):
        self.absoluteOffset = -absoluteOffset
        self.driveMotor = ctre.TalonFX(driveCAN)
        self.turnMotor = ctre.TalonFX(turnCAN)
        self.absoluteEncoder = ctre.CANCoder(absoluteCAN)
        self.absoluteEncoder.configSensorInitializationStrategy(ctre.SensorInitializationStrategy.BootToAbsolutePosition)
        self.absoluteEncoder.configAbsoluteSensorRange(ctre.AbsoluteSensorRange.Signed_PlusMinus180)
        self.absoluteEncoder.configMagnetOffset(self.absoluteOffset)