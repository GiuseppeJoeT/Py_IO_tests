f = open('questions.txt', 'r')
'''
We use the OPEN keyword to open a file. The first argument is the FILE_NAME,
the second is the MODE.
'''
lines = f.readlines()

f.close()

print lines


print('')

# Another way of using the file handle is to iterate over it
with open('questions.txt') as f:
    for line in f:
        print line

