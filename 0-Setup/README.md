# PPS39 OpenFOAM Course
Introduction to OpenFOAM® Computational Library and Viscoelastic Fluid Flow Simulation


## 1 - System preparation

[![System Setup](images/1.png)](http://www.youtube.com/watch?v=m18Arh-FQp0 "System preparation")

Open *Windows PowerShell* as Administrator and run the following command:
```console
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
**Windows 10 users only** should also run the following command in PowerShell as Administrator:
```console
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

After each command you’ll be asked to restart the system, and you should do it.

To finalize this step open again PowerShell as Administrator and run the following command:
```console
wsl --set-default-version 2
```
---
---
## 2 - Windows Subsystem Linux (WSL)

[![System Setup](images/2.png)](http://www.youtube.com/watch?v=if1bGC5suqg "System preparation")

Run the following command in Windows *Command prompt*
```console
wsl –-install -d Ubuntu-22.04
```
---
---
## 3 - Visual Studio Code (VSCode)

[![System Setup](images/3.png)](http://www.youtube.com/watch?v=03MKPOD6puA "System preparation")

Installation website:
```console
https://code.visualstudio.com/
```
---
---
## 4 - Paraview 5.12

[![System Setup](images/4.png)](http://www.youtube.com/watch?v=CfjhF3RAHiw  "System preparation")

Installation website: https://www.paraview.org/download/
---
---
## 5 - OpenFOAM v22.06

[![System Setup](images/5.png)](http://www.youtube.com/watch?v=6NyOLJvoeE0 "System preparation")

5.1 - Add the repository
```console
curl https://dl.openfoam.com/add-debian-repo.sh | sudo bash
```

5.2 - Update the repository information
```console
sudo apt-get update
```

5.3 - install precompiled OpenFOAM v22.06
```console
sudo apt-get install openfoam2206-default
```

5.4 - To open the OpenFOAM shell session:
```console
openfoam2206
```

5.5 - run the following command in linux at the home folder
```console
echo 'shopt -s direxpand' >> .bashrc
```

## 6 - Reduced version of Rheotool (https://github.com/fppimenta/rheoTool/)

[![System Setup](images/6.png)](http://www.youtube.com/watch?v=nNpOZfB-Qso "System preparation")

Move to the home folder
```console
cd
```

6.1 install zip utility

```console
sudo apt-get install zip
```

6.2 Copy and unzip the Reduced version of Rheotool from the course repository

```console
wget https://github.com/Computational-Rheology/PPS39_OFCourse/raw/main/4-Case_studies_Viscoelastic_fluid_flow_solvers/rheotoolPPS39.zip
```

```console
unzip rheotoolPPS39.zip
```

6.3 Load openFOAM environment

```console
openfoam2206
```

6.4 Change to the rheotoolPPS39 folder

```console
cd rheotoolPPS39
```

6.5 Change to the rheotoolPPS39 folder
```console
./downloadEigen
```

6.6 Copy and run the recommended command, e.g.

> echo "export EIGEN_RHEO=/home/<username>/OpenFOAM/<username>-v2206/ThirdParty/Eigen3.2.9">>/home/<username>/.bashrc

6.7 load the .bashrc file

```console
. ~/.bashrc
```

6.8 Change to the src folder

```console
cd src
```

6.9 Compile the Rheotool

```console
./Allwmake
```
