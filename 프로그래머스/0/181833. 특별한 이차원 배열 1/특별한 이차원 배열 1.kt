// n이 매개변수로 주어질 때, n × n 크기의 이차원 배열 arr를 반환

class Solution {
    fun solution(n: Int): Array<IntArray> {
        var answer = Array(n){IntArray(n)}
        
        for(i in 0..n-1){
            answer[i][i] = 1
        }
        
        return answer
    }
}