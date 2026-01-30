// a - z >  97 - 122
// A - Z > 65 - 90

class Solution {
    fun solution(s: String, n: Int): String {
        var answer = ""
        
        for(i in s){
            
            // 공백인 경우
            if(i == ' '){
                answer += i
            }
            // 글자이고 알파벳 한바퀴를 넘은 경우 
            else{     
                if(i.isUpperCase()) answer += ((i - 'A' + n) % 26 + 'A'.code).toChar()
                else if(i.isLowerCase()) answer += ((i - 'a' + n) % 26 + 'a'.code).toChar()
            }
        }
        
        return answer
    }
}