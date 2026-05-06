# =========================
# Educational Ransomware Simulator - Build System
# =========================

PYTHON=python3
PIP=pip

APP=malware.py
UI=decript-window.py
BUILD_SCRIPT=build.py

# -------------------------
# Setup ambiente
# -------------------------
install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements.txt
	$(PIP) install pyinstaller

# -------------------------
# Rodar aplicação
# -------------------------
run:
	$(PYTHON) $(APP)

run-ui:
	$(PYTHON) $(UI)

# -------------------------
# Build automático (PyInstaller)
# -------------------------
build:
	$(PYTHON) $(BUILD_SCRIPT)

# -------------------------
# Limpeza
# -------------------------
clean:
	rm -rf build dist __pycache__ *.spec temp_build temp_spec

# -------------------------
# Build manual direto (Linux)
# -------------------------
build-linux:
	pyinstaller --onefile --noconsole --distpath build/linux $(APP)
	pyinstaller --onefile --noconsole --distpath build/linux $(UI)

# -------------------------
# Help
# -------------------------
help:
	@echo "Available commands:"
	@echo "  make install      - install dependencies"
	@echo "  make install-dev  - install dev tools (PyInstaller)"
	@echo "  make run          - run malware simulator"
	@echo "  make run-ui       - run UI only"
	@echo "  make build        - run build.py"
	@echo "  make build-linux  - manual Linux build"
	@echo "  make clean        - remove build files"