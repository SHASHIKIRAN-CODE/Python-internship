# quiz game
print ("--------------------------")
print("WELCOME TO QUIZ GAME")
questions = ("Who is known as the father of World Wide Web ?",
             "What programming language is primarily used for web development on the front ",
             "Which data structures uses last in,first out(LIFO)method ?",
             "What is the term for the physical compnent of a computer syatem ?",
             "Which protocol is used to send EMAIL messages ?",
             )

options =(("A.Steve Jobs","B.Tim Berners-Lee","C.Bill Gates","D.Mark Andreenssen"),
          ("A.Python","B.Java","C.HTML/CSS","D.C++"),
          ("A.Queue","B.Array","C.Stack","D.Linked list"),
          ("A.Software","B.Firmware","C.Hardware","D.Middleware"),
          ("A.FTP","B.SMTP","C.HTTP","D.POP3")
          )

answers = ("B","C","C","C","B")
guesses =[]
score = 0
question_num = 0


for question in questions :
    print ("--------------------------")
    print(question)
    for option in options[question_num]:
      print (option)

    guess = input ("ENTER YOUR ANSWER : ").upper()
     
    if guess==answers[question_num]:
       score += 1
       print("CORRECT ANSWER")
    else :
       print("INCORRECT")
       print(f"correct answer is : {answers[question_num]}")
        
    question_num+=1

print (f"YOUR SCORE IS :",score)
score = int(score/len(questions)*100)
print (f"TOTAL PERCENTSGE : {score}%")


      

