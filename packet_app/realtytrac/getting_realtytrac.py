async def getting_realtytrac_async(urls, s, gotits):
    ans = await s.get(urls[0][0])
    print("oneloha")
    gotits[0] = True
    return ans.html, urls[0][1]


async def getting_realtytrac_async1(urls, s, gotits):
    ans = await s.get(urls[1][0])
    print("batwoloha")
    gotits[1] = True
    return ans.html, urls[1][1]


async def getting_realtytrac_async2(urls, s, gotits):
    ans = await s.get(urls[2][0])
    print("threeloha")
    gotits[2] = True
    return ans.html, urls[2][1]


async def getting_realtytrac_async3(urls, s, gotits):
    ans = await s.get(urls[3][0])
    print("fouroloha")
    gotits[3] = True
    return ans.html, urls[3][1]


async def getting_realtytrac_asyns4(urls, s, gotits):
    print(urls[4])
    ans = await s.get(urls[4][0])
    print("fiveloha")
    gotits[4] = True
    return ans.html, urls[4][1]
