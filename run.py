import sys

output = sys.argv

"""
    Show help error with -h or empty execution
"""
if len(sys.argv) == 1 or sys.argv[0] == '-h':
    fp = open('data/help/help.txt', 'r')
    try:
        output = fp.read(-1)
    finally:
        fp.close()

print(output)
