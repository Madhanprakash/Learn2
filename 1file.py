print("Hello, World!")
a = 2
b = 3
c = a + b
print("The sum of", a, "and", b, "is", c)

d = 10
e = d - c
print("The subtraction between", d, "and", c, "is", e)

f = 5
g = f * e
print("The Multiple of", f, "and", e, "is", g)       

h = g / a
print("The division of", g, "by", a, "is", h)   

i = 12
j = i % b
print("The percentage of", i, "divided by", b, "is", j)      

k = 13
l = k ** 2
print("The square of", k, "is", l)      

M = 14
n = M // a  
print("The floor division of", M, "by", a, "is", n) 

def mac(o,p):
    q=o+p
    return q

def area(r,s):
    t=r*s
    return t

print("The value of a is", a)
print("The value of b is", b)
print("The value of c is", c)
print("The value of d is", d)
print("The value of e is", e)
print("The value of f is", f)
print("The value of g is", g)
print("The value of h is", h)
print("The value of i is", i)
print("The value of j is", j)
print("The value of k is", k)
print("The value of l is", l)
print("The value of M is", M)
print("The value of n is", n)   
print("The value of q is", mac(a,M)) 
print("The value of t is", area(f,g))

Total = a+b+c+d+e+f+g+h+i+j+k+l+M+n
print("The total sum of all variables is:", Total)

if  Total >= 100:
    print("The total sum is greater than or equal to 100.")

elif Total < 100:
    print("The total sum is less than 100.")

elif Total == 100:  
    print("The total sum is equal to 100.") 

else:
    print("The total sum is not equal to 100.")


if Total > 282.5:
    if Total < 300:
        print("The total sum is between 282.5 and 300.")

    else:
        print("The total sum is not between 282.5 and 300.")

else:
    print("The total sum is  282.5 is correct.")

Task1 = [a,b,c,d]
for Task2 in Task1:
    print("The value of Task2 is:", Task2)

count = c
while count <=5:
    print("The value of count is:", count)
    count += 1


print(a == b)
print(a != b)
print(a > b)    
print(a < b)
print(a >= b)   
print(a <= b)  

Age = 25
if Age >= 18:
    print("You are an adult.")
else:   
    print("You are a minor.")   


print(Age >= 18 and Age <= 65)  
print(Age < 18 or Age > 65)
print(not (Age >= 18 ))

score = 25
print("Your score is", score)   
score += 15
print("Your updated score is", score)
score -= 15 
print("Your updated score is", score)
score *= 2
print("Your updated score is", score)
score /= 5
print("Your updated score is", score)   

name = "Madhan Prakash"
name2 = "Today task has been completed"
integer_value = 2
float_value = 2.5
string_value = "Learning Python"

print("Name:",name, type(name))
print("Status:",name2, type(name2))
print("Learn Duration Type:",integer_value, type(integer_value))
print("Learn Duration:",float_value, type(float_value))
print("Learning Objective:",string_value, type(string_value))


number_text = "500"
number = int(number_text)
print("The value is:", number + 500)

for i in range(1,5):
    print("Number:", i)