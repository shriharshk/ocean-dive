// obj_player Step Event
if (keyboard_check(vk_up)) {
    vertical_speed = -5;
} else if (keyboard_check(vk_down)) {
    vertical_speed = 5;
} else {
    vertical_speed = 0;
}

y += vertical_speed;
y = clamp(y, 0, room_height - sprite_height);

// After importing the Draw Sprite Along Path asset, you can animate the
// mermaid along a curved path in the Draw event using the provided
// `draw_sprite_along_path()` script.
