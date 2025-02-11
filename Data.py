from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
مرحبا {}

- مرحبـاً بـك عزيـزي {}
- فـي بـوت كود تيرمكس$بايروجرام التابع لميوزك

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @SourceRiley
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")],
        [InlineKeyboardButton(text=" الرجوع للرئيسية ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- بدأ الاستخراج الكود", callback_data="generate")],
        [InlineKeyboardButton("- قناة السورس", url="https://t.me/SourceRiley")],
        [
            InlineKeyboardButton("- كيف تستخدمني ?", callback_data="help"),
            InlineKeyboardButton("- حول ", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - حول البوت
/help - لتسوي روحك كلشي متعرف
/start - حتى تشغل البوا
/generate - حتى تبدا بأستخراج البوت
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
- حـول البـوت . 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس ميوزك
- قنـاة السـورس : @SourceRiley

- المطور : @ZZXZ_X .

- المطور : @E_l_k_e_a_t_i_b .

- لغـة البـوت : بـايثـون .
    """
