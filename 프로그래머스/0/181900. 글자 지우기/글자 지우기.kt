// my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열 반환
// filterIndexed : 요소의 값(value)뿐 아니라 인덱스(index)까지 함께 고려하여 필터링할 때 사용
// 형식 : filterIndexed { index, value -> 조건 }

class Solution {
    fun solution(my_string: String, indices: IntArray): String {
        var answer: String = ""
        
        answer = my_string.filterIndexed { index, _ -> index !in  indices} // 코틀린에는 not in 문법 없음
        
        return answer
    }
}