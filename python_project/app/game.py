import random


def test():
  options = ('rock', 'paper', 'scissor')
  user_option = input('rock, paper, scissor =>')
  user_option = user_option.lower()
  print(user_option)
  if not user_option in options:
    print('This selection is not correct')
    return None, None
  computer_option = random.choice(options)
  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  return user_option, computer_option


def check_rules(user_option , computer_option, user_wins, computer_wins):
	if user_option == computer_option:
    print('Tie')
    
  elif  user_option == 'rock':
    if computer_option == 'scissors':
      print('rock win to scissors')
      print ('user win')
      user_wins +=1
    else:
      print ('Paper win to rock')
      print  ('Computer win')
      computer_wins += 1
    
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper win to rock')
      print( 'User win')
      user_wins +=1
    else:
      print('scissors win to paper')
      print ('Computer win ')
      computer_wins += 1
    
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('Scissors win to paper')
      print('user won')
      user_wins +=1
    else:
      print('rock wint against scissors')
      print ('computer win')
          computer_wins += 1
  return user_wins, computer_wins

def run_game ():
	computer_wins = 0
	user_wins = 0
  rounds = 1
	while True:
	
	    print ('*' * 10)
	    print ('ROUNDS', rounds)
	    print ('*' * 10)
	  
	    print ('computer_wins', computer_wins)
	    print ('user_wins', user_wins)
			rounds += 1
	
		  user_option, computer_option = choose_options()
		  user_wins, computer_wins =check_rules(user_option, computer_option, user_wins, computer_wins)
	
	    
	  
	    if computer_wins == 2:
	      print ('The winner is the computer')
	      break
	  
	    if user_wins == 2:
	      print('The winner is the user')
	      break
run_game()