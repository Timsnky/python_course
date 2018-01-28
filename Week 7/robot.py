import math
import random

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width=width
        self.height=height
        self.clean={}
        for i in range(self.width):
            for j in range(self.height):
                self.clean[(i,j)]=False
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.x=math.floor(pos.getX())
        self.y=math.floor(pos.getY())
        self.clean[(self.x,self.y)]=True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.clean[(m,n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleantiles=0
        for i in self.clean.keys():
            if self.clean[i]==True:
                cleantiles+=1
        return cleantiles          
                       

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x=random.random()*self.width
        y=random.random()*self.height
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        self.x=math.floor(pos.getX())
        self.y=math.floor(pos.getY())
        if (self.x,self.y) in self.clean.keys():
            return True
        else:
            return False

    def __str__(self):
        return str('<'+str(self.width)+','+str(self.height)+'>')


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.x=[]
        self.y=[]
        self.room=room
        self.speed=speed
        self.direction=random.choice(range(360))
        self.position=self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
           
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position=position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction=direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.x.append(round(self.position.getX(),2))
        self.y.append(round(self.position.getY(),2))
        self.room.cleanTileAtPosition(self.position)
        self.Next=self.position.getNewPosition(self.direction,self.speed)
        if self.room.isPositionInRoom(self.Next)!=True:
            self.direction=random.choice(range(360))
            self.position=self.position
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction=self.direction
            self.position=self.Next
            self.room.cleanTileAtPosition(self.position)
        self.room.cleanTileAtPosition(self.position)
        self.setRobotPosition(self.position)
        self.setRobotDirection(self.direction)
        return (self.direction,self.position)
                    
    def __str__(self):
        return '('+str(self.position)+','+str(self.direction)+','+str(self.room.getNumCleanedTiles())+')'

class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        self.Next=self.position.getNewPosition(self.direction,self.speed)
        if self.room.isPositionInRoom(self.Next)!=True:
            self.direction=random.choice(range(360))
            self.position=self.position
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction=self.direction
            self.position=self.Next
        self.setRobotPosition(self.position)
        self.setRobotDirection(self.direction)
        return (self.direction,self.position)

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        self.Next=self.position.getNewPosition(self.direction,self.speed)
        if self.room.isPositionInRoom(self.Next)!=True:
            self.direction=random.choice(range(360))
            self.position=self.position
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction=random.choice(range(360))
            self.position=self.Next
            self.room.cleanTileAtPosition(self.position)
        self.setRobotPosition(self.position)
        self.setRobotDirection(self.direction)
        return (self.direction,self.position)

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    timesteps1=0.0
    for i in range(num_trials):
        timesteps=0.0
        r=robot_type(RectangularRoom(width,height),speed)
        while r.room.getNumCleanedTiles()< (min_coverage*r.room.getNumTiles()):
            for e in range(num_robots):
                       r.updatePositionAndClean()
                       timesteps+=1
        timesteps1+=timesteps
    return (timesteps1/num_trials)
            
            
num_robots=2
speed=1.0
width=8
height=8
min_coverage=0.8
num_trials=30
robot_type=StandardRobot

c=runSimulation(num_robots, speed, width, height, min_coverage, num_trials,robot_type)
print c    




