package main

import (
	"testing"
	"fmt"
)

func TestFirst(t *testing.T) {
	result := solveFirst([]int{
		0,
		2,
		7,
		0,
	})

	checkResult(t, result, 5)
}

func TestSecond(t *testing.T) {
	result := solveSecond([]int{
		0,
		2,
		7,
		0,
	})

	checkResult(t, result, 4)
}

func checkResult(t *testing.T, actualResult int, requiredResult int) {
	t.Helper()

	if actualResult != requiredResult {
		t.Error(fmt.Printf("steps count must be %+v, but: %+v", requiredResult, actualResult))
	}
}
