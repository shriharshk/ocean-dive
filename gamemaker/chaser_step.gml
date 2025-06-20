// obj_chaser Step Event
// Follow the player's x and y position with slight lag
var target = obj_player;
if (instance_exists(target)) {
    x = lerp(x, target.x - 200, 0.05);
    y = lerp(y, target.y, 0.05);
}
