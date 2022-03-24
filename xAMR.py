import sentencepiece

import amrlib

from txtai.pipeline import Translation
from deep_translator import GoogleTranslator

translate = Translation()

gtos = amrlib.load_gtos_model()
stog = amrlib.load_stog_model()


def choose_translator(input_lang, source_lang, target_lang, x_language_sentence):
    if input_lang == 'bg':
        translated_sentence = GoogleTranslator(source=source_lang, target=target_lang).translate(x_language_sentence)
    else:
        translated_sentence = translate(x_language_sentence, source=source_lang, target=target_lang)
    return translated_sentence


class xAMR:

    def __init__(self, language, sentence):
        """
          parameters:
            language: str => source language of the sentence. Accepted languages: mk, en, de, it, es and many more
            sentence: str => sentence
        """
        self.language = language
        self.x_language_sentence = sentence
        self.translated_en_to_x_language = ""
        self.generated_sentence = ""
        self.en_sentence = ""
        self.amr_graph = ""

    def _translate_to_english(self):
        self.en_sentence = choose_translator(input_lang=self.language, source_lang=self.language, target_lang="en",
                                             x_language_sentence=self.x_language_sentence)
        return self.en_sentence

    def _parse_sentence_to_graph(self):
        if not self.en_sentence:
            self._translate_to_english()
        self.amr_graph = stog.parse_sents([self.en_sentence])
        return self.amr_graph

    def _generate_sentence_from_graph(self):
        if not self.generated_sentence:

            if self.amr_graph[0] is None:
                self.generated_sentence = ""
                return self.generated_sentence

            sents, _ = gtos.generate(self.amr_graph)
            self.generated_sentence = sents[0]
        return self.generated_sentence

    def _translate_english_to_x_language(self):
        self.translated_en_to_x_language = choose_translator(self.language, "en", self.language, self.en_sentence)
        return self.translated_en_to_x_language

    def pipeline(self):
        self._translate_to_english()
        self._parse_sentence_to_graph()
        self._generate_sentence_from_graph()
        self._translate_english_to_x_language()
