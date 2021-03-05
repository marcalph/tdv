package main
import "fmt"


// O(n) time 0(1) space
func IsValidSubsequence(array []int, sequence []int) bool {
	// Write your code here.
	i2:=0
	for i1,_ :=range array {
		if array[i1]==sequence[i2] {
			if i2+1==len(sequence){
				return true
			}
			if i2<len(sequence) {
				i2++
			}
		}
	}
	return false
}



// double for loop
func main(){
	array:=[]int{5,1,22,25,6,-1,8,10}
	sequence:=[]int{5}
	res:=IsValidSubsequence(array, sequence)
	fmt.Println(res)
}