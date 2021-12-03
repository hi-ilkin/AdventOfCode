package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)


func binaryArray2Int(val []int) int64 {
	// source https://stackoverflow.com/a/37533144/4379029
	s := strings.Trim(strings.Join(strings.Split(fmt.Sprint(val), " "), ""), "[]")
	res, err := strconv.ParseInt(s, 2, 64)
	if err != nil {
		fmt.Println(err)
	}
	return res

}

// probably there is a better way of applying bitwise not directly
func bitwiseNot(arr []int) []int{
	for pos, value := range arr{
		if value == 1{
			arr[pos] = 0
		}else{
			arr[pos] = 1
		}
	}
	return arr
}

func solve_part_1(scanner *bufio.Scanner) int64 {

	scanner.Scan()
	scanned_val := scanner.Text()
	size := len(scanned_val)
	msb_tracker := make([]int, size)

	for scanner.Scan() {

		for pos, char := range scanned_val{
			char := string(char)
			if char == "0"{
				msb_tracker[pos] --
			} else if char == "1"{
				msb_tracker[pos] ++
			} else {
				fmt.Println(pos, char)
				continue
			}
		}
		scanned_val = scanner.Text()
	}

	for pos, value := range msb_tracker{
		if value > 0{
			msb_tracker[pos] = 1
		} else {
			msb_tracker[pos] = 0
		}
	}
	gamma := binaryArray2Int(msb_tracker)
	epsilon := binaryArray2Int(bitwiseNot(msb_tracker))
	power_consumption := gamma*epsilon

	fmt.Printf("Power consumption is : %d (gamma=%d,  epsilon=%d)", power_consumption, gamma, epsilon)
	return power_consumption
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	solve_part_1(scanner)
	
}
