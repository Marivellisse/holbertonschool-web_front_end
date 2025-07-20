import re

# Read the HTML file
with open("30-styleguide.html", "r") as f:
    html_content = f.read()

# Check for paragraph in blockquote
blockquote_with_p = re.search(r'<blockquote>[\s\S]*?<p>[\s\S]*?</p>[\s\S]*?</blockquote>', html_content)

# Check for cite in blockquote
blockquote_with_cite = re.search(r'<blockquote>[\s\S]*?<cite>.*?</cite>[\s\S]*?</blockquote>', html_content)

if blockquote_with_p:
    print("paragraph in block quote")
else:
    print("p not found")

if blockquote_with_cite:
    print("cited author correctly")
else:
    print("cite not found")
