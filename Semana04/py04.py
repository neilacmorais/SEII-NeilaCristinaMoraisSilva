courses = ['hisory', 'math', 'physics', 'compsci']
print(courses)

print(len(courses))

print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])


courses.append('art')
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.insert(0, 'art')
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses_2 = ['art', 'education']
courses.extend(courses_2)
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.remove('math')
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.pop()
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
pop = courses.pop()
print(pop)
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.reverse()
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.sort(reverse=True)
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)
print(nums)

courses = ['hisory', 'math', 'physics', 'compsci']
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

nums = [1, 5, 2, 4, 3]
print(min(nums))

nums = [1, 5, 2, 4, 3]
print(max(nums))

nums = [1, 5, 2, 4, 3]
print(sum(nums))

courses = ['hisory', 'math', 'physics', 'compsci']
print(courses.index('compsci'))

courses = ['hisory', 'math', 'physics', 'compsci']
print('art' in courses)
print('math' in courses)

for index, item in enumerate(courses):
	print(index, item)

for index, item in enumerate(courses):
	print(index)
	print(item)

for index, item in enumerate(courses, start=1):
	print(index, item)


courses = ['hisory', 'math', 'physics', 'compsci']
courses_str = ', '.join(courses)
print(courses_str)

courses = ['hisory', 'math', 'physics', 'compsci']
courses_str = ' - '.join(courses)
print(courses_str)

new_list = courses_str.split(' - ')
print(new_list)

list_1 = ['hisory', 'math', 'physics', 'compsci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'art'
print(list_1)
print(list_2)

#tuples
tuple_1 = ('hisory', 'math', 'physics', 'compsci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

#get an error
#list_1[0] = 'art'
print(tuple_1)
print(tuple_2)

#sets
cs_courses = {'hisory', 'math', 'physics', 'compsci'}
print(cs_courses)

cs_courses = {'hisory', 'math', 'physics', 'compsci', 'math'}
print(cs_courses)

cs_courses = {'hisory', 'math', 'physics', 'compsci'}
print('math' in cs_courses)

cs_courses = {'hisory', 'math', 'physics', 'compsci'}
art_courses = {'hisory', 'math', 'art', 'design'}
print(cs_courses.intersection(art_courses))	

cs_courses = {'hisory', 'math', 'physics', 'compsci'}
art_courses = {'hisory', 'math', 'art', 'design'}
print(cs_courses.difference(art_courses))	

cs_courses = {'hisory', 'math', 'physics', 'compsci'}
art_courses = {'hisory', 'math', 'art', 'design'}
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
print(type(empty_set))
empty_set = {} #This it's wrong. This is a dict.
print(type(empty_set))
