from dataclasses import dataclass

@dataclass
class ScriptResponse:

    title:str

    thumbnail:str

    long_script:str

    short_script:str

    description:str

    tags:str

    pinned_comment:str

    pexels_keywords:list