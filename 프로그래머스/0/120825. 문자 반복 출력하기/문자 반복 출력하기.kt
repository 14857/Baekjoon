class Solution {
    fun solution(my_string: String, n: Int): String {
        var answer: String = ""
        var s = StringBuilder()
        
        for(i in my_string){
            repeat(n){
                s.append(i)
            }
        }
        
        answer = s.toString()
        
        return answer
    }
}