class Solution {
    fun solution(rank: IntArray, attendance: BooleanArray): Int {
        var answer: Int = 0
        
        val attendList = mutableListOf<MutableList<Int>>()
        
        for (i in 0 until attendance.size){
            if (attendance[i] == true){
                attendList.add(mutableListOf(rank[i],i)) //[순위, 인덱스]
            }
        }
        
        
        //attendList.sort()
        
        attendList.sortBy { it[0] }
        print(attendList)
      
        answer = 10000  * attendList[0][1] + 100 * attendList[1][1] + attendList[2][1]
        
        
        return answer
    }
}