# Assignment 1: Set up a project directory using git

## Introduction

Learn to manage a project using git and GitHub.

## Goals

- Create a project directory in `OMICS/projects/yourgitlogin`
- Add a `README.md` in your project directory
- Change your README.md
- After each successful change, do `commit README.md -m "describe why this change is good"`
- Your project README.md should include the following sections:
  - Introduction
  - Literature Review
  - Methodology
  - Results
  - Discussion
  - Conclusion
  - References

## Datasets

N/a

# Walkthrough

For your project.
 - Choose a login name for https://github.com. Most choose one of two naming styles:
   - Professional: Your initials and last name
   - Fun
   - Techy or Gamer-style
 - Fork from https://github.com/DamLabResources/OMICS
 - Clone from https://github.com/yourgitlogin/OMICS
 - On your PC, add your project directory (`OMICS/projects/yourgitlogin`) and create a `README.md`:
```
$ cd OMICS
$ cd projects
$ mkdir yourgitlogin
$ cd yourgitlogin
$ pwd
  ~OMICS/projects/yourgitlogin
$ nano README.md  
$ git status
$ git add README.md
$ git commit README.md -m 'Beginnings of my project README'
```

# Tests

N/A

Copyright (C) 2024-present, Drexel Medicine, PhD. All rights reserved
