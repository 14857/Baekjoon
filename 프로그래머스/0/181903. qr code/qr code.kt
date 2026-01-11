// 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 순서대로 붙인 문자열

class Solution {
    fun solution(q: Int, r: Int, code: String): String {
        var answer: String = ""

        for(i in r..code.length-1 step q){
            answer += code[i]
        }
        
        return answer
    }
}