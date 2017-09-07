from detect.new.old.py import*
def test():

    right()
    #time.sleep(2)

    left()
    time.sleep(5)

    runall()
    #time.sleep(2)
    stop()
    

if __name__==("__main__"):
    setup()
    setupMotor()    
test()
