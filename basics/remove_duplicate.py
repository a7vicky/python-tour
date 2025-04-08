def remove_duplicates(lst):
    return list(set(lst))

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 1, 2, 3]
    print("Original list:", sample_list)
    print("List after removing duplicates:", remove_duplicates(sample_list))