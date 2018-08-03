# COMP1730/6730 Homework 1. Semester 2, 2018.
# Submission is due 9am, Monday the 6th of August, 2018.

## YOUR ANU ID: uNNNNNNN
## YOUR NAME:

import robot

## Functions to move right and left by two spaces.
def right_two_spaces():
    robot.drive_right()
    robot.drive_right()

def left_two_spaces(): #name of this function was wrong by added an extra "_ß"
    robot.drive_left()
    robot.drive_left()

## Perform an unstacking manoeuvre.
## Assumption: At the start of the manoeuvre, the robot (gripper) is
## in front of the stack, at the base of the stack, and the gripper
## is folded back.
def unstack_to_the_left():
    # Step 1: Grasp the next block above the base.
    grasp_blocks_above()
    # Step 2: Move to the left.
    left_two_spaces()
    # Step 3: put down the block(s) we're holding, and re-position
    # the gripper so that we can repeat the manoeuvre in front of
    # the blocks that were put down.
    put_down_blocks()

## Raise gripper and grasp the block one level up.
## Assumption: Gripper is folded and lift is at base level.
def grasp_blocks_above():
    #the order was wrong
    #it should lift up first and then open the gripper
    robot.lift_up()
    robot.gripper_to_open()
    robot.gripper_to_closed()

## Put down the blocks we're holding, and position gripper to
## repeat the unstacking manoeuvre.
## Assumption: The gripper is one level up, holding one or more blocks.
def put_down_blocks():
    # Move the lift down, and release the blocks.
    robot.lift_down()
    robot.gripper_to_open()
    # Because there is now a block to the right (the one that we
    # unstacked from), we must do the up-fold-down manoeuvre.
    robot.lift_up()
    robot.gripper_to_folded()
    robot.lift_down()

## Unstack a tower of two blocks.
## Assumption: The robot starts in front of the left position, and
## the tower to be unstacked is in the middle.
def unstack_tower_of_two():
    # Move to the middle
    right_two_spaces()
    # and do the unstacking manoeuvre
    unstack_to_the_left()

## Unstack a tower of three blocks.
## Assumption: The robot starts in front of the left position, and
## the tower to be unstacked is in the right-most position (so that
## there is enough space to the left of it to unstack it).
def unstack_tower_of_three():
    # Move to the right-most stack
    right_two_spaces()
    right_two_spaces()
    # and do the unstacking manoeuvre twice
    unstack_to_the_left()
    unstack_to_the_left()
    
def test_unstack_two():
    # Set up a simulation with a tower of two boxes in the middle:
    robot.init(pos = 0, boxes = [[], [], ["red", "green"], [], []])
    # Test the unstacking-of-two function:
    unstack_tower_of_two()

def test_unstack_three():
    # Set up a simulation with a tower of three boxes to the right
    robot.init(pos = 0, boxes = [[], [], [], [], ["red", "green", "blue"]])
    # Test the unstacking-of-three function:
    unstack_tower_of_three()
