def main():
  import random
  print("To play the game, please divide the group into two teams")
  team_1_name = input("Please give the first team a name")
  team_2_name = input("Please give the second team a name")
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum_team_1 = 0
  dice_sum_team_2 = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum_team_1 += roll
    if roll == 1:
      print(f'{team_1_name}:You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'{team_1_name}:You rolled a {roll}! Critical Success!')
    else:
      print(f'{team_1_name}:You rolled a {roll}')
    print(f'{team_1_name}:You have rolled a total of {dice_sum_team_1}')

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum_team_2 += roll
    if roll == 1:
      print(f'{team_2_name}:You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'{team_2_name}:You rolled a {roll}! Critical Success!')
    else:
      print(f'{team_2_name}:You rolled a {roll}')
    print(f'{team_2_name}:You have rolled a total of {dice_sum_team_2}')

  if dice_sum_team_1 > dice_sum_team_2:
    print(f"Congratualations to {team_1_name}!")
  elif dice_sum_team_1 < dice_sum_team_2:
    print(f"Congratualations to {team_2_name}!")
  else:
    print("Tie! Play again!")

if __name__== "__main__":
  main()
