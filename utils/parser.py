class AIOutputParser:

    @staticmethod
    def parse(content):

        sections = {
            "script": "",
            "title": "",
            "description": "",
            "tags": "",
            "thumbnail": ""
        }

        current = None

        for line in content.splitlines():

            line = line.strip()

            if line == "===SCRIPT===":
                current = "script"
                continue

            elif line == "===TITLE===":
                current = "title"
                continue

            elif line == "===DESCRIPTION===":
                current = "description"
                continue

            elif line == "===TAGS===":
                current = "tags"
                continue

            elif line == "===THUMBNAIL===":
                current = "thumbnail"
                continue

            if current:
                sections[current] += line + "\n"

        return {
            "script": sections["script"].strip(),
            "title": sections["title"].strip(),
            "description": sections["description"].strip(),
            "tags": sections["tags"].strip(),
            "thumbnail": sections["thumbnail"].strip()
        }