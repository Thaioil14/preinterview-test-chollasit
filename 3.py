x = input()
y = input().lower()
sx = x.split(", ")
ans1 = []
ans2 = []
for i in sx:
    lowi = i.lower()
    if y in lowi and i not in ans1:
        inx = lowi.index(y)
        ans1.append(i)
        ans2.append(str(inx))
        
if len(ans1) > 0:
    z = ', '.join(ans2)
    print(ans1)
    print(z)
else:
    print("No results found")
