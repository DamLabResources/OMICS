# Drexel Medicine OMICS class

## [Week 1 Summary: Intro to JupyterHub, Linux and GitHub](#week-1-details-intro-to-jupyterhub-linux-and-github-1)

1. [Log in to Drexel Medicine VPN and JupyterHub](#1-log-in-to-drexel-medicine-jupyterhub)
2. [Open a terminal window in JupyterHub](#2-open-a-terminal-window-on-jupyterhub)
3. [Make a directory to store your projects (w/Linux commands)](#3-make-a-directory-to-store-your-projects-wlinux-commands)
4. [Commit (save version) and backup your project (w/GitHub)](#4-save-and-backup-your-projects-wgithub)
5. [Lab instructions](#5-week-1-lab-instructions)


# Weekly Details

## Week 1 Details: Intro to JupyterHub, Linux and GitHub

### 1. Log in to Drexel Medicine JupyterHub
* Install Drexel Medicine VPN: https://drexel.edu/it/help/a-z/VPN/
* Login to the Drexel Medicine:
<p><img src="images/wk01a_vpn_login.png" alt="Connect" width="400"></p>    
<p><img src="images/wk01b_vpn_login.png" alt="Login"   width="400"></p>    
<p><img src="images/wk01c_vpn_login.png" alt="Accept"  width="400"></p>    

### 2. Open a terminal window on JupyterHub
#### 2a. Open JupyterHub
http://10.11.19.48/

#### 2b. Open a terminal window
In web browser, from JupyterLab menu:    
```
File -> New -> Terminal
```


### 3. Make a directory to store your projects (w/Linux commands):
In the terminal window that you just opened, type each command and press the [Enter] button:    
* Show the name of your present working directory (`pwd`)
* List the contents of your home directory (`ls`)
* Change directory to the `repos` directory (`cd repos`)

### 4. Save and backup your projects (w/GitHub)
#### 4a. Create an account on https://github.com
#### 4b. Copy (Fork) the Drexel Medicine OMICS class, https://github.com/dvklopfenstein/OMICS, to your GitHub account (Fork)
<p><img src="images/wk01d_fork_desc.png" alt="Connect" width="400"></p>    
<p><img src="images/wk01e_fork_button.png" alt="Connect" width="400"></p>    
#### 4c. Download (git clone) a copy to your PC     


<p><img src="images/wk01f_clone.png" alt="Connect" width="400"></p>    
```
git clone https://github.com/<your_profile>/OMICS
```

### 5. Week 1 Lab Instructions
#### 5a. Create a batch file, `week01_lab.sh` which contains all commands from step 2:
`nano` is a command-line text editor.    
But you can use your favorite editor:
  * `nano week01_lab.sh`
  * `vim week01_lab.sh`
  * `emacs week01_lab.sh`

```
$ cd ~/repos/OMICS
$ nanno week01_lab.sh
```
#### 5b. Commit `week01_lab.sh` to your local disk:
```
$ cd ~/repos/OMICS
$ git add week01_lab.sh
$ git commit week01_lab.sh -m 'Adding lab batch file'
```
#### 5c. Backup your work to GitHub:
```
$ git remote -v
origin 	https://github.com/[studentrepo]/OMICS.git (fetch)
origin 	https://github.com/[studentrepo]/OMICS.git (push)
$ git branch
* main
$ git push origin main
```

#### 5d. Run your batch file:
```
source week01_lab.sh | tee week01_lab.txt
```



Copyright (C) 2023-present, Drexel Medicine. All rights reserved
