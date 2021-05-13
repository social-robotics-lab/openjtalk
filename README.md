# Description
Open JTalkを用いてテキストを音声合成するプログラム

# Install
```
git clone https://github.com/social-robotics-lab/openjtalk.git
cd openjtalk
docker build -t openjtalk .
```

# Run
```
docker run -it --name openjtalk --mount type=bind,source="$(pwd)"/src,target=/tmp --rm openjtalk /bin/bash
python sample.py
```
