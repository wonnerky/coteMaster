def solution(new_id):
    answer = ''
    for ele in new_id:
        if 65 <= ord(ele) <= 90:
            answer += chr(ord(ele) + 32)
        elif 48 <= ord(ele) <= 57 or 45 <= ord(ele) <= 46 or ord(ele) == 95 or 97 <= ord(ele) <= 122:
            answer += ele
        else:
            continue
    result = ''
    for ele in answer.split('.'):
        if ele:
            result += ele + '.'
    result = result[:-1]
    if not result:
        result = 'aaa'
    elif len(result) > 15:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    elif len(result) < 3:
         result = result + (result[-1] * (3 - len(result)))
    return result



new_id = "...!@BaT#*..y.abcdefghijklm"
print(new_id)
print(solution(new_id))