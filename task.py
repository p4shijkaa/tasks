
# def insert_dash(num):
#
#   digits = [d for d in str(num)]
#
#   for i in range(len(digits)-1):
#     if int(digits[i])%2 and int(digits[i+1])%2:
#         digits[i] = digits[i] + '-'
#
#   return ''.join(digits)
#
#
# print(insert_dash(454793))

# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
 #     return -1
#
# print(find_even_index([1,2,3,4,3,2,1]))


# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
#
#
# print(high('man i need a taxi up to ubud'))


def two_sum(numbers, target):
    required = {}
    for i in range(len(numbers)):
        if target - numbers[i] in required:
            return [required[target - numbers[i]],i]
        else:
            required[numbers[i]]=i


print(two_sum([1234,5678,9012], 14690))




def rot13(s):
    l = []
    for i in s:
        if i.isalpha():
            if ord(i) - 96 < 13:
                l.append(chr(ord(i)+13))
            else:
                l.append(chr(ord(i)-13))
        else:
            l.append(i)
    return "".join(l)

print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))





