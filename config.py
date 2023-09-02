from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

### GENERIC DEFINITIONS ###

E_OK = 0
E_ERR = 1

### GEOMETRY DEFINITIONS ###

# the output is comprised of 4 sections:
# * the word to be defined
# * the type of that word (noun, verb,...)
# * the definition
# * the "see also" section

# in principle the remaining constants do not need to be adjusted
WIDTH  = 890
HEIGHT = 714

MIN_HEIGHT = 416
LINE_HEIGHT = 46

X_PADDING = 40
Y_PADDING = 20
Y_PADDING2 = 40

X_SPACING = 0

WORD_DEFINITION_LINE_WIDTH = 50
WORD_DEFINITION_LINE_SPACING = 10

### COLOR RELATED DEFINITIONS ###

BG_COLOR = "#ffffff"
FONT_COLOR = "#000000"

### FONT RELATED DEFINITIONS ###

# Example font families available on Linux
#   Bitstream Vera Serif
#   FreeSerif
#   Liberation Serif
FONT_SERIF_FAMILY = 'FreeSerif'

# here we define the font preperties
FONT_WORD_TO_DEFINE_PROPS = font_manager.FontProperties(family=FONT_SERIF_FAMILY, weight='bold')
FONT_WORD_TYPE_PROPS = font_manager.FontProperties(family=FONT_SERIF_FAMILY, weight='regular', style='italic')
FONT_WORD_DEFINITION_PROPS = font_manager.FontProperties(family=FONT_SERIF_FAMILY, weight='regular')

# then we find the font from the properties
FONT_WORD_TO_DEFINE_BASE = font_manager.findfont(FONT_WORD_TO_DEFINE_PROPS)
FONT_WORD_TYPE_BASE = font_manager.findfont(FONT_WORD_TYPE_PROPS)
FONT_WORD_DEFINITION_BASE = font_manager.findfont(FONT_WORD_DEFINITION_PROPS)

# then we pick the font sizes
FONT_SIZE_WORD_TO_DEFINE = 100
FONT_SIZE_WORD_TYPE = 60
FONT_SIZE_WORD_DEFINITION = 36
