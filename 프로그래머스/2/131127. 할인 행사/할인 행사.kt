// 회원을 대상으로 매일 한 가지 제품을 할인 -> 할인하는 제품은 하루에 하나씩만 구매 가능
// 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수 반환

// 정현이가 원하는 제품을 나타내는 문자열 배열 want
// 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number
// XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount


class Solution {
    fun solution(want: Array<String>, number: IntArray, discount: Array<String>): Int {
        var answer: Int = 0
        var map = mutableMapOf<String, Int>()
        
        
        for(i in want.indices){
            map[want[i]] = number[i]
        }
        
        println(map)
        
        for(i in 0..discount.size-10){
            var period = discount.slice(i..i+9)
            // println(period)
            var chk = 1
            
            for((key, value) in map){
                if(value > period.count{ it == key }) chk = 0
            }
            
            answer += chk
        }
        
        
        
        
        
        return answer
    }
}