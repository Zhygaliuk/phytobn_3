import re


def main():
    number = 0
    pattern = re.compile(r'.*((25/Mar/2009:(1[2 9]|2[0 3]):(2[5 9]|[3 5]\d):(0[6-9]|[1-5]\d)|'
                         r'2[5-9]/Mar/2009:\d\d:\d\d:\d\d|'
                         r'30/Mar/2009:(0\d|1[1 6]):(0\d|1[1 9]):(0\d|1[1 8])) )'
                         r'.*GET.*.css.*2\d\d')

    with open('access.log', 'r') as f:
        contents = f.read()
        result = pattern.finditer(contents)
        for match in result:
            print(match.group(0))
            number += 1
        print(number)
    f.close()


if __name__ == '__main__':
    main()

