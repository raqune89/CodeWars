#Bob is preparing to pass IQ test. 
# The most frequent task in this test is to find out which one of the given numbers differs from the others. 
# Bob observed that one number usually differs from the others in evenness. 
# To check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)


def iq_test(numbers):
    num = numbers.split()
    odd_num = 0
    even_num = 0
    position = 0

    #populate the odd/even variables
    for i in range (len(num)):
        if (int(num[i]) % 2 == 0):
            even_num += 1
        else:
            odd_num += 1

    if (odd_num > even_num):    
        for i in range (len(num)):
            if (int(num[i]) % 2 == 0):
                position = i + 1
    else:
        for i in range (len(num)):
            if (int(num[i]) % 2 != 0):
                position = i + 1
    return position
