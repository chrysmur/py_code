'''
Suppose we are given as input an array of students, sorted by descending GPA, with ties broken
on name

Bisect  bisect_left, will return the rightmost value at or after finding the target, 
li = [1,2, 6, 9, 14, 15]
bisect.bisect_left(li, 10) should return index 4 ==> 14
'''


import bisect
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)

def search_student(students, target, comp_gpa):
    i =  bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))

    return 0 <= i < len(students) and student[i] == target