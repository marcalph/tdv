def tournamentWinner(competitions, results):
    # Write your code here.
	scores={}
    for match, res in zip(competitions, results):
		# update scores
		scores[match[0]]= scores.get(match[0],0) + 3 if res else  scores.get(match[0],0) + 0
		scores[match[1]]= scores.get(match[1],0) + 3 if not res else  scores.get(match[1],0) + 0		
	return max(scores, key=scores.get)