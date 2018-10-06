#Create list from 1-million, print smallest and largest numbers as well as sum of all in list
million = []
for value in range(1, 1000001):
    million.append(value)
print(min(million))
print(max(million))
print(sum(million))

#Create list of odds from 1-19 and print them
odds = []
for odd in range(1,20,2):
    odds.append(odd)
    print(odd)
print("The first three items in the list are:")
print(odds[:3])

#Create list of multiples of 3 from 3-30 and print them
threes = []
for three in range(3,31,3):
    threes.append(three)
    print(three)

#Create list of cubes from 1-10 and print them
cubes = []
for value in range(1,11):
    value = value**3
    cubes.append(value)
    print(value)

#List comprehension of the above
cubes = [value**3 for value in range(1,11)]
print(cubes)
