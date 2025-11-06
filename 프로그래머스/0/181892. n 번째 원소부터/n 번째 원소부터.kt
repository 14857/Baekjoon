class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        for (i in n-1 until num_list.size){
            answer += num_list[i]
        }
        
        return answer
    }
}