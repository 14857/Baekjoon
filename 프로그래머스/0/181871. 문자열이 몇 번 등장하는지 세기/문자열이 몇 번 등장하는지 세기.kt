//indexOf(pat, idx) : idx 위치부터 문자열(pat)을 다시 검색

class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var idx = 0
        
        while(true){
            idx = myString.indexOf(pat, idx)
            if (idx == -1) {break}
            answer++
            idx++
        }
        
        return answer
    }
}