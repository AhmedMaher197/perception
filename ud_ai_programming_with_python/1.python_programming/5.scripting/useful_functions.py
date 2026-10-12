num_useful_func = 10
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

# if __name__ == '__main__': is a Python idiom that checks if      
# the script is being run directly (as the main program) rather than        
# being imported as a module.
# When Python runs a file, it sets the special variable __name__ to
# '__main__' if that file is the entry point. If the file is imported       
# by another script, __name__ is set to the module's name instead
if __name__ == '__main__':
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)
    
    
    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)
    
    print("All tests passed!")