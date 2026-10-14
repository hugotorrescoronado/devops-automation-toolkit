#!/bin/bash

echo "=== SYSTEM HEALTH REPORT ==="

echo ""
echo "Hostname:"
hostname

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Memory Usage:"
free -m

echo ""
echo "CPU:"
top -bn1 | head