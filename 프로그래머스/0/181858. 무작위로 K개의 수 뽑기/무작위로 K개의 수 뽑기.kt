class Solution {
    fun solution(arr: IntArray, k: Int): IntArray {
        var answer: IntArray = intArrayOf()
        answer = arr.distinct().toIntArray()
        
        if (answer.size < k){
            repeat(k-answer.size){
                answer += intArrayOf(-1)
            }
        }else{
            answer = answer.slice(0..k-1).toIntArray()
        }
        
        
        return answer
    }
}