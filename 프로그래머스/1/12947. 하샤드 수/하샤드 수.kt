// 하샤드 수 : x의 자릿수의 합으로 x가 나누어지는 수

class Solution {
    fun solution(x: Int): Boolean {
        var answer = true
        var cnt = 0
        
        for(i in x.toString()){
            cnt += i.digitToInt()    
        }
        
        if(x % cnt != 0) answer = false
        
        return answer
    }
}