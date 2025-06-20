# Mermaid Runner - GameMaker Implementation

This folder contains simple GameMaker Language (GML) scripts to build the Mermaid Runner prototype. Import these scripts into a GameMaker project and assign them to objects/events as noted.

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
