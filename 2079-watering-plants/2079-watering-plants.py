class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        capa = capacity
        for i in range(len(plants)):
            steps += 1
            if capa < plants[i]:
                steps += 2*i                
                capa = capacity

            capa -= plants[i]
            
        return steps