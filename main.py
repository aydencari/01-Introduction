#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print('Hello, my name is Ashley Sutton')
name = ''
count = 0
while (name != 'give me the scoop'):
    name = input("Type: Give me the Scoop to get my questions and answers!")
    name = name.lower().strip()
    count = count + 1 
if(name.lower().strip() == 'give me the scoop'):
    print('What is your name?: Ashley Sutton / What is your favorite game?: Final Fantasy / What concerns do you have about this class?" I have zero programming experience. / What are you excited about (in general)?: Mostly about getting a glimpse at how games are made. / What is your stackoverflow.com user number?: 11991359 / What is the URL to your github.com profile?: https://github.com/aydencari')
else:
    print('Type: Give me the Scoop <-- to receive the answer silly ;p')
print('You guessed it in {0} tries!'.format(count))