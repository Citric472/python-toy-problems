class BrickArrangement:
    def __init__(self, A):
        self.A = A
        self.N = len(A)

    def moves_needed(self):
        total_bricks = sum(self.A)

        if total_bricks % self.N != 0:
            return -1  # It's not possible to have exactly 10 bricks in each box

        target_bricks = total_bricks // self.N
        moves = 0
        accumulated_bricks = 0

        for bricks in self.A:
            diff = bricks - target_bricks
            accumulated_bricks += diff

            # If accumulated_bricks is positive, it means we have excess bricks, and we need moves to distribute them
            # If it's negative, it means we need to take bricks from the next box
            moves += abs(accumulated_bricks)

        return moves

# Example usage:
A1 = [7, 15, 10, 8]
arrangement1 = BrickArrangement(A1)
print(arrangement1.moves_needed())  # Output: 7

A2 = [11, 10, 8, 12, 8, 10, 11]
arrangement2 = BrickArrangement(A2)
print(arrangement2.moves_needed())  # Output: 6

A3 = [7, 14, 10]
arrangement3 = BrickArrangement(A3)
print(arrangement3.moves_needed())  # Output: -1
