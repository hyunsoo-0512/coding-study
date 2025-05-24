import sys
input = sys.stdin.readline

card1=int(input())
card1_list=list(map(int, input().split()))

card2=int(input())
card2_list=list(map(int, input().split()))

card1_list=set(card1_list)

result=[1 if k in card1_list else 0 for k in card2_list]


print(*result)