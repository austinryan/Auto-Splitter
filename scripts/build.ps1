& "$PSScriptRoot/compile_resources.ps1"
pyinstaller `
  --windowed `
  --onefile `
  --additional-hooks-dir=Pyinstaller/hooks `
  --icon=res/icon.ico `
  --splash=res/splash.png `
  "$PSScriptRoot/../src/AutoSplit.py"

If ($IsLinux) {
  Move-Item $PSScriptRoot/../dist/AutoSplit $PSScriptRoot/../dist/AutoSplit.elf
  If ($LastExitCode -eq 0) {
    Write-Host 'Added .elf extension'
  }
}