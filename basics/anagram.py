def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")
    
    str1 = "hello"
    str2 = "world"
    print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")