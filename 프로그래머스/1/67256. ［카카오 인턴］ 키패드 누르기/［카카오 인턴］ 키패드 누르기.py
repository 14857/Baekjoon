# 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작
# 키패드상 거리 계산
def solution(numbers, hand):
    answer = ''
    
    keypad = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    check = [2, 5, 8, 0]
    
    left_hand = '*'
    right_hand = '#'
    
    
    for num in numbers:
        if(num in left):
            answer += 'L'
            left_hand = num
            
        elif (num in right):
            answer += 'R'
            right_hand = num
            
        else:
            # 키패드상 거리 고려하기
            l_pos = keypad[left_hand]
            r_pos = keypad[right_hand]
            n_pos = keypad[num]
            
            l_dist = abs(l_pos[0] - n_pos[0]) + abs(l_pos[1] - n_pos[1])
            r_dist = abs(r_pos[0] - n_pos[0]) + abs(r_pos[1] - n_pos[1])
            
            if l_dist < r_dist:
                answer += 'L'
                left_hand = num
            elif l_dist > r_dist:
                answer += 'R'
                right_hand = num
            else:
                if hand == "right":
                    answer += 'R'
                    right_hand = num
                else:
                    answer += 'L'
                    left_hand = num
    
    return answer