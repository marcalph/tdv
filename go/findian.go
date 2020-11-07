package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main() {
	// walrus operator tolerated because inside a function
	var scanstr string
	fmt.Println("Please enter string")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	scanstr = scanner.Text()
	str := strings.ToLower(scanstr)
	switch {
	case strings.HasPrefix(str, "i") && strings.Contains(str, "a") && strings.HasSuffix(str, "n"):
		fmt.Println("Found!")
	default:
		fmt.Println("Not Found!")
	}
}