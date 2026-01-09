class Solution {
    fun solution(my_strings: Array<String>, parts: Array<IntArray>): String {
        var answer: String = ""
        
        for ((idx,q) in parts.withIndex()){
            answer += my_strings[idx].substring(q[0],q[1]+1)
        }
        
        
        return answer
    }
}