class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        var runningSum : [Int] = []
        
        for (index, num) in nums.enumerated() {
            if index == 0 {
                runningSum.append(num)
            } else {
                var newNum = runningSum[index - 1] + num
                runningSum.append(newNum)
            }
        }
        return runningSum   
    }
}
