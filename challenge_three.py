class StringGenerator:
    def __init__(self, N):
        self.N = N

    def generate_string(self):
        if self.N % 2 == 0:
            # If N is even, create a string with pairs of letters
            half_N = self.N // 2
            letters = [chr(ord('a') + i) * 2 for i in range(half_N)]
            return ''.join(letters)
        else:
            # If N is odd, create a string with pairs of letters and one additional letter
            half_N = self.N // 2
            letters = [chr(ord('a') + i) * 2 for i in range(half_N)]
            return ''.join(letters) + chr(ord('a') + half_N)

# Examples
generator1 = StringGenerator(3)
print(generator1.generate_string())   # Output: "aab"

generator2 = StringGenerator(5)
print(generator2.generate_string())   # Output: "aabb"

generator3 = StringGenerator(30)
print(generator3.generate_string())  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
