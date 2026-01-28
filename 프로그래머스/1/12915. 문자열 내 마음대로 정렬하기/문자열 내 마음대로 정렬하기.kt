//각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
// sortedBy: 하나의 기준을 람다로 뽑아서 정렬할 때 사용
// sortedWith: 비교 로직 전체를 직접 지정해서 정렬할 때 사용
// compareBy: sortedWith에 넘길 비교 기준(Comparator)를 람다로 만들어주는 도구

class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        var answer = arrayOf<String>()
        
        answer = strings.sortedWith( 
                         compareBy( {it[n]}, {it} )
                 ).toTypedArray()
        
        return answer
    }
}