
import csv
import enum
from msilib.schema import Condition
import time
import handle_file
import play_tts
import send_cmd
        
# Parse to define columns
def parse(row):
    tc_no = row[0]
    step_no = row[1]
    type_data = row[2]
    action_data = row[3]
    timeout_no = int(row[4])
    log_ok = row[5]
    log_error = row [6]
    return tc_no, step_no, type_data, action_data, timeout_no, log_ok, log_error

def handle_step(row):
    tc_no, step_no, type_data, action_data, timeout_no, log_ok, log_error = parse(row)
    if(type_data == "tts"):
        print(action_data)
        play_tts.speak(action_data)
    elif (type_data == "touch"):
        x = int(action_data.split(',')[0])
        y = int(action_data.split(',')[1])
        print("x: " + str(x) +  " y: " + str(y))
        try:
            send_cmd.send_touch(x,y)
        except:
            print("An exception occured when failed connection")
            
# Process test case
def handle_testcase(csvreader):
    for row in csvreader:
        if (row[2] != 'type'):
            handle_step(row)
    
    
def handle_csv():
    file = handle_file.open_file('speech1.csv')
    csvreader = handle_file.skip_head_line(file)    
    handle_testcase(csvreader)
    handle_file.close_file(file)
    