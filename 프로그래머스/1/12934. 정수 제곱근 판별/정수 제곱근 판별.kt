import kotlin.math.sqrt
class Solution {
    fun solution(n: Long): Long {
        var answer: Long = 0
        var cnt = 1L
        
        val root = sqrt(n.toDouble()).toLong()
        return if (root * root == n) (root + 1) * (root + 1) else -1
    }
}