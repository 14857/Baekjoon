// map 활용

class Solution {
    fun solution(s: String): IntArray {
        var answer = IntArray(s.length)
        var map : MutableMap<Char,Int> = mutableMapOf()
        
        for(idx in s.indices){
            if(s[idx] !in map){
                answer[idx] = -1 
            }else{
                answer[idx] = idx - map[s[idx]]!!
            }
            map[s[idx]] = idx // 값 업데이트
        }
        
        return answer
    }
}