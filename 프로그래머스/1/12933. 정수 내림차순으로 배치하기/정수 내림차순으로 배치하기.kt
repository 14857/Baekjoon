class Solution {
    fun solution(n: Long): Long {
        var answer: Long = 0
        
        var s = n.toString().toList().sortedDescending().joinToString("")
        // println(s)
        answer = s.toLong()
        return answer
    }
}