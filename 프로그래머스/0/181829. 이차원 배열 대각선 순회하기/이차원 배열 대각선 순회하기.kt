// i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 반환

class Solution {
    fun solution(board: Array<IntArray>, k: Int): Int {
        var answer: Int = 0
        
        for(i in board.indices){
            for(j in board[i].indices){
                if(i + j <= k) answer += board[i][j]
            }
        }
        
        return answer
    }
}