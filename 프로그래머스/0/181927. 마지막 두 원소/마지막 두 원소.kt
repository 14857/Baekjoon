class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        val last = num_list[num_list.size - 1]
        val secondLast = num_list[num_list.size - 2]

        return if (last > secondLast) {
            num_list + (last - secondLast)
        } else {
            num_list + (last * 2)
        }
        
        answer = num_list
        return answer
    }
}