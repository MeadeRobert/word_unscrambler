*Universal Word Unscrambler

**About:

Universal Word Unscrambler is a web-app, written by Robert Meade [https://github.com/MeadeRobert](https://github.com/MeadeRobert), that aims to allow anyone to make sense of arbitrary letter combinations that may contain meaning obscured by a language of which they have no knowledge. The program tries to provide as many words or acronyms as it can with little to no concern for false positives. It is thus not a Scrabble word-finder, but a tool to decipher meaning from chaos. It will find sequences, 2-9 characters in length, that are valid spelling combinations in any of the languages specified that are installed on the system. These languages are given above by their ISO 639-1 Codes.
The Universal Word Unscrambler was developed in response to a Dutch word scramble puzzle. The puzzle demonstrated that such a utility for word unscrambling involving arbitrary target languages was not readily available. The challenge involved the letters "nrtoepw" which contained a hidden message, "ontwerp." The hidden message translates to "design" in english, fitting for the puzzle since it was made to show how people sometimes lack the background to interpret meaning in information as part of a freshman Engineering Design class.
Universal Word Unscrambler makes use of python's enchant library and aspell on a debian based linux server to reference letter combinations against system dictionaries. Although it uses a naive approach to the generation of possible words, generationg a list of permutations in O(n!) time, it should be suitable for most workloads. If you have a request for an additional system dictionary to be installed, email [meade.develop3r@gmail.com](meade.develop3r@gmail.com) and with a request or download the source at [https://github.com/MeadeRobert/word_unscrambler](https://github.com/MeadeRobert/word_unscrambler). 

**Dependencies:

- Flask
- Enchant
- apsell/myspell/hunspell dictionaries