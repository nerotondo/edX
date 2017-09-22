bob_count = 0
front_itr = 0
back_itr  = 3

while back_itr <= len(s):
    if s[front_itr:back_itr] == 'bob':
        bob_count += 1
        
    front_itr += 1
    back_itr  += 1
        
print('Number of times bob occurs is: ' + str(bob_count))