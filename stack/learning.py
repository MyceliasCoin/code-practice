import queue

# from class queue, Queue is created as an object
# now L is a Queue of maximum size 20
L = queue.Queue(maxsize=20)

# data is inserted into Queue using put()
# data is inserted at the end
L.put(5)
L.put(9)
L.put(1)
L.put(7)

# get() takes data from head of Queue (FIFO)
# get() removes and returns element
print(L.get())
print(L.get())
print(L.get())
print(L.get())

# note that attempting to add data into a Queue above maxsize results in Overflow
# and attempting to remove an element from an empty Queue is called Underflow
# put() and get() do not return error upon Overflow and Underflow, but goes into infinite loop
