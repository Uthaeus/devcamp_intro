heading = 'Python: An Introduction'

header, _, subheader = heading.partition(': ')

print(header)     # => 'Python'
print(subheader)  # => 'An Introduction'

heading = 'Python: An Introduction'

first, second, third = heading.partition(': ')

print(first)    # => 'Python'
print(second)   # => ':'
print(third)    # => 'An Introduction'

heading = 'Python: An Introduction, and Python: Advanced'

first, second, third = heading.partition(': ')

print(first)    # => Python
print(second)   # => :
print(third)    # => An Introduction, and Python: Advanced