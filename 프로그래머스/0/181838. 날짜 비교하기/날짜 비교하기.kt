class Solution {
    fun solution(date1: IntArray, date2: IntArray): Int {
        var answer: Int = 0
        var date_1 = ((date1[0] * 12 + date1[1]) * 31 + date1[2])
        var date_2 = ((date2[0] * 12 + date2[1]) * 31 + date2[2])
        
        answer = if(date_1 < date_2) 1 else 0
        
        return answer
    }
}