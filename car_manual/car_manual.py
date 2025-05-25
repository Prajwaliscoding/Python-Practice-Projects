command=""
while True:
    command=input(">")
    if command.lower()=="help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the car''')
    elif command.lower()=="start":
        print("Car has started.")
    elif command.lower()=="stop":
        print("Car has stopped.")
    elif command.lower()=="quit":
        print("Car quitted.")
    else:
        print("I don't understand.")
