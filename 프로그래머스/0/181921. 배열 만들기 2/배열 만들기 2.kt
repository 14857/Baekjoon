// 이진수로 치환해서 생각하기 -> 더 간단하고 편리한 방법
class Solution {
    fun solution(l: Int, r: Int): IntArray {
        //var answer: IntArray = intArrayOf()
         var answer = mutableListOf<Int>()

        val lLen = l.toString().length
        val rLen = r.toString().length
        
        for (len in lLen..rLen) {
            val limit = 1 shl len   // 2^len
            for (mask in 0 until limit) {
                val sb = StringBuilder()
                for (i in len - 1 downTo 0) {
                    sb.append(if (mask and (1 shl i) == 0) '0' else '5')
                }
                val num = sb.toString().toInt()
                if (num in l..r) answer.add(num)
            }
        }

        return if (answer.isEmpty()) intArrayOf(-1)
        else answer.distinct().sorted().toIntArray()
    }
}