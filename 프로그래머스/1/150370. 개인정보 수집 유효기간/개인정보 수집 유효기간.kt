// 오늘 날짜로 파기해야 할 개인정보 번호를 오름차순으로 배열에 담아 반환
// 모든 달은 28일까지 있다고 가정

class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        
        val today = today.split(".")
        val now = today[0].toInt()*365 + today[1].toInt()*28 + today[2].toInt()
        var map = mutableMapOf<String, Int>()

        // 약관별 기간
        for(i in terms.indices){
            var temp = terms[i].split(" ")
            var char = temp[0]
            var num = temp[1]
            map[char] = num.toInt()
        }
        
        // 만료 날짜 계산 및 파기 여부 확인
        for(i in privacies.indices){
            // temp = [yyyy, mm, dd, 약관] 모두 string 형식
            var temp = privacies[i].split("."," ")
            var year = temp[0].toInt()
            var month = (temp[1].toInt() + map[temp[3]]!!)
            var day = temp[2].toInt()
            
            if (month > 12) {
                year += (month - 1) / 12
                month = (month - 1) % 12 + 1
            }
            
            // 파기 여부 확인
            if(year*365 + month*28 + day <= now){
                answer += i+1
            }  
        }    
        return answer
    }
}