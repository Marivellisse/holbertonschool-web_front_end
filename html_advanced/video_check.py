#!/usr/bin/env python3
with open('38-styleguide.html') as f:
    if 'BigBuckBunny.mp4' in f.read():
        print('video has correct source')
