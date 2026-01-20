class Solution {
    fun solution(str1: String, str2: String): Int {
        var answer: Int = 0
        
        answer = if(str1 in str2) 1 else 0
        
        return answer
    }
}