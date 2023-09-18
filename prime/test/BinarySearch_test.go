package test

import (
	"testing"

	"github.com/abdulrahman-02/Algorithms/prime/src"
)

func TestBinarySearch(t *testing.T) {
	array := []int{1, 2, 3, 4, 5}
	target := 5
	expected := true

	actual := src.BinarySearch(array, target)
	if actual != expected {
		t.Errorf("Expected %v, got %v", expected, actual)
	}
}
