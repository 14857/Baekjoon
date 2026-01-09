class Solution {
    fun solution(my_string: String, s: Int, e: Int): String {
        var answer: String = ""
        
        answer += my_string.substring(0,s)
        answer += my_string.substring(s,e+1).reversed()
        answer += my_string.substring(e+1)
        
        return answer
    }
}