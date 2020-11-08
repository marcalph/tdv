package main

import (
	"fmt"
	"strings"
	"log"
	"bufio"
	"os"
)

type Name struct {
	fname, lname string
}

func main() {
	var fn string
	var res []Name
	var tmp Name
	res = make([]Name, 0)
	fmt.Println("please enter filename (e.g. 'names.txt'):")
	fmt.Scanln(&fn)
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		tmp = Name{
			fname:strings.Split(scanner.Text(), " ")[0], 
			lname:strings.Split(scanner.Text(), " ")[1]}
		res = append(res, tmp)
    }
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
	}
	for i, names := range res {
		fmt.Printf("On line %d \n", i+1)
		fmt.Printf("first name is: %s\nlast name is: %s\n", names.fname, names.lname)
	}
}


