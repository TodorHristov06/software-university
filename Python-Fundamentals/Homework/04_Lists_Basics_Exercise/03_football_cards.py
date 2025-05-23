team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
game_terminated = False

players = input().split()
for player in players:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)

    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print("Game was terminated")
    
# team_A = 11
# team_B = 11

# cards = input().split()
# sent_off_players = []

# for card in cards:
#     if card in sent_off_players:
#         continue

#     sent_off_players.append(card)

#     if 'A' in card:
#         team_A -= 1
#     elif 'B' in card:
#         team_B -= 1

#     if team_A < 7 or team_B < 7:
#         print(f'Team A - {team_A}; Team B - {team_B}')
#         print('Game was terminated')
#         break

# if team_A >= 7 and team_B >= 7:
#     print(f'Team A - {team_A}; Team B - {team_B}')
