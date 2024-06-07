# Sorting in the dictionary
nba_players = {                            # Creation an NBA players dictionary
    "James Harden": [2191, 2818, 2335],    # Key is name ones and list with average points per year
    "Lebron James": [2251, 1505, 1698],
    "Damian Lillard": [1962, 2067, 2009],
}

for name, points in nba_players.items():   # Iteration on the key and value dictionary
    average_result = sum(points) / len(points)   # Calculating the average points per three years
    print(f"{name} {int(average_result)}")       # Output the value through f-string
