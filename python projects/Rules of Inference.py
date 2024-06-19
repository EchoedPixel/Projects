propositions = []
conc = []

def User_Input():
    global propositions
    global conc
    print('Enter conclusion...')
    conc = input().strip()
    while True:
        print(f"Enter a value for item number {len(propositions) + 1} (or 'done' to finish): ")
        proposition = input().strip()
        if proposition.lower() == "done":
            break
        propositions.append(proposition)
    print("Propositions:", propositions)

def apply_conjunction(item1, item2, lst):
    if len(item1) == 1 and len(item2) == 1 and item1 != item2:
        if f"{item1}∧{item2}" not in lst:
            lst.append(f"{item1}∧{item2}")
            print(f"{item1}∧{item2}")
            print("conjunction")

def apply_addition(item1, item2, lst):
    if item1 != item2:
        if len(item1) == 1 and len(item2) == 1:
            lst.append(f"{item1}∨{item2}")
            print(f"{item1}∨{item2}")
            print('addition')

def check(propositions, conc):
    lst = propositions.copy()
    for item1 in propositions:
        for item2 in propositions:
            if ('→' in item1 and '→' not in item2):
                q = item1.split('→')
                if item2 == q[0]:
                    print('modus ponens.')
                    lst.append(q[1])
                    print(q[1])
            elif ('→' in item2 and '→' not in item1):
                q = item2.split('→')
                if item1 == q[0]:
                    print('modus ponens.')
                    lst.append(q[1])
                    print(q[1])
            elif ('~' in item1 and '→' in item2) or ('~' in item2 and '→' in item1):
                if '~' in item1:
                    x = item1.split('~')
                    y = item2.split('→')
                    if (x[1] == y[1]):
                        lst.append(f'~{y[0]}')
                        print(f'~{y[0]}')
                        print('modus tollens')
                elif '~' in item2:
                    x = item2.split('~')
                    y = item1.split('→')
                    if (x[1] == y[1]):
                        lst.append(f'~{y[0]}')
                        print(f'~{y[0]}')
                        print('modus tollens')
            elif ('→' in item1 and '→' in item2):
                x = item1.split('→')
                y = item2.split('→')
                if x[1] == y[0]:
                    lst.append(f"{x[0]}→{y[1]}")
                    print(f"{x[0]}→{y[1]}")
                    print('hypothetical syllogism.')
                elif x[0] == y[1]:
                    lst.append(f"{x[1]}→{y[0]}")
                    print(f"{x[1]}→{y[0]}")
                    print('hypothetical syllogism.')
            elif ('∨' in item1 and '~' in item2) or ('∨' in item2 and '~' in item1):
                if '∨' in item1:
                    x = item1.split('∨')
                    y = item2.split('~')
                    if x[0] == y[1]:
                        lst.append(x[1])
                        print(x[1])
                        print('disjunctive syllogism')
                elif '∨' in item2:
                    x = item2.split('∨')
                    y = item1.split('~')
                    if x[0] == y[1]:
                        lst.append(x[1])
                        print(x[1])
                        print('disjunctive syllogism')
            elif '∧' in item1:
                apply_conjunction(item1, item2, lst)
            elif len(item1) == 1 and len(item2) == 1:
                apply_addition(item1, item2, lst)
            elif '∨' in item1 and '∨' in item2:
                x = item1.split('∨')
                y = item2.split('∨')
                if (x[0] == ('~' + y[0])):
                    lst.append(f"{x[1]}∨{y[1]}")
                    print(f"{x[1]}∨{y[1]}")
                    print('resolution')
                elif (y[0] == ('~' + x[0])):
                    lst.append(f"{x[1]}∨{y[1]}")
                    print(f"{x[1]}∨{y[1]}")
                    print('resolution')
    for i in range(len(lst)):
        lst[i] = lst[i].replace('(', '').replace(')', '')
    propositions = [x for i, x in enumerate(lst) if x not in lst[:i]]
    print("new list: ", propositions)
    if conc in propositions:
        print(f"Conclusion '{conc}' found!")
        return propositions
    else:
        print(f"Conclusion '{conc}' not found in derived propositions.")
        return propositions

def main():
    User_Input()
    derived_propositions = propositions.copy()
    while True:
        derived_propositions = check(derived_propositions, conc)
        if conc in derived_propositions:
            print("Conclusion found!")
            break

if __name__ == "__main__":
    main()
