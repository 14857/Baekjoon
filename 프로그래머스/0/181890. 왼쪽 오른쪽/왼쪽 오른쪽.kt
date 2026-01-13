// 먼저 나오는 문자열 "l" -> "l" 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트
// 먼저 나오는 문자열 "r" -> "r" 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트
// "l"이나 "r"이 없다면 빈 리스트를 반환

class Solution {
    fun solution(str_list: Array<String>): List<String> {
        var answer: List<String> = listOf<String>()

        if("l" in str_list || "r" in str_list){
            var char = str_list.indexOfFirst{it == "l" || it == "r"}
            
            if (str_list[char] == "l"){
                answer = str_list.slice(0 until char)
            }
            else if (str_list[char] == "r"){
                answer = str_list.slice(char+1 until str_list.size)
            }
        }
        
        return answer
    }
}