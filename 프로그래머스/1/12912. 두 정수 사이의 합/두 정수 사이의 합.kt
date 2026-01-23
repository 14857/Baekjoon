class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0
        
        for(i in minOf(a,b)..maxOf(a,b)){
            answer += i
        }
        
        return answer
    }
}