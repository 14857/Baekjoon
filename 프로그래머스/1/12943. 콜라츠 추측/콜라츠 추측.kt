// 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
// 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
// 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

class Solution {
    fun solution(num: Int): Int {
        var answer = 0
        var n = num.toLong()
        
        if(n == 1L) return 0
        
        while(n != 1L){
            
            if(answer >= 500){
                answer = -1
                break
            } 
            
            if(n%2L == 0L) n = n/2
            else n = n*3 + 1
            answer++
        }
        
        return answer
    }
}