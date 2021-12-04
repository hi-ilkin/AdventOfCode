package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func binaryArray2Int(val []string) int64 {
	// source https://stackoverflow.com/a/37533144/4379029
	s := strings.Trim(strings.Join(val, ""), "[]")
	res, err := strconv.ParseInt(s, 2, 64)
	if err != nil {
		fmt.Println(err)
	}
	return res

}

// probably there is a better way of applying bitwise not directly
func bitwiseNot(arr []string) []string {
	for pos, value := range arr {
		if string(value) == "1" {
			arr[pos] = "0"
		} else {
			arr[pos] = "1"
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

		for pos, char := range scanned_val {
			char := string(char)
			if char == "0" {
				msb_tracker[pos]--
			} else if char == "1" {
				msb_tracker[pos]++
			} else {
				fmt.Println(pos, char)
				continue
			}
		}
		scanned_val = scanner.Text()
	}

	msb_value := make([]string, size)
	for pos, value := range msb_tracker {
		if value > 0 {
			msb_value[pos] = "1"
		} else {
			msb_value[pos] = "0"
		}
	}
	fmt.Println(msb_tracker)
	fmt.Println(msb_value)
	gamma := binaryArray2Int(msb_value)
	epsilon := binaryArray2Int(bitwiseNot(msb_value))
	power_consumption := gamma * epsilon

	fmt.Printf("Power consumption is : %d (gamma=%d,  epsilon=%d)", power_consumption, gamma, epsilon)
	return power_consumption
}

func get_data(scanner *bufio.Scanner) []string {
	var data []string
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	return data
}

func get_bit(data []string, pos int, mode string) string {

	counter := 0
	for _, value := range data {
		char := string(value[pos])
		if char == "1" {
			counter += 1
		} else {
			counter -= 1
		}
	}

	if mode == "O2" {
		if counter >= 0 {
			return "1"
		} else {
			return "0"
		}
	} else { // CO2 mode
		if counter < 0 {
			return "1"
		} else {
			return "0"
		}
	}
}

func get_valid_list(data []string, pos int, msb string) []string {
	var valid_list []string
	for _, value := range data {
		value := string(value)
		if string(value[pos]) == msb {
			valid_list = append(valid_list, value)
		}
	}
	return valid_list
}

func get_ratings(data []string, item_size int) (string, string) {

	o2_list := data
	co2_list := data

	for i := 0; i < item_size; i++ {

		if len(o2_list) > 1 {
			msb := get_bit(o2_list, i, "O2")
			o2_list = get_valid_list(o2_list, i, msb)
		}

		if len(co2_list) > 1 {
			lsb := get_bit(co2_list, i, "CO2")
			co2_list = get_valid_list(co2_list, i, lsb)
		}
	}
	return o2_list[0], co2_list[0]
}

func solve_part_2(scanner *bufio.Scanner) int64 {
	data := get_data(scanner)
	size := len(data[0])

	o2, co2 := get_ratings(data, size)
	o2_rating := binaryArray2Int(strings.Split(o2, ""))
	co2_rating := binaryArray2Int(strings.Split(co2, ""))
	life_support_rating := o2_rating * co2_rating

	fmt.Printf("O2 rating: %d, co2 rating: %d, life support rating: %d", o2_rating, co2_rating, life_support_rating)

	return 0
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	solve_part_2(scanner)

}
