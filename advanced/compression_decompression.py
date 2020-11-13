
def decomp(string, start=0, times=1):
    for _ in range(times):
        i = start
        while i < len(string) and string[i] != "]":
            if string[i].islower():
                yield string[i]
            else:
                sub_times = 0
                while string[i].isdigit():
                    sub_times = sub_times * 10 + int(string[i])
                    i += 1
                i += 1  # skip open bracket
                for item in decomp(string, i, sub_times):
                    # Decomp iterator generates many characters, and then at the very end,
                    # it generates an integer. that int is the start to the next compressed string
                    if isinstance(item, str):
                        yield item
                    else:
                        print("\ni:",i)
                        print("item:",item)
                        i = item
            i += 1
    if start > 0:
        yield i


for i in decomp('4[ab]c2[3[a]b]'):
    print(i, end="")
print()


def unroll(string, start=0, times=1):
    import re
    print(string)
    starts = []
    ends = []
    nums = []
    for i in range(len(string)):
        nums = re.findall("\d+", string)
        if string[i] == "[":
            starts.append(i)
        if string[i] == "]":
            ends.append(i)
        if len(starts) == len(ends) > 0:
            break
    # print(nums)
    # print(starts)
    # print(ends)
    if len(starts) == 0:
        print("no brackets left")
        return string
    # raise Exception
    return unroll(string[:starts[0]-len(nums[0])]+int(nums[0])*string[starts[0]+1:ends[-1]] + string[ends[-1]+1:])


unroll("20[3[a]b]3[abc]4[ab]c")



