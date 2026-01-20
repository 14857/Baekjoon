class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        
        answer = kotlin.math.abs(a - b)
        
        if(a%2 == 1 || b%2 == 1){
            if(a%2 == 1 && b%2 == 1){
                answer = a*a + b*b

            }else{ answer = 2*(a+b)}
            
        }
        
        return answer
    }
}