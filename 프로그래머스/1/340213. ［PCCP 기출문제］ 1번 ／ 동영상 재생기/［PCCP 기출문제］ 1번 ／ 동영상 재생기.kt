// 동영상의 길이를 나타내는 문자열 video_len
// 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos
// 오프닝 시작 시각을 나타내는 문자열 op_start
// 오프닝이 끝나는 시각을 나타내는 문자열 op_end
// 사용자의 입력을 나타내는 1차원 문자열 배열 commands
// 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return

class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        var answer: String = ""
        
        // command 에 따라 pos 조절
        // 현재 재생 위치가 오프닝 구간인 경우 자동으로 오프닝이 끝나는 위치로 이동
        var parts = pos.split(":")
        var h = parts[0].toInt()
        var m = parts[1].toInt()
        var totaltime = h*60 + m
        
        var opstart = op_start.split(":")
        var opstartTime = opstart[0].toInt()*60 + opstart[1].toInt()
        
        var opend = op_end.split(":")
        var opendTime = opend[0].toInt()*60 + opend[1].toInt()
        
        var video = video_len.split(":")
        var videoTime = video[0].toInt()*60 + video[1].toInt()
        
        println(totaltime)
        println(opstartTime)
        println(opendTime)
        println(videoTime)
        
        println("")

        //println(totaltime)
        
        for (i in commands){
            // 현재 위치 op 확인
            if (totaltime >= opstartTime && totaltime <= opendTime){
                // op 인 경우 op end로 이동
                totaltime = opendTime
                println(totaltime)
                println("")
            }
            
            // command 수행
            if (i == "next"){
                // 영상 끝인 경우
                if (totaltime + 10 >= videoTime){
                    totaltime = videoTime
                }else{
                    // 아닌 경우 +10 실행
                    totaltime = totaltime + 10
                }
                
            }
            else if(i == "prev"){
                // 이미 영상 시작 부분인 경우
                if (totaltime - 10 < 0){
                    totaltime = 0
                }else{
                    // 아닌 경우 -10 실행
                    totaltime = totaltime - 10
                }
            }
            
            // 중간 출력값 문자열
            println(totaltime)            
        }
        
        if (totaltime >= opstartTime && totaltime <= opendTime){
                // op 인 경우 op end로 이동
                totaltime = opendTime
                println(totaltime)
                println("")
            }

        // 최종값
        println(totaltime)
        answer = "0".repeat(2 - (totaltime/60).toString().length) +(totaltime/60).toString() + ":" + "0".repeat(2 - (totaltime%60).toString().length) + (totaltime%60).toString()
        
        print(answer)
        
        return answer
    }
}