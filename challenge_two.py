class MaxDigitSumPair:
    def __init__(self, A):
        self.A = A

    def digit_sum(self, number):
        return sum(int(digit) for digit in str(number))

    def find_max_sum_pair(self):
        digit_sums = {}
        max_sum = -1

        for num in self.A:
            sum_digits = self.digit_sum(num)

            if sum_digits in digit_sums:
                pair_sum = num + digit_sums[sum_digits]
                max_sum = max(max_sum, pair_sum)
            else:
                digit_sums[sum_digits] = num

        return max_sum

# Examples
A1 = [51, 71, 17, 42]
pair_finder1 = MaxDigitSumPair(A1)
print(pair_finder1.find_max_sum_pair())  # Output: 93

A2 = [42, 33, 60]
pair_finder2 = MaxDigitSumPair(A2)
print(pair_finder2.find_max_sum_pair())  # Output: 102

A3 = [51, 32, 43]
pair_finder3 = MaxDigitSumPair(A3)
print(pair_finder3.find_max_sum_pair())  # Output: -1
