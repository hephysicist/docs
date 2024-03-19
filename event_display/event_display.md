# Event display
These instructions work on lxplus with Scientific Linux 7 or Red Hat Enterprise Linux 8. If you are using different system release, please use Singularity containers:
```
cmssw-sl7
```
For further information check this [cmssw page](https://cms-sw.github.io/singularity.html).

To start working with the event display you first need to install cmssw
```
export CMSSW=CMSSW_10_6_30
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel $CMSSW
cd $CMSSW/src
cmsenv
```
Then copy the ISpy code from [GitHub](https://github.com/cms-outreach/ispy-analyzers) to the source directory of your environment and try to compile:
```
git clone https://github.com/cms-outreach/ispy-analyzers.git ISpy/Analyzers 
git clone https://github.com/cms-outreach/ispy-services.git ISpy/Services

scram b
```
To access the files on CERN storage you may need to run `voms-proxy-init --rfc --voms cms` command and init your GRID proxy. 
Configuration files are stored in the `ISpy/Analyzers/python` directory. 
You can find an [example configuration file](https://github.com/hephysicist/docs/blob/8b27590540f080e07c58b74f887e0aeb7d0cdd44/event_display/ispy_miniAOD.py) in the current directory. After editing the config, you can run the analysis by typing:
```
cmsRun python/ispy_miniAOD.py #Put here the name of your config file
```
This results in the creation of _.ig_ file with events to show at the event display in the parent directory. Please, save this file locally. 
Open the browser-based [event display app](https://ispy-webgl.web.cern.ch/) and click on the first icon from the left to upload your _.ig_ file. 
After that, you will see the event constituents and detector layout. 

