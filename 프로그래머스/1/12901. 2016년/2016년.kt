class Solution {
    fun solution(a: Int, b: Int): String {
        var answer = ""
        var cnt = b
        var months = arrayOf(0,31,29,31,30,31,30,31,31,30,31,30,31)
        var days = arrayOf("THU","FRI","SAT","SUN","MON","TUE","WED")
        
        for(i in  1..a-1){
            cnt += months[i]
        }
                
        answer = days[cnt%7]
        
        return answer
    }
}