class Solution {
    fun solution(number: String): Int {
        var answer: Int = 0
        
        var lst = number.toList() // 각 자릿수가 Char -> 변환 필요
        answer = lst.sumOf{it.digitToInt()}  % 9 // .digitToInt() 사용하여  int로 변경

        return answer
    }
}