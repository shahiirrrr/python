

# def add():
#     a=10
#     b=20 
#     sum=a+b
#     print(sum)
# add()    


# def add1(a,b):
#     n=a
#     m=b
#     sub=n*m
#     print(sub)
# add1(5,6)    



# def add2(a,b):
#     n=a
#     m=b
#     x=b/a
#     return x
# p=int(input("enter:"))
# k=int(input("enter:"))
# print(add2(p,k))



#NAME CAP

# def cap(name):
#     words=name.split()
#     a=[word.capitalize() for word in words]
#     b=" ".join(a)
#     return b
# name=input("enter a name:")
# b=cap(name)
# print(b)




# def sumsq(numbers):
#     sum=0
#     for num in numbers:
#         sum += num ** 2
#     return sum
# numbers=[]
# for i in range(3):
#     num=int(input("enter the number:"))
#     numbers.append(num)
# d=sumsq(numbers)
# print(d)    


#REMOVE SPECIAL CHARACTERS FROM A STRING

# def spchr(a):
#     result=""
#     for i in a:
#         if i.isalpha():
#             result+=i
#     return result
# a=input("enter a string:")               
# result=spchr(a)
# print(result)



# def square():
#     a=int(input("enter limit:"))
#     d=[]
#     for i in range (a):
#         b=int(input("enter element:"))
#         d.append(b)
#     print(d)
#     for i in range(len(d)):
#         d[i]=d[i]**2
#     print(d)
# square()    


   
# def common(a,b):
#     m=set(a)
#     n=set(b)
#     common=m.intersection(n)
#     d=list(common)
#     return common
# a=[1,2,3]
# b=[2,3,4]
# result=common(a,b)
# print(result)




# def common(a,b):
#     d=[]
#     for i in a:
#         if i in b and i not in d:
#             d.append(i)
#     return d
# a=[1,2,3]
# b=[2,3,4]

# d=common(a,b)
# print(d)



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         factorial=1
#         for i in range (1,n+1):
#             factorial *= i
#         return factorial
# print(factorial(5))



# def prime(n):
#     if n<=1:
#         return False
#     if n<=3:
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     i=5
#     while i *i<=n:
#         if n%i==0 or n%(i+2)==0:
#             return False
#         i+=6
#     return True


 
# def prime(a, b):
#     primenum = []
#     for i in range(a, b):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i/2)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 primenum.append(i)
#     return primenum
 
# start = 2
# end = 7
# lst = prime(start, end)
# if len(lst) == 0:
#     print("no numbers")
# else:
#     print("prime: ", lst)



# def fib(n):
#     d=[]
#     first=0
#     second=1
#     next=first+second
#     d.append(first)
#     d.append(second)
#     for i in range (2,n+1):
#         d.append(next)
#         first=second
#         second=next
#         next=first+second
#     return d
# n=int(input("enter: "))
# result=fib(n)
# print(result)


#FIBONACCI 


# def fib(n):
#     d=[]
#     a,b=0,1
#     for i in range(n):
#         d.append(a)
#         a,b=b,a+b
#     return d
# n=7
# d=fib(n)
# for num in d:
#     print(num,end=",")    


#PRIME NUMBER


# def prime(n):
#     if(n==1 or n==0):
#         return False
#     for i in range (2,n):
#         if(n%i==0):
#             return False
#     return True
# n=int(input("enter:"))
# for i in range(1,n+1):
#     if prime (i):
#         print(i,end=",")        

#LETTER A


# def pattern(n):
#     for i in range(n):
#         for j in range (n,i+1,-1):
#             print(" ",end="")
#         for j in range(2*i+1):
#             if j==0 or j==2*i:
#                 print("*",end="")
#             elif i==2:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# pattern(5)


# def pattern(n):
#     for i in range (1,n+1):
#         for j in range (0,i):
           
#                 print("*",end="")
#         print()
#         if i%2==0:
#             for j in range (1,i+1):

#                 print(j,end="")
#         else:
#              for j in range (i,0,-1):
#                   print(j,end="")
#         print()
# pattern(6)



# def binary(decimal):
#     x=""
#     while decimal > 0:
#         r=decimal%2
#         x=str(r)+x
#         decimal=decimal//2
#     return x
# def octal(decimal):
#     y=""
#     while decimal > 0:
#         r=decimal % 8
#         y=str(r)+y
#         decimal=decimal // 8
#     return y
# def hexa(decimal):
#     z=""
#     while decimal > 0:
#         r=decimal % 16
#         if r < 10:
#             z=str(r)+z
#         else:
#             z=chr(ord('A')+ r-10 )+z  
#         decimal=decimal // 16
#     return z


# decimal=int(input("enter a decimal number: "))


# a=binary(decimal)
# b=octal(decimal)
# c=hexa(decimal)
# print("binary: ",a)
# print("octal: ",b)
# print("hexaddecimal",c)




# a = [ 2,1,4,3]
# d=[]
# a.sort()
# print("Ascending : ", a)

# a.sort(reverse=True)
# print("Descending : ", a)



# def fibonacci(n):
#     s=[0,1]
#     while s[-1] <= n:
#         d=s[-1]+s[-2]
#         if d<=n:
#             s.append(d)
#         else:
#             break
#     for num in s:
#         if num <= n:
#             print(num)
# try:
#     n=int(input("enter a +ve number: "))
#     if n<= 0:
#         print("enter a +ve")
#     else:
    
    
#         fibonacci(n)
# except ValueError:
#     print("enter +ve :")




# def a():

#     a=["apple","banana","cherry","date"]
#     d=[]
#     for i in a:
#         for j in a:
#             if i != j and any(letter in j for letter in i):
#                 d.append((i,j))
#     for x in d:
#         print(x)
# a()


# def a():
#     n=[3,8,12,7,6,10,21,15]
#     sum=18
#     d=[]
#     for i in range(len(n)):
#         for j in range(i+1, len(n)):
#             if n[i]+n[j]==sum:
#                 d.append((n[i],n[j]))
#     for x in d:
#         print(x)
# a()




# def a():
#     n=[2,3,4,5,6]
#     d=[]
#     for i in range(len(n)):
#         for j in range(i+1, len(n)):
#             p=n[i]*n[i]
#             sum=n[i]+n[j]
#             if p %2==0 and sum %2 !=0:
#                 d.append((n[i],n[j]))  
#     for x in d:
#         print(x)
# a()



# def a():
#     a="python"
#     b=""
#     for i in range(len(a)):
#         if a[i]=="t" or a[i]=="h":
#             a.format(i)
#         else:
#             b=b+a[i]
#     for j in range (len(b)):
#         print(b[j],end=".")
# a()



# def ab():
#     a=input("enter a sentence: ")
#     d=a.split()
#     count=len(d)
#     print("words in sentence: ",count)
# ab()





# def ab():
#     a=input("enter a sentence: ")
#     d=a.split()
#     lg=""
#     c=0
#     for x in d:
#         if len(x) > c:
#             lg=x
#             c=len(d)
#     print("longest word: ",lg)

# ab()




def capital():
    a=input("enter the sentence: ")
    d=a.split()
    for x in d:
        if x[0].isupper():
            print(x)
        else:
            print("no words")
capital()