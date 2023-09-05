# definitive
A simple program to generate dictionary style definitions.

# usage

This is an example of how definitive can be used on Ubuntu 20.04 / 22.04:
```
sudo apt update
sudo apt install python3-matplotlib fonts-freefont-ttf
git clone https://github.com/ghomem/definitive.git
cd definitive
python3 definitive.py -w complexity -c noun -d 'Spirit demon that enter codebase through well-meaning but ultimately very clubbable; Very, very bad.' -s autokafka -o /tmp/definitive-definition.png'
```

To inspect the self-explanatory command line options we can simply run:
```
python3 definitive.py -h
```
