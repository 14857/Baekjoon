// 문자열 a,b의 길이가 최대 100,000 -> Int나 Long으로는 변환 불가능(NumberFormatException)
// BigInteger : 자릿수 제한이 사실상 없는 정수형 클래스
import java.math.BigInteger

class Solution {
    fun solution(a: String, b: String): String {
        var answer: String = ""
        
        answer = (BigInteger(a) + BigInteger(b)).toString()
        
        return answer
    }
}