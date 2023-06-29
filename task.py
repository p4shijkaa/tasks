def insert_dash(num):

  digits = [d for d in str(num)]

  for i in range(len(digits)-1):
    if int(digits[i])%2 and int(digits[i+1])%2:
        digits[i] = digits[i] + '-'

  return ''.join(digits)


print(insert_dash(454793))


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high('man i need a taxi up to ubud'))

def two_sum(numbers, target):
    required = {}
    for i in range(len(numbers)):
        if target - numbers[i] in required:
            return [required[target - numbers[i]],i]
        else:
            required[numbers[i]]=i


print(two_sum([1234,5678,9012], 14690))


# def encode_rot13(s):
#     l = []
#     for i in s:
#         if i.isalpha():
#             if i.islower() and ord(i) - 96 > 13 or i.isupper() and ord(i) - 64 > 13:
#                 l.append(chr(ord(i)-13))
#             else:
#                 l.append(chr(ord(i)+13))
#         else:
#             l.append(i)
#     return "".join(l)
#
# print(encode_rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))
# # #"Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes."

# def check(i):
# //////////
#
# res = "".join([lambda i: check(i) for i in s])

# def encode_rot13(message):
#     def decode(symbol):
#         if symbol.islower() and ord(symbol) - 96 > 13 or symbol.isupper() and ord(symbol) - 64 > 13:
#             char = chr(ord(symbol)-13)
#         else:
#             char = chr(ord(symbol)+13)
#             return symbol if not symbol.isalpha() else char
#         return chr((ord(symbol) - ord(char) + 13) % 26 + ord(char))
#     return "".join(decode(symbol) for symbol in message)
#
#
# print(encode_rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))


# def get_card(n):
#     if (n % 2 == 0 and (n // 2) % 2 == 1) or n == 4:
#         return n // 2
#     else:
#         return 1


# def card_game(n):
#     alice = 0
#     bob = 0
#     flag = True
#     while n > 0:
#         this_turn = get_card(n)
#         if flag:
#             alice += this_turn
#         else:
#             bob += this_turn
#         flag = not flag
#         n -= this_turn
#     return alice
# #
# # print(card_game(100000000000))


# def domain_name(url):
#     exceptions = ["http", "https", "www", "com"]
#     url = url.replace("//", " ").replace(":", " ").replace(".", " ")
#     l = []
#     for i in url.split():
#         if i in exceptions:
#             continue
#         else:
#             l.append(i)
#     return "".join(l[0])
#
#
# print(domain_name("http://github.com/carbonfive/raygun"))


# def ips_between(start, end):
#     a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
#     b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
#     return abs(a-b)
#
#
#
# print(ips_between("20.0.0.10", "20.0.1.0"))

#
# def snail(array):
#     results = []
#     while len(array) > 0:
#         # go right
#         results += array[0]
#         del array[0]
#
#         if len(array) > 0:
#             # go down
#             for i in array:
#                 results += [i[-1]]
#                 del i[-1]
#
#             # go left
#             if array[-1]:
#                 results += array[-1][::-1]
#                 del array[-1]
#
#             # go top
#             for i in reversed(array):
#                 results += [i[0]]
#                 del i[0]
#
#     return results
#
#
# print(snail([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]))



# def format_duration(seconds):
#     words = ["year", "day", "hour", "minute", "second"]
#
#     if not seconds:
#         return "now"
#     else:
#         m, s = divmod(seconds, 60)
#         h, m = divmod(m, 60)
#         d, h = divmod(h, 24)
#         y, d = divmod(d, 365)
#
#         time = [y, d, h, m, s]
#
#         duration = []
#
#         for x, i in enumerate(time):
#             if i == 1:
#                 duration.append(f"{i} {words[x]}")
#             elif i > 1:
#                 duration.append(f"{i} {words[x]}s")
#
#         if len(duration) == 1:
#             return duration[0]
#         elif len(duration) == 2:
#             return f"{duration[0]} and {duration[1]}"
#         else:
#             return ", ".join(duration[:-1]) + " and " + duration[-1]
#
#
# print(format_duration(62))


# def solution(string, markers):
#     ss = string.split('\n')
#     for i in range(len(ss)):
#         s = ss[i]
#         for marker in markers:
#             index = s.find(marker)
#             if index >= 0:
#                 s = s[:index].rstrip()
#         ss[i] = s
#     return '\n'.join(ss)
#
# print(solution(' a #b\nc\nd $e f g', ['#', '$']))

# def decipher_this(string):
#     words = []
#     for word in string.split():
#         code = ''.join(char for char in word if char.isdigit())
#         new_word = chr(int(code))+''.join(char for char in word if not char.isdigit())
#         words.append(new_word[:1]+new_word[-1]+new_word[2:-1]+new_word[1] if len(new_word)>2 else new_word)
#     return ' '.join(words)
#
# #
# #
# print(decipher_this('72olle 103doo 100ya'))


# def in_array(array1, array2):
#     new_list = []
#     for i in array1:
#         for x in array2:
#             if i in x:
#                 new_list.append(i)
#     return list(sorted(set(new_list))) if len(new_list) > 0 else []
#
#
# print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))

from collections import deque

# def shifted_diff(first, second):
#     s1 = []
#     s2 = []
#     if len(first) == len(second):
#         for i in first:
#             s1.append(i)
#         for i in second:
#             s2.append(i)
#         if s1[0] in s2 and not first == second[::-1]:
#             return s2.index(s1[0])
#         else:
#             return -1
#     return -1

#
# def shifted_diff(first, second):
#     return (second + second).find(first) if len(first) == len(second) else - 1
#
# print(shifted_diff("efgo", "ogfe"))

# def alphanumeric(password):
#     clear_list = []
#     for i in password:
#         if i.isdigit() or i.isalpha() and not " " in password and "_" not in password:
#             clear_list.append(i)
#     return True if len(password) == len(clear_list) > 0 else False
#
#
# print(alphanumeric("     "))







