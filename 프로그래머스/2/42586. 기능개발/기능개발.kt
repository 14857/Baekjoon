// 각 배포마다 몇 개의 기능이 배포되는지 반환
// 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능

import kotlin.math.ceil

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var fin = MutableList(progresses.size) { 0 }
        
        // 기능별 걸리는 시간
        for(i in progresses.indices){
            fin[i] = ceil((100-progresses[i]) / speeds[i].toDouble()).toInt()
        }
        println(fin)
        
        while (fin.isNotEmpty()) {

            val start = fin[0]
            var count = 1
            var i = 1
            
            while (i < fin.size && fin[i] <= start) {
                count++
                i++
            }
            answer.add(count)

            // 배포된 만큼 제거
            fin = fin.drop(count).toMutableList()

            //println(fin) // 확인용
        }
        
        return answer.toIntArray()
    }
}