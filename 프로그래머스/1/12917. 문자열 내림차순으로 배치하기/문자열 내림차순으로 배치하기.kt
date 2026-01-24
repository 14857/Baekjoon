// 문자 단위로 정렬 후 합치기
// toCharArray() + sortedDescending() + joinToString("")

class Solution {
    fun solution(s: String): String {
        var answer = ""
        
        answer = s.toCharArray().sortedDescending().joinToString("")
        
        return answer
    }
}