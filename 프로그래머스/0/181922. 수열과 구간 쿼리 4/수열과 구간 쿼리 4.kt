class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        
        for ((idx,q) in queries.withIndex()){
            var s = q[0]
            var e = q[1]
            var k = q[2]

            for (i in s..e){
                if(i % k == 0){
                    arr[i] += 1
                }
            }
            // println(arr.contentToString()) // 확인용
        }
        answer = arr
        
        return answer
    }
}