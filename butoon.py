def button():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btn,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
      input_state==False:
          return 1 #button is pressed
if button()==1 and GPIO.stby==False: #or whatever motor uses to stop
    try: #the actual running of the function
