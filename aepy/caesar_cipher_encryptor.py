# O(n) spacetime
def caesarCipherEncryptor(string, key):
    # Write your code here.
	return "".join([chr((ord(c)-97+key)%26+97) for c in string])
