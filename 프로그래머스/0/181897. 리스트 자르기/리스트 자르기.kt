// slicer = [a,b,c]
// n = 1 : num_list의 0 ~ b번 인덱스까지
// n = 2 : num_list의 a ~ 마지막 인덱스까지
// n = 3 : num_list의 a ~ b번 인덱스까지
// n = 4 : num_list의 a ~ b번 인덱스까지 c 간격으로


class Solution {
    fun solution(n: Int, slicer: IntArray, num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        var a = slicer[0]
        var b = slicer[1]
        var c = slicer[2]
        
        when(n){
            1 -> answer = num_list.sliceArray(0..b)
            2 -> answer = num_list.sliceArray(a until num_list.size)
            3 -> answer = num_list.sliceArray(a..b)
            4 -> answer = num_list.slice(a..b step c).toIntArray() // sliceArray의 경우 step 지원 X
        }
        
        return answer
    }
}