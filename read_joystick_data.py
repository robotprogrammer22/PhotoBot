# will send a bluetooth command to end the connection
connected = True
# will need to shutdown the robot when done somehow
    # ssh:  sudo shutdown now
    # will need to also end the livestream
        # just do this with ssh????

def read_joystick_data():
    print("data")
    # return direction command to function controlling robot movement
    # will need to break apart the string data coming through bluetooth
    # either send from android as string, or array
    # string will be easier to deal with, since you can just split on "," and get rid of spaces
    # take string, convert to int if needed
    # place both values into a list (first element = left, second = right) and send
    
    example_data_string = "0.75, -0.75"
    # splits on "," to separate the two commands
    split_string = example_data_string.split(", ")
    return split_string
    
    
def move_robot():
    # will need a way to get sensitivity of joystick and round

    # command list will have 2 elements, the left motor power, and the right motor power
    # negative = reverse
    # positive = forward
    # 0 = no movement
    commands = read_joystick_data()
    # look at all elements
    left_motor_power = commands[0]
    right_motor_power = commands[1]
    # value of 0 = none, 1 means forward, value of 2 is reverse
    left_direction = 1
    right_direction = 1
    
    # if the value is negative, it is reverse
    if left_motor_power < 0:
        left_direction = 2
    if right_motor_power < 0:
        right_direction = 2
    
    # don't call motor movement function if both values are 0
    if left_motor_command == 0 and right_motor_command == 0:
        return
    else:
        # left motors are first two variables, right the second two
        run_raw_motors(left_forward, abs(left_motor_power), right_forward, abs(right_motor_power))

while connected:
    move_robot()
    # sleep, so every 0.2 seconds, it will be scanning again for input
    time.sleep(0.2)