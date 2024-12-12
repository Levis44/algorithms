def tournamentWinner(competitions, results):
    idx = 0
    points = {"": 0}
    tournament_winner = ""
    
    for result in results:
        if result == 0:
            winner = competitions[idx][1]
        else:
            winner = competitions[idx][0]

        winner_points = points.setdefault(winner, 0) + 3
        points[winner] = winner_points

        if winner_points > points[tournament_winner]:
            tournament_winner = winner
            
        idx += 1
        
    return tournament_winner

def tournamentWinner_refactor(competitions, results):
    HOME_TEAM_WON = 1
    tournament_winner = ""
    points = {tournament_winner: 0}
    
    for idx, teams in enumerate(competitions):
        homeTeam, awayTeam = teams
        result = results[idx]

        winnerTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        if winnerTeam not in points:
            points[winnerTeam] = 0

        points[winnerTeam] += 3

        if points[winnerTeam] > points[tournament_winner]:
            tournament_winner = winnerTeam
        
    return tournament_winner
