import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime, timedelta

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

reminderss = []
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi! I am your reminder bot. Use /remind HH:MM message to set a reminder.")

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        remind_time, remind_message = context.args[0], ' '.join(context.args[1:])
        reminder_time = datetime.strptime(remind_time, "%H:%M").time()
        now = datetime.now().time()
        reminder_datetime = datetime.combine(datetime.today(), reminder_time)
        if reminder_time < now:
            await update.message.reply_text(f"The {remind_time} time has already Past ,Kindly set a future time")
        else:
            await update.message.reply_text(f"Reminder set for {remind_time} and Message : {remind_message}.")
        # user_id = update.message.from_user.id
        # reminders[user_id] = (remind_time, remind_message) 
        reminderss.append(f"{remind_message} at this {remind_time} time")       
    except (IndexError, ValueError):
        await update.message.reply_text("Invalid input. Use /remind HH:MM message to set a reminder.")

async def reminders(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hi Here are all your reminders\n {reminderss}")
    print(reminderss)

def main() -> None:
    application = Application.builder().token("6778021666:AAG04-ImzepBREVZvT-pCdAzCDcN9F7ANaw").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("remind", remind))
    application.add_handler(CommandHandler("reminders", reminders))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
