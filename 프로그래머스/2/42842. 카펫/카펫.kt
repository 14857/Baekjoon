// 전체 넓이 : brown + yellow
// brown = 2*w + 2*h - 4 -> (brown + 4) / 2 = w+h
// yellow = (w-2)*(h-2)

// 카펫의 가로, 세로 크기를 순서대로 배열에 담아 반환

import kotlin.math.sqrt
class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        var total = brown + yellow
        
        for (h in 1..sqrt(total.toDouble()).toInt()) {
            
            if (total % h != 0) continue
            val w = total / h
            
            if ((w - 2) * (h - 2) == yellow) {
                answer += w
                answer += h
                break
                }
        }
        
        return answer
    }
}