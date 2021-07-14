
import sys
input = sys.stdin.readline

s = list(input().rstrip())
bomb = list(input().rstrip())

stack = []

for i in range(len(s)):
