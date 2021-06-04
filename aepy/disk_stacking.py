
# O(n^2), O(n)
# find tallest stack od disk with constraints
# dp
# recreating the sequence involved is hard!
def diskStacking(disks):
    # Write your code here.
	disks.sort(key= lambda tup: tup[2])
    
	max_heights = [tup[2] for tup in  disks]
	sequences = [None for _ in disks]
	max_height_idx = 0
	
	for i in range(1, len(disks)):
		current_disk = disks[i] 		# down disk
		for j in range(i):
			other_disk = disks[j]		# up disk
			if is_stacking_possible(other_disk, current_disk):
				if max_heights[i] <= current_disk[2]+max_heights[j]:
					max_heights[i] = current_disk[2]+max_heights[j]
					sequences[i] = j
		if max_heights[i]>=max_heights[max_height_idx]:
			max_height_idx = i
			
	return backtrack_sequence(disks, sequences, max_height_idx)
			
			
def backtrack_sequence(disks, sequences, max_height_idx):
	sequence = []
	while max_height_idx is not None:
		sequence.append(disks[max_height_idx])
		max_height_idx= sequences[max_height_idx]
	return sequence[::-1]

				
				
def is_stacking_possible(disk_up, disk_down):
	wu, du, hu = disk_up
	wd, dd, hd = disk_down
	return wu<wd and du<dd and hu<hd