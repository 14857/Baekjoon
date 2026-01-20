// trim() / trim(chars) : 문자열 앞뒤의 공백 / 특정 문자 제거
// trimStart() / trimStart(chars) : 문자열 앞의 공백 / 특정 문자 제거
// trimEnd() / trimEnd(chars) : 문자열 뒤의 공백 / 특정 문자 제거

class Solution {
    fun solution(n_str: String): String {
        var answer: String = ""
        
        answer = n_str.trimStart('0')
        
        return answer
    }
}