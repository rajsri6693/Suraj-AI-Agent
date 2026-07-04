from utils.parser import AIOutputParser

sample = """
===SCRIPT===

Hello Script

===TITLE===

Amazing Title

===DESCRIPTION===

This is description.

===TAGS===

tag1, tag2, tag3

===THUMBNAIL===

A shocked investor looking at a crashing stock market.
"""

result = AIOutputParser.parse(sample)

print(result)