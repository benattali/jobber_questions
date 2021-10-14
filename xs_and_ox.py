major_x = 5
major_y = 4
minor_x = 3
minor_y = 2


xxxoooxxxoooxxx
xxxoooxxxoooxxx
oooxxxoooxxxooo
oooxxxoooxxxooo
xxxoooxxxoooxxx
xxxoooxxxoooxxx
oooxxxoooxxxooo
oooxxxoooxxxooo


adds_char('x' or 'o'(char), minor_x)
    return char * minor_x

repeat these steps major_y times alternating between 'x' and 'o' as first element
    push 'x' minor_x times followed by 'o' minor_x times for major_x times into a list
    push previous element minor_y times into list

char_list = ['x', 'o']
first_elem = ['x', 'o']
char = char_list[0]
elem = first_elem[0]
do something major_y times
    do something major_x
        adds_char(char, minor_x)                              xxxoooxxxoooxxx
        if char == 'x':
            char = char_list[1]
        else:
            char = char_list[0]
    xxxoooxxxoooxxx * minor_y                                'xxxoooxxxoooxxx', 'xxxoooxxxoooxxx'

    if elem == 'x':
        elem = char_list[1]
    else:
        elem = char_list[0]
