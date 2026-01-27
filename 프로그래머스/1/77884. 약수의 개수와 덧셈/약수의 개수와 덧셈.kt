// left부터 right까지의 모든 수들 중에서, 
// 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 반환
class Solution {
    fun solution(left: Int, right: Int): Int {
        var answer: Int = 0
        
        for(i in left..right){
            var cnt = 0
            
            for(j in 1..i){
                if(i%j == 0) cnt += 1 // 약수의 개수 연산
            }
            
            if(cnt%2 == 0) answer += i
            else answer -= i
            
        }
        
        return answer
    }
}