# MADE BY AKRAM!
import math
c,a,b,e=input('Press 1 to divide 2 number\'s:\nPress 2 to multiply 2 number\'s:\nPress 3 to subtract 2 number\'s:\nPress 4 to add 2 number\'s:\nPress 5 to get power of a number:\nPress 6 to get remainder of 2 number\'s:\nPress 7 or greater than 7 to get square root of a number:\n'),input('Enter The Value Of First Operand:\t'),input('Enter The Value Of Second Operand :\t'),input('ENTER NUMBER')
c,a,b,e=float(c),float(a),float(b),float(e)
if c==1:
 print(a/b)
elif c==2:
 print(a*b)
elif c==3:
 print(a-b)
elif c==4:
 print(a+b)
elif c==5:
 print(a**b)
elif c==6:
 print(a%b)
else:
 print(math.sqrt(e))
