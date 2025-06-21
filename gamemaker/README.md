# Mermaid Runner - GameMaker Implementation

This folder contains simple GameMaker Language (GML) scripts to build the Mermaid Runner prototype. Import these scripts into a GameMaker project and assign them to objects/events as noted.

The mermaid swims along a powerful ocean current. Once she is inside this current, attempts to leave will injure her.

## Scripts

- `player_create.gml` – Create Event for `obj_player`
- `player_step.gml` – Step Event for `obj_player`
- `obstacle_create.gml` – Create Event for `obj_obstacle`
- `obstacle_step.gml` – Step Event for `obj_obstacle`
- `controller_create.gml` – Create Event for `obj_controller`
- `controller_step.gml` – Step Event for `obj_controller` (handles obstacle spawning)
- `chaser_step.gml` – Step Event for `obj_chaser` (follows the player)

## Usage

1. Create the objects `obj_player`, `obj_obstacle`, `obj_controller`, and `obj_chaser` in GameMaker.
2. Attach the relevant scripts to their respective events.
3. Place `obj_controller` in the starting room to manage obstacle spawning and game state.
4. Run the game to test the endless runner mechanics.

## Marketplace Assets

Import the following free assets from the GameMaker Marketplace:

1. **Draw Sprite Along Path** – <https://marketplace.gamemaker.io/assets/1602/draw-sprite-along-path>
   - Use this to smoothly animate sprites following predefined paths. Apply it in the mermaid's Draw event or when spawning obstacles that travel along curves.
2. **Dijkstra Path Finding** – <https://marketplace.gamemaker.io/assets/5726/dijkstra-path-finding>
   - Provides scripts for grid-based navigation. Use these scripts in `chaser_step.gml` so the octopus can navigate around obstacles while pursuing the player.
3. **Dusty Chip I Music Library** – <https://marketplace.gamemaker.io/assets/438/dusty-chip-i-music-library>
   - Import these chiptune tracks and play one in `controller_create.gml` using `audio_play_sound()` for background music.
