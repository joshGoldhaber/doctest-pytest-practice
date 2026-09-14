'''
All the functions in this file convert markdown syntax into html.
Implementing these functions will give you practice learning the correct markdown syntax.
'''


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    >>> compile_italic_underscore('_a_ and _b_')
    '<i>a</i> and <i>b</i>'
    >>> compile_italic_underscore('_a_ and _b')          # odd count: last one is literal
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''
    result = ''
    parts = line.split('_')
    # With n underscores we get n+1 parts; pair them up
    i = 0
    while i < len(parts) - 1:
        if i + 1 < len(parts) - 1 or (len(parts) - 1) % 2 == 0:
            # We have a closing underscore
            if (len(parts) - 1 - i) >= 2:
                result += parts[i] + '<i>' + parts[i + 1] + '</i>'
                i += 2
            else:
                result += parts[i] + '_'
                i += 1
        else:
            result += parts[i] + '_'
            i += 1
    if i < len(parts):
        result += parts[i]
    return result


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    >>> compile_bold_stars('**a** **b**')
    '<b>a</b> <b>b</b>'
    >>> compile_bold_stars('a * b * c')
    'a * b * c'
    >>> compile_bold_stars('***')
    '***'
    '''
    result = ''
    while '**' in line:
        start = line.find('**')
        end = line.find('**', start + 2)
        if end == -1:
            break
        result += line[:start] + '<b>' + line[start + 2:end] + '</b>'
        line = line[end + 2:]
    result += line
    return result


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    >>> compile_links('[a](1) and [b](2)')
    '<a href="1">a</a> and <a href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''
    result = ''
    while '[' in line:
        open_bracket = line.find('[')
        close_bracket = line.find(']', open_bracket)
        if close_bracket == -1:
            break
        # The '(' must immediately follow ']'
        if close_bracket + 1 >= len(line) or line[close_bracket + 1] != '(':
            result += line[:close_bracket + 1]
            line = line[close_bracket + 1:]
            continue
        close_paren = line.find(')', close_bracket + 2)
        if close_paren == -1:
            break
        text = line[open_bracket + 1:close_bracket]
        url = line[close_bracket + 2:close_paren]
        link = '<a href="' + url + '">' + text + '</a>'
        result += line[:open_bracket] + link
        line = line[close_paren + 1:]
    result += line
    return result
