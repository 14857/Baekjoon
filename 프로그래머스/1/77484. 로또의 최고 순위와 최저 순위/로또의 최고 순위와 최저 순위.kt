// 알아볼 수 없는 번호를 0으로 표기
// 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정
// 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 반환

// 맞은 개수가 아니라 순위 -> 7 - match (많이 맞을수록 숫자가 작아짐)

class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        // 0 개수 확인
        val zero = lottos.count{it == 0}
        
        // 맞는 개수 확인
        val match = lottos.count { it in win_nums }
        
  
        // 로또 최고 순위 -> 0으로 표시된 번호가 다 맞는 경우 
        answer += minOf(6, 7 - (match + zero))
        // 로또 최저 순위 -> 0으로 표시된 번호가 다 틀린 경우
        answer += minOf(6, 7 - match)
        
        return answer
    }
}