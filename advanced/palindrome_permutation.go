package main


import "fmt"


func permute(a []rune, s int, e int) {
	if s == e {
		fmt.Println(a)
	} else {
		for i := s; i <= e; i++ {
			a[s], a[i] = a[i], a[s]
			permute(a, s+1, e)
			a[s], a[i] = a[i], a[s]
		}
	}
}


func main(){
	permute([]rune("ab"),0, 1)
}