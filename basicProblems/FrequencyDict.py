test = "test@string"

frequency = {
}
for char in set(test):
    frequency[char] = test.count(char)

print(frequency)