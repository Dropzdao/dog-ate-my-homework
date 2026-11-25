import os

# The dog's defence: the homework was on the floor, and the floor is
# dog territory — so eating it was simply enforcing the house rules.
LINE = "Look, you left it on the floor. On the floor. That's dog territory. I was just enforcing the rules."

def main():
    os.makedirs('/output', exist_ok=True)
    open('/output/entry.txt', 'w', encoding='utf-8').write(LINE)

if __name__ == '__main__':
    main()
