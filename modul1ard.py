grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
res = {}
for key in sorted(students):
    for value in grades:
        res[key] = sum(value)/len(value)
        grades.remove(value)
        break
print("Resultant dictionary is : " + str(res))
