class Solution {
    fun solution(n: Int): ArrayList<Int> {
        var answer = ArrayList<Int>() // answer 타입 변경 ->  Mutable 타입 + 크기 자유로움
        
        var x = n
       
        while(x != 1){
            
            answer.add(x)
            
            if(x % 2 == 0){ // 짝수인 경우
                x = x/2
            }
            else{ // 홀수인 경우
                x = x*3 + 1
            }
        }
        
        answer.add(x) // x가 1
        return answer
    }
}