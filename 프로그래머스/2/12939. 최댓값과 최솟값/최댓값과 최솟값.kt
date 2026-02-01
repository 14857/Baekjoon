//  str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환
class Solution {
    fun solution(s: String): String {
        var answer = ""
        var num_list = s.split(" ")

        answer = num_list.minOf{ it.toInt() }.toString() + " " + num_list.maxOf{ it.toInt() }.toString()
        
        
        return answer
    }
}