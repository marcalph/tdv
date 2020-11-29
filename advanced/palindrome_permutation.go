package main


import "fmt"

func Perm(a []rune, f func([]rune)) {
	perm(a, f, 0)
}



func perm(a []rune, f func([]rune), i int) {
	if i > len(a) {
		f(a)
		return
	}
	perm(a, f, i+1)
	for j := i + 1; j < len(a); j++ {
		fmt.Println(a)
		a[i], a[j] = a[j], a[i]
		fmt.Println(a)
		perm(a, f, i+1)
		fmt.Println(a)
		a[i], a[j] = a[j], a[i]
		fmt.Println(a)
    }
}


func main(){
	Perm([]rune("ac"), func(a []rune) {fmt.Println(string(a))})
}