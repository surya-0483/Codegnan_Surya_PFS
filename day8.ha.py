paragraph="Virat Kohli, who was born on 5th november 1988 is one Greatest Cricketers of All Time. His parents are Prem nath kohli and saroj kohli. He is married to an indian film actress Anushka Sharma and also have 2 children namely Vamika kohli and Akaay kohli."
vowels=['a','e','i','o','u','A','E','I','O','U']
vowels_count=0
consonents_count=0
for i in paragraph:
    if i in vowels:
        vowels_count+=1
    elif i not in vowels and i!="." and i!=" ":
        consonents_count+=1
print(f'The number of vowels in the paragraph are: {vowels_count}')
print(f'The number of consonents in the paragraph are: {consonents_count}')
print(f'The number of spaces in the paragraph are: {paragraph.count(" ")}')
