import asyncio

from telegram import Bot

from config import Config


class TelegramService:

    def __init__(self):

        self.bot = Bot(

            token=Config.TELEGRAM_BOT_TOKEN

        )

    async def _send(

        self,

        message

    ):

        await self.bot.send_message(

            chat_id=Config.TELEGRAM_CHAT_ID,

            text=message,

            parse_mode="HTML"

        )

    def send(

        self,

        message

    ):

        asyncio.run(

            self._send(

                message

            )

        )