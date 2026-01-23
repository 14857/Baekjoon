// Char.toInt()가 숫자값이 아니라 문자 코드 반환 -> 123이 1,2,3이 아닌 49,50,51
// .digitToInt() 사용

class Solution {
    fun solution(n: Int): Int {
        var answer = 0

        for(i in n.toString()){
            answer += i.digitToInt()
        }

        return answer
    }
}