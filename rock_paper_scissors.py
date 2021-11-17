''' # **Challenge 2 Datacademy @Platzi**

#**Rock, Paper or Scissors**
This is a game that I was never good at, but that doesn't mean making a show is difficult. 
Write a program that takes as a parameter "rock", "paper", or "scissors" and determine whether player 1 or player 2 won.

** Bonus: determines that the winner is the player who wins 2 out of 3 matches. **

Example: ppt ("rock", "paper") -> "The winner is player 2." 

Rules:
1.The stone crushes the scissors. (The stone wins.)
2.The scissors cut the paper. (The scissors wins.)
3.The paper wraps the stone. (He wins the role.)
4.In the event of a tie (two players choosing the same element or three players each choosing a different object), the game is played again.

**
Op1	Op2	J1	J2	
1	1	0	0	Repite
1	2	0	1	
1	3	1	0	
2	1	1	0	
2	2	0	0	Repite
2	3	0	1	
3	1	0	1	
3	2	1	0	
3	3	0	0	Repite

**
'''
##Start YMR 05/09/2021

#Who Wins in the game
def who_win (option_gamer_1, option_gamer_2):
    options = ['11','12','13','21','22','23','31','32','33']
    results = ['00','01','10','10','00','01','01','10','00']
    concat_gamer = option_gamer_1 + option_gamer_2
    for i in range (9):
        if concat_gamer == options[i]:
            result_end= results[i]
            break    
        else:
            i +=1
            continue
    ##print("-----------------------" + result_end)
    return result_end

#Main method
def main ():
#Game
        game = 1
        while game <= 3:
            
            score_gamer_1  = 0
            score_gamer_2  = 0
            option_gamer_1 = 0
            option_gamer_2 = 0
            msg = """
            Por favor Jugador digite su opción:
            Piedra:1
            Papel :2
            Tijera:3
            """
            option_gamer_1 = input(f'-> JUGADOR 1 {msg}')
            option_gamer_2 = input(f'-> JUGADOR 2 {msg}')
            winner = who_win (option_gamer_1, option_gamer_2)
            if winner == '01':
                score_gamer_1 =+1
                game = game + 1
            elif winner == "10":
                score_gamer_2 +=1
                game = game + 1
            else:
                print ('Juego Tabla')
        if score_gamer_1 > score_gamer_2:
            print("El Ganador de este juego es el Jugador 1")
        else:
            print("El Ganador de este juego es el Juagador 2")

if __name__ == '__main__':
        main()

##End   YMR 05/09/2021