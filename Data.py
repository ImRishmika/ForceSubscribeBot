from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

⚜ Use below buttons to learn more !

👨‍💻 Devoloper :- @ImRishmika
🔌 Powerd By [Cyber Botz SL](t.me/Cyber_Botz_SL)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔅 Cyber Botz SL 🔅", url="https://t.me/Cyber_Botz_SL")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("☘ About ☘", callback_data="about")
        ],
        [InlineKeyboardButton("👨‍💻 Devoloper 👨‍💻", url="https://t.me/ImRishmika")],
        [InlineKeyboardButton("🆘 Support Group 🆘", url="https://t.me/EmoBotSupport")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001742371821` or `/forcesubscribe -1001742371821`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

☘ **Available Commands** ☘

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
    💬 About This Bot 💬

💢 A telegram force subscribing bot by @ImRishmika

💠 Devoloper : [Rishmika Sandanu](t.me/ImRishmika)

💠 Framework : [Pyrogram](docs.pyrogram.org)

💠 Language : [Python](www.python.org)

💠 Sever : [Heroku](https://heroku.com)

🔌⚡ Powerd By [Cyber Botz](t.me/Cyber_Botz_SL)

    """
