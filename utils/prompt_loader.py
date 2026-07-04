from pathlib import Path

class PromptLoader:

    PROMPT_DIR = Path("prompts")

    @classmethod
    def load(cls, filename):

        file_path = cls.PROMPT_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {filename}"
            )

        return file_path.read_text(
            encoding="utf-8"
        )