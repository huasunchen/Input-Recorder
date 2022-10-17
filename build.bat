rmdir /Q /S dist
pyinstaller Irec.spec
mkdir dist\res
copy res\* dist\res\*