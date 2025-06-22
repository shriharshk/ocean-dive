// obj_controller Create Event
spawn_delay = 60; // frames
spawn_timer = 0;

// After importing the Dusty Chip I Music Library asset, play a track
// as background music. Replace `snd_dusty_title` with the actual
// sound resource name from the asset.
if (!audio_is_playing(snd_dusty_title)) {
    audio_play_sound(snd_dusty_title, 1, true);
}
