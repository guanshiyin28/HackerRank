def minion_game(s):
    vowels, n, scores = 'AEIOU', len(s), {'Kevin': 0, 'Stuart': 0}
    for i, char in enumerate(s):
        scores['Kevin' if char in vowels else 'Stuart'] += n - i
    winner = max(scores, key=scores.get)
    print(f'{winner} {scores[winner]}' if len(set(scores.values())) > 1 else 'Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
