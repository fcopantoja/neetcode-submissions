class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = defaultdict(int)
        res = len(students)

        for student in students:
            counts[student] += 1
        
        for s in sandwiches:
            if counts[s] > 0:
                counts[s] -= 1
                res -= 1
            else:
                break
        
        return res