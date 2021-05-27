# O(n^2), O(1) brute force
# find valid starting point w/ refueling
#def validStartingCity(distances, fuel, mpg):
#    # Write your code here.
#	ncities = len(distances)
#	print(ncities, "***")
#	for s in range(ncities):
#		reservoir = 0
#		for i in range(ncities):
#			print(s, i, (s+i)%ncities)
#			reservoir+=fuel[(i+s)%ncities]*mpg-distances[(i+s)%ncities]
#			print(reservoir)
#			if reservoir<0:
#				print("broke")
#				break
#			if i == ncities-1:
#				return s

# O(n), O(1) greedy 
# because only one good answer ie total distance corresponds to total fuel
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	possible_miles = 0
	min_city = 0
	min_possible_miles = 0
	
	ncities = len(distances)
	
	for i in range(1, ncities):
		distance_from_prev = distances[i-1]
		fuel_from_prev = fuel[i-1]
		
		possible_miles += fuel_from_prev*mpg-distance_from_prev
		
		if possible_miles<min_possible_miles:
			min_possible_miles=possible_miles
			min_city=i
	
	return min_city