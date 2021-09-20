"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# TC: O(n)
# SC: O(n)

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        if employees is None:
            return 0
        emp = {}
        imp = 0
        for e in employees:
            emp[e.id] = e
        que = deque([])
        #root = que.popleft()
        que.append(id)
        while( len(que) > 0):
            cur_id = que.popleft()
            cur_e = emp[cur_id]
            imp = imp + cur_e.importance
            subs = cur_e.subordinates
            if subs is not None:
                for s in subs:
                    que.append(s)
                    
        return imp
