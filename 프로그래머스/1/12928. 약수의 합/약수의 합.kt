class Solution {
    fun solution(n: Int): Int {
        var answer = 0
       
        for (i in 1 until n+1){
            if (n%i == 0){
               // print(i)
                answer += i
            }
            
               
        } 
        
        return answer
    }
}