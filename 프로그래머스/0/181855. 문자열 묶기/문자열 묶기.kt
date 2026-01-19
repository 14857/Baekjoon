// strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기 반환

class Solution {
    fun solution(strArr: Array<String>): Int {
        var answer: Int = 0
        var map = mutableMapOf<Int, Int>() // 타입 명시 필요
        
        for (s in strArr) {
            val len = s.length
            map[len] = map.getOrDefault(len, 0) + 1
        }
        
        answer = map.values.maxOrNull()?: 0
        
        return answer
    }
}