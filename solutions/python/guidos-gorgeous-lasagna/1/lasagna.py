"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    bake_time_remaining(10)


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(layer):
    """Calculate the time to prepare the lasagna.

    Parameters:
        layer (int): The number of lasagna sheets.

    Returns:
        int: How long it takes to prepare the lasagna based on the amount of sheets.

    Function that takes total amount of sheets and the preparation time for each sheet and performs an arithmetic operation to get the total prep time.
    """
    return layer * PREPARATION_TIME
preparation_time_in_minutes(5)


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total time currently elapsed.

    Parameters:
        layer (int): The number of lasagna sheets
        elapsed_bake_time (int): The time already taken by the lasagna in the oven

    Returns:
        int: How long time has passed since the commencement of the entire cooking and preparation process.

    Function that takes total amount of sheets and the time the lasagna has taken in the oven and calculates the preparation time before summing up the peparation time and elapsed bake time to get the total time elapsed.
    """
    elapsed_time = preparation_time_in_minutes(layers)
    return elapsed_time + elapsed_bake_time
    elapsed_time_in_minutes(1,2)
    
# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
