class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stude_pref = [0, 0]
        # sandos = [0, 0]
        for i in range(len(students)):
            stude_pref[students[i]] += 1
        for i in range(len(sandwiches)):
            if stude_pref[sandwiches[i]] > 0:
                stude_pref[sandwiches[i]] -= 1
            else:
                return sum(stude_pref)

        return 0
        
        

