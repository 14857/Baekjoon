class Solution {
    fun solution(a: Int, b: Int, c: Int): Int {
        var answer: Int = (a+b+c)*(a*a + b*b + c*c) // 두 숫자만 같은 경우
        
        if (a == b){
            if (b == c){ // 모두 같은 경우의 수
                answer *= (a*a*a + b*b*b + c*c*c)
            }
            
            // 아닌 경우는 a = b / c는 따로
        }
        
        else{ //a != b 인 경우
            if (a != c && b != c){ // 모두 같은 경우의 수
                answer = a+b+c 
            }
        }
        
        
        return answer
    }
}