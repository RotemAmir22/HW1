# ************************ HOMEWORK 1 QUESTION 5 **************************
def question5(sentence):
    # ***** WRITE CODE HERE *****
    # checking if all the letters of the alphabet are in the sentence.
    # checks each letter sparely

    # there are 26 letters in the alphabet
    # if the sentence is shorter than 26 -> all the letters wont appear
    if len(sentence) < 26:
        print(False)

    else:
        # is the letter a in the sentence
        is_a = False
        for letter_a in sentence:
            if letter_a == 'a':
                is_a = True
                break

        # is the letter b in the sentence
        is_b = False
        for letter_b in sentence:
            if letter_b == 'b':
                is_b = True
                break

        # is the letter c in the sentence
        is_c = False
        for letter_c in sentence:
            if letter_c == 'c':
                is_c = True
                break

        # is the letter d in the sentence
        is_d = False
        for letter_d in sentence:
            if letter_d == 'd':
                is_d = True
                break

        # is the letter e in the sentence
        is_e = False
        for letter_e in sentence:
            if letter_e == 'e':
                is_e = True
                break

        # is the letter f in the sentence
        is_f = False
        for letter_f in sentence:
            if letter_f == 'f':
                is_f = True
                break

        # is the letter g in the sentence
        is_g = False
        for letter_g in sentence:
            if letter_g == 'g':
                is_g = True
                break

        # is the letter h in the sentence
        is_h = False
        for letter_h in sentence:
            if letter_h == 'h':
                is_h = True
                break

        # is the letter i in the sentence
        is_i = False
        for letter_i in sentence:
            if letter_i == 'i':
                is_i = True
                break

        # is the letter j in the sentence
        is_j = False
        for letter_j in sentence:
            if letter_j == 'j':
                is_j = True
                break

        # is the letter k in the sentence
        is_k = False
        for letter_k in sentence:
            if letter_k == 'k':
                is_k = True
                break

        # is the letter l in the sentence
        is_l = False
        for letter_l in sentence:
            if letter_l == 'l':
                is_l = True
                break

        # is the letter m in the sentence
        is_m = False
        for letter_m in sentence:
            if letter_m == 'm':
                is_m = True
                break

        # is the letter n in the sentence
        is_n = False
        for letter_n in sentence:
            if letter_n == 'n':
                is_n = True
                break

        # is the letter o in the sentence
        is_o = False
        for letter_o in sentence:
            if letter_o == 'o':
                is_o = True
                break

        # is the letter p in the sentence
        is_p = False
        for letter_p in sentence:
            if letter_p == 'p':
                is_p = True
                break

        # is the letter q in the sentence
        is_q = False
        for letter_q in sentence:
            if letter_q == 'q':
                is_q = True
                break

        # is the letter r in the sentence
        is_r = False
        for letter_r in sentence:
            if letter_r == 'r':
                is_r = True
                break

        # is the letter s in the sentence
        is_s = False
        for letter_s in sentence:
            if letter_s == 's':
                is_s = True
                break

        # is the letter t in the sentence
        is_t = False
        for letter_t in sentence:
            if letter_t == 't':
                is_t = True
                break

        # is the letter u in the sentence
        is_u = False
        for letter_u in sentence:
            if letter_u == 'u':
                is_u = True
                break

        # is the letter v in the sentence
        is_v = False
        for letter_v in sentence:
            if letter_v == 'v':
                is_v = True
                break

        # is the letter w in the sentence
        is_w = False
        for letter_w in sentence:
            if letter_w == 'w':
                is_w = True
                break

        # is the letter x in the sentence
        is_x = False
        for letter_x in sentence:
            if letter_x == 'x':
                is_x = True
                break

        # is the letter y in the sentence
        is_y = False
        for letter_y in sentence:
            if letter_y == 'y':
                is_y = True
                break

        # is the letter z in the sentence
        is_z = False
        for letter_z in sentence:
            if letter_z == 'z':
                is_z = True
                break

        # if the letter is in the sentence - TRUE
        # if the letter is not in the sentence - FALSE
        # print TRUE if all the bool values are TRUE as well, if not then print FALSE

        print(
            is_a and is_b and is_c and is_d and is_e and is_f and is_g and is_h and is_i and is_j and is_k and is_l and
            is_m and is_n and is_o and is_p and is_q and is_r and is_s and is_t and is_u and is_v and is_w and is_x and
            is_y and is_z)
