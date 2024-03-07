
mkdir -p build

cp -r python-subsystem build
cp main.cpp build

cd build

g++ -o out -I./ main.cpp **/*.cpp

cd ..
mv build/out out
