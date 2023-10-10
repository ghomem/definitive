# definitive
A simple program to generate dictionary style definitions on a PNG file.

# usage

This is an example of how definitive can be used on Ubuntu 20.04 / 22.04:
```
sudo apt update
sudo apt install python3-matplotlib fonts-freefont-ttf
git clone https://github.com/ghomem/definitive.git
cd definitive

# from https://grugbrain.dev/#grug-on-complexity
DEFINITION='Spirit demon that enter codebase through well-meaning but ultimately very clubbable; Very, very bad.'
python3 definitive.py -w complexity -c noun -d "$DEFINITION" -s autokafka -o /tmp/definitive-definition.png
```

To inspect the self-explanatory command line options we can simply run:
```
python3 definitive.py -h
```
If the text is not fitting the canvas please make sure there are not font caching issues by removing:
* /home/YOURUSER/.config/matplotlib/
* /home/YOURUSER/.cache/matplotlib/
