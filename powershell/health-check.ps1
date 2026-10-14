Write-Host "=== SYSTEM HEALTH REPORT ==="

$cpu = Get-CimInstance Win32_Processor
$memory = Get-CimInstance Win32_OperatingSystem
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"

Write-Host ""

Write-Host "CPU Information:"
$cpu | Format-Table Name, NumberOfCores -AutoSize

Write-Host ""

Write-Host "Memory Free (KB):"
Write-Host $memory.FreePhysicalMemory

Write-Host ""

Write-Host "Disk Information:"
$disk | Format-Table DeviceID, FreeSpace, Size -AutoSize