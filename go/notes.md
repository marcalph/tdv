## fmt package


## strings package
- Compare
- Contains
- HasPrefix
- Index
- Replace(s, old, new, n)
- ToUpper, ToLower, TrimSpace


## Strconv package
- Atoi
- Itoa
- FormatFloat(f, fmt, prec, bitSize)
- ParseFloat(s, bitSize)


## Arrays
- var x [5]int
- var y [5]int = [5]{1, 2, 3, 4, 5}
- z := [...]int{1, 2, 3, 4}


## Slices
- sli := []int{1, 2, 3}
- sli = make([]int, 10)
- sli = make([]int, 10, 15)
- sli  = append(sli, 100)

## Maps
- var idMap map [string]int  
  idMap = make(map[string]int)
- idMap := map[string]int {"answer":42}
- idMap["question"] = "?"
- delete(idMap, "answer")
- id, p := idMap["answer"] //id is value, p is prensence ok key
- len(idMap)
- for key, val := range idMap {  
    fmt.Println(key, val)  
}  


## Struct
- type struct Person {  
    name string  
    surname string  
}  
  var p Person