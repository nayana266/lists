courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[2:])
courses.remove('Math')
print(courses)

course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)

tuple_1 = ['History', 'Math', 'Physics', 'CompSci']
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
