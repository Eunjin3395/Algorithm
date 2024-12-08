def solution(phone_book):
    _dict = {}
    for number in phone_book:
        _dict[number]= True
    # print(_dict)
    for number in phone_book:
        for i in range(len(number)-1):
            if number[:i+1] in _dict:
                return False    
                
    return True