import cmd
import threading
import enum
# create lock between two thread
lock = threading.Lock()

# create some variable for check between two thread
log_ok_check = "" # send from process_TC thread to handle_log thread about log_ok
log_error_check = "" # send from process_TC thread to handle_log thread about log_error
result = 0  # send from handle_log thread to process_TC thread about result of each step in test case. 
            # It also use as flag of 2 thread to accquire lock
            
    