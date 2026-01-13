class Solution {
    fun solution(arr: IntArray, intervals: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        
        for (i in intervals){
            //println(arr.sliceArray(i[0]..i[1]).contentToString())
            answer += arr.sliceArray(i[0]..i[1])
        }
        
        return answer
    }
}