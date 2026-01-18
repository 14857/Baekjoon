// arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가
// arr에 최소한의 개수로 0을 추가한 배열 반환

// 2의 정수 거듭 제곱 -> 비트 연산으로 판별 (2의 거듭제곱 수는 이진수에서 1이 정확히 하나만 존재)

class Solution {
    
    fun nextPowerOfTwo(n: Int): Int {
        if (n <= 1) return 1
        return Integer.highestOneBit(n - 1) shl 1
    }
    
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        val size = arr.size
        val cap = nextPowerOfTwo(size)
        
        answer = arr
        
        if(size != cap){
            repeat(cap-size){
                answer += intArrayOf(0)
            }
        }
        
        return answer
    }
}