#pirate game

print('Welcome To Sharks And Pirates')
print('This Game Is Licensed Under The MIT Creator License')
print('If You Want The Source Code Please Vist anmoymouse89076 On Github')

#gettings the name
greeting = input('Hello, Possible Pirate! What Is The Password')
if greeting in ('Arrr!'):
	print('Go Away Annoying Pirate')
else:
	print('Welcome, Pirate Hater!')

name = input('Sorry, My Memory Is Like A Godlfish!, I Cant Remember Anything!, Anyway Whats Your Name!')
print('Cool Name!', name)

print('Alrigth', name, 'Lets Get Going, We Dont Want To Be Late')

piratehead = input('Watch Out, There Is Pirates Ahead, What Do We Do? NO. 1 Do you Try To Avoid Them, NO. 2 Do You Go Up To Them And Tell Them How Much You Hate Them')


if piratehead in ('1'):
	print('Lets Go! This Way')
else:
	print('WARNING! If We Do This They Could Capture Us')

#if answer = 2
print('I Told You!')
print('Aaaaaa, Their Chasing Us!')

do = input('What Do We Do')
if do in ('go back'):
	print('Alight, Thats Probally Safer')
	print('This Way!')

if do in('fight them'):
	print('hmmm.... Okay, I mean i dont know')
	
usure = input('Are You Sure You Want To Goahead', name)
if usure in ('yes'):
	print('Okay Dont, Say I Didnt Warn You!!')
	print('Dont Forget, They Probally Have Weapons')
	print('aaaaaaa!')
	print('They Cutted My Hand, Im Going!')
	print('Bye, Bye!')

if usure in ('no'):
	print('Lets Go Back To Option One')

piratehead = input('Watch Out, There Is Pirates Ahead, What Do We Do? NO. 1 Do you Try To Avoid Them, NO. 2 Dont Do Anythin And Go Back?')

if piratehead in ('1'):
	print('Alright, GET LOW!!')
	print('look There Is A Bush')
	print('Lets Hide Behind It')

	print('Ohhh, No!')
	print('They Found Us!')
	print('Lets Run')

ishark = input('Is That A Shark I See?')
if ishark in ('yes'):
	print('Lets Try To Avoid It')

if ishark in ('no'):
	print('Yeah, It Probally Just My Imagination')


print('Ohhh, No!')
print('It Was A Shark And It Got Me!')
print('Bye, Bye')



print('THANKS FOR PLAYING SHARKS AND PIRATES')



