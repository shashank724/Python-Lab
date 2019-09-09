a=[1,2,3,4]
b=[1,2]
a.extend(b)
print(a)

a=[1,2,3,4]
b=['geeks','for','geeks']
a.append(b)
print(a)
b[2]



def myFun(x): 
   x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
anotherlst=[20,30]
lst.append(anotherlst)
myFun(lst); 
print(lst)

def my_function(fname):
  print(fname + " Ayodhya")
my_function("Ravan")
my_function("ram")
my_function("laxman")

t1 = tuple()
print('t1=', t1)

#using list

t2 = tuple([1, 4, 6])
print('t2=', t2)


t1 = tuple('Python')
print('t1=',t1)

#using dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1=',t1)

