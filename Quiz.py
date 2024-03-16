questions  = {'Why is the Earth round?': 'C', 'Why is there a ghost in your room?': 'D'}

options = [['A. It\'s the Earths\'s choice!', 'B. What is Earth?', 'C. It is what it is!', 'D. How would i know?'],
['A. Where is he?', 'B. Oooo! Let me meet him!', 'C. Have you gone insane!', 'D. Let him sit peacefully!']]

print('Welcome to the Quiz Game!')
def new_game():
    correct_guesses = 0
    q_no = 0

    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[q_no]:
            print(i)  

        user_answer = None 
        while user_answer not in ['A','B','C','D']:
            user_answer = input('Enter your answer(a/b/c/d):').upper()

        correct_guesses += check_answer(questions.get(key), user_answer)
        q_no += 1

    show_score(correct_guesses, len(questions))
        
def check_answer(answer, user_answer):
    if user_answer == answer:
        print('Congratulations! You got this one right!')
        return 1
    else:
        print('Oh! Oh! That was incoreect :(')
        return 0

def show_score(correct_guesses, total_questions):
    print(f'You got {correct_guesses} answers correct out of {total_questions} correct!')


def play_again():
    choice = None

    while choice not in ['yes', 'no']:
        choice = input('Do you want to play again?(yes/no):').lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print('Invalid input. Please enter "yes" or "no".')

new_game()
while play_again():
    new_game()

print('Bye, Bye! See you soon!')