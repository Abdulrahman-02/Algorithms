package test

import (
	"testing"

	"github.com/abdulrahman-02/Algorithms/prime/src"
)

func TestLinearSearch(t *testing.T) {
	array := []int{1, 2, 3, 4, 5}
	target := 3
	expected := true

	actual := src.LinearSearch(array, target)
	if actual != expected {
		t.Errorf("Expected %v, got %v", expected, actual)
	}
}
