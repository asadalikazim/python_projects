""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    # Complete this function
    if player_one_turn:
        return P1
    return P2


def get_winner(player_one_score: int, player_two_score: int) -> str:
    """Return 'player one wins' if player_one_score > player_two_score;
    return 'player two wins' if player_one_score < player_two_score;
    return 'tie game' if player_one_score == player_two_score
    
    Preconditio: both variables must be greater than or equal to 0
    
    >>>get_winner(100,50)
    'player one wins'
    >>>get_winner(50,100)
    'player two wins'
    >>>get_winner(50,50)
    'tie game'
    """
    
    if player_one_score > player_two_score:
        return P1_WINS
    elif player_one_score < player_two_score:
        return P2_WINS
    return TIE


def reverse(to_be_reversed: str) -> str:
    """Return a reverse string of to_be_reversed
    
    >>>reverse('abc')
    'cba'
    """
    
    return to_be_reversed[::-1]


def get_row(puzzle: str, row_num: int) -> str:
    """Returns row row_num from puzzle.
    Note that rows are numbered starting form zero (0)
    
    Precondition: 0 <= row_num < number of rows in puzzle
    
    >>>get_row('abcd\nefgh\nijkl\n' , 1)
    'efgh'
    """
    
    row_len = get_row_length(puzzle)
    num_of_char_to_skip = (row_len + 1) * row_num
    
    
    return puzzle[num_of_char_to_skip: num_of_char_to_skip + row_len]


def get_factor(direction: str) -> int:
    """Return the multiplication factor associated with direction.
    
    Precondition: direction must be equal to DOWN or UP or FORWARD or BACKWARD
    
    >>>get_factor('up')
    4
    >>>get_factor('down')
    2
    """
    
    if direction == UP:
        return UP_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR
    elif direction == FORWARD:
        return FORWARD_FACTOR
    return BACKWARD_FACTOR


def get_points(direction: str, words_left: int) -> int:
    """Returns the number of points scored depending on the direction
    the word has been found in, the words_left before the word was found,
    and the threshold, and also considering the bonus points
    for guessing the last word.
    
    Precondition: words_left must be greater than 1 
                  direction must be equal to DOWN or UP or FORWARD or BACKWARD
    
    >>>get_points('backward' , 5)
    15
    >>>get_points ('backward' , 2)
    24
    >>>get_points('backward' , 1)
    39
    """
    
    factor = get_factor(direction)
        
    if words_left >= THRESHOLD:
        return THRESHOLD * factor
    elif words_left > 1:
        return (2 * THRESHOLD - words_left) * factor
    return (2 * THRESHOLD - words_left) * factor + BONUS


def check_guess(puzzle: str, direction: str, guess: str, row_or_col: int, 
                words_left: int) -> int:
    """Return points scored if the guess is found in the direction in the 
    row_or_col in the puzzle. Else return zero (0)
    
    Precondition: direction must be equal to DOWN or UP or FORWARD or BACKWARD

    >>>check_guess('abcdef', 'forward', 'cde', 0, 10)
    10
    >>>check_guess('abcdef', 'forward', 'ced', 0, 10)
    0
    """
    
    if direction == FORWARD:
        row = get_row(puzzle, row_or_col)
        if contains(row, guess):
            return get_points(direction, words_left)
        return 0
    
    if direction == BACKWARD:
        row = reverse(get_row(puzzle, row_or_col))
        if contains(row, guess):
            return get_points(direction, words_left)
        return 0
    
    if direction == DOWN:
        col = get_column(puzzle, row_or_col)
        if contains(col, guess):
            return get_points(direction, words_left)
        return 0
    
    if direction == UP:
        col = reverse(get_column(puzzle, row_or_col))
        if contains(col, guess):
            return get_points(direction, words_left)
        return 0
    
    return None