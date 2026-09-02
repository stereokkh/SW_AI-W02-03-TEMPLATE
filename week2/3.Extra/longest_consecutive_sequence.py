# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         token_list = {}
#         cnts = {}
#         seen = set()

#         def add_token(key, token):
#             #중복제거
#             if key in seen:
#                 return
#             #토큰 중복 x
#             if key not in token_list:
#                 token_list[key] = token
#             #토큰 걸림
#             else:
#                 old_token = token_list[key]
#                 #
#                 if isinstance(old_token, tuple):
#                     if token not in old_token:
#                         token_list[key] = old_token + (token,)

#                 elif old_token != token:
#                     token_list[key] = (old_token, token)

#         for num in nums:

#             if num in seen:
#                 continue
#             seen.add(num)

#             if num in token_list:

#                 temp = token_list.pop(num)

#                 if isinstance(temp, tuple):
#                     token1, token2 = temp

#                     new_count = cnts[token1] + cnts[token2] + 1
#                     #그룹 두개 연결 cnt token1로 token_list 갱신
#                     cnts[token1] = new_count

#                     del cnts[token2]
#                     #token2를 token1로 변경
#                     for key in list(token_list.keys()):
#                         value = token_list[key]

#                         if isinstance(value, tuple):
#                             new_value = []

#                             for token in value:
#                                 if token == token2:
#                                     token = token1

#                                 if token not in new_value:
#                                     new_value.append(token)

#                             if len(new_value) == 1:
#                                 token_list[key] = new_value[0]
#                             else:
#                                 token_list[key] = tuple(new_value)

#                         elif value == token2:
#                             token_list[key] = token1
#                 #그냥 한쪽 연결
#                 else:
#                     token = temp
#                     cnts[token] += 1

#                     if num < token:
#                         add_token(num - 1, token)

#                     else:
#                         add_token(num + 1, token)

#             else:
#                 cnts[num] = 1

#                 add_token(num - 1, num)
#                 add_token(num + 1, num)

#         max_cnt = 0

#         for cnt in cnts.values():
#             if max_cnt < cnt:
#                 max_cnt = cnt

#         return max_cnt


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max = 0
        for num in num_set:
            cnt = 0
            if num - 1 not in num_set:
                flag = num
                while flag in num_set:
                    cnt += 1
                    flag += 1
            if max < cnt:
                max = cnt
        return max