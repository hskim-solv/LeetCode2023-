class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #return sum(abs(seat-student) for seat, student in zip(sorted(seats), sorted(students)))
        
        seats.sort()
        students.sort()
        return sum(abs(e - t) for e, t in zip(seats, students))