# Mermaid Runner - Unity Prototype

This folder contains basic C# scripts to build the Mermaid Runner game in Unity.
Create a new **2D** project and copy the `Assets` directory into it.

The scripts implement a side-scrolling endless runner set underwater with an
ocean current that keeps the mermaid on a fixed path. Leaving the current hurts
the player.

## Scripts

- `PlayerController.cs` – moves the mermaid forward and allows vertical control.
- `OceanCurrent.cs` – clamps the player inside the current and applies damage
  when she attempts to exit.
- `GameManager.cs` – spawns obstacles, tracks health, and plays background music
  (add an `AudioSource` component with a track from the **Dusty Chip I Music
  Library**).
- `Obstacle.cs` – deals damage when the player collides with an obstacle.
- `Chaser.cs` – simple follower script for the octopus pursuing the player.

Attach these scripts to your prefabs:

1. **Player** GameObject with a `Rigidbody2D` and `Collider2D` tagged `Player`.
2. **OceanCurrent** area using a `BoxCollider2D` set as Trigger and the
   `OceanCurrent` script.
3. **GameManager** empty object with the `GameManager` script and an
   `AudioSource` component (add a music file from the Dusty Chip I pack).
4. **Obstacle** prefab with a `Collider2D` set as Trigger using `Obstacle`.
5. **Chaser** object with the `Chaser` script, assigning the Player as target.

## Free Ocean Assets

For environment art, models, and particle effects, browse the [Unity Asset Store's free ocean assets](https://assetstore.unity.com/search#q=ocean&nf-ec_price_filter=0...0). Import any packs you like through **Unity Hub** before testing the scene.

Press **Play** to test the endless running and obstacle spawning.
