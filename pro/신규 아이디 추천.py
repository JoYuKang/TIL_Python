
def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            answer += i
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    #5
    if answer == '':
        answer = 'a'
    #6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] =='.':
            answer  = answer[:-1]
    #7
    while len(answer) <=2:
        answer += answer[-1]
    
    
    return answer

new_id = 	"z--"
print(solution(new_id))