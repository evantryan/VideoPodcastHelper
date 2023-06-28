import bpy

class SequencerButtonsPanel:
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'

    @staticmethod
    def has_sequencer(context):
        return (context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'})

    @classmethod
    def poll(cls, context):
        return cls.has_sequencer(context) and (context.active_sequence_strip is not None)


class SEQUENCER_PT_podcast_modes(SequencerButtonsPanel, bpy.types.Panel):
    bl_label = "Podcast Helper"
    bl_category = "Strip"

    @classmethod
    def poll(cls, context):
        if not cls.has_sequencer(context):
            return False

        strip = context.active_sequence_strip
        if not strip:
            return False

        return strip.type != 'SOUND'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        strip = context.active_sequence_strip

        layout.active = not strip.mute

        col = layout.column()
        col.prop(strip, "video_podcast_helper_modes", text="Mode")