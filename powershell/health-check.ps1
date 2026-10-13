Write-Host "=== SYSTEM HEALTH REPORT ==="

$cpu = Get-Counter '\Processor(_Total)\% Processor Time'

Write-Host "CPU Usage:"
$cpu.CounterSamples.CookedValue

$memory = Get-CimInstance Win32_OperatingSystem

Write-Host "Memory Free:"
$memory.FreePhysicalMemory

$disk = Get-CimInstance Win32_LogicalDisk

Write-Host "Disk Information:"
$disk | Select DeviceID,FreeSpace,Size