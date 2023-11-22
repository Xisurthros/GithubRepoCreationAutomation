@REM Z:\programming\python\RepoCreationAutomation

set "VENV_PATH=Z:\path-to-project\RepoCreationAutomation\venv\Scripts"
set "PROJECT_PATH=Z:\path-to-project\RepoCreationAutomation\main.py"

echo Activating virtual environment...
pushd %VENV_PATH%
call activate

echo Running main.py with arguments: %*
python %PROJECT_PATH% %*

echo Deactivating virtual environment...
call deactivate
popd

echo Done!
