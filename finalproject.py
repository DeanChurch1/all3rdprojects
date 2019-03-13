#Dean Church
#FinalProject


class Quiz(object):
    def __init__(self,term,answer,p_answer):
        self.term = term
        self.answer = answer
        self.p_answer = p_answer

    def test(self,term,answer,p_answer):
        correct = answer
        score = 0
        while term:
            # ask a question
            print(term)
            for i in range(4):
                print("\t", i + 1, "-", answer[i])
            # get answer
            p_answer = input("What's your answer?: ")

            # check answer
            if p_answer == correct:
                print("\nRight!")
                score += 1
            else:
                print("\nWrong.")
            print(answer)
            print("Score:", score)


class Flashcard(object):
    def __init__(self,card,term,terms,definition):
        self.card = card
        self.term = term
        self.terms = terms
        self.definition = definition

    def makecard(self,card,term,terms,definition):
        terms = {}
        print("This is your card maker")
        term = input("What is your question: ")
        if term not in terms:
            definition = input("what is your answer")
            terms[term] = definition
        else:
            print("You have already made that word")
            input("Press enter")

    def viewcard(self,card,term,terms):
        print(terms)

def main():

    choice = None
    while choice != "0":
        print("Choose a number")
        print("1: Make a card")
        print("2: Review your cards")
        print("3: Take a practice test")
        print("4: Answer true and false questions")
        choice = input("What would you like to choose")
        if choice == "1":

        elif choice == '2':

        elif choice == '3':

        elif choice == '4':

        else:
            print("Not a good choice")









main()



