def reverse_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    reversed_arr = reverse_array(arr)
    print("Reversed array:", reversed_arr)