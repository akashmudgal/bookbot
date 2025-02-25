from typing import AnyStr,Dict

def get_num_words(text: AnyStr):
    return len(text.split())

def get_char_count(text: AnyStr):
    char_stats={}
    for char in text:
        char=char.lower()
        if char in char_stats:
            char_stats[char]=char_stats[char]+1
        else:
            char_stats[char]=1
    return char_stats

def sort_char_stats(char_stats: Dict):
    list_dict=[]
    for key in char_stats:
        if key.isalpha():
            list_dict.append({key: char_stats[key]})
    
    sort_on = lambda x: list(x.values())[0]
    list_dict.sort(reverse=True,key = sort_on)
    return list_dict
