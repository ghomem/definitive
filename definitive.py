import textwrap
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

from config import ( WIDTH, HEIGHT, X_WORD_TO_DEFINE, X_WORD_TYPE, X_WORD_DEFINITION, X_SEE_ALSO,
                     Y_WORD_TO_DEFINE, Y_PADDING, Y_PADDING2, BG_COLOR, FONT_COLOR, WORD_DEFINITION_LINE_WIDTH,
                     FONT_WORD_TO_DEFINE, FONT_WORD_TYPE, FONT_WORD_DEFINITION, WORD_DEFINITION_LINE_SPACING )


def main():

    # TODO: parse parameters

    word_to_define  = 'entropitis'
    word_type = 'noun'
    word_definition = 'A condition defined by the uncontrollable urge to introduce superflous complexity in systems or processes.'
    see_also = 'autokafka syndrome'

    output_file = 'result.png'

    ### MAIN SCRIPT ###

    word_type_str = f"({word_type})"
    see_also_str = f"(see also: {see_also})"

    word_definition_lines = textwrap.wrap(word_definition, width=WORD_DEFINITION_LINE_WIDTH)

    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)

    draw = ImageDraw.Draw(img)

    y_spacing = draw.textsize(word_to_define, font=FONT_WORD_TO_DEFINE)[1] + Y_PADDING

    y_word_type = Y_WORD_TO_DEFINE + y_spacing

    y_spacing2 = draw.textsize(word_type, font=FONT_WORD_TO_DEFINE)[1] + Y_PADDING2

    y_word_definition = y_word_type + y_spacing2

    draw.text((X_WORD_TO_DEFINE, Y_WORD_TO_DEFINE), word_to_define, font=FONT_WORD_TO_DEFINE, fill=FONT_COLOR)
    draw.text((X_WORD_TYPE, y_word_type), word_type_str, font=FONT_WORD_TYPE, fill=FONT_COLOR)

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
