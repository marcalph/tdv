package main

import (
	"fmt"
)

func main() {
	// walrus operator tolerated because inside a function
	message := fmt.Sprintf("Hello, world!")
	fmt.Println(message)
}