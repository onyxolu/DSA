def string_maker(student1, student2):
    return student1 + "," + student2 if student1 < student2 else student2 + "," + student1

def student_pairs(student_course_pairs):

    reverse_map = dict()
    result = dict()
    seen_students = set()

    for student, classname in student_course_pairs:
        if student not in seen_students:
            if len(seen_students) >= 1:
                for s in seen_students:
                    result[string_maker(student, s)] = []
            seen_students.add(student)


    for student, classname in student_course_pairs:
        if classname in reverse_map:
            for s in reverse_map[classname]:
                result[string_maker(student, s)].append(classname)
            reverse_map[classname].append(student)
        else:
            reverse_map[classname] = [student]

    return result
student_course_pairs_1 = [
["58", "Linear Algebra"],
["94", "Art History"],
["94", "Operating Systems"],
["17", "Software Design"],
["58", "Mechanics"],
["58", "Economics"],
["17", "Linear Algebra"],
["17", "Political Science"],
["94", "Economics"],
["25", "Economics"],
["58", "Software Design"],
]

print(student_pairs(student_course_pairs_1))