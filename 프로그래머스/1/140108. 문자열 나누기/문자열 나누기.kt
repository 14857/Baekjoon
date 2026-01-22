// 문자열 자르지 않는 방식( slice 사용 x)

class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        var x = s[0]
        var x_cnt = 0
        var x_not = 0
        
        for(i in s.indices){
            if(x_cnt == x_not && x_cnt != 0){
                x = s[i] // 문자열을 자를 필요 x
                answer++ 
                x_cnt = 0
                x_not = 0
            }
            
            if (s[i] == x) x_cnt++
            else x_not++       
        }
        
        answer++ // 마지막 남은 word
        return answer
    }
}