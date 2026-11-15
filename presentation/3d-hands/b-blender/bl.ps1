# Wrapper: runs Store-Blender headless via app execution alias (portable zip blocked by Smart App Control)
$quoted = $args | ForEach-Object { if ($_ -match '\s') { '"' + $_ + '"' } else { $_ } }
$p = Start-Process -FilePath "$env:LOCALAPPDATA\Microsoft\WindowsApps\blender-launcher.exe" -ArgumentList $quoted -Wait -PassThru -WindowStyle Hidden
exit $p.ExitCode
