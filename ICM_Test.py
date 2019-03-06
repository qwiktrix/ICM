from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
filename = "inputs.txt"


def type_cmd(entry):
    keyboard.type(entry)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def setup():
    time.sleep(2)
    #switch to console
    type_cmd("connect")

def run_chess_move(filename):
    with open(filename, "r+") as f:
        lines = [line.rstrip('\n') for line in f]
        time.sleep(2)
        
        for line in lines:
            type_cmd(line)
            if (line[0:4] == 'M340'):
                time.sleep(5)
            elif (line[4:6] == 'X:'):
                #Need to input longest time to move motors, based off of testing
                time.sleep(10)
            elif (line[4:6] == 'Z:'):
                #Same as above need to change sleep time for full
                #movement ofZ movement
                time.sleep(30)
        f.write("")
    
setup()
run_chess_move(filename)
