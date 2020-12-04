# 자료 구조 해시 테이블로 만들면 서치하기 더 편하지 않을까?

# id 값 가진 importance 요소 서치
# 해당 id importance 값 추출 및 해당 subordinates 재 서치
# 해당 id 값들 다시 서치 후 value 추출

# 정답 sol

# employees 값에서 id가 key 이고 값이 employees 인 dictonary 생성
# 객체에서 해당 id 값 가진 stack 생성
# stack에서 pop 으로 제거 및 추출 후 해당 값에서 importance 추출 및 subortinates 값 stack 에 삽입 반복
# totalImp return

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {e.id: e for e in employees}

        stack = [emp[id]]
        totalImp = 0

        while stack:
            e = stack.pop()
            totalImp += e.importance
            for s in e.subordinates:
                stack.append(emp[s])
        return totalImp
