// map : 컬렉션(리스트·배열·문자열 등)의 각 요소를 하나씩 다른 값으로 변환해, 새로운 컬렉션을 만드는 함수

class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var change = myString.map{ if (it == 'A') 'B' else if (it == 'B') 'A' else it }.joinToString("")
        
        if(pat in change){ answer = 1}
        
        return answer
    }
}