class Solution {
    fun solution(s: String): Boolean {
        var answer = false
        
        if (s.length == 6 || s.length == 4 ){
            if (s.all{it.isDigit()} == true){
                return true
            }else{
                return false
            }
        }
        
        return answer
    }
}