// set, list의 경우 - 이용해 차집합 계산 가능

class Solution {
    fun solution(arr: IntArray, delete_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        answer =  arr.filter { it !in delete_list }.toIntArray()
        
        return answer
    }
}