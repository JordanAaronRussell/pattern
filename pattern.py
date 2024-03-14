'''This is a program which prints each letter of a string, including spaces,
for any string specified.'''

stars = '*****'
count = 1 #count starts ar 1 to avoid invalid index value once condition has been met.

for star in range(0, len(stars) * 2): #multiply the length of the string by 2 to avoid hardcoding and ensure that the program works with any string
    if star <= len(stars):
        print(stars[:star])
        count += 1

    else:
        print(stars[:star - count])
        count += 2 #count increments in twos to ensure backwards indexing of 'stars'
        #counting in ones would simply repeat last print statement. 





