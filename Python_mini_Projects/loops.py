"""
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#avg of them
summ = 0
for heights in student_heights:
  summ = summ + heights


print(summ)
print(len(student_heights))
print(int(summ/len(student_heights)))  


#finding the maxmium in the list

student_gardes = input().split()
for n in range(0, len(student_gardes)):
  student_gardes[n] = int(student_gardes[n])

count = 0
for g in range(0, len(student_gardes)):
  if(student_gardes[g]) > count:
    count = student_gardes[g]
    
print(count)    

"""

#finding the sum of all the even numbers in the range of the user gives to us

user_number = int(input("Give the number between 1 to 1000\n"))
if user_number > 1000:
    print("Please put the number in the range")

even_sum = 0
for n in range( 2 , user_number + 1 , 2):
    if n%2 == 0:
        even_sum += n
   


print(even_sum)








