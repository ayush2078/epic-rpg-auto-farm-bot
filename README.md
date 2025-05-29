# epic-rpg-auto-farm-bot

# Step 1: Deploy on Railway

1. Go to [https://railway.app](https://railway.app) and **log in** or **sign up**.

2. Click **New Project** → **Deploy from GitHub repo** → select your repo.

3. Once deployed, go to your Railway project dashboard → **Variables** section.

4. Add a variable:

   ```
   Key: BOT_TOKEN
   Value: your_actual_bot_token
   ```

5. In **Deploy > Settings** set the start command:

   ```
   python main.py
   ```

---

# Step 2: Update channel ID in `main.py`

Open `main.py` and find the line:

```python
channel = bot.get_channel(YOUR_CHANNEL_ID)  # Replace this with your actual channel ID
```

Replace `YOUR_CHANNEL_ID` with your Discord channel’s ID (right-click channel → Copy ID).

---

# Step 3: Run & Test

* Deploy the app on Railway.
* Wait for the bot to come online (check logs on Railway).
* In your Discord server, type:

  ```
  !start
  ```
* Your bot should begin sending Epic RPG commands like `rpg hunt` automatically.
