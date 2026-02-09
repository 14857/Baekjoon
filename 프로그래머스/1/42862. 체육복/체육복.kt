// 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다
//  여벌 체육복이 있는(+ 도난 당하지 않은) 학생만 다른 학생에게 체육복을 빌려줄 수 있다.

// 체육 수업을 들을 수 있는 학생의 최댓값을 반환

class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0
        var now =  MutableList(n){1}

        // 현재 각 학생이 가진 체육복 수
        for(i in lost){
            now[i-1]--
        }
        
        for(i in reserve){
            now[i-1]++
        }
        
        
        // 빌려주기 연산
        for(i in 0..n-1){
            
            if(i == n-1){
                if(now[i] == 0 && (now[i-1] > 1)){
                    now[i]++
                    now[i-1]--
                }
            }
            else if(i == 0){
                if(now[i] == 0 && (now[i+1] > 1)){
                    now[i]++
                    now[i+1]--
                }
            }
            else{
                if(now[i] == 0 && (now[i-1] > 1)){
                    now[i]++
                    now[i-1]--
                }
                else if(now[i] == 0 && (now[i+1] > 1)){
                    now[i]++
                    now[i+1]--
                }
            }
            
        }
        
        // 체육복 있는 경우 확인
        for(i in now){
            if(i > 0) answer++            
        }
        
        println(now)

        return answer
    }
}