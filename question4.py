# ************************ HOMEWORK 1 QUESTION 4 **************************
def question4(input_list):
    # ***** WRITE CODE HERE *****
    # FINDS TH 4 MINIMUM NUMBER IN A GIVEN LIST
    # if the length of the list is shorter than 4- there is no 4th minimum number
    if len(input_list) < 4:
        print("error")

    #     the maximum number is 100,000
    min1 = 100000
    min2 = 100000
    min3 = 100000
    min4 = 100000

    # compares the numbers to see what is the smallest out of the four
    # change the values according to the minimum
    for i in input_list:
        if i < min1:
            min4 = min3
            min3 = min2
            min2 = min1
            min1 = i

        elif i < min2:
            min4 = min3
            min3 = min2
            min2 = i

        elif i < min3:
            min4 = min3
            min3 = i

        elif i < min4:
            min4 = i

    print(min4)
