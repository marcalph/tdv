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
- map := map[string]int {"answer":42}