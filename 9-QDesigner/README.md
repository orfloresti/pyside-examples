# Comments for designer

## Export dependencies
`export LD_LIBRARY_PATH=/home/orlando_floresti/PythonProjects/pyside6-env/lib/python3.8/site-packages/PySide6/Qt/lib/`

## Import path to the system to use uic
`export PATH="/home/orlando_floresti/PythonProjects/pyside6-env/lib/python3.8/site-packages/PySide6/:$PATH"`

## Compile ui
`uic -g python <name>.ui -o <name>.py`

## Compile resources
`rcc -g python resources.qrc -o resources_rc.py`