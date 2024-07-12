def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f'key:{k}, value:{v}')


a = {1: 'one', 2: 'two', 3:'three'}
print_dict(a)
print('######')
return_value = print_dict(a)
print(return_value)
print('##########')


def get_first_last_word(text):
    return text[0], text[-1]


print(get_first_last_word('My name is Kato'))

print('******')

def get_first_last_word2(text):
    words = text.split()
    return words[0], words[-1]

text = ' My name is Akinori.'
text = text.replace('.', '')
r = get_first_last_word2(text)
first, last = get_first_last_word2(text)
print(r)
print(first)
print(last)

