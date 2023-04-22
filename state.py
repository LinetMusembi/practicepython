#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def  even_num():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)
# Write a function that takes a list of integers as input and prints the sum of all 
# the even numbers in the list.    
        
def sum_odd():
    sum=0
    for i in range(15):
        if i%2==0:
            sum=sum+i
            print("sum=",sum)
#Write a function that takes a list of intergers as input and prints the sum of
# all numbers that are only divisible by 5 
def divisible_by_5():
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")            
    else:
        print(f"{i} is not divisible by 5")  

# 
    return answer 
# A function named concatenate_args that takes any number of string arguments in
# positional arguments format and concatenates them into a single string

 
def concatenate_args(*strings):
    answer = ""
    for string in strings:
        answer += string

    return answer

# A function named concatenate_kwargs that takes any number of string arguments in 
# keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**weeks):
    strin = " "
    for week in weeks.values():
        strin += week
    return strin
# Below is the function display_student(name, age). Assign a new name show_student
# (name, age) to it and call it using the new name.

def display_student(name, age):
    print(name, age)

display_student("Lynet", 26)


showStudent = display_student
showStudent("Lynet", 26)

#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def  even_num():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)