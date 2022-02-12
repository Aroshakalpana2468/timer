#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Countdown Timer Telegram bot by TeLe TiPs] (https://github.com/teletips/CountdownTimer-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/CountdownTimer-TeLeTiPs/blob/main/LICENSE
 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
import requests
import asyncio
from plugins.teletips_t import *
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.raw.functions.messages import UpdatePinnedMessage




bot=Client(
    "Countdown-TeLeTiPs",
    api_id = int(os.environ ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

stoptimer = False

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 GROUP', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/pc1games12'),
                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/BUDDY3_FF')
            ]
        ]         
          
@bot.on_message(filters.command(['start','help']) & filters.private)
async def start(client, message):
    text = START_TEXT
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply_sticker("  CAACAgUAAxkBAAEGXuhiB2ebnfsYb7g53quwI5ltRjwpgAACxQMAAqC3-VX9k95mFsQW_x4E ")
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("MORE BOT", url="https://t.me/ak_program_1_bot")
            ],
            [
                InlineKeyboardButton("LIVE STREAM", url="https://t.me/aastrem")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                GROUP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
           
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                TUTORIAL_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 GROUP', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/pc1games12'),
                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/BUDD3_FF')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

@bot.on_message(filters.command(["logo"]))
async def logo(_, m : Message):
    if len(m.command) <2:
        return await m.reply_text("Please provide a name")
    else: 
        try:
            hee = await m.reply("making your logo...")
            name = m.text.split(None, 1)[1]
            req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
            IMG = req.text
            await hee.delete()
            await m.reply_photo(IMG) 
        except Exception as e:
            await m.reply_text(f"Error: {e}")
          
          
@bot.on_message(filters.command('set'))
async def set_timer(client, message):
    global stoptimer
    try:
        if message.chat.id>0:
            return await message.reply('⛔️ Try this command in a **group chat**.')
        elif not (await client.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            return await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')    
        elif len(message.command)<3:
            return await message.reply('❌ **Incorrect format.**\n\n✅ Format should be like,\n<code> /set seconds "event"</code>\n\n**Example**:\n <code>/set 86400 "TIME LEFT UNTIL NEW YEAR"</code>')    
        else:
            user_input_time = int(message.command[1])
            user_input_event = str(message.command[2])
            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if 0<user_input_time<=10:
                while user_input_time and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs'.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(1)
                    user_input_time -=1
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif 10<user_input_time<60:
                while user_input_time>0 and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs'.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif 60<=user_input_time<3600:
                while user_input_time>0 and not stoptimer:
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**m** : {:02d}**s**\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs'.format(user_input_event, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif 3600<=user_input_time<86400:
                while user_input_time>0 and not stoptimer:
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs'.format(user_input_event, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(7)
                    user_input_time -=7
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif user_input_time>=86400:
                while user_input_time>0 and not stoptimer:
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**d** : {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs'.format(user_input_event, d, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(9)
                    user_input_time -=9
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            else:
                await get_user_input_time.edit(f"🤷🏻‍♂️ I can't countdown from {user_input_time}")
                await get_user_input_time.unpin()
    except FloodWait as e:
        await asyncio.sleep(e.x)

@bot.on_message(filters.command('stopc'))
async def stop_timer(Client, message):
    global stoptimer
    try:
        if (await bot.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            stoptimer = True
            await message.reply('🛑 Countdown stopped.')
        else:
            await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')
    except FloodWait as e:
        await asyncio.sleep(e.x)

print("Countdown Timer is alive!")
bot.run()

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
