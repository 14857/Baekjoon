class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        var answer: Int = 0
        
        for(i in numbers){
            if(answer > n){
                break
            }
            answer += i         
        }
        
        return answer
    }
}