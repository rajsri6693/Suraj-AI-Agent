from models.content import Content


class NotionParser:

    @staticmethod
    def parse(page):

        properties = page["properties"]

        def get_title(name):

            items = properties[name]["title"]

            if not items:
                return ""

            return "".join(

                item["plain_text"]

                for item in items

            )

        def get_text(name):

            items = properties[name]["rich_text"]

            if not items:
                return ""

            return "".join(

                item["plain_text"]

                for item in items

            )

        return Content(

            topic=get_title("Topic"),

            content_type=properties["Content Type"]["select"]["name"],

            script=get_text("Script"),

            title=get_text("Title"),

            description=get_text("Description"),

            tags=get_text("Tags"),

            thumbnail_prompt=get_text("Thumbnail Prompt"),

            status=properties["Status"]["status"]["name"],

            page_id=page["id"]

        )