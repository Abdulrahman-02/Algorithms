package test

import (
	"testing"

	"github.com/abdulrahman-02/Algorithms/prime/src"
)

func TestTwoCrystallBalls(t *testing.T) {
	array := []bool{false, false, false, true, true}
	expected := 3

	actual := src.TwoCrystalBalls(array)
	if actual != expected {
		t.Errorf("Expected %v, got %v", expected, actual)
	}
}
