print (" Shashank S")

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print ("Addition of {} and {} is {}".format(a,b,a+b))
print ("Addition of",a,"and",b,"is",(a+b))

 print (2+3)
5
print (2-3)
-1
 print (2%3)
2
 print (2//3)

0
 print (2**3)
8
 print (2*3/5)
1.2
 print (2+3*6)
20

course = "python programming"
print (course.upper())
print (course.replace("python","java"))

course = "python programming"
print (course.lower())

print (course[0:6])
print (len(course))
print (course[5])

a = " lab"
print (course+a)

b = '"CMR" "University"'
print (b)

#Swapping
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = a
a = b
b = c
print ("After swapping: \na =",a,"\nb=",b)

#Fibonacci
length = int(input("Enter the value:"))
x = 0
y = 1
iteration = 0
if length <= 0:
   print("Please provide a number greater than zero")
elif length == 1:
   print("This Fibonacci sequence has {} element".format(length), ":")
   print(x)
else:
   print("This Fibonacci sequence has {} elements".format(length), ":")
   while iteration < length:
       print(x, end=', ')
       z = x + y
       x = y
       y = z
       iteration += 1


         
***********Output***********


Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/cs2016b103/shashank/pythonlab1.py ================== Shashank S
Enter the value of a:30
Enter the value of b:20
Addition of 10 and 20 is 50

PYTHON PROGRAMMING
java programming
python
18
n
python programming lab
"CMR" "University"
Enter the value of a:10
Enter the value of b:20
After swapping: 
a = 20 
b= 10
Enter the value:5
This Fibonacci sequence has 5 elements :
0, 1, 1, 2, 3,5
