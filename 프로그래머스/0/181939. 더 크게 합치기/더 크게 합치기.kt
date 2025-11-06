class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        
        var ans1 = a.toString() + b.toString()
        var ans2 = b.toString() + a.toString()
        
        answer = maxOf(ans1.toInt(),ans2.toInt())
        
        return answer
    }
}