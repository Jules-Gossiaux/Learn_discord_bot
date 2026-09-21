## Installation de discord.py

Le projet utilise Python 3.11 ou supérieur et `discord.py` 2.x.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Le point d'entrée est `src/client.py`. Le token doit être placé dans un fichier
`.env` local sous la forme `DISCORD_TOKEN=ton_token_discord`. Ce fichier est
ignoré par Git.
