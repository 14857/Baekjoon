// trim() : 앞뒤 공백 제거
// \\s+ : 공백 1개 이상 (스페이스, 탭 포함) -> \s는 공백 문자 의미, +는 반복 의미
// Regex : 문자열의 패턴을 표현하는 문법

class Solution {
    fun solution(my_string: String): List<String> {
        var answer: List<String> = listOf<String>()
        
        // 문장 앞 뒤 공백 제거 + 연속된 공백을 하나로 묶어 split
        answer =  my_string.trim().split(Regex("\\s+"))
        
        return answer
    }
}