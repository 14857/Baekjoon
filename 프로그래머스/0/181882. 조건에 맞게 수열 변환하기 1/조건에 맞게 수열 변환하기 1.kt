class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        answer = arr
        
        for(idx in answer.indices){
            if(answer[idx] >= 50 && answer[idx]%2 == 0){
                answer[idx] = answer[idx] / 2
            }
            else if(answer[idx] < 50 && answer[idx]%2 == 1){
                answer[idx] = answer[idx] * 2
            }
        }
        
        return answer
    }
}