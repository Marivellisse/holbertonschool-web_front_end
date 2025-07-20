#!/usr/bin/env python3

with open('34-styleguide.html', 'r') as f:
    original_content = f.read()

with open('38-styleguide.html', 'r') as f:
    new_content = f.read()

original_sections = original_content.count('<section>')
new_sections = new_content.count('<section>')

if new_sections == original_sections + 1:
    print('added section')
else:
    print('incorrect number of sections')
