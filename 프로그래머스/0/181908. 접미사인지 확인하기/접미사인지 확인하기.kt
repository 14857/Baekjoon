// 접미사 여부 확인
// is_suffix 길이와 동일한 my_string의 접미사를 찾아 동일한지 판단
class Solution {
    fun solution(my_string: String, is_suffix: String): Int {
        var answer: Int = 0
        
        if (my_string.length >= is_suffix.length){
            var suffix = my_string.substring(my_string.length - is_suffix.length)

            if (suffix == is_suffix){
                answer = 1
            }
        }
        
        
        return answer
    }
}