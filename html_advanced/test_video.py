import re

# Read the HTML file
with open("38-styleguide.html", "r") as f:
    html_content = f.read()

# Check for video element with correct source
video_source_pattern = r'<source src="https://intranet-projects-files\.s3\.amazonaws\.com/webstack/BigBuckBunny\.mp4"'
if re.search(video_source_pattern, html_content):
    print("video has correct source")
else:
    print("video source not found or incorrect")

# Check for other video attributes
if 'controls' in html_content:
    print("video has controls")
if 'loop' in html_content:
    print("video has loop")
if 'poster=' in html_content:
    print("video has poster")
