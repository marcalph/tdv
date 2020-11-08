package main

import (
	"fmt"
	"encoding/json"
)


func main() {
	var jsonMap map[string]string
	jsonMap = make(map[string]string)
	var str1, str2 string
	fmt.Println("please enter name:")
	fmt.Scanln(&str1)
	jsonMap["name"] = str1
	fmt.Println("please enter address:")
	fmt.Scanln(&str2)
	jsonMap["address"] = str2
	jsonObject, _ := json.Marshal(jsonMap)
	fmt.Println(string(jsonObject))
}