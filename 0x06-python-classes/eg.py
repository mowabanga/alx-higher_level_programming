class Robot:
    """Represents a robot with a name.
    """
    population = 0 #a class variabble
    
    def __init__(self, name):
        """initializes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))
        
        # when this person is created
        # the robot adds to the population
        Robot.population += 1
        
    def die(self):
        """I am dying
        """
        print("{} is being destroyed!".format(self.name))
        
        Robot.population -= 1
        
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))
            
    def say_hi(self):
        """Greeting by the robot
        """
        print("Greetings, my masters call me {}".format(self.name))
        
    @classmethod
    def how_many(cls):
        """Print the current population
        """
        print("We have {:d} robots".format(cls.population))


rob1 = Robot("R2-D2")
rob1.say_hi()
Robot.how_many()

rob2 = Robot("C-3PO")
rob2.say_hi()
Robot.how_many()
rob1.die()
rob2.die()