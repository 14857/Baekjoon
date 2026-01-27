// 자연수 n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수 반환
// toString(3) : 10진수 -> 3진수
// reversed() : 문자열 뒤집기
// toInt(3) : 3진수 -> 10진수

class Solution {
    fun solution(n: Int): Int {

        var answer = n.toString(3).reversed().toInt(3)
        
        return answer
    }
}