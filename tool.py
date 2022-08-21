from concurrent.futures import thread
import threading
import handle_testcase
import handle_log

# creating thread 
t1 = threading.Thread(target=handle_testcase.handle_testcase)
t2 = threading.Thread(target=handle_log.handle_log)

# starting thread 1
t1.start()
# starting thread 2
t2.start()

#wait until thread 1 is completely excuted
t1.join()
#wait until thread 2 is completely excuted
t2.join()