class Solution {
    fun solution(picture: Array<String>, k: Int): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        for(p in picture){
            // 가로 k배 늘리기
            var tmp = p.replace(".",".".repeat(k))
            tmp = tmp.replace("x","x".repeat(k))
            
            // 세로 k배 늘리기
            repeat(k){
                answer += tmp
            }
            
        }
        
        return answer
    }
}