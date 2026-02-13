class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var answer = 0
        var items = mutableMapOf<String, Int>()
        var mul = 1
        
        // 의상 종류별 분류
        for(info in clothes){
            items[info[1]] = items.getOrDefault(info[1],0) + 1  
        }
        // println(items)
        
        // 모든 경우의 수 세기
        for(v in items.values){
            mul = mul*(v +1)
        }
        
        // 아무것도 입지 않은 경우 제외
        answer = mul-1
        
        return answer
    }
}