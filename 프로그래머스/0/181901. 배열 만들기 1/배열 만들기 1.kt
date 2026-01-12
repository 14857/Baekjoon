class Solution {
    fun solution(n: Int, k: Int): IntArray {
        var answer: IntArray = intArrayOf()
        var num = k
        
        while(num <= n){
            answer += num
            num = num+k
        }
        
        return answer
    }
}