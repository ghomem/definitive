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

# this constant allows for adding more vertical space, which is necessary when the definition is long
# this size refers to the situation where SCALING_FACTOR == 1
BASE_HEIGHT = 714

# this constant allows for fine tuning the resulting image size keeping proportions
SCALING_FACTOR = 1

# in principle the remaining constants do not need to be adjusted
WIDTH  = round(890 * SCALING_FACTOR)
HEIGHT = round(BASE_HEIGHT * SCALING_FACTOR)

X_PADDING = round(40 * SCALING_FACTOR)
Y_PADDING = round(20 * SCALING_FACTOR)
Y_PADDING2 = round(40 * SCALING_FACTOR)

X_SPACING = 0

X_WORD_TO_DEFINE = 0 + X_PADDING
Y_WORD_TO_DEFINE = 0 + Y_PADDING

X_WORD_DEFINITION = 0 + X_PADDING
X_WORD_TYPE = 0 + X_PADDING

X_SEE_ALSO = 0 + X_PADDING

WORD_DEFINITION_LINE_WIDTH = 50
WORD_DEFINITION_LINE_SPACING = round(10 * SCALING_FACTOR)

### COLOR RELATED DEFINITIONS ###

BG_COLOR = 'white'
FONT_COLOR = (0, 0, 0)

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
FONT_SIZE_WORD_TO_DEFINE = round(100 * SCALING_FACTOR)
FONT_SIZE_WORD_TYPE = round(60 * SCALING_FACTOR)
FONT_SIZE_WORD_DEFINITION = round(36 * SCALING_FACTOR)

# and finally we instantiate the fonts
FONT_WORD_TO_DEFINE = ImageFont.truetype(FONT_WORD_TO_DEFINE_BASE, size=FONT_SIZE_WORD_TO_DEFINE)
FONT_WORD_TYPE = ImageFont.truetype(FONT_WORD_TYPE_BASE, size=FONT_SIZE_WORD_TYPE)
FONT_WORD_DEFINITION = ImageFont.truetype(FONT_WORD_DEFINITION_BASE, size=FONT_SIZE_WORD_DEFINITION)
