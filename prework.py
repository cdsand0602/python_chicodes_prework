# Question 1 - Write a function to print "Hello_USERNAME"
def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name('Crystal')


# Question 2 - Print first odd numbers

def odd_number():
    for i in range(0,101,2):
        print(i)

odd_number()


# Question 3 - Write a function that returns the max number in a given list

def max_number(a_list):
    max_number = max(a_list)
    return max_number

# Question 4 - Write a function to return if the given year is a leap year

def is_loop(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

    is_leap_year(2020)


# Question 5 - Write a function to check if all numbers in a list are consecutive

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] == a_list[i + 1]:
            i += 1     
        else: 
             status = False
             break
    print(status)