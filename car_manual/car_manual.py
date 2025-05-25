command=""
while True:
    command=input(">").lower()
    if command=="help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the car''')
    elif command=="start":
        print("Car has started.")
    elif command=="stop":
        print("Car has stopped.")
    elif command=="quit":
        print("Car quitted.")
    else:
        print("I don't understand.")
