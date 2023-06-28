import bpy

@bpy.app.handlers.persistent
def update_helper_modes(scene, depsgraph):
    if scene.sequence_editor:
        for strip in scene.sequence_editor.sequences_all:
            if strip.type == 'META':
                mode = strip.video_podcast_helper_modes
                if mode == 'IGNORE':
                    continue
                else:
                    for inner_strip in strip.sequences:
                        if inner_strip.video_podcast_helper_modes == 'IGNORE':
                            continue
                        elif inner_strip.video_podcast_helper_modes == mode:
                            inner_strip.mute = False
                        else:
                            inner_strip.mute = True