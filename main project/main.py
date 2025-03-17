#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase # We will not be using any sensors for this project.

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# The main code.
ev3.speaker.beep() # Signal start

robot.straight(525) # On the way to pick up the blocks.
robot.turn(90)
robot.straight(600) # The robot should've picked up the red block while performing this action.
robot.turn(90)
robot.straight(500) # The robot should've picked up the yellow block while performing this action.
robot.turn(100) # Turn a bit more than before to avoid hitting the unwanted blocks.
robot.straight(580) # Going back to base.
robot.straight(-70) # The robot will go backwards by a bit to leave the blocks in the box without further interruptions

# Celebration (not necessary)
ev3.speaker.beep() # Signal end
ev3.speaker.say("Mission completed successfully")
ev3.turn(1080) # The robot will spin 3 times to celebrate success