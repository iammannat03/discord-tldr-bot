# Discord TLDR Bot

A Discord bot that provides concise summaries of conversations in your server using Google's Gemini AI.

## Features

- Summarize recent messages in a channel
- Customizable number of messages to summarize
- Easy-to-use commands
- Powered by Google's Gemini AI for high-quality summaries

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
4. Get your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
5. Get your Gemini API key from the [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

1. Start the bot:
   ```bash
   python bot.py
   ```
2. Use the following commands in your Discord server:
   - `!tldr [number]` - Summarize the last N messages (default: 5)
   - `!help_tldr` - Show help information

## Requirements

- Python 3.8 or higher
- Discord.py
- Google Generative AI Python SDK
- Discord bot token
- Gemini API key

## Contributing

Feel free to submit issues and enhancement requests!
