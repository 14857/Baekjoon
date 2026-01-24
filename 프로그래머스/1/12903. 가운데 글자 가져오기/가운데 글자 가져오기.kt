// 단어 s의 가운데 글자를 반환
// 단어의 길이가 짝수인 경우 두글자 반환

class Solution {
    fun solution(s: String): String {
        var answer = ""
        
        if(s.length%2 == 0) answer = s.substring(s.length / 2 - 1, s.length / 2 + 1)
        else answer = s.substring((s.length-1)/2,(s.length-1)/2+1)
        
        return answer
    }
}