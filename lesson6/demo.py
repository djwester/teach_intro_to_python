
def walk(nSteps):
    for i in range(nSteps * 2):
        print("left foot")
        print("right foot")

def goDownStairs():
    print("go down some stairs")    

def goAroundStairLanding():
    print("turn left")
    walk(2)
    print("turn left")

def nStepsToRunFromWalk(nWalkingSteps):
    return nWalkingSteps / 3

# print("walk to end of hall")
# walk(5)
# goDownStairs()
# goAroundStairLanding()
# goDownStairs()
# walk(4)
# print("tada")

v = nStepsToRunFromWalk(12)
print(v)
