class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        
        // 새 변수를 쓸 때 무조건 선언해야 함
        var ans1 = 2*a*b
        var ans2 = a.toString() + b.toString()
        answer = maxOf(ans1, ans2.toInt())
        
        return answer
    }
}