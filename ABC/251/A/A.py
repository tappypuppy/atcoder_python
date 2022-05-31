S = input()

counter = 0

ans = ''

while counter < 6:
    for c in S:
        ans += c
        counter += 1

        if(counter == 6):
            break

print(ans)