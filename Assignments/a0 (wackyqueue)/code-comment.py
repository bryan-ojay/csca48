with open('wackyqueue.py') as infile:
    lines = [x.strip() for x in infile.readlines() if not x.isspace()]
    in_docstring = False
    line_count = docstring_count = comment_count = 0
    for line in lines:
        if '"""' in line or "'''" in line:
            in_docstring = not in_docstring
            if line != '"""' or line != "'''":
                docstring_count += 1
        elif line[0] == '#':
            comment_count += 1
        elif not in_docstring:
            line_count += 1
        else:
            docstring_count += 1
print(f'Source lines of code: {line_count}')
print(f'Docstring lines: {docstring_count}')
print(f'Comment lines: {comment_count}')
ratio = (comment_count + docstring_count)/line_count
if ratio != 1:
    num = ratio if ratio > 1 else int(1/ratio)
    word =  "more" if ratio > 1 else "less"
    print(f'You have {num:.2f} times {word} comments than code')