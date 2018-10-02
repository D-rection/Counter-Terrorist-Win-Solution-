import random

def encrypt(text):
    key = random.randint(1, 2 * len(text))
    result = []
    for c in text:

        result.append(ord(c) + (ord(c) % key))
        key = key + 1
    return result

def decrypt(key, message):
    n = key
    answer = {}
    count = -1
    for number in message:

        count = count + 1
        answer[count] = []
        for i in range(number + 1):
            if i == 0:
                continue
            if number - i == i % n:
                answer[count].append(chr(i))
                break
        n = n + 1
    return  answer


def get_all_strings(number, dict, list_str):
    if number < 0:
        return list_str
    result = []
    new_list_str = []
    for answer_str in list_str:
        for str in dict[number]:
            new_list_str.append(str + answer_str)
    result = get_all_strings(number - 1,dict,new_list_str)
    return result


def hack_message(message):
    answers = []
    for i in range(20):
        if i == 0:
            continue
        answers.append(decrypt(i,message))
    for i in answers:
        result = get_all_strings(len(i) - 1,i,[""])
        for answer in result:
            print(answer)

decode_message = [144, 122, 135, 134, 139, 88, 64, 116, 133, 114, 129, 120, 111, 138, 66, 20, 146, 64, 101, 194, 121, 64, 127, 132, 117, 64, 194, 114, 135, 64, 202, 126, 210, 216, 64, 198, 222, 200, 202, 64, 222, 220, 64, 242, 222, 234, 228, 64, 230, 202, 228, 236, 202, 228, 64, 116, 136, 20, 120, 126, 160, 144, 160, 20 ,64, 64, 64, 64, 202, 236, 194, 216, 80, 72, 190, 142, 138, 168, 182 ,78 ,198, 222, 218 ,218, 194, 220, 200, 190, 204, 222, 228, 190, 202, 240, 202, 240, 234, 232, 202, 78, 186 ,82 ,118, 118, 20 ,64, 64, 64, 64 ,94 ,94, 64, 178, 138, 88 ,64 ,134 ,158, 154, 154, 130 ,156 ,136, 158 ,164 ,66 ,66, 66 ,66 ,20 ,126, 124 ,20]
message = encrypt("qwer")
print(decode_message)
print()
stat = hack_message(decode_message)
print()
