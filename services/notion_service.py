from notion_client import Client

from config import Config
from utils.notion_parser import NotionParser


class NotionService:

    def __init__(self):

        self.client = Client(
            auth=Config.NOTION_TOKEN
        )

    # ---------------------------------
    # Rich Text Helper
    # ---------------------------------

    def _rich_text(self, text):

        if not text:
            text = ""

        chunks = []

        for i in range(0, len(text), 1900):

            chunks.append({

                "type": "text",

                "text": {

                    "content": text[i:i + 1900]

                }

            })

        return chunks

    # ---------------------------------
    # Save New Content
    # ---------------------------------

    def save_content(self, content):

        self.client.pages.create(

            parent={

                "database_id": Config.NOTION_DATABASE_ID

            },

            properties={

                "Topic": {

                    "title": self._rich_text(content.topic)

                },

                "Content Type": {

                    "select": {

                        "name": content.content_type

                    }

                },

                "Script": {

                    "rich_text": self._rich_text(content.script)

                },

                "Title": {

                    "rich_text": self._rich_text(content.title)

                },

                "Description": {

                    "rich_text": self._rich_text(content.description)

                },

                "Tags": {

                    "rich_text": self._rich_text(content.tags)

                },

                "Thumbnail Prompt": {

                    "rich_text": self._rich_text(content.thumbnail_prompt)

                },

                "Status": {

                    "status": {

                        "name": content.status

                    }

                }

            }

        )

        print("✅ Content Saved To Notion")

    # ---------------------------------
    # Get First Approved Content
    # ---------------------------------

    def get_approved_content(self):

        response = self.client.databases.query(

            database_id=Config.NOTION_DATABASE_ID,

            filter={

                "property": "Status",

                "status": {

                    "equals": "Approved"

                }

            },

            page_size=1

        )

        if len(response["results"]) == 0:

            return None

        page = response["results"][0]

        return NotionParser.parse(page)

    # ---------------------------------
    # Update Status
    # ---------------------------------

    def update_status(self, page_id, status):

        self.client.pages.update(

            page_id=page_id,

            properties={

                "Status": {

                    "status": {

                        "name": status

                    }

                }

            }

        )

    # ---------------------------------
    # Update Video Link
    # ---------------------------------

    def update_video_link(self, page_id, link):

        self.client.pages.update(

            page_id=page_id,

            properties={

                "Video Link": {

                    "url": link

                }

            }

        )

    # ---------------------------------
    # Update Error
    # ---------------------------------

    def update_error(self, page_id, message):

        self.client.pages.update(

            page_id=page_id,

            properties={

                "Error": {

                    "rich_text": self._rich_text(message)

                }

            }

        )