from random import sample
print('A GAME OF KNOWLEDGE')
name = input('enter your name: ')
print(name + ' WELCOME TO THE QUIZ GAME')
num_score = 0
def quiz(num_score):
    questions = ['Who was the legendary Benedictine monk who invented champagne ?',
                 'Name the largest freshwater lake in the world ?',
                 'Where would you find the Sea of Tranquility ?',
                 'What item of clothing was named after its Scottish inventor ?',
                 'What kind of weapon is a falchion ?',
                 'Which word goes before vest, beans and quartet ?',
                 'What is another word for lexicon ?',
                 'Name the seventh planet from the sun.',
                 'Who invented the rabies vaccination ?',
                 'What is the diameter of Earth ?',
                 'Name the largest ocean in the world.',
                 'What is the capital city of Spain ?',
                 'Which country is Prague in ?',
                 'Who played Neo in The Matrix ?',
                 'Name the only footballer to have played for Liverpool, Everton, Manchester City and Manchester United.',
                 'Who was called the divine ponytail in football ?',
                 'In needlework, what does UFO refer to ?',
                 'What is John Leach famous for making ?',
                 'When was William Shakespeare born ?',
                 'Who was the architect who designed the Millennium Dome ?']
    answer_list = ['dom perignon',
                   'lake superior',
                   'the moon',
                   'mackintosh',
                   'sword',
                   'String',
                   'dictionary',
                   'uranus',
                   'louis pateur',
                   '8000 miles',
                   'pacific ocean',
                   'madrid',
                   'czech republic',
                   'keanu reeves',
                   'peter beardsley',
                   'roberto baggio',
                   'unfinished project',
                   'pottery',
                   '23 april 1564',
                   'robert rogers']
    x=sample(questions,10)
    for i in range(len(x)):
        a=input(x[i]).lower()
        index = questions.index(x[i])
        correct_answer = answer_list[index]
        if a == correct_answer:
           num_score+=1 
           print('You are correct')
        else:
            print('You are wrong  ')
            print(f' The correct answer is {correct_answer} .')
    print(f"You got {num_score} out of 10")         
quiz(num_score)         

s = input("Would you like to play again").lower()
if s == "yes":
   quiz(num_score)
else:
    exit()

