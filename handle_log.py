import ctypes
from ipaddress import ip_address
import time
from dlt import dlt, dlt_broker

from dlt.helpers import bytes_to_str

def handle_log():
    broker = dlt_broker.DLTBroker(ip_address="10.220.50.114", port=3500, filename='/home/thu/dlt/python-dlt/log/testing_log.dlt')
    broker.start()
