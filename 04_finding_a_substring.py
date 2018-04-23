sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops') 
query_two = sentence.index('oops')

print(query) # => -1
print(query_two) # => error
# find will return an negative if value is not included in the string
# index will return an error

query = 'oops' in sentence

print(query) # => false

query = 'quick' in sentence

print(query) # => true