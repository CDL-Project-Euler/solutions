# def main():
#     sol_sum = 0
#     with open('sudoku.txt') as f:
#         for i in range(50):
#             puzzle = []
#             for j in range(9): 
#                 puzzle.append([int(x) for x in f.readline().split()])
#             sol_sum += sum(solve_sudoku(puzzle)[0][:3])
#     print(sol_sum)

def solve_sudoku(puzzle: list) -> list:
    # Solves sudoku puzzle


print(solve_sudoku)