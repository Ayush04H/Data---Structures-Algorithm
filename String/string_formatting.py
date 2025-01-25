name = 'ABC'
course = 'XYZ'
s1 = 'Welcome %s to %s'%(name,course)
s2 = 'Welcome {0} to {1}'.format(name,course)
s3 = f'Welcome {name} to {course}'
print(s1)
print(s2)
print(s3)