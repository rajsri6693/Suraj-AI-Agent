from notion_client import Client
from config import Config

client = Client(auth=Config.NOTION_TOKEN)

print(type(client.databases))
print(dir(client.databases))