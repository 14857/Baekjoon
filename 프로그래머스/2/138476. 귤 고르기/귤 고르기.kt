// 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화
// 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값 반환

class Solution {
    fun solution(k: Int, tangerine: IntArray): Int {
        var answer: Int = 0
        val map = mutableMapOf<Int, Int>()
        var left = k
        
        // 귤 크기별 개수
        for(i in tangerine){
             map[i] = map.getOrDefault(i,0) + 1
        }
        
        // 크기별 귤 개수만 뽑아서 내림차순 정렬
        val counts = map.values.sortedDescending()
        
        for(c in counts){
            if(left <= 0 )break
            left -= c
            answer++
        }
       
        return answer
    }
}