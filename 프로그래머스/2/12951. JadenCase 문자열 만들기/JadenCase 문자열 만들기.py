def solution(s):
    words = s.split(" ")  # 공백을 유지하기 위해 split(" ") 사용
    result = []
    
    for word in words:
        if len(word) > 0 and word[0].isalpha():  # 첫 문자가 알파벳이면 JadenCase 변환
            result.append(word[0].upper() + word[1:].lower())
        else:  # 첫 문자가 숫자이거나 공백이면 그대로 추가
            result.append(word.lower())  
    
    return " ".join(result)
