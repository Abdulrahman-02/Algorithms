package src

func LinearSearch(array []int, target int) bool {
	for i := range array {
		if array[i] == target {
			return true
		}
	}
	return false
}
