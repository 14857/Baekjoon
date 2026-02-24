class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var odd = 0
        var even = 0
        
        for(i in num_list){
            if(i % 2 == 0) even++
            else odd++
        }
        
        answer += even
        answer += odd
        
        return answer
    }
}