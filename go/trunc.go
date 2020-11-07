package main

import (
	"fmt"
)

func main() {
	// walrus operator tolerated because inside a function
	var number float64
	fmt.Println("Please enter float")
	fmt.Scan(&number)
	transformed := int(number)
	fmt.Println(transformed)
}