[Click here to try it out](https://xhlulu.github.io/material-ui-in-pyodide/index.html).


This is a simple demo of using the `material-ui` React component inside `pyodide`. Everything here is written using pure Python and uses pyodide, react, react-dom, and material-ui on the JS side. No other library was imported to make this work.

The Python source code in `main.py`, and `index.html` loads the required JS libraries (react, material-ui, pyodide) and run a simple JS script to fetch and run `main.py`.

## Source

This demo was adapted from [this example](https://github.com/mui-org/material-ui/tree/master/examples/cdn).