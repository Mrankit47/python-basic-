# WAF to count the number of vowels in a string
def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1

    return count


string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))