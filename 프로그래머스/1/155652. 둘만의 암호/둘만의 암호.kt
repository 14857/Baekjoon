// 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꾼다
// index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다
// skip에 있는 알파벳은 제외하고 건너뛴다

class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        var answer: String = ""
          
        for(char in s){
            var change = char
            var cnt = 0
            
            while(cnt < index){
                change++
                if (change > 'z') change = 'a' // z를 넘어갈 경우 다시 a로
                if (change !in skip) { // skip에 없는 경우 진행
                    cnt++
                }
            }
            answer += change
        }       
        return answer
    }
}