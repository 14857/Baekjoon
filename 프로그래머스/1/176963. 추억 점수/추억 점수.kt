// 추억 점수:  사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값
// name : 그리워하는 사람의 이름을 담은 문자열 배열 
// yearning : 각 사람별 그리움 점수를 담은 정수 배열
// photo : 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 

class Solution {
    fun solution(name: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        var answer: IntArray = intArrayOf()
        
        for(p in photo){
            var score = 0
            for(person in p){
                if(person in name){
                    score += yearning[name.indexOf(person)]
                }
            }
            //println(score) // 확인용
            answer += score
        }
        
        return answer
    }
}