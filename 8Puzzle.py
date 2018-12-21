import random
import string

# define class puzzle to save 8Puzzle Problem data to solve it with our algorithm later
class Puzzle:

    def __init__(self):
        # set initial state as Global State

        # define 2D array type --> 3*3
        self.Point_number = [ [ None for j in range(3) ] for i in range(3) ]
        self.Point_number[0][0]=1;
        self.Point_number[0][1]=2;
        self.Point_number[0][2]=0;          # initiate Goal_State
        self.Point_number[1][0]=7;
        self.Point_number[1][1]=8;
        self.Point_number[1][2]=3;
        self.Point_number[2][0]=6;
        self.Point_number[2][1]=5;
        self.Point_number[2][2]=4;

        self.current_Point=(0,2)        # current_Point --> empty slot in the puzzle
        if True:
            print("All Done!")

    def moveRight(self):               # empty slot --> move Right
        (col,row)=self.current_Point

        if not col==2:

            self.Point_number[col][row]=self.Point_number[col+1][row]
            self.Point_number[col+1][row]=0
            self.current_Point=(col+1,row)
            return 1               # successfuly moved
        if col==2:
            return 0                # move failed


    def moveLeft(self):                 # empty slot --> move Left
        (col,row)=self.current_Point
        if not col==0:
            self.Point_number[col][row]=self.Point_number[col-1][row]
            self.Point_number[col-1][row]=0
            self.current_Point=(col-1,row)
            return 1            # successfuly moved
        if col==0:
            return 0    # move failed



    def moveUp(self):                  # empty slot -->move up
        (col,row)=self.current_Point
        if not row==0:
            self.Point_number[col][row]=self.Point_number[col][row-1]
            self.Point_number[col][row-1]=0
            self.current_Point=(col,row-1)
            return 1         # successfuly moved
        if row==0:
            return 0        # move failed


    def moveDown(self):              # empty slot -->move down
        (col,row)=self.current_Point
        if not row==2:
            self.Point_number[col][row]=self.Point_number[col][row+1]
            self.Point_number[col][row+1]=0
            self.current_Point=(col,row+1)
            return 1            # successfuly moved
        if row==2:
            return 0        # move failed





    def move (self,dir):        #  moving the empty slot...
        if dir == 'u':
            return self.moveUp()
        if dir == 'd':
            return self.moveDown()
        if dir == 'l':
            return self.moveLeft()
        if dir == 'r':
            return self.moveRight()

    def scramble(self,level):
        for i in range(level):
            while not self.move(random.choice('udlr')):          # if returns false
                pass;

    def show(self):         # show the current state of the problem
        print(self.Point_number[0])
        print(self.Point_number[1])
        print(self.Point_number[2])

    def isSolved(self):
        if not self.Point_number[0][0]==1:
            return 0;
        if not self.Point_number[0][1]==2:
            return 0;
        if not self.Point_number[0][2]==0:          # initiate Goal_State
            return 0;
        if not self.Point_number[1][0]==7:
            return 0;
        if not self.Point_number[1][1]==8:
            return 0;
        if not self.Point_number[1][2]==3:
            return 0;
        if not self.Point_number[2][0]==6:
            return 0;
        if not self.Point_number[2][1]==5:
            return 0;
        if not self.Point_number[2][2]==4:
            return 0;
        return 1;

# testing class methods
a=Puzzle()
a.show()
print a.isSolved()
a.scramble(10)
a.show()
print a.isSolved()
a.show()
print a.isSolved()
a.scramble(20)
a.show()
