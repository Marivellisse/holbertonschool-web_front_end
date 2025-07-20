import re

# Read the HTML file
with open("33-styleguide.html", "r") as f:
    html_content = f.read()

# Check for table caption
caption_match = re.search(r'<caption>.*?</caption>', html_content)
if caption_match:
    print("table has correct caption")
else:
    print("where is the caption?")

# Check for column headers with correct scope
title_col = re.search(r'<th scope="col">Title</th>', html_content)
director_col = re.search(r'<th scope="col">Director</th>', html_content)
date_col = re.search(r'<th scope="col">Release Date</th>', html_content)

if title_col:
    print("correctly labelled title column")
if director_col:
    print("correctly labelled director column")
if date_col:
    print("correctly labelled release date column")

# Check for row headers with correct scope
row_scopes = re.findall(r'<th scope="row">', html_content)
if len(row_scopes) >= 3:
    print("all table cell headers in tbody have correct scope")

# Check for specific movie titles and data
if "Star Wars: Episode IV - A New Hope" in html_content:
    print("Found Star Wars: Episode IV - A New Hope")
if "Star Wars: Episode V - The Empire Strikes Back" in html_content:
    print("Found Star Wars: Episode V - The Empire Strikes Back")
if "Star Wars: Episode VI - Return of the Jedi" in html_content:
    print("Found Star Wars: Episode VI - Return of the Jedi")
if "George Lucas" in html_content and "May 25th, 1977" in html_content:
    print("Found George Lucas and May 25th, 1977")
if "Irvin Kershner" in html_content and "May 21st, 1980" in html_content:
    print("Found Irvin Kershner and May 21st, 1980")
if "Richard Marquand" in html_content and "May 25th, 1983" in html_content:
    print("Found Richard Marquand and May 25th, 1983")
