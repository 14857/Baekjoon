// 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴

class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var F_lst = MutableList(n+1){0} 
        F_lst[1] = 1
        
        if(n >= 2){
            for(i in 2..n){
                F_lst[i] = (F_lst[i-1] + F_lst[i-2]) % 1234567
            }  
        }

        answer = F_lst[n]
        return answer
    }
}