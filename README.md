# Educational Discord Bot

Petit bot Discord écrit en Python avec `discord.py`. Le projet montre une
structure simple mais professionnelle : point d'entrée unique, gestion des
commandes, événements Discord, logs, gestion d'erreurs et limitation de débit.

## Objectif du projet

Ce projet est purement éducatif. Il sert à apprendre :

- la connexion d'un bot à Discord ;
- les intents et les événements Discord ;
- les commandes préfixées (`!ping`, `!bonjour`) ;
- la gestion des erreurs et des cooldowns ;
- l'organisation d'un petit projet Python maintenable.

## Configuration du token

Le token est chargé depuis un fichier local `.env` grâce à `python-dotenv`.
Ce fichier est ignoré par Git et ne doit jamais être commité.

Crée un fichier `.env` à la racine du projet :

```dotenv
DISCORD_TOKEN=ton_token_discord
```

Cette approche est utilisée même pour cette démo éducative afin de montrer une
pratique professionnelle et d'éviter les fuites accidentelles de secrets.

## Fonctionnalités

- `!bonjour` : répond à l'utilisateur avec une mention ;
- `!ping` : affiche la latence WebSocket du bot ;
- `!help` : affiche les commandes disponibles ;
- journalisation de la connexion et des erreurs ;
- message d'information lors de la suppression d'un message en cache ;
- message d'information lors de la modification d'un message en cache ;
- protection anti-spam sur `!ping` avec un cooldown par utilisateur ;
- filtrage des messages envoyés par des bots pour éviter les boucles ;
- limitation du contenu affiché dans les messages d'audit.

## Installation

Python 3.11 ou supérieur est recommandé.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuration Discord

Dans le Developer Portal Discord :

1. crée une application et un bot ;
2. active **Message Content Intent** dans les intents privilégiés ;
3. invite le bot sur un serveur avec uniquement les permissions nécessaires,
   notamment `View Channel` et `Send Messages` ;
4. vérifie que le token est présent dans le fichier local `.env`.

Le bot utilise uniquement les intents par défaut et l'intent `message_content`.

## Lancement

Depuis la racine du projet :

```powershell
python src/client.py
```

Un message de niveau `INFO` confirme la connexion dans la console.

## Structure

```text
.
├── docs/                 # Notes pédagogiques complémentaires
├── src/
│   └── client.py         # Configuration, bot, commandes et événements
├── .gitignore
├── README.md
└── requirements.txt
```

## Limites connues

Les événements de suppression et de modification de `discord.py` concernent
les messages présents dans le cache du bot. Ils ne constituent donc pas un
système d'audit complet. Pour une application réelle, il faudrait notamment
prévoir un stockage dédié, une gestion des permissions, des tests automatisés,
une configuration par environnement et un vrai système de secrets.
