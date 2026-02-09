// 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음 가능
// 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return
class Solution {
    fun solution(babbling: Array<String>): Int {
        var answer = 0
        val words = arrayOf("aya", "ye", "woo", "ma")

        for (b in babbling) {
            var now = b

            // 연속 발음 체크
            if (now.contains("ayaaya") || now.contains("yeye") || now.contains("woowoo") || now.contains("mama")
            ) continue

            //발음 치환
            for (w in words) {
                now = now.replace(w, " ")
            }

            //전부 치환되었는지 확인
            if (now.trim().isEmpty()) answer++
        }

        return answer
    }
}
