## When we import a module
Python checks multiple locations that are in a lists `sys.path`

 ```python
[
    '/Users/ihelerea/dev/Adri/repos/python_code_collection/Python/Python-Imports',
    '/Users/ihelerea/dev/Adri/repos/python_code_collection',
    '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python39.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages',
    '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend'
]
 ```

### If the module is not in our working directory
Let's ues an example and move the module in the parent directory
1. To import the module we need to declare his location 
2. Hardcode the path ```sys.path.append('/Users/ihelerea/dev/Adri/repos/python_code_collection/Python/')```
3. For multiple use, avoid to hardcode this path we can save it on .env as a new environment variable
   - Change `sys.path` by adding the environment variable
   - Edit `~/.bash_profile` and config to use your specific python version