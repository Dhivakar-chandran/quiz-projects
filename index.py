player=input('do you want to play?  ')

if player.lower() != 'yes':
    quit()

print ('ok lets play')

score =0

question=input('what is the national bird ')
if question.lower() == 'peacock':
    print ('correct')
    score+=1
else:
    print ('incorrect')

question=input('what is the national animal ')
if question.lower() == 'tiger':
    print ('correct')
    score+=1
else:
    print ('incorrect')

question=input('what is the national flower ')
if question.lower() == 'lotus':
    print ('correct')
    score+=1
else:
    print ('incorrect')

question=input('what is the national tree ')
if question.lower() == 'ashoka':
    print ('correct')
    score+=1
else:
    print ('incorrect')

print ('your score is ' + str(score))