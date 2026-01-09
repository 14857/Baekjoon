class Solution {
    fun solution(a: Int, b: Int, c: Int, d: Int): Int {
        var answer: Int = 0
        
        var nums = listOf(a,b,c,d)
        var countMap = nums.groupingBy{it}.eachCount()
        var count = countMap.values.sortedDescending() 
        
        answer = when(count){
            listOf(4) -> {// p*1111
                val p = countMap.keys.first()
                p * 1111
            }
            listOf(3,1) -> { // (10 × p + q)2
                val p = countMap.filterValues { it == 3 }.keys.first()
                val q = countMap.filterValues { it == 1 }.keys.first()
                (10 * p + q) * (10 * p + q)  
            }
            listOf(2,2) -> { //  (p + q) × |p - q|
                val (p,q) = countMap.filterValues { it == 2 }.keys.toList()
                (p + q) * kotlin.math.abs(p - q)
            } 
            listOf(2,1,1) -> { // q × r
                val (q,r) = countMap.filterValues { it == 1 }.keys.toList()
                q * r
            }
            else -> {
                nums.minOrNull()!!
            }
        }
        return answer
    }
}