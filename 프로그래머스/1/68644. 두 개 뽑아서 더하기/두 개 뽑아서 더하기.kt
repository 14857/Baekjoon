//서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수

class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var set = mutableSetOf<Int>()
        
        for (i in numbers.indices) {
            for (j in i + 1 until numbers.size) {
                set.add(numbers[i] + numbers[j])
            }
        }
        
        answer = set.sorted().toIntArray()
        return answer
    }
}