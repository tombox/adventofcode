"""
https://adventofcode.com/2021/day/4
"""
import numpy as np
from nptyping import NDArray, Int

def load_data(filename: str) -> tuple:
    " Load bingo data "
    lines = open(filename, "r").read().splitlines()
    draws = [int(x) for x in lines[0].split(',')]
    total_boards = (len(lines)-1) // 6
    boards = []
    for board_id in range(total_boards):
        board = []
        for row in range(5):
            board += [(int(x)) for x in lines[board_id*6+row+2].split()]
        np_board = np.array(board)
        np_board.resize(5,5)
        boards.append(np_board)

    return draws, boards


def check_wins(board: NDArray[Int]) -> int:
    return -5 in board.sum(axis=0) or -5 in board.sum(axis=1)

def mark_board(board: NDArray[Int], draw: int) -> None:
    board[board == draw] = -1

def score_board(board: NDArray[Int]) -> int:
    board[board <0] = 0
    return board.sum()

def part1(file: str) -> int:
    " Day 04 puzzle part 1"
    draws,boards  = load_data(file)   

    for draw in draws:
        for board in boards:
            mark_board(board, draw)

        for board in boards:
            if check_wins(board):
                return score_board(board)*draw
    
    return 0


def part2(file: str) -> int:
    " Day 04 puzzle part 2"
    draws,boards  = load_data(file)

    for draw in draws:
        for board in boards:
            mark_board(board, draw)

        for board in boards:
            if check_wins(board):
                score = score_board(board)*draw
                board[board >=-1] = -2
    return score


def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 4512

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 71708

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 1924

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 34726

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
