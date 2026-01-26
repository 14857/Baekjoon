// 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수

class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()
        
        for(nums in commands){
            var i = nums[0]
            var j = nums[1]
            var k = nums[2]
            var slice_array = array.slice(i-1..j-1).sorted()
            
            answer += slice_array[k-1]
            
        }
        
        
        return answer
    }
}