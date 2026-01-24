// 한 상자에 사과를 m개씩 담아 포장
// 상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
// 과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산
// (최저 사과 점수) x (한 상자에 담긴 사과 개수 = m)

// 사과는 상자 단위로만 판매하며, 남는 사과는 버린다

class Solution {
    fun solution(k: Int, m: Int, score: IntArray): Int {
        var answer: Int = 0
        
        // 상자의 개수 -> score.size / m
        // 필요한 최소 사과 개수 -> score.size % m 버리기 
        var for_sale = score.sorted().drop(score.size % m)
        //println(for_sale)
        
        // for_sale에서 m개 원소 중 가장 작은 수
        for_sale.chunked(m).forEach{ chunk ->
            var minValue = chunk.minOrNull()!!
            answer += minValue * m 
        }
        
        return answer
    }
}