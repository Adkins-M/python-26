EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """   
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers):
    """
    This function calculates how long it takes to prepare a specific number
    of layers of lasagna by multiplying by the constant TIME_PER_LAYER 
    and returns the time taken to do preparation
    """
    prep_time = number_of_layers * TIME_PER_LAYER
    return prep_time
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This function takes calls the calculates the total time it took to 
    prepare and bake the lasagna. By calling the preparation time function, 
    we avoid repetition of calculating the preparation time
    already defined in the funtion preparation_time_in_minutes
    """
    total_time_in_kitchen = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_time_in_kitchen

bake_time_remaining(30)
preparation_time_in_minutes(2)
elapsed_time_in_minutes(3, 20)