# Import Modules
import pytse_client as tse
from telegram.ext import Updater, MessageHandler , CommandHandler , Filters


# Set Token
token = Updater("Token Here ...", use_context=True)


# Start Function for Start Robat
def start(update, context):
    context.bot.send_message(chat_id= update.message.chat_id, text="با سلام به ربات اطلاع دهنده بورس خوش آمدید . جهت پیدا کردن اطلاعات سریع نماد خود نام فقط نام نماد را به صورت فارسی وارد کنید به صورت مثال (خودرو یا قشیر)")


# MessageHandler For Handel Message And Gathering Nemad From TSETMC.com

def nemad(update, context):
    nemad1 = update.message.text
    ticker = tse.Ticker(nemad1)
    context.bot.send_message(chat_id=update.message.chat_id, text='نام شرکت {} \n گروه نماد {} \n EPS نماد {} \n P/E نماد {} \n حجم مبنای نماد {} \n قیمت پایانی نماد {} '.format(ticker.title, ticker.group_name, ticker.eps, ticker.p_e_ratio, ticker.base_volume, ticker.adj_close))
    context.bot.send_message(chat_id=update.message.chat_id, text='آدرس دقیق نماد \n {}'.format(ticker.url))


# Set Dispatcher From function
token.dispatcher.add_handler(CommandHandler('start', start))   
token.dispatcher.add_handler(MessageHandler(Filters.text, nemad))                   
                             

                        
                        
                        
# Strat Robot !
token.start_polling()


# Delete IDLE Command !
token.idle()
