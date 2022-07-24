

nums_of_teams = int(input('Enter the number of teams in the tournament: '))
while nums_of_teams <= 1 :
    print("The minimum number of teams is 2, try again.")
    nums_of_teams = int(input('Enter the number of teams in the tournament: '))

teams  = []
for _ in range(nums_of_teams):
    name = input(f'Enter the name for team #{_ + 1 }: ')
    while len(name) < 2:
        print("Team names must have at least 2 characters, try again.")
        name = input(f'Enter the name for team #{_ + 1}:')
    while len(name.split(" ")) >2:
        print("Team names may have at most 2 words, try again.")
        name = input(f'Enter the name for team #{_ + 1}:')
    teams.append(name)

numbers_of_games = int(input("Enter the number of games played by each team: "))
while numbers_of_games != len(teams) - 1  :
    print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    numbers_of_games = int(input("Enter the number of games played by each team: "))

teams_wins = {}
for team in teams :
    numbers_of_wins = int(input(f"Enter the number of wins Team {team} had:  "))
    while numbers_of_wins  < 0:
        print("The minimum number of wins is 0, try again.")
        numbers_of_wins = int(input(f"Enter the number of wins Team {team} had:  "))
    
    while numbers_of_wins  > len(teams) - 1 :
        print(f"The maximum number of wins is {len(teams) - 1}, try again.")
        numbers_of_wins = int(input(f"Enter the number of wins Team {team} had:  "))
    
    teams_wins[team] = numbers_of_wins
    
print("Generating the games to be played in the first round of the tournament...")
wins = sorted(teams_wins, reverse=True ,key=teams_wins.get)
index = 0
for index in range(int(len(wins)/ 2)):
    print(f"Home : {wins[-1-index]} VS Away : {wins[index]}")
    

