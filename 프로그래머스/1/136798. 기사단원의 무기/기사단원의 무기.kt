class Solution {
    fun solution(number: Int, limit: Int, power: Int): Int {
        var answer: Int = 0
        var nums : MutableList<Int> = mutableListOf()
        
        // 약수의 개수 list 선언
        for (i in 1 until number+1){
            var cnt = 0
            var j = 1
            
            while(j*j <= i){
                if(i%j ==0){
                    cnt += if(j*j == i) 1 else 2
                }
                j++
            }
            nums.add(cnt)
        }
        //println(nums) 
        
        // 공격력 제한수치를 넘는 경우 power로 대체
        for (i in nums.indices){
            if (nums[i] > limit){
                nums[i] = power
            }
        }
        
        //println(nums)
        
        // 전체 합
        answer = nums.sum()
        
        return answer
    }
}