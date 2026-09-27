ages = [21, 18, 30, 35, 42]

for age in ages:
    print(age) #print all elements in ages array


for i in range(len(ages)):
    print(ages[i]) #print all elements in ages array using index

for k in range(3):
    print(k) #print numbers from 0 to 2


#Nested loop example
teams = [["Jake", "Amy"], ["John", "Mary"], ["James", "Bathsheba"]]

for team in teams:
    for name in team:
        print(name) #print all the names in the team


#while loop
k = 1
while k < 10:
    print(k)
    k += 1