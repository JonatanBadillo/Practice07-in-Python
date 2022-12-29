'''
The company knows the salary and the labor old of each employee
Develop a program that reads those data and do:
    *If the salary is less than 500 and his labor old is equal or higuer than 10 years, give him a 20% salary increase
    *If the salary is less than 500, but his laabor old is less than 10 years, give him a 5% salary increase
    *If the salary is higher or equal to 500 , print the salary without changes
'''

salary = int(input("Introduce your salary : "))
labor_old = int(input("Introduce your labor old : "))

if salary<500 and labor_old>=10 :
    salary = (salary * 0.20) + salary
elif salary<500 and labor_old < 10 :
    salary = (salary * 0.05) + salary
elif salary>=500:
    salary = salary

print(f"Yor salary is: {salary}")