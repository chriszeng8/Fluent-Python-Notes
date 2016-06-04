#The standard tuple uses numerical indexes to access its members.
# jane = ('Jane', 29, 'female')
# print '\nField by index:', jane[0]

#A namedtuple assigns names, as well as the numerical index, to each member.
import collections

BasketballPlayer = collections.namedtuple('Basketball_Player',['name','team','pts','reb','ast']);

s_curry = BasketballPlayer('Steph Curry','Golden State Warriors','30.1','5.4','6.7');
k_thompson = BasketballPlayer('Klay Thompson','Golden State Warriors','22.1','3.8','2.1');

# print s_curry
# print k_thompson

print(s_curry.name, 'has an average',s_curry.pts,' pts per game')

