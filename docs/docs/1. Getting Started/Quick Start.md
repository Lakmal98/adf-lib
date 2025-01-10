# Quick Start

## Basic Usage

The ADF Library provides a simple way to create and manipulate documents programmatically. Here's how to get started:

### Importing Required Components

```python
from adf_lib import ADF, Text, Table, Link
from adf_lib.constants.enums import HeadingLevel
```

### Creating Documents

#### Initialize a New Document
```python
doc = ADF()
```

#### Adding Basic Elements

##### Headings
```python
# Add a top-level heading (H1)
doc.add(Text("My Document").heading(HeadingLevel.H1))

# Other heading levels
doc.add(Text("Section").heading(HeadingLevel.H2))
doc.add(Text("Subsection").heading(HeadingLevel.H3))
```

##### Formatted Text
```python
# Basic paragraph
doc.add(Text("Simple paragraph").paragraph())

# Formatted paragraph with multiple styles
doc.add(Text("This is a formatted paragraph", "strong", "em").paragraph())

# Individual formatting options
doc.add(Text("Bold text", "strong").paragraph())
doc.add(Text("Italic text", "em").paragraph())
```

### Document Manipulation

#### Exporting Documents
```python
# Export as dictionary
adf_dict = doc.to_dict()

# Export as JSON (if supported)
adf_json = doc.to_json()
```

### Common Patterns

#### Combining Elements
```python
# Create a document with multiple elements
doc = ADF()
doc.add(Text("Report Title").heading(HeadingLevel.H1))
doc.add(Text("Introduction").heading(HeadingLevel.H2))
doc.add(Text("This is the introduction text.").paragraph())
```

#### Working with Links
```python
# Adding a link
doc.add(Link("Visit our website", "https://example.com"))

# Link within formatted text
doc.add(Text("Click ").append(Link("here", "https://example.com")).append(" for more info").paragraph())
```

#### Working with Tables
```python
# Create a simple table
table = Table()
table.addRow(["Header 1", "Header 2"])
table.addRow(["Data 1", "Data 2"])
doc.add(table)
```

### Best Practices

1. Document Structure
   - Start with a clear heading hierarchy
   - Use consistent formatting throughout
   - Group related content under appropriate headings

2. Performance
   - Build documents incrementally
   - Use batch operations when possible
   - Export only when necessary

3. Error Handling
```python
try:
    doc.add(Text("Content").heading(HeadingLevel.H1))
except Exception as e:
    print(f"Error adding content: {e}")
```

### Common Issues and Solutions

#### Issue: Invalid Formatting
```python
# Incorrect
doc.add(Text("Text", "invalid_style"))  # Will raise an error

# Correct
doc.add(Text("Text", "strong"))  # Uses valid style
```

#### Issue: Heading Levels
```python
# Valid heading levels
for level in HeadingLevel:
    doc.add(Text(f"Heading {level}").heading(level))
```