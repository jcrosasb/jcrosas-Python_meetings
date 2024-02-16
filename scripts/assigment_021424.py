# def stars_pattern(num_lines):
#     for i in range(1, num_lines + 1):
#         print(' '*(num_lines-i) + '*'*(2*i-1))

# def diamond_pattern2(size):
#     for i in range(size//2 + 1):
#         print(' '*(size//2 - i) + '*')



def pyramid_pattern(num_floors):
    '''Function to print a star pyramid.
       For a given num_floors (number of floors), the function will print num_floors lines, 
       each one consisting of a string with a width of 2 * num_floors - 1. The number of 
       stars for each line also increases in odd numbers (i.e 1, 3, 5, ..., (2*num_floors - 1))
       Parameters:
            num_floors: the number of floors the pyramid will have.'''
    line_width = 2 * num_floors - 1  # Width of each line
    for i in range(1, num_floors + 1):
        stars = '*' * (2*i - 1)  # The number of stars in each floor of the pyramid will be an odd number   
        print('{:^{}}'.format(stars, line_width))  # The stars are centered (^) in the line 

#star_pyramid(15)


def diamond_pattern(size):
    for i in range(size//2 + 1):
        if i == 0:
            print('{:>{}}'.format('*', (size//2 + 1) - i))
        else:
            print('{:>{}}'.format('*', (size//2 + 1) - i) + ' '*(i-1) + '{:>{}}'.format('*', i+1))
    for i in range(size//2-1,-1,-1):
        if i == 0:
            print('{:>{}}'.format('*', (size//2 + 1) - i))
        else:
            print('{:>{}}'.format('*', (size//2 + 1) - i) + ' '*(i-1) + '{:>{}}'.format('*', i+1))



def many_diamond_patterns(numbers):
    for number in numbers:
        if number & 1 == 1:
            diamond_pattern(number)

many_diamond_patterns([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])