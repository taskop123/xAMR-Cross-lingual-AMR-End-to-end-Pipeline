from xAMR import xAMR

if __name__ == '__main__':
    x_sentence = xAMR('x', '<sentence in x language.>')
    x_sentence.pipeline()

    print(f'AMR graph representation: {x_sentence.amr_graph}')
    print(f'Final mk sentence: {x_sentence.translated_en_to_x_language}')
