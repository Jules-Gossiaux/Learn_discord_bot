## Événements et commandes

`@bot.event` indique à `discord.py` qu'une fonction gère un événement Discord.

Dans ce projet :

- `on_message` filtre les bots et transmet les messages au système de commandes ;
- `on_message_delete` signale les suppressions de messages mises en cache ;
- `on_message_edit` signale les modifications de contenu ;
- `@bot.command()` déclare les commandes `!bonjour`, `!ping` et `!help`.

`message.channel.send(...)` envoie un message dans le canal courant.
`message.author.bot` indique que l'auteur est un bot.
`message.content` contient le texte du message.

