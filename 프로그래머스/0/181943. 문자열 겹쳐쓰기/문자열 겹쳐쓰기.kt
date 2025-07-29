class Solution {
    fun solution(my_string: String, overwrite_string: String, s: Int): String {
        var answer: String = ""
        
        answer += my_string.slice(0 until s)
        
        answer += overwrite_string
        
        answer += my_string.slice(s+overwrite_string.length..my_string.length-1)
        
        println(answer)
        
        return answer
    }
}