// 문자열로 접근 하는 것이 아니라 문자 개수 카운팅하기
// 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍 반환

class Solution {
    fun solution(X: String, Y: String): String {
        var answer : String = ""
        var countX = IntArray(10)
        var countY = IntArray(10)
        var result = StringBuilder()
        
        for(i in X){ countX[i - '0']++ } 
        for(i in Y){ countY[i - '0']++ } 
        
        // 큰 수부터 문자열에 추가
        for(i in 9 downTo 0){
            val repeat = minOf(countX[i], countY[i])
            repeat(repeat) {
                result.append(i)
            }
        }
        
        if (result.isEmpty()) return "-1"
        if (result.all { it == '0' }) return "0"
        else{ answer = result.toString()}
        
        return answer
    }
}

