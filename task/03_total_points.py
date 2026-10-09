def total_points(numbers):
    if not numbers:
        return None
    team_total = 0
    opponent_total = 0
    for num in numbers:
        team_points = int(num.split(":")[0])
        opponent_points = int(num.split(":")[1])
        if team_points > opponent_points:
            team_total += 3
        elif team_points == opponent_points:
            team_total += 1
            opponent_total += 1
        else:
            opponent_total += 3
    return f"{team_total}:{opponent_total}"

match_results = ["2:3", "1:1", "4:2", "0:0", "2:1"]

print(total_points(match_results))