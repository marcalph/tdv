def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	cur = [""]*len(phoneNumber)
	res = []
	
	def helper(i, cur, res):
		if i == len(phoneNumber):
			res.append("".join(cur)) # O(n)
		else:
			digit = phoneNumber[i]
			letters = keypad[digit]
			for l in letters:
				cur[i] = l
				helper(i+1, cur, res)
	helper(0, cur, res)
	return res
	

keypad = {
	"1": ["1"],
	"2": ["a","b","c"],
	"3": ["d","e","f"],
	"4": ["g","h","i"],
	"5": ["j","k","l"],
	"6": ["m","n","o"],
	"7": ["p","q","r","s"],
	"8": ["t","u","v"],
	"9": ["w","x","y","z"],
	"0": ["0"]
}