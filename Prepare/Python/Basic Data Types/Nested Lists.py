if __name__ == '__main__':
    # Load the input immediately into a nested list
    students = [[input(), float(input())] for _ in range(int(input()))]
    # Extract the grades from the nested list and sort them.
    # What if several students have a lowest grade? Remove duplicates by using set()
    grades = sorted(set([score for name, score in students]))
    names = sorted([name for name, score in students if score == grades[1]])
    [print(name) for name in names]
