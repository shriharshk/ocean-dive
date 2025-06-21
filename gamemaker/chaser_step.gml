// obj_chaser Step Event
// Follow the player's x and y position with slight lag
var target = obj_player;
if (instance_exists(target)) {
    x = lerp(x, target.x - 200, 0.05);
    y = lerp(y, target.y, 0.05);
}

// Optional: replace the simple lerp with the Dijkstra Path Finding asset.
// Example usage after importing the asset:
// var chase_path = scr_dijkstra_path(global.nav_grid, x, y, target.x, target.y);
// path_start(chase_path, 4, path_action_stop, false);
