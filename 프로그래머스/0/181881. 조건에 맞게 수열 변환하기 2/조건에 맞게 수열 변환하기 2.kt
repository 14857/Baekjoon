class Solution {
    fun solution(arr: IntArray): Int {
        var answer: Int = 0 
 
        for (i in arr) {
            var cnt = 0
            var num = i

            while (true) {
                if (num >= 50 && num % 2 == 0) {
                    num /= 2
                } else if (num < 50 && num % 2 == 1) {
                    num = num * 2 + 1
                } else { // 더이상 바뀌지 않는 경우
                    break
                }
                cnt++
            }
            answer = maxOf(answer, cnt)
        }
        return answer
    }
}