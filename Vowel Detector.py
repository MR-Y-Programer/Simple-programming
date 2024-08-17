'''detects and counts vowel letters of input and prints them.'''
Value=input('Enter a Word:')
count=0
for j in Value:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
      status='m';print(j);count=count+1
    elif j!='a' and j!='e' and j!='i' and j!='o' and j!='u':
        status='s'
print('you have',count,'Vowel letter')
if status=='s':
   print('please enter a word with vowel letters!')