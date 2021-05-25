# O(n), O(1)
def hasSingleCycle(array):
    # Write your code here.
    fast, slow = 0, 0
	seen = set()
	print(array)
	print("****")
	for _ in array:
		slow = update(slow, array)
		seen.add(slow)
	return len(seen)==len(array)

def update(idx, array):
	idx += array[idx]
	idx = idx%len(array)
	return idx