// 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더한다

class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        
        answer =  arr
        
        for(q in queries){
            for(i in q[0]..q[1]){
                answer[i] += 1
            }
        }
        
        return answer
    }
}