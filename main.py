import json
from adf_lib import ADF, Text, Table, Link, HeadingLevel

# Create a new document
doc = ADF()

# Add a heading
doc.add(Text("My Document").heading(HeadingLevel.H1))

# Add a paragraph with a link
link = Link(href="https://example.com", title="Example")
p1 = Text("Hello I").paragraph()
p2 = Text("am", "strong").paragraph()
p3 = Text("a heading").heading()
doc.add(Text.merge_paragraphs(p1, p2, p3,Text("Click here", link.to_mark(), "strong", 'em').paragraph()))
doc.add(Text("Click here", link.to_mark(), "strong", 'em').paragraph())

# Create a table
table = Table(width=100, is_number_column_enabled=True)
table.add_row(
    [
        table.header([Text("Header").paragraph()]),
        table.header([Text("Content").paragraph()]),
    ]
)
table.add_row(
    [
        table.cell([Text("Header").paragraph()]),
        table.cell([Text("Content").paragraph()]),
    ]
)
doc.add(table.to_dict())

# Convert to dictionary
adf_dict = doc.to_dict()

# dump to JSON file
with open("output.json", "w") as f:
    json.dump(adf_dict, f, indent=2)
