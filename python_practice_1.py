type(123)
type('hello')
type(True)

x = 1
print(x)
x = x + 1
print(x)
x = x *3 + x
print(x)

True == True
True == False
True != True
True != False
not False
True and True
True and False

is_first_of_month = True
report_has_been_sent = False
should_process_report = is_first_of_month and not report_has_been_sent
print(should_process_report)

4 + 5 > 10 -2
0.1 + 0.2

text = '\nThis string\ncan contain\na lot of\ntext!\n'
print(text)

'hello' == "hello"
'abc' != 'def'
'abd' + 'def'
'abceder'*3

name = 'World'
'Hello, {}!'.format(name)
f'Hello {name}!'


s = 'Hello, Codeup!   '
s.lower()
s.upper()
s.strip()
s.isdigit()
'123'.isdigit()
s.strip().split(', ')
', '.join(['one', 'two', 'three'])

[n for n in range(10)]
[n * 2 for n in range(10)]
[n * 2 for n in range(10) if n% 2 == 0]

numbers = [1,2,3]
numbers.append(4)
numbers

numbers.pop()
len(numbers)

numbers[0]
numbers[-1]
numbers[:2]
numbers [1:2]
numbers[1:]

type(99.9)
type('False')
type (False)
type('0')
type([{}])
type({'a': []})

[1] * [2]