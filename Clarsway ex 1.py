#Ex 1
while True:
    letter =input ("Enter your letter:")
    vowel = 'a','e','o','i','u','y'
    if letter == vowel:
        print('your letter is vowel')
    else:
        print('your letter is consonant')

____________________________
#Ex 2
while True:
    The_amount =float(input("Enter the amount:"))
    if The_amount <= 999:
        print('your amount is lower than 1000')
    elif The_amount >= 2001:
        print('your amount is higher than 2000')
    else:
        print('your amount is between 1000 and 2000')
#############################
#Ex 3
number1 = float(input('pick your first number: '))
number2 = float(input('pick your second number: '))
number3 = float(input('pick your third number: '))
total = number1 + number2 + number3
if number1 == number2 == number3:
    print ('All number are the same amount')
    print (total)
    print ('This amount multiplied by 4 becomes',total*4)
    print('This amount multiplied by 5 becomes',total *5)

else :
    print (('The total of amount is') ,total)
################
#Ex 4

number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))
number3 = float(input('Enter your third number: '))
number4 = float(input('Enter your fourth number: '))
max_number = max(number1, number2, number3, number4)
print('The largest number is',max_number)

#####################
#Ex 5



income =float(input("Enter your income:"))
if income <= 67000:
               tax_rate = 0.24
               tax = income * tax_rate
               after_tax = income - tax
               print("Your net income is", after_tax)

elif income <= 97000:
               tax_rate = 0.31
               tax = income * tax_rate
               after_tax = income - tax
               print("Your net income is", after_tax)

elif income >= 97000:
               tax_rate = 0.34
               tax = income * tax_rate
               after_tax = income - tax
               print("Your net income is", after_tax)

else:
               print("Invalid")
################
#EX 6
while True:
    text = input("Enter your text here:")
    if  len (text) == 1:
        text_answer = text * 6
        print(text_answer)

    elif len (text) == 2:
        opposite_answer = text[::-1]
        print(opposite_answer)

    elif len (text) == 3:
        modified_answer = text[-1] + text[0] + text[1]
        print (modified_answer)

    elif len (text) == 4:
        text4 = text[-1] + text[1] + text[2] + text[0]

        print(text4)

    elif len (text) == 5:
        text5 = ''.join(letter+"t" for letter in text)
        print(text5)

    else:
        print('your should be max 5 letter try agine Thank you :)')
######################
#Ex 7
question1 = input("complete the word(Stu_y)?")
if question1 == 'd':
    pass
else:
    print('your answer is false,Game over:(')
    exit()
question2 = input("complete the second word bo_k?")
if question2 == 'o':
    pass
else:
    print('your answer is false,Game over:(')
    exit()
question3 = input("complete the third word ho_e?")
if question3 == 'm':
        print('perfect all answer are good:)')
else:
        print('your answer is false,Game over:(')