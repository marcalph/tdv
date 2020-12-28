package main
import "fmt"

// O(n^2) time O(1) space
func first_try(array []int, target int) []int{
	for i1, _ := range array[:len(array)-1] {
		for i2 := i1+1; i2<len(array); i2++ {
			if array[i1]+array[i2] == target {
				return []int{array[i1], array[i2]}
			}
		}
	}
	return []int{}
}

// hash table!!
// O(n) time, O(n) space
func solution(array []int, target int) []int{
	nums := map[int]bool{}
	for _, num := range array {
		candidate := target - num
		if _, found := nums[candidate]; found{
			return []int{candidate, num}
		}
		nums[num] = true
	}
	return []int{}
}



// double for loop
func main(){
	array:=[]int{3,5,-4,8,11,1,-1,6}
	target:=10
	res:=first_try(array, target)
	fmt.Println(res)
	res=solution(array, target)
	fmt.Println(res)
}