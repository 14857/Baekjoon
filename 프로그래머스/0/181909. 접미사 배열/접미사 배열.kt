class Solution {
    fun solution(my_string: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        // my_string의 모든 접미사
        for (i in 0..my_string.length -1){
            answer += my_string.substring(i)
        }
        
        // 접미사 사전 순으로 정렬
        answer.sort()
        
        return answer
    }
}