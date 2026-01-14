class Solution {
    fun solution(names: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        for (i in names.indices step 5){
            answer += names[i]
        }
        
        return answer
    }
}