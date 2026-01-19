// num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트 반환

class Solution {
    fun solution(num_list: IntArray): List<Int> {
        
        var answer = (num_list.sorted().take(5))
    
        return answer
    }
}