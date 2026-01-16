# 0108
students = [
    {"name": "John", "grades": [85, 92, 78, 100]},
    {"name": "Sarah", "grades": [88, 95, 90, 89]},
    {"name": "Tyler", "grades": [70, 75, 82, 80]},
    {"name": "Emma", "grades": [95, 98, 88, 92]},
    {"name": "Emma2", "grades": [1, 2, 3, 4]},
]
# 각각의 학생들에 대해서
# 점수가 80점 이상인 것들만 확인해서 평균을 구하겠다.
# 90이 넘으면 리스트에 담겠다.

# 점수가 80점 이상인 것들만 확인해서 평균을 구하는 함수.
def get_average(grades):
    count = 0
    total = 0
    for grade in grades:
        if grade >= 80:
            count +=1
            total += grade

    if count == 0:
        return None            
    
    return total / count
            
def get_average(grades):
    grades = [grade for grade in grades if grade >= 80]

    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)


top_students = []
for student in students:
    name = student['name']
    grades = student['grades']
    average_over_80 = get_average(grades)

    if average_over_80 == None:
        continue

    if average_over_80 >= 90:
        top_students.append(name)
print(top_students)
