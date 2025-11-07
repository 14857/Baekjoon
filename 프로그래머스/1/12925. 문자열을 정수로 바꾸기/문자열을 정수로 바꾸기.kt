class Solution {
    fun solution(s: String): Int {
        var answer = 0
        
        if(s[0] == '+'){
            answer = s.substring(1).toInt()
        }else if(s[0] == '-'){
            answer = -s.substring(1).toInt()
        }else{
            answer = s.toInt()
        }
        
        return answer
    }
}