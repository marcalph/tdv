/* You have n candies, the ith candy is of type candies[i].
   You want to distribute the candies equally between a sister and a brother so that each of them gets n   / 2 candies (n is even). The sister loves to collect different types of candies, so you want to give  her the maximum number of different types of candies.
   Return the maximum number of different types of candies you can give to the sister.
*/
package main

import (
	"fmt"
)

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func distribute(candies []int)  int{
	var set map[int]bool
	set = make(map[int]bool)
	for _, elt := range candies {
		set[elt] = true
	}
	fmt.Println(candies)
	return int(min(len(set), len(candies)/2))
}

func main() {
	candies := []int{1,1,2,3}
	fmt.Println(candies)
	fmt.Println(distribute(candies))

	candies = []int{1,1}
	fmt.Println(candies)
	fmt.Println(distribute(candies))

	candies = []int{1,11}
	fmt.Println(candies)
	fmt.Println(distribute(candies))
}