age = int(input('Please enter your age : '))
if age<0 :
    print('ENTER ERROR')
elif age<=6 :
    print('FREE')
elif 6<=age<=17 :
    student = input('Is student?')
    if student == 'yes' :
        print('RM8')
    else:
        print('RM12')
elif 18<=age<=59 :
    student = input('Is student?')
    if student == 'yes' :
        print('RM15')
    else :
        print('RM20')  
elif age>=60 :
    print('RM10')