// s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i] 찾기
// withIndex() : 컬렉션을 “값 + 인덱스 쌍”으로 순회

class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer = IntArray(queries.size)
        
        for((idx, q) in queries.withIndex()){ // 컬렉션을 [값 + 인덱스 쌍]으로 순회
            var s = q[0]
            var e = q[1]
            var k = q[2]
            
            var minValue = Int.MAX_VALUE // int 자료형이 가질 수 있는 최댓값
            
            for (i in s..e){
                if(arr[i] > k && arr[i] < minValue){
                    minValue = arr[i]   
                }
            }
            
            answer[idx] = if (minValue == Int.MAX_VALUE) -1 else minValue
        }
        return answer
    }
}