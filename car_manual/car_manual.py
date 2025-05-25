command=""
started=False
while True:
    command=input(">").lower()
    if command=="help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the car''')
    elif command=="start":
        if started:
            print("Car has already started.")
        else:
            started=True
            print("Car has started.")
    elif command=="stop":
        if not started:
            print("Car has already stopped.")
        else:
            started=False
            print("Car has stopped.")
    elif command=="quit":
        print("Car quitted.")
    else:
        print("I don't understand.")
