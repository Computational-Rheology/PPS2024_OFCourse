# PPS39 OpenFOAM Course
Introduction to OpenFOAM® Computational Library and Viscoelastic Fluid Flow Simulation


## 0 - System preparation

Open Windows PowerShell as Administrator and run the following command:

> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

**Windows 10 users only** should also run the following command in PowerShell as Administrator:

> DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V

After each command you’ll be asked to restart the system, and you should do it.

To finalize this step open again PowerShell as Administrator and run the following command:

> wsl --set-default-version 2

## 1 - Install Windows Subsystem Linux (WSL)

