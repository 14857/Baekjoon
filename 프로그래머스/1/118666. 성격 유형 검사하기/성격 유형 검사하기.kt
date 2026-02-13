// 성격 유형은 총 16(=2 x 2 x 2 x 2)가지가 나올 수 있습니다
// [매우 비동의, 비동의 약간 비동의, 모르겠음, 약간 동의, 동의, 매우 동의]
// [n3,n2,n1,-, a1,a2,a3]
// [1,2,3,4,5,6,7] -> 인덱스 + 1
// [3,2,1,0,1,2,3]

// 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단

// survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나
// 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형
// 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형

class Solution {
    fun solution(survey: Array<String>, choices: IntArray): String {
        
        val answer = StringBuilder()
        var score = arrayOf(3,2,1,0,1,2,3)
        var result = mutableMapOf<Char, Int>(            
            'R' to 0, 'T' to 0, 'F' to 0, 'C' to 0, 'M' to 0, 'J' to 0, 'A' to 0, 'N' to 0
        )
        
        // 점수 매기기
        for(i in survey.indices){       
            if(choices[i] > 4) {
                result[survey[i][1]] = result[survey[i][1]]!! + score[choices[i]-1]}
            else if(choices[i] < 4) {
                result[survey[i][0]] = result[survey[i][0]]!! + score[choices[i]-1]}
        }
        
        // 최종 결과
        answer.append(if (result['R']!! >= result['T']!!) 'R' else 'T')
        answer.append(if (result['C']!! >= result['F']!!) 'C' else 'F')
        answer.append(if (result['J']!! >= result['M']!!) 'J' else 'M')
        answer.append(if (result['A']!! >= result['N']!!) 'A' else 'N')
        
        return answer.toString()
    }
}