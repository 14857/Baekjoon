// 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때
// 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산
// 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없습니다

// 보유한 병의 수 : n = n + (-a+b)(n/a)
// 돌려받는 병의 수 : b*(num/a)

class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer: Int = 0
        var num = n
        
        while(num>=a){
            answer += b*(num/a)
            num += (-a+b)*(num/a)
        }
        
        return answer
    }
}