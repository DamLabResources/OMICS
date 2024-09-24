# Solutions

Place your solution files here as you create them.

Do not add your solution files to git (as you will create merge conflicts).

This is automatically done for you by the `.gitignore` file in the directory above.
That file contains the contents.

```
solution
```

Which tells git to ignore any files matching that pattern (ie, are in the `solution` directory).
This is a powerful way to keep your large data files from accidentally being commited. 
Check out the `.gitignore` file at the root of the repo if you're interested.

So, how did **this** file get in here you ask?

```bash
git add -f path/to/file
```

The `-f` or `--force` will override ignore patterns when you need to.
