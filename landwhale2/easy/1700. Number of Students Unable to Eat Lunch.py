class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(sandwiches) > 0:
            if count > len(students):
                break
            
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                students = self.rotate(students, 1)
                count += 1
    
        return len(sandwiches)
    def rotate(self, l, n):
        return l[-n:] + l[:-n]
