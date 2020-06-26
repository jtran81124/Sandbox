#If file is in the same folder, then you dont have to go through directory

# r read, w write, a append: can only add info, r+ allows read and writing
employeeFile = open("employees.txt", "r")

# check if its able to be read
# print(employeeFile.readable())
# print(employeeFile.readlines()[0])
# print(employeeFile.readline())
# print(employeeFile.readlines()) 
#gets put into an array, 
#can read an index

#useful for loop
for employee in employeeFile.readlines():
    print(employee)



#remember to always close file at the end
employeeFile.close()

employee_file = open("employees.txt", "a")
employee_file.write(" \nAustin - Toppings")
employee_file.close()

#creating a new file
employee_file1 = open("employees1.txt", "w")
employee_file1.write("The big brown fox jumped over the lazy dog")
employee_file1.close()