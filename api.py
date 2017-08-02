class SendingAPI(object):
    def testing(self):
        return "Testing"

import zerorpc

s = zerorpc.Server(SendingAPI())
s.bind("tcp://0.0.0.0:4242")
print("Sending Data")
s.run()