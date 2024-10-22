# Drexel Medicine Advanced OMICS
MIIM-620S

1. [Course](#course)
2. [Layout](#repository-layout)
3. [Schedule](#weekly-schedule)
4. [Projects](projects/README.md)
5. [Grading](grading/README.md)
6. [Cheatsheets](#cheatsheets)
7. [Datasets](datasets/)

## Course 

### Course Description

Recent advances in molecular biology and computational achievements
have generated an explosion of data that surveys biological processes on a massive scale.
Collectively referred to as ‘omics scale data,
these techniques have revolutionized our ability
to explore complex phenotypes in microbiology & immunology.
This course covers the history, application, and computational analysis
of ‘omics scale data and provides hands-on analysis experience. 

### Course Objectives

1. Recognize popular next-generation sequencing technologies and distinguish their appropriate uses. 
2. Recognize how to apply OMICS scale techniques to multiple facets of microbiology and immunology. 
3. Design OMICS scale experiments to inspect biological functions across DNA, RNA, and proteins. 
4. Perform basic terminal activities such as moving, copying, inspecting files, and
   calling installed tools as well as
   employ pipes to chain small functions together to create complex analyses. 
5. Utilize Jupyter Notebooks to perform data analysis and visualization of OMICS scale data. 
6. Practice presenting OMICS scale data analysis to both traditional & computational biological audiences. 

### Faculty Team

| Instructor              |ABC| Role
|-------------------------|---|-------------------------------
| Dr. Will Dampier        |WND| Co-Director, Instructor
| Dr. Katherine Innamorati|KAI| Instructor
| Dr. DV Klopfenstein     |DVK| Instructor
| Dr. Joshua Chang Mell   |JCM| Co-Director, Instructor

### Major Learning Activities 

| Name               | Grade  | Description
|--------------------|--------|-----------------------
|Class Participation | 25%    | Participation in weekly lecture and in-class learning activities.
|Weekly Assignment   | 50%    | Completing weekly assignments
|Project             | 25%    | Weekly analysis of your own dataset


## Repository Layout

This repository contains all of the learning content for the course and will be the way you submit all assignments.

The `content` folder contains the learning content organized by week.
You will `pull` this from the main repository each week.

Within each week's assignment you will be asked to create or add to a `./projects/{github-user}/README.md` file as you complete the assignments in each week's folder.
As you complete the assignment you will commit these notes and when complete, make PRs to the main repository.
This is how you will _submit_ assignments.

The `projects` folder contains information about the ongoing project and is where you will keep information and notes.

## Cheatsheets
* [GNU/Linux and vim](https://github.com/kubeopsskills/linux-cheatsheet#directory-commands)
* [GNU/Linux basics](https://github.com/progrmoiz/linux-cheatsheet/blob/master/cheatsheet/my-linux-cheatsheet.md)
* [My favorite vim cheatsheet](https://vim.rtorr.com)
* [Markdown styling](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


## Weekly Schedule

|Week                             |Date       |Module               | Topic                                          |Instructors   | Status 
|---------------------------------|-----------|---------------------|------------------------------------------------|--------------|-------
|  **1**                          |08/21/2024 | Hello World         | Command line and GNU/Linux OS                  |DVK, JCM      | unreleased
|  **2**                          |08/28/2024 | Hello World         | vim, the powerful and ubiquitous editor        |DVK           | unreleased
|   [3](content/wk03/README.md)   |09/04/2024 | Hello World         | git part I                                     |DVK           | **released**
|   [4](content/wk04/README.md)   |09/11/2024 | Hello World         | git part II                                    |DVK           | **released**
|   [5](content/wk05/README.md)   |09/18/2024 | Hello World         |Seqkit command line tools for manipulating fastx|WND, JCM      | **released**
|   [6](content/wk06/README.md)   |09/25/2024 | Align all the things| NGS read alignment                             |WND, JCM      | **released**
|   [7](content/wk07/README.md)   |10/02/2024 | Align all the things| Visualizing alignments with IGV & file transfer|WND, JCM      | **released**
|    8                            |10/09/2024 | Align all the things| nf-core pipelines and project discussion       |WND, JCM      | na
|   [9](content/wk09/README.md)   |10/16/2024 | Align all the things| Variant calling                                |WND, JCM      | **released**
| [**10**](content/wk10/README.md)|10/23/2024 | OMICS as count table| Transcriptomics                                |WND, JCM      | **released**
|   11                            |10/30/2024 | OMICS as count table| Statistical Analysis of Count-Data             |WND, JCM      | unreleased
|   12                            |11/06/2024 | OMICS as count table| Peak analysis in OMICS data (ChIP-Seq)         |WND, JCM      | unreleased
|   13                            |11/13/2024 | OMICS as count table| Enrichment Analysis                            |WND, DVK      | unreleased
|   14                            |11/20/2024 | OMICS as count table| Visualization of OMICs scale data              |WND           | unreleased
|   15                            |11/27/2024 |                     | Project (Remote)                               |WND           | unreleased
|   16                            |12/04/2024 |                     | Project                                        |Everyone      | unreleased
|   17                            |12/04/2024 |Project Presentations| Project Presentations                          |Everyone      | unreleased

Copyright (C) 2023-present, Drexel Medicine. All rights reserved
