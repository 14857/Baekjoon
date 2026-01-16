class Solution {
    fun solution(myString: String, pat: String): String {
        var answer: String = ""
        
        answer = myString.slice(0..myString.lastIndexOf(pat)+pat.length-1)
        
        return answer
    }
}