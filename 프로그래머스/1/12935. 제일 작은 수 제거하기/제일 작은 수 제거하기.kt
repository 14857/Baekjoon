class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer = intArrayOf(-1)
 
        if(arr.size > 1){
            answer = arr.filter{ it != arr.minOrNull()!! }.toIntArray()
        }
        
        return answer
    }
}