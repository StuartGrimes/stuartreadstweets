from collections import Counter
# import json
#
# with open('examplejson.json') as data_file:
#     data = json.load(data_file)
#
# # result = [el for el in data]
# # print result
# result = [el['glossary']['title'].encode('utf-8') for el in data for match in el['glossary']['GlossDiv']['titl']]
# print result
#
# summary = sum([4,5,1])
#
# print summary
data = ['I am a piece of text', 'St. Paddys day is here', 'Today is Tuesday', 'Tuesday is my favourite day']

counter = Counter(data)
print counter


