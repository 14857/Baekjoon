class Solution {
    fun solution(numbers: IntArray): Int {
        var answer: Int = 0
        
        for(i in 0..9){
            if(i !in numbers) answer += i
        }
        
        if(answer == 0) answer = -1
        
        return answer
    }
}