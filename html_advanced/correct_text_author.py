import re
import os

# Try to find the correct HTML file
filenames = ["index.html", "29-index.html"]
html_content = ""

for filename in filenames:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            html_content = f.read()
        break

# Expected data
expected_texts = [
    "I am completely blown away. Thanks to Techium, we've just "
    "launched our 5th website!",
    "Thank you so much for your help. Techium company is awesome!",
    "I love your system. Definitely worth the investment. I'd be "
    "lost without Techium company."
]

expected_authors = ["Yuri Y.", "Dorrie S.", "Sven H."]

# Extract blockquotes and cites using regex
blockquote_pattern = (r'<blockquote>\s*([^<]+)\s*<cite>([^<]+)'
                      r'</cite>\s*</blockquote>')
matches = re.findall(blockquote_pattern, html_content)

# Check and print results
for i in range(3):
    if i < len(matches):
        quote_text = matches[i][0].strip()
        cite_text = matches[i][1].strip()

        text_correct = expected_texts[i] in quote_text
        author_correct = cite_text == expected_authors[i]
    else:
        text_correct = False
        author_correct = False

    ordinal = ['first', 'second', 'third'][i]
    print(f"{ordinal} article has correct text: {text_correct}")
    print(f"{ordinal} author cited correctly: {author_correct}")
