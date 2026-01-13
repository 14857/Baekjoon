// num_list의 첫 번째 ~ n 번째 원소 담은 리스트 반환 -> 인덱스 0 ~ n-1

class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        answer = num_list.slice(0..n-1).toIntArray()
        
        return answer
    }
}