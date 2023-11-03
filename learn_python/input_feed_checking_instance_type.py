import sys
type = sys.argv[1]
if type == "t2.micro":
    print("ok, we will create the free tier(1vCPU/1Gig Mem) instance for you..")
elif type == "t2.large":
    print("ok, we will create 2vCPU/8Gig memory instance for you...")
elif type == "t2.small":
    print("ok, we will create 1vCPU/1Gig memory instance for you..")
else:
    print("ok, please provide valid instance_type...")
