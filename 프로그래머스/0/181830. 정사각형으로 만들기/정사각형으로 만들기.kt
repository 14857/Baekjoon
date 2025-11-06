class Solution {
    fun solution(arr: Array<IntArray>): Array<IntArray> {
        var answer: Array<IntArray> = arrayOf<IntArray>()
        
        var num1 = arr.size
        var num2 = arr[0].size
        
        if (num1>num2){ // 각각 요소에 0 추가
            
            answer = arr
            
            for (i in 0 until answer.size){
             answer[i] = answer[i] + IntArray(num1-num2) {0}
                
            }
        }else{ // 마지막에 0으로만 구성된 array 추가
          //  answer += arr[i]
            answer = arr
            repeat(num2-num1){answer += IntArray(num2) {0}}
            
        }
        
        return answer
    }
}