import argparse
ap=argparse.ArgumentParser(description="This is the Calculator")

ap.add_argument("x",type=int,help="Enter an integer")
ap.add_argument("y",type=int,help="Enter an integer")
ap.add_argument("op",type=str,help="Enter an operator(+ , - , * , /)")

args=ap.parse_args()

if args.op=="+":
    print(f"The sum of the integers is {args.x + args.y}.")
elif args.op=="-":
    print(f"The difference of the integers is {args.x - args.y}.")
elif args.op=="*":
    print(f"The multiplication of the integers is {args.x * args.y}.")
elif args.op=="/":
    print(f"The division of the integers results {args.x / args.y}.") 
else:
    print("Something went wrong")
