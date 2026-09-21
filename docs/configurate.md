## Création et configuration du bot sur le Developer Portal
1. Se rendre sur le developer portal: https://discord.com/developers/applications
2. Créer un projet
3. Dans `Installation`, choisir uniquement les permissions nécessaires, par exemple `View Channel` et `Send Messages`.
4. copier l'url d'installation et l'ouvrir dans un nouvel onglet
5. Choisir le serveur dans lequel on veut dev le bot
6. Dans l'onglet `Bot`, activer `Message Content Intent` dans `Privileged Gateway Intents`.
7. Copier le token uniquement dans la configuration locale prévue par la démo.

Le projet est éducatif : le token est exceptionnellement présent dans
`src/client.py`. Pour tout projet réel, utiliser une variable d'environnement
ou un gestionnaire de secrets.
