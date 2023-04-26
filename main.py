import logging
import asyncio

from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token_file = "token.txt"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def read_token(filename : str) -> str:
    token = ""
    with open(filename, 'r') as f:
        token = str(f.readline().strip())
    return token

async def create_event(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

def run_bot(token : str):
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('create_event', create_event))


if __name__ == "__main__":
    token = read_token("token.txt")
    if (token != ""):
        run_bot(token)
    else:
        logger.error(f"Empty token file {token_file}")
