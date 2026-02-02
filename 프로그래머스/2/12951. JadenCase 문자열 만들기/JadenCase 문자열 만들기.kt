// JadenCase : 각 단어의 첫 글자는 대문자, 나머지 글자는 전부 소문자로 만드는 문자열 포맷
// Kotlin의 split()은 List<String>(읽기 전용 리스트)를 반환 -> .toMutableList() 또는 map 사용

class Solution {
    fun solution(s: String): String {
        var answer = ""
        var words = s.lowercase().split(" ").toMutableList()
        
        for(i in words.indices){
            var word = words[i]
            
            if(word.isNotEmpty() && word[0].isLowerCase()){
                words[i] = word[0].uppercaseChar() + word.substring(1)
            }
        }   
        answer = words.joinToString(" ")
        return answer
    }
}