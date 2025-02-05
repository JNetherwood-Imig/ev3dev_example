#! /usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

from laser_sensor import LaserSensor

ev3 = EV3Brick() # Create EV3 brick object
left_motor = Motor(Port.A) # Create left motor with port a
right_motor = Motor(Port.B) # Create right motor with port b

# Create a drivebase using the motors
# The drivebase is used for precise control of the robot when driving
# The last two numbers are important to have correct
# If these numbers are not correct, the robot will not drive correctly
drivebase = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# Configures default drivebase settings
# Increase or decrease values as you see fit for your program
drivebase.settings(straight_speed=500, straight_acceleration=800, turn_rate=300, turn_acceleration=800)

# Create a distance sensor object
dist_sensor = LaserSensor(Port.S1)

# Quick example usage of the distance sensor
def test_distance_sensor():
    print("Current distance is " + dist_sensor.get_distance() + " millimeters.")
    ev3.speaker.beep()

# Quick example usage of the drivebase which drives forward 1000 mm, turns around, then comes back
def test_drivebase():
    drivebase.straight(1000)
    drivebase.turn(180)
    drivebase.straight(1000)

# Main code of the program, which will be run when you press start
# Write your additional code in here
def main():
    print("Program is running...")
    test_distance_sensor()
    test_drivebase()

# Don't worry about this, it just runs the program
if __name__ == "__main__":
    main()
