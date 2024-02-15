# Moon Tank (Base)
ÉTS, LOG725, TP2. 
Par Gabriel C. Ullmann, 2024.

## Instructions
- Installez pygame : `pip install pygame`
- Exécutez le jeu : `python main.py`

# Execution
- Pour exécuter le programme, j'ai ajouté un fichier exécutable (.exe). Veuillez cliquer sur le dossier "dist", puis sur "main.exe".

## Fonctionnalités déjà implémentées
- 2 entités (Player et Wall)
- Chargement des sprites pour les entités
- Collision
- Mouvement

## Sprites
- Tank: https://www.pngkey.com/download/u2q8a9w7t4u2e6r5_tanks-2d-top-down-tank/
- Les autres sprites sont par Gabriel C. Ullmann, 2017
- Background : https://opengameart.org/content/commando-team-action-loop-cut
- Sound effect : https://opengameart.org/content/chaingun-pistol-rifle-shotgun-shots 

## Fonctionnalité
# Menu Principal
- L'utilisateur a deux options : "start" pour commencer le jeu ou "quit" pour quitter le jeu.

# Déroulement du jeu
- L'utilisateur contrôle le joueur avec les flèches.
- Pour tirer des balles, il doit ramasser les munitions par terre, car il commence avec 0 munition.
- Le joueur n'a qu'un seul essai pour chaque balle.
- Un indicateur du nombre de balles restantes est affiché à droite.
- Un bouton de réinitialisation est également affiché à droite.
- Il n'y a qu'un seul niveau dans le jeu.

## Patrons
- J'ai utilisé quelques patrons tels que l'Observer et l'ECS.
