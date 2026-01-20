class Solution {
    fun solution(num_list: IntArray, n: Int): Int {
        var answer: Int = 0
        
        answer =  if(n in num_list) 1 else 0
        
        return answer
    }
}