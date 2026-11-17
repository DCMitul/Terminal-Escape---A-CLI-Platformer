import os

# print(os.get_terminal_size())     # This is supposed to print the number of columns and rows the currently opened terminal has


# print('''
# ##############################
# #                            #
# #                            #
# #                            #
# #                            #
# #                            #
# #                            #
# #                            #
# ##############################
# ''')

# I used the above to test the dimensions that would fit well
# 10:3 is the current final (column:row)
ASPECTRATIO = [10,3]

SIZE = os.get_terminal_size()
ROWCHAR = '#'        # The charector that the boundary will use
EMPTYCHAR = ' '      # The empty charector for the body :)


if SIZE[0] < 80 or SIZE[1] < 24:
    print("Sorry the terminal width and/or height are too less. Try increasing the window size or decreasing the font size and try again.")
    os._exit(0)



# n is the number of columns the game would use and nn is the number of rows
if SIZE[0]/SIZE[1] == ASPECTRATIO[0]/ASPECTRATIO[1]:
    n = SIZE[0]
    nn = SIZE[1]
else:
    temp = ASPECTRATIO
    while True:
        if temp[0] <= SIZE[0] and temp[1] <= SIZE[1]:
            temp = [temp[0] + ASPECTRATIO[0], temp[1]+ASPECTRATIO[1]]
            print(temp)
            continue
        else:
            temp = [temp[0]-ASPECTRATIO[0],temp[1]-ASPECTRATIO[1]]
            break
    n = temp[0]
    nn = temp[1]




for i in range(1,nn+1):
    if i == 1 or i == nn:
        print(ROWCHAR * n)
    else:
        print(ROWCHAR + (EMPTYCHAR * (n-2)) + ROWCHAR)




