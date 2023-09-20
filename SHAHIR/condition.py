#if (5>2):
   # print("greater")
    
#if (5<2):
   # print("greater")    


#if (5<2):
    #print("greater")
#else:
 #   print("not greater") 


#a=5
#b=5
#if (a>b):
#    print("a is grater")
#elif (a==b):
 #   print("a equal to b")
#else:
#    print("not equal")


#a=9
#b=11
#c=15
#if(a>b)and(a>c):
 #   print("a is greater")
#elif(b>a)and(b>c):
 #   print("b is greater")
#else:
 #   print("c is greater")


#a=77
#b=18
#c=8
#if(a>b):
#    if(a>c):
#        print(a)
#    else:
#        print(c)
#elif(b>a):
#    if(b>c):
#        print(b)
#    else:
#        print(c)
#elif(c>a):
#    if(c<b):
#        print(c)
#    else:
#        print(b) 
#else:
#    print(a) 





#EVEN OR ODD

#num=(int(input("enter the number")))
#if(num%2)==0:
#    print("number is even")
#else:   
 #   print("number is odd")



#POSITIVE NEGATIVE OR ZERO

#x=int(input("Enter a number: "))
#if x>= 0:
#   if x== 0:
#       print("Zerooo")
#   else:
#       print("Positive")
#else:
#   print("Negative")




#LEAP YEAR

#year = int(input("Enter a year: "))


#if (year % 400 == 0) and (year % 100 == 0):
#   print("leap year")


#elif (year % 4 ==0) and (year % 100 != 0):
#    print("leap year")

#else:
#    print("not a leap year")



#x=int(input("number:"))
#for i in range(x):
 #if(i%3==0):
#    print(i)



#NUMBER IS DIVISIBLE BY 7

#x=int(input("enter the number:"))
#if x%7==0:
#    print(x,"is div by 7")
#else:
#    print(x,"not div by 7")  


#DISPLAY HELLO IF ENTERD NUMBER IS MULTIPLE OF 5
#x=int(input("enter the number:"))
#if x%5==0:
#    print("hello")
#else:
#    print(x," is not a multiple of 5")





#d={28:"feb",31:["jan","march","may","july","aug","oct","dec"],30:["april","june","sep","nov"]}
#n=int(input("enter the days:"))
#if(n==31):
#    print(d[31])
#if(n==30):
#    print (d[30])




#i=0
#while (i<=10):
#    print("heyy")
#    i=i+1


#for i in range(10):
#    print("hi")




#sum=0
#i =0
#while(i <= 9):
#    num = int(input("Number %d = " %i))
#    sum = sum + num
#    i = i + 1
#print("Sum: ", i)





#print("10 Odd Numbers:")
#i = 1

#while(i <= 10):
#    print(2 * i - 1)
#    i = i + 1



#x = int(input("Enter a number: "))
#i = 1
#while i <= x:
#    if i % 2 == 0:
#       print(i, end=" ")
#    i = i + 1



   



#x = int(input("Enter a number: "))
#i = 1
#while i <= x:
#    if i % 2 != 0:
#       print(i, end=" ")
#    i = i + 1  


#n=0
#while(n<10):
#    n=n+1 
#    print("sq of",n,"is",n*n)








#LENGTH OF STRINGS

#list=("hello","python","heyy")
#i=0
#while i < len(list):
#    a=list[i]
#    length = len(a)
#    print(f"length of '{a}'is: {length}")
#    i+=1




#COUNT OF EACH CHARACTERS  


#d={ }
#a=str(input("enter the word:"))
#count=0
#l=""
#i=0
#while (i<=len(a)-1):
#    if(a[i]in l):a=[1,2,3,4,5,6]
# i=0
# x=[]
# while i<len(a):
#     if a[i] % 2 == 0:
#         x.append(a[i])
#     i=i+1
# print("even numbers",x)  
#        count+=1
#        l+=a[i]
#        d[a[i]]=count
#    else:
#        count =1
#        l+=a[i]
#        d[a[i]]=count
#    i=i+1  
#print(d)    




# COMMON ELEMENTS

# a=[1,2,3,4]
# b=[3,4,5,6]
# c=[ ]
# i=0
# j=0
# while i<len(a) and j<len(b):
#     if a[i]==b[j]:
#         c.append(a[i])
#         i+i+1
#         j=j+1
#     elif a[i] < b[j]:
#         i=i+1
#     else:
#         j=j+1
# print("commen eln:",c)                     
      




#REVERSE OF A STRING USING WHILE LOOP

# x=input("enter a string:")
# i=len(x)-1
# d=""
# while i>= 0:
#     d+=x[i]
#     i=i-1
# print("rev of string",d)    


# x=input("enter a string:")
# d=""
# count=len(x)
# while count > 0:
#     d+=x[count -1]
#     count = count-1
# print("r str:",d)    



#SUM OF LIST OF INTEGERS

# a=[1,2,3,4,5,6,7,8,9]
# i=0
# sum=0
# while i<len(a):
#     sum += a[i]
#     i=i+1
# print(sum)    


#FIND THE EVEN NUMBERS IN A LIST

# a=[1,2,3,4,5,6]
# i=0
# x=[]
# while i<len(a):
#     if a[i] % 2 == 0:
#         x.append(a[i])
#     i=i+1
# print("even numbers",x)        





#CAPITALIZE FIRST LETTER OF A WORD IN A STRING

# a=["hello","car","anime"]
# c=[]
# i=0
# while i<len(a):
#     c.append(a[i].capitalize())
#     i=i+1
# print(c)



#SQ(LIST) USING FOR LOOP

# a=[1,2,3,4,5]
# d=[]
# for n in a:
#    d.append(n**2) 
# print(d)



#SUM OF SQ OF  3 INPUT NUMBERS USING FOR LOOP

# num=[]
# for i in range(3):
#     x=int(input("enter number:"))
#     num.append(x)
# sum=0
# for n in num:
#     sum+=n**2
# print("sum of sq:",sum)    
                  


#FIND THE LARGEST INTEGER IN THE LIST


# a=[1,2,3,4,5]
# i=0
# x=a[0]
# while i<len(a):
#     if a[i]>x:
#       x=a[i]
#     i=i+1
# print("largest integer:",x)        





#NUMBER OF WORDS IN A STRING

# a=input("enter the string:")
# x = len(a.split())
# print ("Number Of Words: ",x)


# a="hello python"
# count=1
# i=0
# while i<len(a):
#     if (a[i]==' '):
#         count=count+1
#     i=i+1
# print(count)    



# TAKE A LIST OF STRINGS AND PRINT NEW LIST CONTAINING ONLY MORE THAN 5 CHARACTERS

# a=["hyy","python"]
# i=0
# d=[]
# while i<len(a):
#     if len(a[i])>5:
#         d.append(a[i])
#     i=i+1
# print(d)




#STAR  PATTERN USING FOR LOOP

# for i in range (0,5):
#     for j in range (0,i+1):
#         print("*",end=" ")
#     print() 

# for i in range (5,-1,-1):
#     for j in range (0,i):
#         print("*",end=" ")
#     print() 


# n=5
# for i in range(1,n+1):
#     print(" "* (n-i)+ "*" *i) 
        
  
# n=5
# for i in range(n,0,-1):   
#     print(" "* (n-i)+ "*" *i)  


#NUMBER PYRAMID

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    
                    


# n=5
# for i in range (0,n):
#     for j in range(1,i+1):
#         print(j*2-1,end=" ")
#     print()    



# n=5
# for i in range (0,n):
#     for j in range(1,i+1):
#         print(j*2,end=" ")
#     print() 





# n=4
# x=1
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(x*2-1,end=" ")
#         x=x+1
#     print()  




# n=3
# x=1
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(x*2,end=" ")
#         x=x+1
#     print()   


# x=1
# n=3
# stop=2
# for i in range (n):
#     for j in range(1,stop):
#         print(x,end=" ")
#         x=x+1
#     print()
#     stop+=2
   


