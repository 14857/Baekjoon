class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        if(arr.count{it == 2} == 0){
            answer = intArrayOf(-1)
        }
        else{
            val start = arr.indexOfFirst { it == 2 }
            val end = arr.indexOfLast { it == 2 }
            
            answer += arr.slice(start..end)
        }
        
        
        
        return answer
    }
}