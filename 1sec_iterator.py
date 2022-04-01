import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_every_sec(sc): 
    
    ## do your stuff
    # Append new coordinates to the list.
    # Calculate Average, mode (most appeared)
    
    
    
    
    #Recursive. Calling its own func again.
    s.enter(60, 1, do_every_sec, (sc,))

s.enter(60, 1, do_every_sec, (s,))


#Run by uncommenting
#s.run()