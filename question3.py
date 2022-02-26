# ************************ HOMEWORK 1 QUESTION 3 **************************
def question3(input_num):
    # ***** WRITE CODE HERE *****
    # SUMS ALL THE ODD NUMBERS FROM 1 UNTIL THE NUMBER INPUTTED
    # IF THE NUMBER ENTERED IS SMALLER OR EQUALS 1, THERE IS NO CALCULATIONS NEEDED
    if input_num <= 1:
        print(input_num)

    # USING A SEPARATE VALUE TO CALCULATE THE SUM
    # i IS THE SMALLEST ODD NUMBER TO ADD TO THE SUM
    # IF THE NUMBER IS ODD WE WILL ADD IT TO THE SUM
    # RUNS UNTIL WE REACH INPUT_NUM
    count_sum = 0
    for i in range(1, input_num + 1):
        if i % 2 != 0:
            count_sum += i

    print(count_sum)
