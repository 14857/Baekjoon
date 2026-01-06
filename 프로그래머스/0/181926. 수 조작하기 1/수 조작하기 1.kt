// 수 조작하기
// 각 문자에 따라 n의 값 바꾸기

class Solution {
    fun solution(n: Int, control: String): Int {
        var answer: Int = n
        
        for (i in control){
            if (i == 'w'){
                answer += 1
            }
            else if(i == 's'){
                answer -= 1
            }
            else if(i == 'd'){
                answer += 10
            }
            else if(i == 'a'){
                answer -= 10
            }
        }
        
        return answer
    }
}