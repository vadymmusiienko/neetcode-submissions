class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, s) for pos, s in zip(position, speed)]
        cars.sort()
        n = len(cars)

        time_to_target = []
        for pos, s in cars:
            time_to_target.append( (target - pos) / s)
        
        fleets = n

        # Whenever car[i] catches up to car[i+1] -> fleet - 1
        next_fleet = time_to_target[-1]
        for i in range(n - 2, -1, -1):

            # Car caught up
            if time_to_target[i] <= next_fleet:
                fleets -= 1
            else:
                next_fleet = time_to_target[i]
        
        return fleets
        

        