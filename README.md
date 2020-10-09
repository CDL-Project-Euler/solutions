# Solutions
Solution codes for Project Euler problems less than 100, as completed for educational purposes by Collège du Léman students.

## How to upload your solutions
To be able to use Github, you will need the [`Git`](https://git-scm.com/) installed on your device. Depending on your operating system, there may be different ways of accomplishing this task.

### MacOS Installation
To install these tools, you will need to open the `Terminal` application on your Mac.

You will first need to install [`Hombrew`](https://brew.sh/), a package manager (an app-store for your terminal), and you can do so by pasting the following command in your terminal and hitting enter:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Once this is done, to install `Git`, paste the following command and also hit enter:

```
brew install git
```

### Windows Installation
Simply follow the instructions [here](https://git-scm.com/download/win).

### Cloning from Github
Now that you have the tools ready, follow these steps to get the project files onto your system:

1. Open up your CLI (Command Line Intrface), e.g. `Terminal` on MacOS, or `Powershell` on Windows.

2. Create a directory/folder for your programming endeavours (skip this step if you already have such a folder) with the following command:
```
mkdir your_folder_name
```

3. After, move into said directory with the following command:
```
cd your_folder_name
```

4. If you have your own folder in a separate location, you can move into it with the following:
```
cd path/to/your_folder_name
```

5. Once in your desired folder, you can clone this repository (i.e. project files) onto your machine and move into it via:
```
git clone https://github.com/CDL-Project-Euler/solutions.git
cd solutions
```

### Editing files
Once inside the solutions folder, you can do a numbere of things:
- `git pull origin master` to sync your local repository with the one on Github
- `touch filename.some_extension` to create a file
- `open filename.some_extension` to open a file
- `code .` to open the folder in [`VSCode`](https://code.visualstudio.com/)

### Uploading to Github
After making changes to the files, you can run the following commands to upload them back onto Github:

```
git pull origin master
git add .
git commit -m "commit message, e.g. Solution for some_problem, yay for me!"
git push origin master
```

You may be asked to enter your username/email and password for Github, in such a case, do so.

## Solutions formatting
The solutions uploaded to this repository are divided into four folders that each have folders for
the appropriate solutions. If this folder does not exist, you may create it following the `pXXX`
naming scheme. The following rules within a single `pXXX` solutions folder apply:

1. Your name / username used must be consistent across all solutions pushed to this repository

2. If your solution is contained within a single file, this file should have your name / username
and the extension.

3. If your solution requires more than a single file, it must be contained within an additional
folder also bearing your name / username, and no extension. Within it, you are free to name as you like.

4. Don't upload binaries and compiled versions of your solutions.

