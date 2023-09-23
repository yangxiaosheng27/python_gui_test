@echo off

echo from python_gui_test import main >main.py && echo main() >>main.py || echo failed to create main.py && pause && exit

if exist "build" (
    rmdir /s/q build
    if exist "build" (echo failed to remove 'build' && pause && exit)
)
if exist "dist" (
    rmdir /s/q dist
    if exist "dist" (echo failed to remove 'dist' && pause && exit)
)

conda activate ai && pyinstaller -D -w --icon=./a.ico --key 123456abc main.py && echo Successfully created file main.exe && timeout /t 5 && cd dist/main && ren main.exe python_gui_test.exe && cd ../.. && ren "dist/main" python_gui_test && cd setup/InnoSetup6 && ISCC.exe "../setup.iss" && echo Successfully created installation package && exit || echo build failed && pause && exit