class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf() // stk
        var i = 0
        
        while(i < arr.size){ // i가 arr의 길이보다 작으면 반복
            if(answer.isEmpty()){
               answer += arr[i]
                i++
            }else if(answer.isNotEmpty() && answer.last() == arr[i]){
                answer = answer.dropLast(1).toIntArray()
                i++
            }else if(answer.isNotEmpty() && answer.last() != arr[i]){
                answer += arr[i]
                i++
            }
        }
        
        if(answer.isEmpty()){ answer = intArrayOf(-1)}
        
        return answer
    }
}