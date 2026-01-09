class Solution {
    fun solution(my_string: String, is_prefix: String): Int {
        var answer: Int = 0
        
        if(my_string.length >= is_prefix.length){
            var prefix = my_string.substring(0,is_prefix.length)
        
            if(prefix == is_prefix){
                answer = 1
            }
        }
        
        
        return answer
    }
}