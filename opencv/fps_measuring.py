import time

fps = 5
time_delta = 1./fps

t0 = time.clock()
while True:
    time.sleep(1)
    t1 = time.clock()
    print(t0, t1, t1 - t0, (int)((t1 - t0) * 10000), time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))