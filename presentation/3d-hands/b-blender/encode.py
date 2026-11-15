# Encode out/frames/*.png -> out/hand_phone.mp4 (H.264) using Blender's own FFmpeg (no external ffmpeg needed)
import bpy, os, sys
B = r"C:\Users\tutuh\Documents\Hackjuntion_Finnland_2026\3d-hands\b-blender"
log = open(os.path.join(B, "work", "log_encode.txt"), "w"); sys.stdout = sys.stderr = log
fdir = os.path.join(B, "out", "frames")
files = sorted(f for f in os.listdir(fdir) if f.endswith(".png"))
scn = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
scn.sequence_editor_create()
strip = scn.sequence_editor.strips.new_image("frames", os.path.join(fdir, files[0]), 1, 1) if hasattr(scn.sequence_editor, "strips") else scn.sequence_editor.sequences.new_image("frames", os.path.join(fdir, files[0]), 1, 1)
for f in files[1:]: strip.elements.append(f)
scn.frame_start, scn.frame_end = 1, len(files)
r = scn.render; r.fps = 24; r.resolution_x, r.resolution_y, r.resolution_percentage = 1280, 720, 100
scn.view_settings.view_transform = 'Standard'; scn.view_settings.look = 'None'; scn.view_settings.exposure = 0
r.image_settings.file_format = 'FFMPEG'
r.ffmpeg.format = 'MPEG4'; r.ffmpeg.codec = 'H264'; r.ffmpeg.constant_rate_factor = 'HIGH'; r.ffmpeg.ffmpeg_preset = 'GOOD'
r.ffmpeg.gopsize = 12
r.use_sequencer = True
r.filepath = os.path.join(B, "out", "hand_phone.mp4")
bpy.ops.render.render(animation=True)
print("encoded", len(files), "frames ->", r.filepath); log.close()
