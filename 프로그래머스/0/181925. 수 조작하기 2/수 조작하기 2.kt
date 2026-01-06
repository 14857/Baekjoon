class Solution {
    fun solution(numLog: IntArray): String {
        var answer: String = ""
        
        for (i in 1 until numLog.count()){
            var char = numLog[i]-numLog[i-1]
            answer += if(char == 1) 'w' else if(char == -1) 's' else if(char == 10) 'd' else 'a'
        }
        
        return answer
    }
}