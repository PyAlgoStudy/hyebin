from collections imnport deque

def solution(priorities, location):
    index = deque([i for i in range(len(priorities))])
    answer = 0 
    maxinum = max(priorities)
    
while True:
    INDEX = index.popleft()
    
    if priorities[INDEX] < maxinum:
        index.append(INDEX)
        
    else:
        answer+=1
        priorities[INDEX]=0
        maxinum=max(priorities)
        
        if INDEX == location:
            return answer
