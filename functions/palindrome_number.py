def palindrome_number(number):
    temp = number
    reverse = 0
    while(number>0):
        dig = number%10
        reverse = reverse*10 + dig
        number = number//10

        if temp == reverse:
            return True
        else:
            return False