#
#   Binds REP socket to tcp://*:5555
#   Expects data from sendData.py, appends and plots
#

import time
import zmq
import matplotlib.pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

array = []

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #Convert data back to int
    data = [int(message)]

    #Append new data
    array.extend(data)
	#clears the figure
    #plt.clf()
    plt.plot(array, 'ro')
    plt.show()

    socket.send_string("Data received and plotted")
