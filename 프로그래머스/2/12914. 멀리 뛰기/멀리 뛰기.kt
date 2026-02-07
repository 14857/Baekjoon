// 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법 / 1234567 반환

class Solution {
    fun solution(n: Int): Long {
        var answer: Long = 0
        
        if(n <= 2){ return n.toLong() }
        
        // 3 이상인 경우
        var methods = LongArray(n+1){0}
        methods[1] = 1
        methods[2] = 2
        
        for(i in 3..n){
            methods[i] = (methods[i-1] + methods[i-2]) % 1234567
        }

        answer = methods[n].toLong()
   
        return answer
    }
}