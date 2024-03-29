from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start"),
            types.BotCommand("help", "Guide"),
            types.BotCommand("lang", "Change language"),
        ]
    )
