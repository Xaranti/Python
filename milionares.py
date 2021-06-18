#Milionerzy
import random
lifeline = {1:"50/50",2:"Ask a friend",3:"Double tap"}

def chose_answer():
    print ("Choose answer 'a','b','c','d' or 'lifeline' ")
    myChoice = input("I choose: ")
    if (choosing.get(myChoice))==choosing.get(a4):
        print("Well done, it't right answer")
        won= price[i]
        print("Till now You won: ",won)
    elif myChoice in ('a','b','c','d'):
        print("Wrong answer mate, game over")
        quit()
    elif myChoice=='lifeline':
        try:
            print (lifeline)
            lifeline_chose = input("Choose a lifeline: 1,2,3 or type anythin else to return: ")
            if lifeline_chose=='1':
                lifeline.pop(1)
                print("Answers left:")
                print(a1, ' - ',choosing[(a1)])
                print(a4, ' - ',choosing[(a4)])
                print ("Choose answer: ")
                myChoice = input("I choose: ")
                if (choosing.get(myChoice))==choosing.get(a4):
                    print("Well done, it't right answer")
                    won= price[i]
                    print("Till now You won: ",won)
                    return None
                else:
                    print("Wrong answer mate, game over")
                    quit()
            elif lifeline_chose=='2':
                lifeline.pop(2)
                print("You have asked Your friend...")
                friend = random.randint(0,100)
                if friend>=33:
                    print("Friend: 'I think right answer will be",a4)
                    #chose_answer()
                else:
                    print("Friend: 'I think right answer will be",random.choice(toChoose))
                    #chose_answer()
            if lifeline_chose=='3':
                lifeline.pop(3)
                print("You have two tries now!")
                print ("Choose answer 'a','b','c' or 'd'")
                myChoice = input("I choose: ")
                if (choosing.get(myChoice))==choosing.get(a4):
                    print("Well done, it't right answer")
                    won= price[i]
                    print("Till now You won: ",won)
                else:
                    print("Wrong answer, last try")
                    chose_answer()
            else:
                chose_answer()
        except:
            print("This lifeline was used")
            chose_answer()
    else:
        chose_answer()
   

EasyOnes = ["Third number of Fibonacci numbers is: ","Which actor played the role of Harry Potter",\
"Which was it NOT a programin language","End the joke: '6 is afraid of 7 becouse:'",\
"What mean SQL?"]
Answer1 = [0,"Statham","C++",'7 is bigger','Standard Quality Language']
Answer2 = [2,'Grint',"C","6 is afraid of everything","Sequenced Query Language"]
Answer3 = [3,"Karolak","C#","7 is psycho","System Quality Laboratory"]
AnswerTrue = [1,"Radcliff","C+",'7 8 9','Structured Query Language']
price=[500,1000,2000,5000,10000,20000,40000,75000,150000,225000,500000,1000000]
toChoose = ['a','b','c','d']
won = 0

for i in range(len(EasyOnes)):
    question = EasyOnes.index(random.choice(EasyOnes))
    q1=EasyOnes[question]
    print("Question %d: %s" % (i+1,q1))
    answers = toChoose.copy()
    a1 = random.choice(answers)
    answers.remove(a1)
    a2 = random.choice(answers)
    answers.remove(a2)
    a3 = random.choice(answers)
    answers.remove(a3)
    a4 = random.choice(answers)
    answers.remove(a4)
    choosing = {a1:Answer1[question],a2:Answer2[question],a3:Answer3[question],a4:AnswerTrue[question]}
    #print(Answer1[question])
    Answer1.pop(question)
    Answer2.pop(question)
    Answer3.pop(question)
    AnswerTrue.pop(question)
    EasyOnes.pop(question)
    for x, y in sorted(choosing.items()):
        print(x," - ", y)
    chose_answer()

