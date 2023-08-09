#!/usr/bin/env bash
export ARCHFLAGS='-arch arm64 -arch x86_64'
VERSION=$(sed -n -e 's#\(pycryptodome==[^ ]*\).*#\1#gp' ./requirements.txt)
echo $VERSION
rm -rf ./build/pytemps
mkdir -p ./build/pytemps
export PATH=$(pwd)/build/pytemps/bin:$PATH
export PYTHONPATH=./build/pytemps:.:$(python3 -c "import sys;print(':'.join(sys.path))")
python3 -m pip install -U cython==0.29.33 --no-binary :all:
python3 -m pip install cytoolz==0.12.2 --no-binary :all: --target ./build/pytemps
python3 -m pip install $VERSION --target ./build/pytemps
python3 -m pip install -r ./build_configs/macos/requirements.txt --target ./build/pytemps
python3 -m pip install -U -r ./build_configs/macos/requirements.pyinstaller.txt
pyinstaller --distpath ./out ./build_configs/macos/build.spec;
