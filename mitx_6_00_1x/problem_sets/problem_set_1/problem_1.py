vowel_count = 0
for c in s:
    if c in 'aeiou':
        vowel_count += 1
        
print('Number of vowels: ' + str(vowel_count))