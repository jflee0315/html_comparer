## Description

Compare two html documents, ignoring all the tags and scripts, and generate the difference report.

## Purpose

To create a component that can potentially be useful in different systems or with different data types. For this reason, I design it in a way that is flexible for changes.
Some use cases including scenarios when you want to detect updates of a public API or a web page.

## How to use

1. Run tests by executing the file "test/runtest.py" using python3.
2. Place two different html file(Containing valid html format) on the root level(same level as main.py) of the project.
3. Execute the main.py with python3 (I use 3.7.0).
4. After execution, there should be an output file named "output.html" being generated. Open the file with any browser and take a look. It should display the difference between the two input file.


## Exeternal libraries

The comparison tool developed by Google
https://github.com/google/diff-match-patch

## Author

Jeffrey Lee 
https://github.com/jflee0315/html_comparer