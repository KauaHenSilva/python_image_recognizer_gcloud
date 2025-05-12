all:
	@cd app && python3 app.py 

start_in_server:
	@sudo apt-get update && sudo apt-get upgrade -y
	@sudo apt install -y libgl1
	@sudo apt-get install python3-pip -y
	@sudo apt-get install python3-venv -y
	@python3 -m venv .venv

dependencies:
	@python3 -m pip install -r requirements.txt