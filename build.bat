pip install pyinstaller

if exist dist rmdir /s /q dist
pyinstaller ^
  --onefile ^
  --clean ^
  --name CarNumberPlz ^
  src/src.py