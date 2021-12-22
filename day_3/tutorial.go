package main

import (
	"errors"
	"fmt"
	"math"
)

func main(){
	fmt.Println("Hello world")

	// variables
	var x int = 5 // same with x := 5
	var y int = x + 5
	fmt.Println(y)

	// conditions, 
	if x > 5  {
		fmt.Println("x is bigger than 6")
	} else if x > 2 {
		fmt.Println("x is bigger than 2")
	} else {
		fmt.Println("x is dumdum")
	}

	// arrays
	var a [5]int
	b := []int{5,3,2,1}
	fmt.Println(a, a[0])
	b = append(b, 0)
	fmt.Println(len(b))

	// maps
	vertices := make(map[string]int)
	vertices["triangle"] = 2
	vertices["square"] = 3
	vertices["dodecagon"] = 12

	delete(vertices, "square")
	fmt.Println(vertices)

	// loops: only for loop is available
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// while loop
	i := 0
	for i > 5 {
		i++
	}
	fmt.Println(i)

	// range loop. you get key instead of index for range map 
	for index, value := range b {
		fmt.Println("Index: ", index, "Value: ", value)
	}

	// go doesn't have error handling
	result, err := sqrt(64)
	
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}
	
	x = 5
	inc(&x)
	fmt.Println(x);

	// struct
	p := person{name: "Ilkin", age: 27}
	fmt.Println(p.name, p.age)

}

// functions, returning multiple values
func sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, errors.New("Undefined for negative numbers")
	} else{
		return math.Sqrt(x), nil
	}
}

// accepting pointer
func inc(x *int){
 *x++
}

// struct
type person struct {
	name string
	age int
}