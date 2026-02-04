// 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 반환

class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var answer: Int = 0
        var length = mutableListOf<Int>()
        var width = mutableListOf<Int>()
        
        for(i in sizes){
            if(i[0] < i[1]){ 
                width.add(i[1])
                length.add(i[0])
            }
            else{
                width.add(i[0])
                length.add(i[1]) }
        }
        
        answer = width.maxOrNull()!! * length.maxOrNull()!!
        
        return answer
    }
}