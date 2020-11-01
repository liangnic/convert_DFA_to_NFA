"""This module is the entry point to your assignment. There is some scaffolding
to help you get started. It will call the appropriate method (task_1, 2 etc.)
and load the input data. You can edit or remove as much of this code as you
wish to."""

from parser import Parser
from sys import stdin
import string

def task_1(parser):
    """For each state of the NFA, compute the Epsilon closure and output
    it as a line of the form s:a,b,c where s is the state, and {a,b,c} is E(s)"""
    nfa = parser.parse_fa()
    ret = {s : [] for s in nfa['states'] }

    for x,d,y in nfa['delta']:
        if d == '':
            if y not in ret.get(x):
                ret.setdefault(x, []).append(y)
    for x in ret:
        visited = [x]
        queue = [x]
        while queue:
            e = queue.pop(0)
            for n in ret.get(e):
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
        for i in visited:
            if i not in ret.get(x):
                ret.setdefault(x, []).append(i)
                
    for s in ret:
        contents = ",".join(ret[s])
        print(s + ":" + contents)
    print("end")

def task_2(parser):
    nfa = parser.parse_fa()
    closures = parser.parse_closures()

    ret = {}
    ret['states'] = nfa['states']
    ret['alphabet'] = nfa['alphabet']
    ret['start'] = nfa['start']
    ret['final'] = nfa['final']
    for x,y,z in nfa['delta']:
        if y != '':
            ret.setdefault('delta', []).append((x,y,z))
            for i in closures:
                if i != x:
                    for j in closures.get(i):
                        if j == x:
                            ret.setdefault('delta', []).append((i,y,z))
                            break

    for i in closures:
        if i not in ret['final']:
            for j in closures.get(i):
                if j in ret['final']:
                    ret['final'].append(i)
                
    print(",".join(ret['states']))
    print(",".join(ret['alphabet']))
    print(ret['start'])
    print(",".join(ret['final']))
    for s in ret['delta']:
        print(",".join(s))
    print("end")

def task_3(parser):
    efnfa = parser.parse_fa()
    ret = {}
    start = ('A', [efnfa['start']])
    ret['states'] = [start]
    ret['alphabet'] = efnfa['alphabet']
    ret['start'] =  [start]
    if efnfa.get('start') in efnfa.get('final'):
        ret.setdefault('final', []).append('A')
    
    visited = [[efnfa['start']]]
    queue = [start]
    count = 0
    asc = list(string.ascii_uppercase)
    while queue:
        Sname, oldStates = queue.pop(0)
        for alph in ret['alphabet']:
            newStates = []
            for state in oldStates:
                for x,y,z in efnfa['delta']:
                    if x == state and y == alph and z not in newStates:
                        newStates.append(z)
            newStates = sorted(newStates)
            if newStates not in visited:
                visited.append(newStates)
                if newStates == []:
                    queue.append(('Error',newStates)) #"error a error" will outputed
                    ret.setdefault('delta', []).append((Sname, alph, 'Error'))
                    ret.setdefault('states', []).append(('Error', newStates))
                else:
                    count+=1
                    queue.append((asc[count],newStates))
                    ret.setdefault('delta', []).append((Sname, alph, asc[count]))
                    ret.setdefault('states', []).append((asc[count], newStates))
                    for s in newStates:
                        if s in efnfa['final']:
                            ret.setdefault('final', []).append(asc[count]) 
            else:
                for Ename, states in ret['states']:
                    if states == newStates:
                        ret.setdefault('delta', []).append((Sname, alph, Ename))
                        break
                        
    ret['states'] = sorted(ret['states'])
    ret['delta'] = sorted(ret['delta'])
    print(",".join([r[0] for r in ret['states']]))    
    #print(ret['states'])     
    print(",".join(ret['alphabet']))
    print(ret['start'][0][0])
    print(",".join(ret['final']))
    for s in ret['delta']:
        print(",".join(s))
    print("end")
                    
def task_4(parser):
    """For each string, output 1 if the DFA accepts it, 0 otherwise.
    The input is guaranteed to be a DFA."""
    dfa = parser.parse_fa()
    test_strings = parser.parse_test_strings()

    for test in test_strings:
        ret = 1
        state = dfa['start']
        for i in test:
            for x,y,z in dfa['delta']:
                if state == x and y == i:
                    state = z
                    break
        if state in dfa.get('final'):
            print(ret)
        else:
            print(0)

    print("end")

if __name__ == '__main__':

    parser = Parser()
    command = parser.parse_command()

    if command == 'epsilon-closure':
        task_1(parser)
    elif command == 'nfa-to-efnfa':
        task_2(parser)
    elif command == 'efnfa-to-dfa':
        task_3(parser)
    elif command == 'compute-dfa':
        task_4(parser)
    else:
        print(f'Command {repr(command)} not recognised.')

