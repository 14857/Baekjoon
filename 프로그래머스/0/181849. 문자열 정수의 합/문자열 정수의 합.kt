class Solution {
    fun solution(num_str: String): Int {
        var answer: Int = 0
        
        for(i in num_str){ 
            answer += i.toInt() - 48
        }
        
        return answer
    }
}