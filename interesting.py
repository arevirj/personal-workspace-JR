
def palindrome(start: str) -> str:
    b: int = len(start) - 1
    reverse: str = ''
    while b >= 0:
        reverse += start[b]
        b -= 1
    if reverse == start:
        start_string: str = ''
        k: int = 0
        while k < len(start):
            start_string += start[k]
            k += 1
        return start_string
    else:
        return 'False'


def is_interesting(ex: str) -> str:
    if ex == '':
        return 'None'
    half: int = 0
    if len(ex) // 2 == 0:
        half = int(len(ex) / 2)
    else:
        half = int((len(ex) / 2) + 0.5)
    substrings = [ex[i: j] for i in range(half + 1) for j in range(i + half, len(ex) + 1)]
    for sub in substrings:
        winner: str = str(palindrome(sub))
        if winner == 'False':
            continue
        else:
            return winner
    return 'False'


guess = is_interesting(input('Enter a string to check if it contains a Palindrome:'))
print(guess)