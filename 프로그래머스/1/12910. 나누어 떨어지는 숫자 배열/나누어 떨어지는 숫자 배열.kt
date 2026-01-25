class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var answer = intArrayOf()
        
        for(i in arr){
            if(i % divisor == 0) answer += i
        }
        
        if(answer.size == 0) answer = intArrayOf(-1)
        else answer = answer.sorted().toIntArray()
        
        return answer
    }
}