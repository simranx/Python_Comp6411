from stringDatabase import StringDatabase
from game import Game


class Guess:
    """
    @author: Simranjeet Singh

    This is the main class which is the entry point. It contains the main menu of the project.
    """

    database = StringDatabase()

    listOfGames = [] #List of games
    letterFrequency = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97,
                       'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99,
                       's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}
    #This variable stores the frequecies of characters

    def calculate_score(self,game,currentGuess):

        """
        This method is created to calculate the score of each game played by the user.
        The score initializes with 0 and gets updated after each function of the menu.
        It returns the score in the end.
        """

        score = 0.00                    #Initialize score
        for i in range(len(game.word)):
            if currentGuess[i] == '_':
                score += self.letterFrequency.get(game.word[i])  #Add the frequency value of unfound characters to score
        if game.numOfRounds>0:
            score = score/game.numOfRounds
        score = score*(1-game.badGuess/10) #10% score decreased for wrong guesses
        return score

    def main_menu(self):

        """
        This method is created to display the main menu as specified in the Assignment.
        It shows the current guessed letters along with a menu which gives 4 options for the user to choose from.
        """

        flag = True # For the main program
        print('** The great guessing game **')
        print('')
        while flag:
            selectedWord = self.database.select_new_word()
            # print(selectedWord)

            currentGuess = '____'
            userChoice = ''
            flagRound = True #For each game
            gamePlayed = Game()
            gamePlayed.word = selectedWord
            while flagRound:
                print('Current Guess : ', currentGuess)
                print()
                print('g = guess, t = tell me, l for a letter, and q to quit')
                userChoice = input() #Input menu choice
                if userChoice=='g':
                    userGuess = input('Enter your guess: ')  #Enter the four letter word you have guessed
                    if userGuess==selectedWord:
                        flagRound = False #End game
                        #calculateScore
                        gamePlayed.score = self.calculate_score(gamePlayed,currentGuess)
                        gamePlayed.status = 'Success'
                        self.listOfGames.append(gamePlayed)
                        print('You made right guess. The word is : ', selectedWord)
                        print()
                    else:
                        flagRound = True
                        gamePlayed.badGuess += 1
                        print('Sorry!!! Your guess is not correct. Please try again.')
                        print()
                elif userChoice=='t':

                    #Score is being calculated after the choice
                    gamePlayed.score = 0-self.calculate_score(gamePlayed,currentGuess)
                    flagRound = False #Current game finished
                    gamePlayed.status = 'Gave Up'
                    self.listOfGames.append(gamePlayed)
                    print('The right word is : ', selectedWord)
                    print()
                elif userChoice=='l':
                    gamePlayed.numOfRounds += 1
                    userLetter = input('Enter a letter: ') #letter input
                    if selectedWord.count(userLetter)>0:
                        count = selectedWord.count(userLetter) #variable to store number of letters correctly guessed.
                        print('You found ', count, ' letters')
                        print()
                        tempString = ''
                        for i in range(len(selectedWord)):
                            if selectedWord[i] == userLetter:
                                tempString += userLetter
                            else:
                                tempString += currentGuess[i] #add the correctly guessed letter to initial string
                        currentGuess = tempString
                        if currentGuess == selectedWord: #if all letters guessed correctly, round stops
                            flagRound = False

                            gamePlayed.score = self.calculate_score(gamePlayed,currentGuess) #score is being calculated
                            gamePlayed.status = 'Success'
                            self.listOfGames.append(gamePlayed)
                            print('You made right guess. The word is : ', selectedWord)
                            print()
                    else:
                        gamePlayed.missedLetters += 1 #wrong guess
                        print('The letter you entered is not part of the word. Try again!!!')
                        print()
                elif userChoice =='q':
                    flagRound=False #not necessary but still good practice to make this false first
                    flag = False #quit everything and print score
                    gamePlayed.status = 'Quit   '
                    self.listOfGames.append(gamePlayed)
                else:
                    print('Please enter correct choice from the displayed menu.') #for all other choices
                    print()
        #Printing the computed scores

        print('Game\tWord\tStatus \t  Bad Guesses \t Missed Letters\t  Score')
        print()
        print('----\t----\t------ \t  ----------- \t --------------\t  -----')
        print()
        itr = 1
        totalScore = 0.00
        for g in self.listOfGames:
            print(itr, '\t', g.word, ' ', g.status, ' ', g.badGuess, '\t\t ', g.missedLetters, '\t\t  ', float(g.score))
            print()
            itr += 1
            totalScore += g.score #summation of all scores in the end

        print('Final score: ', float(totalScore))
        print()


guessObj = Guess()
guessObj.main_menu()



