import sys
import csv

# Function to open&read file and skip the first line
def open_file(file_name):
    try:
        file = open('speech.csv')
        # Open() method is used to open file and return a file object
        print ("Opened file " + file_name + " successfully" )  
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])
    return file

def close_file(file):
    try:
        file.close()
        print ("Closed file successfully") 
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])

def skip_head_line(file):
    # Use csv.reader object to read the CSV file
    csvreader = csv.reader(file)
    #move the first line - title line
    next(csvreader)
    return csvreader
