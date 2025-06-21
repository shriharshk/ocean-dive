# ocean-dive

This repository contains prototypes for the **Mermaid Runner** endless runner game.

- `unity/` – C# scripts for a Unity implementation.
- `mermaid_runner.py` – A legacy Pygame prototype.
- `gamemaker/` – GML scripts for a GameMaker implementation.

Use the GameMaker scripts to create objects (`obj_player`, `obj_obstacle`, `obj_controller`, `obj_chaser`) and attach the code to their events as explained in `gamemaker/README.md`. The GameMaker implementation also makes use of free Marketplace assets: **Draw Sprite Along Path**, **Dijkstra Path Finding**, and **Dusty Chip I Music Library**.

For a Unity version of the game, copy the contents of the `unity/Assets` folder into a new Unity 2D project. The included scripts handle player movement, obstacle spawning, and the ocean current mechanic.
To quickly gather art and prefabs, visit the [Unity Asset Store search for free ocean assets](https://assetstore.unity.com/search#q=ocean&nf-ec_price_filter=0...0). Import any suitable models, terrain, or particle effects through **Unity Hub** to enhance the underwater environment.

The latest prototype features an **ocean current** acting as the runner's path. Once the mermaid is pulled into the current she cannot escape without taking damage.
