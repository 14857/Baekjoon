class Solution {
    fun solution(arr: IntArray, query: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        answer = arr
        
        for (i in query.indices){
            if(i%2 == 0){
                answer = answer.slice(0..query[i]).toIntArray()
                //println(answer.contentToString()) // query 처리 후 확인
            }else{
                answer = answer.slice(query[i] until answer.size).toIntArray()
                //println(answer.contentToString()) // query 처리 후 확인
            }
        }
        
        return answer
    }
}