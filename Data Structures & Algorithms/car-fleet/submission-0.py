class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n < 2:
            return n

        cars = [(pos, s) for pos, s in zip(position, speed)]
        cars.sort()

        # if time_to_target is strictly decreasing -> n fleets
        time_to_target = []
        for pos, s in cars:
            time_to_target.append( (target - pos) / s)
        
        fleets = n

        print(time_to_target)
        # Whenever car catches up -> fleet - 1
        next_fleet = time_to_target[-1]
        for i in range(n - 2, -1, -1):

            # Car catches up
            if time_to_target[i] <= next_fleet:
                fleets -= 1
            else:
                next_fleet = time_to_target[i]
        
        return fleets
        

        