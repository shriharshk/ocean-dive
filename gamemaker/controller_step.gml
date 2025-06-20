// obj_controller Step Event
spawn_timer += 1;
if (spawn_timer > spawn_delay) {
    instance_create_layer(room_width + 32, irandom_range(50, room_height - 50), "Instances", obj_obstacle);
    spawn_timer = 0;
}
