
# Write your code here
def switch_case(argument):
    seat_facing_num = argument % 12

    switcher = {
        1: "{0} WS\n".format((argument + 11)),
        2: "{0} MS\n".format((argument + 9)),
        3: "{0} AS\n".format((argument + 7)),
        4: "{0} AS\n".format((argument + 5)),
        5: "{0} MS\n".format((argument + 3)),
        6: "{0} WS\n".format((argument + 1)),
        7: "{0} WS\n".format((argument - 1)),
        8: "{0} MS\n".format((argument - 3)),
        9: "{0} AS\n".format((argument - 5)),
        10: "{0} AS\n".format((argument - 7)),
        11: "{0} MS\n".format((argument - 9)),
        0: "{0} WS\n".format((argument - 11)),
    }
    print(switcher.get(seat_facing_num, "Invalid month"))


T = int(input())

if 1<=T<=10**5:
    for index in range(0,T):
        N = int(input())
        if 1<=N<=108:
            switch_case(N)

        
        
