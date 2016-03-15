# ###########################
# ### List comprehensions ###
# ###########################
#
# l = [i for i in range(10)]
# print "1. ",l
#
# l = [i for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
# print "2. ",l
#
# l = [i*2 for i in [0, 1, 2, 3, 4, 5, 6, 7, 99, 'fish']]
# print "3. ",l
#
# l = ['woohoo' for i in [0, 1, 2, 3, 4, 5, 6, 7, 99, 'fish']]
# print "4. ",l
#
# def square(x): return x*x
# l = [square(i) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
# print "5. ",l
#
# l = ['woohoo' for _ in [0, 1, 2, 3, 4, 5, 6, 7]]
# print "6. ",l
#
# ### "_" underscroe used for throw awa value ###
# l = [_ for _ in [0, 1, 2, 3, 4, 5, 6, 7]]
# print "7. ",l
#
# l = [ (x,y)
#     for x in range(6)
#         for y in ["a","b","c"]]
# print "8. ",l
#
# l = [ (x,y,z)
#     for x in range(4)
#         for y in range(4)
#              for z in range(4)]
# print "9. ",l
#
# l = [(x,x+1)
#      for x in range(5)]
# print "10. ",l
#
# l = [x for x in [(1,'A'), (2,'B'), (3,'C'), (4,'D')]]
# print "11. ",l
#
# l = [y for _, y in [(1,'A'), (2,'B'), (3,'C'), (4,'D')]]
# print "12. ",l
#
# l = [x for x, _ in [(1,'A'), (2,'B'), (3,'C'), (4,'D')]]
# print "13. ",l
#
# l = [letter * count  for count, letter in [(1,'A'), (2,'B'), (3,'C'), (4,'D')]]
# print "14. ",l
#
# l = [letter.lower()  for letter in "Hello World"]
# print "15. ",l
#
# print '16. ',
# print '*'.join(l)
#
# print '17. ',
# print ''.join([str(i) for i in range(10)])
#
# l = [i for i in range(100) if i%2 == 0]
# print '18. ', l
#
# l = [(x,y) for x in range(10)
#           for y in range(10)
#                if x <> y]
# print '19. ', l

# total_words = sum([len(tweet.split()) for tweet in ['This is one one of those tweets', 'The weather in ireland is always shite', 'It nearly paddys day whey hey']])
# print total_words