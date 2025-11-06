class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        
        if (n%2 == 0){
            // 짝수인 경우 -> n 이하의 모든 양의 정수의 제곱의 합
            for (i in 0 until n+1 step 2){
                answer += i*i
            }
        }
        else{
            // 홀수인 경우 -> n 이하의 홀수인 모든 양의 정수의 합
            for (i in 1 until n+1 step 2){
                answer += i
            }
            
        }
        return answer
    }
}