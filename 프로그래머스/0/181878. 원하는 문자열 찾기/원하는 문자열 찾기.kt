class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        
        var myString_l = myString.lowercase()
        var pat_l = pat.lowercase()
        
        answer = if(pat_l in myString_l) 1 else 0
        
        return answer
    }
}