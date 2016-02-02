import os

filename = "testfile"

try:
    os.mkfifo(filename)
except RuntimeError as err:
    print("Failed to create FIFO: %s" % err)
else:
    fifo = open(filename, 'w')
    # write stuff to fifo
    print >> fifo, "hello"
    fifo.close()
    os.remove(filename)

