// 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수
// 자릿수를 동일 자릿수로 맞추었을 때 더 큰 수로 정렬

class Solution {
    fun solution(numbers: IntArray): String {
        var answer = ""
        
        answer = numbers .map { it.toString() } // 각 원소 문자열로 변환
            .sortedWith { a, b -> // 정렬
                (b + a).compareTo(a + b)
            }
            .joinToString("") // 하나로 합치기
        
        if(answer[0] == '0') answer= "0"
        
        return answer
    }
}