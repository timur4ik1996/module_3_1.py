calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Самара'))
print(string_info('Москва'))
print(is_contains('VARejka', ['ShapKA', 'noskiy', 'SHTany', 'varejka'])) # Urban ~ urBAN
print(is_contains('Urban', ['ban', 'BaNaN', 'BANan'])) # No matches
print(calls)

