#!/bin/python3

import os
import sys


def identity_matrix():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

def clock_wise_rot(x, y, k):
    return [
        [1, x - y, k + x + y],
        [0, 0, -1],
        [0, 1, 0],
    ]

def counter_clock_wise_rot(x, y, k):
    return [
        [1, k + x + y, -x + y],
        [0, 0, 1],
        [0, -1, 0],
    ]


def multiply(a, b):
    c = [
        [0] * len(b[0])
        for _ in range(len(a))
    ]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

    return c

def multiply_counter_clock_wise_rot(x, y, k, a):
    return [[
        a[0][i] + (k + x + y) * a[1][i] + (-x + y) * a[2][i]
        for i in range(3)
    ], [
        a[2][i]
        for i in range(3)
    ], [
        -a[1][i]
        for i in range(3)
    ]]

def multiply_clock_wise_rot(x, y, k, a):
    return [[
        a[0][i] + (x - y) * a[1][i] + (k + x + y) * a[2][i]
        for i in range(3)
    ], [
        -a[2][i]
        for i in range(3)
    ], [
        a[1][i]
        for i in range(3)
    ]]

def kingRichardKnights(n, commands, knights):
    new_commands = []

    t = identity_matrix()
    for i, c in enumerate(commands):
        m = multiply([[1, c[0], c[1]]], t)

        new_command = [m[0][1], m[0][2], c[2]]
        if (i % 4) == 1:
            new_command[0] -= c[2]
        elif (i % 4) == 2:
            new_command[0] -= c[2]
            new_command[1] -= c[2]
        elif (i % 4) == 3:
            new_command[1] -= c[2]
        new_commands.append(new_command)

        # t = multiply(counter_clock_wise_rot(c[0], c[1], c[2]), t)
        t = multiply_counter_clock_wise_rot(c[0], c[1], c[2], t)

    to_process = {}
    for k in knights:
        i, j = (k // n) + 1, (k % n) + 1

        l = -1
        r = len(new_commands)
        while r - l > 1:
            s = (l + r) // 2
            x, y, k = new_commands[s]
            if (x <= i <= x + k and
                    y <= j <= y + k):
                l = s
            else:
                r = s

        to_process.setdefault(l, [])
        to_process[l].append((i, j))

    ans = {
        k: k
        for k in to_process.get(-1, [])
    }

    t = identity_matrix()
    for i, c in enumerate(new_commands):
      
        t = multiply_clock_wise_rot(c[0], c[1], c[2], t)
        for k in to_process.get(i, []):
            m = multiply([[1, k[0], k[1]]], t)
            ans[k] = [m[0][1], m[0][2]]

    result = []
    for k in knights:
        result.append(ans[(k // n) + 1, (k % n) + 1])

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = int(input())

    commands = []
    for _ in range(s):
        commands.append(list(map(int, input().rstrip().split())))

    kn = int(input())
    knights = []
    for _ in range(kn):
        knights.append(int(input().strip()))

    result = kingRichardKnights(n, commands, knights)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()