# a = ["ade", "sania", "sherlyn"]

# def printLst(value):
#     for x in value:
#         print(x)

# printLst(a)

# class Lift: def __init__(self, lantai, bebanMaksimum):
#     self.lantai = lantai 
#     self.bebanMaksimum = bebanMaksimum 

#     def goDown(self): 
#         if (self.lantai > 0): 
#             self.lantai = self.lantai - 1 
#         else: 
#             print('Elevator is already at the bottom') 
            
#     def goUp(self):
#         self.lantai = self.lantai + 1 

# class move:
#     def __init__(self, name)

class lift:
    def __init__(self, weight, destinationFloor, startingFloor , maxFloor = 20, maxWeight = 5):
        self.startingFloor = startingFloor
        self.weight = weight
        self.destinationFloor = destinationFloor
        self.maxFloor = maxFloor
        self.maxWeight = maxWeight

    def door(self):
        if self.weight >= self.maxWeight:
            print("Overload")
            return False
        else:
            return True
        
    def move(self):
        if (self.destinationFloor <= self.maxFloor):
            while self.startingFloor != self.destinationFloor:
                if self.startingFloor > self.destinationFloor:
                    self.startingFloor -= 1
                    print("Go to {} floor".format(self.startingFloor))
                elif self.startingFloor < self.destinationFloor:
                    self.startingFloor += 1
                    print("Go to {} floor".format(self.startingFloor))

            print("you already arrive in floor {}".format(self.startingFloor))
        else:
            print("out of range")

    def start(self):
        door = lift.door(self)

        if door == True:
            move = lift.move(self)
        else:
            pass

print("1, Max floor = 20 floor")
print("2, Max person = 5 floor")

current = int(input("Input current floor : "))
destination = int(input("Input your destination floor : "))
weight = int(input("Person in lift : "))

x = lift(weight, destination, current)
x.start()
