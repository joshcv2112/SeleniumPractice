# This won't compile, for now
def get_letter(num):
    
    # switch case maybe to find proper letter.
    
    return letter


# {3,5} = E3
# x = 3
# y = 5
# returns 'E3'

def foo(x, y):
    result = ''

    num_letters = y % 26
    temp_y = y
    for i in range(1, num_letters):
        result += get_letter(y - (26 * num_letters))
        temp_y -= 26
    result += get_letter(temp_y)

    return result += str(x)


