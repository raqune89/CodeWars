# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    count=0                         
    letter=''                       

    for i in s:                     
        count += 1                  
        letter += i.upper()         
        for ind in range(count - 1):
            letter += i.lower()
        if count < len(s):
            letter += '-'
    return letter
