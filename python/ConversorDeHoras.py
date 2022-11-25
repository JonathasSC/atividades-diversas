# def timeConversion(s):
#     hour = int(s[0:2]) + 12
#     minu = s[3:5]
#     sec = s[6:8]
#     peri = s[8:]
#     peri = "AM"
#     print(f"{hour}:{minu}:{sec}{peri}")
#     print(f"{hour}:{minu}:{sec}")
# timeConversion('07:05:45PM')


# def timeConversion(s):
#     if s[-2:] == 'AM' and s[:2] == "12":
#         return "00" + s[2:-2]
    
#     elif s[-2:] == 'AM':
#         return s[:-2]
    
#     elif s[-2:] == 'PM' and s[:2] == "12":
#         return s[2:-2]

#     else:
#         return str(s[:2])+12 + s [2:8] 

def timeConversion(s):
    # Write your code here
    time = s.split(':')
    if "PM" in time[2] and time[0] != "12":
        time[0] = int(time[0])+12
    elif "AM" in time[2] and time[0] == "12":
        time[0] = "00"
    return str(time[0])+":"+time[1]+":"+time[2][:2]