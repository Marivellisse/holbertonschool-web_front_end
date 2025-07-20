#!/usr/bin/env python3
import re
import sys

def check_video_implementation(filename):
    try:
        with open(filename, "r") as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return False

    # Check for video element with correct source URL
    video_source_pattern = r'<source\s+src="https://intranet-projects-files\.s3\.amazonaws\.com/webstack/BigBuckBunny\.mp4"'
    if re.search(video_source_pattern, html_content):
        print("video has correct source")
        return True
    else:
        # Try alternate patterns in case formatting is different
        alt_patterns = [
            r'src="https://intranet-projects-files\.s3\.amazonaws\.com/webstack/BigBuckBunny\.mp4"',
            r'BigBuckBunny\.mp4'
        ]
        
        for pattern in alt_patterns:
            if re.search(pattern, html_content):
                print("video has correct source")
                return True
        
        print("video source not found or incorrect")
        return False

if __name__ == "__main__":
    check_video_implementation("38-styleguide.html")
