class Solution {
    fun solution(myString: String): List<String> {
        var answer: List<String> = listOf<String>()
        
        // 앞뒤 x 제거 + x 연속되는 경우 고려 + 정렬
        answer = myString.trim('x').split(Regex("x+")).sorted()
        
        return answer
    }
}