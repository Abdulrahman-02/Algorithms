package src

func BinarySearch(array []int, target int) bool {
	left := 0
	right := len(array) - 1

	for left < right {
		mid := (left + right) / 2
		if array[mid] == target {
			return true
		} else if array[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return false
}
