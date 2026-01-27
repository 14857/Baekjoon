class Solution {
    fun solution(k: Int, score: IntArray): IntArray {
        var answer: IntArray = intArrayOf() 
        var top_k : MutableList<Int> = mutableListOf() // 명예의 전당
        
        for(i in score){
            top_k.add(i)
            
            if(top_k.size > k){
                top_k = top_k.sorted().drop(1).toMutableList()
            }
            
            answer += top_k.minOrNull()!!
        }
        
        return answer
    }
}