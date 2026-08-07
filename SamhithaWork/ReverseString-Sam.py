s = "samhitha"
letters = list(s)
left = 0
right = len(letters) - 1
while left < right:
    letters[left], letters[right] = letters[right], letters[left]
    left = left + 1
    right = right - 1
reversed_string = "".join(letters)
print(reversed_string)
