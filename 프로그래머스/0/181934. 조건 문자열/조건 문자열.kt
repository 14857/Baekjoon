class Solution {
    fun solution(ineq: String, eq: String, n: Int, m: Int): Int {
        var answer: Int = 0
        
        if (ineq == "<" && eq == "="){
            if(n <= m){
                answer = 1
            }
        }
        else if(ineq == "<" && eq == "!"){
            if(n < m){
                answer = 1
            }
        }
        else if(ineq == ">" && eq == "="){
            if(n >= m){
                answer = 1
            }
        }
        else{
            if(n > m){
                answer = 1
            }
        }
        
        return answer
    }
}