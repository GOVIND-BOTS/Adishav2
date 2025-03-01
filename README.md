
# AdishaV2 - Ultimate Telegram Music Bot

README = """
AdishaV2 is a powerful and feature-rich Telegram music bot built using Pyrogram v2. It supports YouTube, Spotify, Apple Music, SoundCloud, Resso, and Telegram files, with additional features like admin commands, global bans, and federation management.

## Features
- Stream music from YouTube, Spotify, Apple Music, SoundCloud, and more.
- Admin Controls: Play, Pause, Resume, Stop, Skip.
- Auto Thumbnail Fetching: YouTube thumbnails for now playing.
- Special Welcome Messages: Custom messages for Owners/Sudo users.
- Interactive Buttons: For seamless user experience.
- Editable Eval System: Results update without re-executing commands.
- Global Ban & Federation Management: For moderation.
- Fun Mode (OYO Mode) for entertaining group members.

![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)
![Adisha Music](https://example.com/adisha-music.png)

## Commands List
### Music Commands
- `/play [song name/url]` - Play a song
- `/pause` - Pause current track
- `/resume` - Resume paused track
- `/stop` - Stop music playback
- `/skip` - Skip to next track
- `/queue` - Show current queue

Click the button below to deploy **AdishaV2** on **Heroku** effortlessly:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/GOVIND-BOTS/Adishav2)

### Admin Commands
- `/ban @user` - Ban a user
- `/unban @user` - Unban a user
- `/mute @user` - Mute a user
- `/unmute @user` - Unmute a user
- `/fban @user` - Federation ban a user
- `/unfban @user` - Unban from federation
- `/createfed name` - Create a federation

### Owner/Sudo Commands
- `/eval code` - Run Python code
- `/speedtest` - Check server speed
- `/reload` - Reload bot modules
- `/sudo` - Show sudo users

## VPS Deployment Guide
### Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip ffmpeg -y
```
### Clone the Repository
```bash
git clone https://github.com/GOVIND-BOTS/AIMUSICBOT
cd AIMUSICBOT
```
### Install Requirements
```bash
pip3 install -U -r requirements.txt
```
### Configure Bot
Create a `.env` file and add your bot credentials:
```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_user_id
```
### Run the Bot
```bash
python3 -m AdishaV2
```

## Support & Contact
For any help or issues, join our [Support Group](https://t.me/GOVINDSUPPORT) or check out the [GitHub Repository](https://github.com/GOVIND-BOTS/Adishav2).

Enjoy the best music experience on Telegram with AdishaV2!
"""

print(README)
```

