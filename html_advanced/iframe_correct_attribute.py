from bs4 import BeautifulSoup

with open("styleguide.html") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section")
if len(sections) < 1:
    print("incorrect number of sections")
    exit()

iframe_section = sections[-1]  # last section
iframe = iframe_section.find("iframe")

print("iframe has correct title:", iframe.get("title") == "Holberton School")
print("iframe has correct width:", iframe.get("width") == "350px")
print("iframe has correct height:", iframe.get("height") == "200px")
print("iframe has correct src:", iframe.get("src") == "https://www.youtube.com/embed/41N6bKO-NVI")
print("iframe has correct text:", iframe.string.strip() == "Holberton Sally")

