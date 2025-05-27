import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from transformers import pipeline
import torch

# Load environment variables
load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the summarization pipeline with memory optimizations
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",  # Using a more efficient model
    device=0 if torch.cuda.is_available() else -1,  # Use GPU if available
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32  # Use half precision if GPU available
)

# Clear CUDA cache if available
if torch.cuda.is_available():
    torch.cuda.empty_cache()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='tldr')
async def tldr(ctx, num_messages: int = 5):
    """
    Summarize the last N messages in the channel
    Usage: !tldr [number_of_messages]
    """
    messages = []
    async for message in ctx.channel.history(limit=num_messages):
        if not message.author.bot:
            messages.append(f"{message.author.name}: {message.content}")
    if not messages:
        await ctx.send("No messages found to summarize!")
        return
    text = "\n".join(messages)
    try:
        summary = summarize_text(text)
        await ctx.send(f"📝 **TLDR Summary:**\n{summary}")
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error while summarizing: {str(e)}")

@bot.command(name='help_tldr')
async def help_tldr(ctx):
    help_text = """
🤖 **TLDR Bot Commands:**
`!tldr [number]` - Summarize the last N messages (default: 5)
`!help_tldr` - Show this help message

Example: `!tldr 10` will summarize the last 10 messages in the channel.
    """
    await ctx.send(help_text)

def summarize_text(text, max_length=60, min_length=10):
    # Hugging Face models have a max input length
    if len(text) > 1000:
        text = text[:1000]
    
    # Clear CUDA cache before summarization if available
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 