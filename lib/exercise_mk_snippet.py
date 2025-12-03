def make_snippet(string):
    word_list = string.split( )
    print (len(word_list))
    if len(word_list) <= 5:
        return string
    else: 
        trunc_str = word_list[0:5]
        str_from_list = str(' '.join(trunc_str))
        trunc_indicator = "..."
        print(str_from_list + trunc_indicator)        
        return str_from_list + trunc_indicator