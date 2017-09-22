''' If s is an empty string, that's what should get printed. Otherwise, we can
    assume there is a longest substring and it's value can be initialized to
    the first character of the string
'''
if not s:
    longest = ''
else:
    longest = s[0]

''' Iterators for comparing characters and selecting portions of the string
'''
front_itr = 0
back_itr  = 1

while back_itr < len(s):
    if s[back_itr] >= s[back_itr - 1]:
        ''' If we have found a new longest substring, save it
        '''
        if len(s[front_itr:back_itr + 1]) > len(longest):
            longest = s[front_itr:back_itr + 1]

        back_itr += 1
    else:
        ''' If we've reached the end of an alphabetical substring, reposition
            the iterators
        '''
        front_itr = back_itr
        back_itr += 1

print('Longest substring in alphabetical order is: ' + longest)