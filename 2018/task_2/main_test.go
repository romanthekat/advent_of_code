package main

import (
	"fmt"
	"testing"
)

func TestFirst(t *testing.T) {
	input := []string{
		"abcdef",
		"bababc",
		"abbcde",
		"abcccd",
		"aabcdd",
		"abcdee",
		"ababab",
	}
	result := solveFirst(input)

	checkResult(t, result, 12)
}

//func TestSecond(t *testing.T) {
//	input := []string{
//		"abcdef",
//		"bababc",
//		"abbcde",
//		"abcccd",
//		"aabcdd",
//		"abcdee",
//		"ababab",
//	}
//	result := solveFirst(input)
//
//	checkResult(t, result, 12)
//}

func checkResult(t *testing.T, actualResult int, requiredResult int) {
	t.Helper()

	if actualResult != requiredResult {
		t.Error(fmt.Printf("checksum must be %+v, but: %+v", requiredResult, actualResult))
	}
}
