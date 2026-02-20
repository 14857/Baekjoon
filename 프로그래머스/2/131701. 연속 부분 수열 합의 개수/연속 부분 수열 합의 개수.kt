// 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수
// 최대 길이 = elements 크기

class Solution {
    fun solution(elements: IntArray): Int {
        var answer: Int = 0
        var sums = mutableSetOf<Int>()
        var nums = elements + elements
        
        //println(nums)
        
        // 원형 수열 길이별 계산
        for(size in elements.indices){
            var total = 0
            
            for(i in 0..elements.size){
                //println(nums.slice(i..i+size))
                total = nums.slice(i..i+size).sumOf { it }
                //println(total)  
                sums.add(total)
            }
            //println(sums)
            answer =  sums.size
        }
        
        return answer
    }
}