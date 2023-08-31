import sys
import textwrap
import argparse
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

from config import ( E_OK, E_ERR, WIDTH, HEIGHT, X_WORD_TO_DEFINE, X_WORD_TYPE, X_WORD_DEFINITION, X_SEE_ALSO,
                     Y_WORD_TO_DEFINE, Y_PADDING, Y_PADDING2, BG_COLOR, FONT_COLOR, WORD_DEFINITION_LINE_WIDTH,
                     FONT_WORD_TO_DEFINE, FONT_WORD_TYPE, FONT_WORD_DEFINITION, WORD_DEFINITION_LINE_SPACING )


def main():

    parser = argparse.ArgumentParser(description='Generate a dictionary entry on a png file.')
    parser.add_argument( '-w', '--word',        required=True, help='Word to be defined')
    parser.add_argument( '-c', '--word-class',  required=True, help='Word class, such as noun, adjective, verb, etc')
    parser.add_argument( '-d', '--definition',  required=True, help='The definition of the word')
    parser.add_argument( '-s', '--see-also',    required=True, help='Other related words')
    parser.add_argument( '-o', '--output-file', required=True, help='Other related words')

    args = parser.parse_args()

    word_to_define  = args.word
    word_class = args.word_class
    word_definition = args.definition
    see_also = args.see_also
    output_file = args.output_file

    ### MAIN SCRIPT ###

    word_class_str = f"({word_class})"
    see_also_str = f"(see also: {see_also})"

    word_definition_lines = textwrap.wrap(word_definition, width=WORD_DEFINITION_LINE_WIDTH)

    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)

    draw = ImageDraw.Draw(img)

    y_spacing = draw.textsize(word_to_define, font=FONT_WORD_TO_DEFINE)[1] + Y_PADDING

    y_word_class = Y_WORD_TO_DEFINE + y_spacing

    y_spacing2 = draw.textsize(word_class, font=FONT_WORD_TO_DEFINE)[1] + Y_PADDING2

    y_word_definition = y_word_class + y_spacing2

    draw.text((X_WORD_TO_DEFINE, Y_WORD_TO_DEFINE), word_to_define, font=FONT_WORD_TO_DEFINE, fill=FONT_COLOR)
    draw.text((X_WORD_TYPE, y_word_class), word_class_str, font=FONT_WORD_TYPE, fill=FONT_COLOR)

    y_pos = y_word_definition
    for line in word_definition_lines:
        draw.multiline_text((X_WORD_DEFINITION, y_pos), line, font=FONT_WORD_DEFINITION, fill=FONT_COLOR)
        y_pos = y_pos + draw.textsize(line, font=FONT_WORD_DEFINITION)[1] + WORD_DEFINITION_LINE_SPACING

    y_pos = y_pos + 2 * Y_PADDING

    draw.text((X_SEE_ALSO, y_pos), see_also_str, font=FONT_WORD_DEFINITION, fill=FONT_COLOR)

    try:
        img.save(output_file)
        print(f"Output saved to {output_file}.")
        print('Crop the bottom of the image to obtain optimal proportions')
    except e:
        print(f"problem saving {output_file}")


# execute the main function
main()
