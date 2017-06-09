import sys
import os
import re
import requests

from pyquery import PyQuery as pq


url = 'https://www.codeeval.com/browse/%s/'


def fetch_html(n):
    res = requests.get(url % n)
    if res.status_code == 200:
        return res.text
    return ''


def save_html(n, dirname='html'):
    text = fetch_html(n)
    with open('{0}/{1:03}.html'.format(dirname, n), 'w') as f:
        f.write(text)


def load_html(n, dirname='html'):
    with open('{0}/{1:03}.html'.format(dirname, n)) as f:
        return f.read()


def html_to_pq(text):
    if not text:
        return None
    return pq(text)('#requisition')


def extract(content):
    title = ''
    test_input = []
    test_output = []
    text = []
    add_to_test_input = True

    g = lambda s: re.sub('\s+', ' ', s).strip()

    for node in content.children():
        if node.tag in ('style', 'script'):
            continue

        if node.tag == 'h2':
            text.append('# %s' % node.text)
            text.append('')
            title = node.text
        elif node.tag == 'h3':
            if text[-1]:
                text.append('')
            text.append('## %s' % g(node.text))
            text.append('')
        elif node.tag == 'br':
            text.append('')
        elif node.tag == 'pre':
            if text[-1]:
                text.append('')
            text.append('```')
            for t in node.text_content().split('\n'):
                text.append(t)
            text.append('```')
            text.append('')
        elif node.attrib.get('class') == 'description-input-output':
            if text[-1]:
                text.append('')
            text.append('```')
            if test_input:
                add_to_test_input = False
            for i, line in enumerate(node.text.split('\n'), start=1):
                # text.append('{0}. `{1}`'.format(i, line))
                text.append(line)
                if add_to_test_input:
                    test_input.append(line)
                else:
                    test_output.append(line)
            text.append('```')
            text.append('')
        elif node.tag in ('ul', 'ol'):
            for j, li in enumerate(node.getchildren(), start=1):
                prefix = '*' if node.tag == 'ul' else ('%s.' % j)
                if li.text:
                    text.append('{0} {1}'.format(prefix, g(li.text)))
        elif node.text:
            text.append(g(node.text))

    return title, test_input, test_output, '\n'.join(text)


def snake(s):
    return s.lower().replace(' ', '_')


def fetch_problem(n):
    content = html_to_pq(fetch_html(n))
    # content = html_to_pq(load_html(n))
    if not content:
        return

    title, test_input, test_output, markdown = extract(content)
    if not title:
        return

    dirname = '{0:03}_{1}'.format(n, snake(title))

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    with open('%s/README.md' % dirname, 'w') as f:
        f.write(markdown)

    with open('%s/test_input.txt' % dirname, 'w') as f:
        f.write('\n'.join(test_input))

    with open('%s/test_output.txt' % dirname, 'w') as f:
        f.write('\n'.join(test_output))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--all', dest='fetch_all', action='store_true')
    parser.add_argument('ns', metavar='N', type=int, nargs='*')
    args = parser.parse_args()

    if not args.ns and not args.fetch_all:
        parser.error('meh...')

    if args.fetch_all:
        for i in range(1, 241):
            fetch_problem(i)
    else:
        for i in args.ns:
            fetch_problem(i)
