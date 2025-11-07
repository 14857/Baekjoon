//  상품을 받을 직원의 수를 return
class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        // 선물 받은 직원의 수
        var answer: Int = 0
        
        
        // 출근 인정 시각
        var admittime : IntArray = intArrayOf()
        for (i in schedules){
            if ( 50 <= i%100 && i%100 < 60){
                var temp = i + 50
                admittime = admittime + temp
            }
            else{
                admittime = admittime +  (i+10)
            }
        }
        
        // print(admittime.contentToString())
        
        // 직원별로 지각 여부 확인 -> 0인 경우 answer += 1  
        for (i in 0 until timelogs.size){
            var late = 0
            var cntday = startday
            
            for (j in timelogs[i]){
                
               // print(cntday)
                
                if (cntday == 6 || cntday == 7){
                    cntday = (cntday % 7) + 1
                }else{
                    if (j > admittime[i]){
                        late += 1
                       // println(j)
                    }
                    cntday = (cntday % 7) + 1
                }
            }        
            
            if (late == 0){
                answer += 1
            }
        }  
        return answer
    }
}