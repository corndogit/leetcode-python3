class Solution:
    @staticmethod
    def ship_within_days(weights: list[int], days: int) -> int:
        min_capacity = max(weights)
        max_capacity = sum(weights) // 2
        curr_capacity = min_capacity  # find how many days it takes to ship using a ship of current capacity
        exceeded_max_capacity = False

        while not exceeded_max_capacity:
            curr_days_taken = 1
            curr_weight = 0

            for package in weights:  # find how many days are needed to ship with current capacity
                if curr_weight + package <= curr_capacity:
                    curr_weight += package
                else:
                    curr_days_taken += 1
                    curr_weight = package

            if curr_days_taken <= days:
                return curr_capacity

            # increment current capacity
            curr_capacity += 1

            if curr_capacity > max_capacity:
                exceeded_max_capacity = True

        return max_capacity  # if no smaller answer is found


if __name__ == "__main__":
    ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ex2 = [3, 2, 2, 4, 1, 4]
    ex3 = [1, 2, 3, 1, 1]

    print("ex1: expected output = 15, output =", Solution.ship_within_days(ex1, 5))
    print("ex2: expected output = 6, output =", Solution.ship_within_days(ex2, 3))
    print("ex3: expected output = 3, output =", Solution.ship_within_days(ex3, 4))
