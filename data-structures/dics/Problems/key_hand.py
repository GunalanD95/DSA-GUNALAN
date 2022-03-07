# Handling missing keys in Python dictionaries
import collections

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print(country_code.get('India'))

print(country_code.get('USA')) # usng .get method will return None if there is no key

'''
“defaultdict” is a container that is defined in a module named “collections“.
 It takes a function(default factory) as its argument. 
 By default, the default factory is set to “int” i.e 0. 
 If a key is not present in the defaultdict, the default factory value is returned and displayed. 
 It has advantages over get() or setdefault(). 
'''


defd = collections.defaultdict(lambda : 'Key Not found')
defd.update({'India' : '0091',})
print(defd['India'])
print(defd['CHINA'])