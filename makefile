build:
	pyinstaller --onefile -w --distpath bin/dist --specpath build/ --workpath bin/build --icon icon.ico src/main.py