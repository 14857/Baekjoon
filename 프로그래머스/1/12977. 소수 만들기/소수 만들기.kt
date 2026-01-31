class Solution {
    
    // 소수 판별 함수
    fun check(num:Int): Int{
        var answer = 1
        
        for(i in 2..num-1){
            if(num%i == 0) answer = 0
            //println("${i} : ${num}")
        }
        
        //println("${num} ${answer}")
        return answer
    }
    
    fun solution(nums: IntArray): Int {
        var answer = 0
 
        for(i in 0 until nums.size){
            for(j in i+1 until nums.size){
                for(k in j+1 until nums.size){
                    answer += check(nums[i]+nums[j]+nums[k])
                    //println("${nums[i]}, ${nums[j]}, ${nums[k]}:  ${nums[i]+nums[j]+nums[k]}")
                }
            }
        }

        return answer
    }
}