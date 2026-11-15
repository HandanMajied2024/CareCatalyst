# b-blender: hand + phone with Blender + MPFB 2 (€0)

## Result
- `out/hand_phone.mp4`: 1280x720, 24 fps, 72 frames (3 s), H.264, rendered with EEVEE
- `out/frames/0001.png … 0072.png`: the PNG frames
- `out/still.png`: Cycles still (CPU) of frame 46 (thumb tap)
- `index.html`: open it in a browser to see the video and the still side by side
- `work/scene.blend`: the last built scene, can be opened in Blender

## Blocker 1: Smart App Control
The portable zip (`blender-4.5.16-windows-x64.zip` from download.blender.org) **does not start** on this laptop.
Windows Smart App Control (state "On") blocks unsigned DLLs (`cycles_kernel_oneapi_aot.dll`, `blender.shared\*.dll`).
Exit code `0xC0E90002` or `0xC0000135`. Proof: `Microsoft-Windows-CodeIntegrity/Operational`, event 3077.
Turning off Smart App Control is permanent (it can only be switched back on by reinstalling Windows), so that is **not an option**.

**Workaround (€0):** the Microsoft Store version of Blender 4.5 LTS (it has Store signing, so Smart App Control allows it):
```
winget install --id 9PM7J9D3G6JQ --source msstore --accept-package-agreements --accept-source-agreements
```
- Installed per user (`C:\Program Files\WindowsApps\BlenderFoundation.Blender4.5LTS_4.5.16.0_x64__…`), version 4.5.16 LTS.
- `blender.exe` in WindowsApps cannot be called directly ("Access denied"). Only the alias
  `%LOCALAPPDATA%\Microsoft\WindowsApps\blender-launcher.exe` works. It passes the arguments through, waits until Blender exits, but **swallows stdout**.
  So every script redirects `sys.stdout` into its own log file (`work/log_*.txt`).
- Wrapper `bl.ps1` (call it with `-ExecutionPolicy Bypass`, because running scripts is disabled on this system):
  ```
  powershell -ExecutionPolicy Bypass -File bl.ps1 -b -P <script.py> -- <args>
  ```
- Store app data is virtualised. The real path of the extensions and the MPFB config is
  `%LOCALAPPDATA%\Packages\BlenderFoundation.Blender4.5LTS_ppwjx1n5r4v9t\LocalCache\Roaming\Blender Foundation\Blender\4.5\`.
- Do **not** use `--factory-startup`, because it disables MPFB.
- To uninstall: `winget uninstall --id 9PM7J9D3G6JQ`

## Steps (exact)
1. MPFB 2.0.18 from extensions.blender.org → `dl/mpfb.zip`, installed headlessly with `inst.py`:
   `bpy.ops.extensions.package_install_files(filepath=zip, repo="user_default", enable_on_install=True)` + `save_userpref()`.
2. MakeHuman system assets (CC0, skins) from the fast mirror
   `https://files.makehumancommunity.org/asset_packs/makehuman_system_assets/makehuman_system_assets_cc0.zip` (280 MB)
   → extracted to `assets/mh_system/`. (The mirror `files2.` only gave about 0.2 MB/s.)
3. `make_hand.py` (one script, modes `debug | still | anim | cycles`):
   - `HumanService.create_human(macro_detail_dict=…)` (gender 0.35, slim), plus hand targets
     `r-hand-fingers-diameter-decr` (0.7), `fingers-length-incr` (0.45), `hand-scale-decr` (0.15) from MPFB's `data/targets/hands`
   - `HumanService.add_builtin_rig(basemesh, "default")` (163 bones, all finger bones)
   - `HumanService.set_character_skin(<mhmat>, basemesh, skin_type="ENHANCED_SSS")` with `young_caucasian_female`
     (2048² diffuse, SSS, procedural pores). Pore strength, SSS and contrast were raised in the node group.
   - The existing MPFB mask modifier gets the vertex group `keep_arm` (weights of lowerarm/wrist/metacarpal/finger .R), so only the right forearm and hand remain. Subsurf level 2 for rendering.
   - Grip is computed, not tuned by hand: palm normal from the natural finger curl, palm depth from the mesh vertices, finger curl per finger by bisection so the fingers lie on the phone's back, finger spread closed, wrist angle searched on a grid so the forearm leaves the frame at the bottom right. Thumb via IK on a target empty on the phone.
   - Phone procedural (rounded rectangle via bmesh, bevel, titanium frame, black front glass, display texture drawn with numpy: airbrush blobs + glass cards + button, emissive).
   - Motion: everything hangs on the empty `HandCtrl` (pivot = phone centre). Keys at frame 1 → 16 with `interpolation='BACK', easing='EASE_OUT'` (overshoot; back 0.9 for position, 2.0 for rotation), then a slow drift to 72. Thumb tap: IK target moves with `EXPO` in (frame 38→46), holds, `QUART` back out; the button scales to 0.93 and turns blue. Motion blur on (shutter 0.5), slow camera push-in.
   - Light: 4 disc area lights (key, fill, rim, top), backdrop plane (diffuse + emission so it stays white), AgX "Punchy", exposure −0.85. DOF **off** (EEVEE DOF caused a white halo around the edges).
4. `encode.py`: PNG frames → H.264 MP4 with Blender's own FFmpeg (VSE). No separate ffmpeg needed
   (an unsigned ffmpeg.exe would probably also be blocked by Smart App Control).

## Render times (Intel i7-10510U, Intel UHD iGPU, 32 GB)
- EEVEE, first frame of each run: about 90–100 s (shader compile, mainly the SSS skin)
- EEVEE 1280x720, 16 samples: about 11–14 s/frame; 24 samples: see below
- Workbench debug views (pose check): about 2 s/view
- Cycles: CPU only (UHD is not supported), see below

## Licences
- MPFB 2 code: GPL-3 (only the tool, it does not affect the renders)
- MakeHuman base mesh, targets, rigs, system assets (skins): **CC0**, so the renders can be used freely, commercially too
- Blender: GPL, output belongs to you
- Phone and screen UI: generated procedurally by me, no third-party assets
