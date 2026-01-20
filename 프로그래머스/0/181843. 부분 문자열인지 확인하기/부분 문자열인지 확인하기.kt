class Solution {
    fun solution(my_string: String, target: String): Int {
        var answer: Int = 0
        
        answer = if(target in my_string) 1 else 0
        
        return answer
    }
}