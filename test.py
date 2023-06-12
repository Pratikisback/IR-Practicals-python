# a = "Hello" #String
# b = 2 #integer
# c = [1,2,3,4] #list
# d = {"a": 1, "b": 1} #dictionary
# e = ("a", "b", "c") #tuple
# f = {"hef", "teh", "hda", "lkj"} #set
# g = True #Boolean
# h = False #Boolean
# i = 22.34

# for i in range(1,1000):
#     if i%8 == 0:
#         print(i)
#

# print(sum(test_list))
#
# print(test_list[3])
#
# test_list = [12, 67, 98, 34]
# reversetestlist =test_list[::-1]
# print(reversetestlist)
#
# # a = [x for x in range(1, 1001) if x%8 ==0]
# # print(a)
#
# a = ["Hello", 1, 22.32, True, {"first":"name"}, {"Bat","Ball","Stumps"}, [2,1,3,4,1]]
# b = list(a[5])
# print(b)
# for i in b:
#     print(i)


# test_list1 = ["a", "b", "ab", "b", 2, 2, 45, 45, "ab" ]
# # b = set(test_list1)
# # b = tuple(b)
# # c = list(b)
# # print(c)
# # print(type(c))
# #
# #
#
# for i in test_list1:
#

# a =1
# b = 2
# dicty = {a:b}
# print(dicty)

#
# test_list2 = ['a','b','ab', 'c', 1,2,3,4]
# strings = []
# integers = []
#
# for i in test_list2:
#     if isinstance(i, str):
#         strings.append(i)
#     elif isinstance(i, int):
#         integers.append(i)
#
# print(strings)
# print(integers)
#


dict1 = {x:x**3 for x in range(6)}
# print(dict1)
#
# print(dict1[4])
# print(dict1.get(3))
for key, values in dict1.items():
    print(values)