class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        num_list.sort()
        answer = num_list.drop(5).toIntArray() // drop 의 반환타입은 List<Int>
        
        return answer
    }
}