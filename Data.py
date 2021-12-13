from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝑯𝒆𝒚 {}

𝑾𝒍𝒄 𝒕𝒐 {}

𝑰 𝒂𝒎 𝒂 𝑻𝒊𝒎𝒆 𝑻𝒆𝒍𝒍𝒆𝒓 𝒃𝒐𝒕 𝒂𝒏𝒅 𝑰 𝒄𝒂𝒏 𝒔𝒉𝒐𝒘 𝒕𝒊𝒎𝒆 𝒐𝒇 𝒅𝒊𝒇𝒇𝒆𝒓𝒆𝒏𝒕 𝒑𝒍𝒂𝒄𝒆𝒔 𝒊𝒏 𝒅𝒊𝒇𝒇𝒆𝒓𝒆𝒏𝒕 𝒘𝒂𝒚𝒔.

𝑼𝒔𝒆 𝒉𝒆𝒍𝒑 𝒃𝒐𝒕𝒕𝒐𝒏 𝒃𝒆𝒍𝒐𝒘 𝒕𝒐 𝒍𝒆𝒂𝒓𝒏 𝒉𝒐𝒘 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 !

❤️✨
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔴 MrX", url="https://t.me/Starfvivviir")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🆘 About", callback_data="about")
        ],
        [InlineKeyboardButton("📣 Channel", url="https://t.me/Tg_Galaxy")],
        [InlineKeyboardButton("👥 Group", url="https://t.me/Stagvvufxwfut")],
    ]

    # Help Message
    HELP = """
Use below commands to use me. I can be used everywhere including here, groups, channels and even inline mode so that you can use me in groups where I'm not present.

**Available Commands** :-
/time - `Time at present (defaults to India).`
/time any_time_zone - `Time of that time zone at present.`
/timezones - `List all timezones.`
/search <continent/country/city> - `Search for timezone(s) for that continent/country/city.`
/gmt - `GMT time at present.`
/unixtime - `Unix Time at present. Same around the globe.`
/unix - `What is unix time?`
/about - `About this bot and source code.`
/help - `This Message.`
/start - `Check if bot is alive.`

**Inline Mode** :-
Format :- "`@TimeXbot_xbot <pass some text>`"
Use above format to use inline mode as follows:
- Pass no text or pass "time" to get current time.
- Pass any timezone to get that timezone's current time.
- Pass "gmt" to get current GMT time.
- Pass "unix" as text to get current unix time or learn 'What is unix ?'
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to show time of different places in different ways,

Channel : [Click Here](https://t.me/Tg_Galaxy)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using bot 😽
    """
