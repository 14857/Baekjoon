class Solution {
    fun solution(str_list: Array<String>, ex: String): String {
        var answer: String = ""
        
        for(str in str_list){
            if (ex !in str){
                answer += str
            }
        }
        
        return answer
    }
}