# PPS39 OpenFOAM Course
Introduction to OpenFOAM® Computational Library and Viscoelastic Fluid Flow Simulation


## 0 - System preparation
Whatch this video
[![System Setup](https://youtu.be/-UVMnzBTUXg/0.jpg)](https://youtu.be/-UVMnzBTUXg"System preparation")

Open *Windows PowerShell* as Administrator and run the following command:
```console
> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
**Windows 10 users only** should also run the following command in PowerShell as Administrator:
```console
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

After each command you’ll be asked to restart the system, and you should do it.

To finalize this step open again PowerShell as Administrator and run the following command:
```console
> wsl --set-default-version 2
```

## 1 - Install Windows Subsystem Linux (WSL)

Run the following command in Windows *Command prompt*
```console
> wsl –-install -d Ubuntu-22.04
```