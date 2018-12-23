import random
import string
class Queens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self):
         # Store the puzzle (problem) size and the number of valid solutions
         self.size = 8
         self.solutions = 0
         self.solve()
    def put_queen(self, Queen_positions, target_row):
         """
         Try to place a queen on target_row by checking all N possible cases.
         If a valid place is found the function calls itself trying to place a queen
         on the next row until all N queens are placed on the NxN board.
         """
         # Base (stop) case - all N rows are used
         if target_row == 8:
             self.show_full_board(Queen_positions)
             # self.show_short_board(Queen_positions)
             self.solutions += 1
         else:
             # For all N columns positions try to place a queen
             for column in range(8):
                 # Reject all invalid positions
                 if self.check_place(Queen_positions, target_row, column):
                     Queen_positions[target_row] = column
                     self.put_queen(Queen_positions, target_row + 1)

    def solve(self):
         """Solve the n queens puzzle and print the number of solutions"""
         Queen_positions = [-1] * 8
         self.put_queen(Queen_positions, 0)
         print("Found", self.solutions, "solutions.")



    def check_place(self, Queen_positions, used_rows, column):
         """
         Check if a given position is under attack from any of
         the previously placed queens (check column and diagonal positions)
         """
         for i in range(used_rows):
             if Queen_positions[i] == column or \
                 Queen_positions[i] - i == column - used_rows or \
                 Queen_positions[i] + i == column + used_rows:

                 return False
         return True

    def show_full_board(self, Queen_positions):
         """Show the full NxN board"""
         for row in range(8):
             line = ""
             for column in range(8):
                 if Queen_positions[row] == column:
                     line += "# "
                 else:
                     line += "! "
             print(line)
         print("\n")

    def show_short_board(self, Queen_positions):
         """
         Show the queens positions on the board in compressed form,
         each number represent the occupied column position in the corresponding row.
         """
         line = ""
         for i in range(8):
             line += str(Queen_positions[i]) + " "
         print(line)


def main():

   Queens(8)
if __name__ == "__main__":
     # execute only in script
     main()
