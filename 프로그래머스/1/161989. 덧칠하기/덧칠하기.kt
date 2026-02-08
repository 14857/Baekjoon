// 롤러로 페인트칠해야 하는 최소 횟수 반환
// greedy 알고리즘 -> 처음 페인트칠 하는 위치는 section 처음

class Solution {
    fun solution(n: Int, m: Int, section: IntArray): Int {

        var answer = 0
        var last = 0   // 마지막으로 칠해진 위치

        for (i in section) {
            // 덜 칠한 경우
            if (i > last) {
                last = i + m - 1
                answer++
            }
        }

        return answer
    }
}
