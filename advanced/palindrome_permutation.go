package main


import "fmt"


func count(s string) map[rune]int {
	// create hashmap of char frequency from string
	m := make(map[rune]int)
    for _, r := range s {
        m[r]++
	}
	return m
}


var perms []string
func permute(a []rune, s int, e int) []string{
	if s == e {
		perms = append(perms, string(a))
	} else {
		for i := s; i <= e; i++ {
			a[s], a[i] = a[i], a[s]
			permute(a, s+1, e)
			a[s], a[i] = a[i], a[s]
		}
	}
	return perms
}


func reverse(str string) (result string) { 
    for _, v := range str { 
        result = string(v) + result 
    } 
    return
} 


func main(){
	const s string = "abcabcd"
	// m char freq counter for given string s
	m := count(s)
	// chars unique chars in given string
	// cnt check if at most one char has a pair number of occurences
	var runes []rune // runes w/ pair occurence
	var pivot rune
	cnt := 0
	for c, f := range m {
		if f % 2 != 0 {
			cnt++
			pivot = c
			if f>1 {
				for i:=0; i < f/2; i++{
					runes = append(runes, c)
				}	
			}
		}else{
			for i:=0; i < f/2; i++{
				runes = append(runes, c)
			}
		}
	}
	if cnt>1 {
		fmt.Println("impossible")
	} else {
		fmt.Println("possible")
		perms = permute(runes, 0, len(runes)-1)
		fmt.Println(perms)
		fmt.Println("results")
		for _, v := range perms {
			fmt.Println(v+string(pivot)+reverse(v))
		}

	}
}