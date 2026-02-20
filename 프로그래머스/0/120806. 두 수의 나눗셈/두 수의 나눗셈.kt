// num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 

class Solution {
    fun solution(num1: Int, num2: Int): Int {
        var answer: Int = 0
        
        answer = ((num1.toDouble()/num2) * 1000).toInt()
        
        return answer
    }
}