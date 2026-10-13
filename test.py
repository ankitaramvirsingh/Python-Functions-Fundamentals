def student_profile(*args):
    name = args[0]
    age = args[1]
    course = args[2]

    profile = f'''
    Student Profile
    ---------------
    Name:{name}
    Age:{age}
    Course:{course}
'''
    return profile

print(student_profile('Ankita',23,'python'))