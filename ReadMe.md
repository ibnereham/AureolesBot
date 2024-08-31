
# Aureoles Discord Bot

Aureoles is a Discord bot designed to manage and enhance your server's functionalities, including logging, moderation, general chat features, and F1 race day alerts. To get started, you need to configure the environment variables and install the necessary Python packages.

## Environment Variables

Before running the Aureoles bot, make sure to set up your environment variables in an `.env` file. Below is the list of variables you need to configure:



```
TOKEN=<EnterYourID>               # Your bot's Discord token
MONGODB_AU_URL=<EnterYourID>      # MongoDB connection URL for data storage
SRV_NAME="ServErName"             # Name of the server the bot is associated with
GEN_CHAT=<EnterYourID>            # General chat channel ID
FreeSpeechRoleID=<EnterYourID>    # Role ID for free speech permissions
WARN_LOG_CHANNEL=<EnterYourID>    # Channel ID for logging warnings
MSG_LOG_CHANNEL=<EnterYourID>     # Channel ID for logging messages
AdminRoleID=<EnterYourID>         # Role ID for admin users
GuildID=<EnterYourID>             # Discord server (guild) ID
```
### Note: Free Speech role is the role which makes you invunerable to message delete when bad words are detected.
Replace `<EnterYourID>` with the appropriate IDs and credentials for your Discord server.

## Installing Requirements

To install the required Python packages, use the provided `requirements.txt` file. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command will install all the necessary dependencies for the Aureoles bot to function correctly.

## Running the Bot

Once you have set the environment variables and installed the required packages, you can run the bot with:

```bash
python bot.py
```

Ensure that your Discord bot has the appropriate permissions in the server and that your environment variables are correctly set up.
# Aureoles Discord Bot Preset Commands

This is a list of commands available for the Aureoles Discord Bot.

## Commands

- **`/rules`**
  - Displays the server rules.

- **`/addbadwords`**
  - Description: Add bad words to the filter list.  
  - Usage: `/addbadwords <words>` (words separated by space).

- **`/checkbadwords`**
  - Displays the current list of filtered bad words.

- **`/resetbadwords`**
  - Resets the list of filtered bad words to empty.

- **`/removebadwords`**
  - Description: Removes specified words from the filter list.  
  - Usage: `/removebadwords <words>` (words separated by space).

- **`/removeonewarn`**
  - Description: Removes one warning from a user.

- **`/checkwarn`**
  - Description: Checks the number of warnings a user has.

- **`/resetwarn`**
  - Description: Sets the warning count for a user to zero.

- **`/removefromf1`**
  - Description: Removes the user from the F1 notification list.

- **`/addtof1`**
  - Description: Adds the user to the F1 notification list.

# Need Help?

If you encounter any errors or issues, feel free to contact me on Discord: **@h6s**