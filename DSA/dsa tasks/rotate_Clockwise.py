def rotate_array(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]


array = list(map(int, input("Enter numbers: ").strip().split()))

steps = int(input("Enter the number of steps to rotate the array clockwise: "))

print("Original array:", array)
print("Array after rotating by", steps, "steps:", rotate_array(array, steps))
