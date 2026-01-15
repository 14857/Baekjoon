// replace("a", "A") ≠ replace('a', 'A') : 문자열 치환, 문자 치환 차이

class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        
        answer = myString.lowercase()
        answer = answer.replace('a', 'A')
        
        return answer
    }
}