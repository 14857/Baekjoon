// 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 반환
// 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단

class Solution {
    fun solution(s: String): String {
        var answer = ""       
        var words = s.replace(' ','@').split('@')
        
        for (word_idx in words.indices){ // 단어별로 판단
            if(words[word_idx].isEmpty()){
                answer += ' '
            }
            
            else{
                for(i in words[word_idx].indices){
                    if(i%2 == 0) answer += words[word_idx][i].uppercase()
                    else answer += words[word_idx][i].lowercase()
                }
                answer += ' '
            }
         
        }
        answer = answer.dropLast(1)
        return answer
    }
}