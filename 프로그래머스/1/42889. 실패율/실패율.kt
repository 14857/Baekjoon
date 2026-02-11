// 실패율 : 스테이지에 도달 & 클리어하지 못한 플레이어의 수 / 스테이지 도달 플레이어 수
// 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 반환

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        
        val fail = DoubleArray(N)
        var total = stages.size
        
        for (i in 0 until N) {

            val not = stages.count { it == i + 1 }

            fail[i] =
                if (total == 0) 0.0
                else not.toDouble() / total

            total -= not
        }
        
        answer = fail.indices
                .sortedByDescending { fail[it] }
                .map { it + 1 }
                .toIntArray()
        
        
        return answer
    }
}