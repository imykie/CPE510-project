# Yoruba Grammar Checker / Ayẹwo Gbolohun Yorùbá

A bilingual command-line tool for validating Yoruba sentence grammar using context-free grammar rules.

## Features / Àwọn Ẹ̀yà

- **Bilingual Interface**: Full support for both Yoruba and English
- **Grammar Validation**: Validates Yoruba sentences against grammar rules  
- **Yoruba Character Support**: Proper handling of Yoruba diacritics and tone marks
- **Input Validation**: Sanitizes input and validates Yoruba text patterns
- **Interactive Commands**: User-friendly prompts in both languages
- **Error Handling**: Comprehensive error handling with bilingual messages
- **Custom Grammar Files**: Support for different Yoruba grammar configurations

## Requirements / Àwọn Ìbéèrè

- Python 3.6+
- `core.validator` module (SentenceValidator class)
- Unicode support for Yoruba characters

## Installation / Fifi sori ẹrọ

1. Ensure you have Python 3.6+ installed / Rí dájú pé o ní Python 3.6+ tí a fi sórí ẹrọ
2. Navigate to the `yoruba_checker` directory / Lọ sí fódà `yoruba_checker`
3. Make sure the `core` module and `grammar` directory are present / Rí dájú pé `core` àti `grammar` fódà wà

## Usage / Bí a ṣe ń lò ó

### Basic Usage / Lílò Ìpilẹ̀

```bash
python app.py
```

This uses the default grammar file `./grammar/yoruba_grammar.cfg`.

### Custom Grammar File / Fáìlì Grammar Àkànṣe

```bash
python app.py path/to/your/yoruba_grammar.cfg
```

### Interactive Commands / Àwọn Àṣẹ Ìbánisọ̀rọ̀

Available commands in both languages:

**English Commands:**
- **Enter Yoruba text**: Type any Yoruba sentence to check grammar
- **`help`**: Show available commands  
- **`q`** or **`quit`**: Exit the program

**Yoruba Commands:**
- **Tẹ ọ̀rọ̀ Yorùbá**: Tẹ gbolohun Yorùbá láti ṣayẹwo grammar
- **`iranlọ́wọ́`** or **`egba`**: Han àwọn àṣẹ tí ó wà
- **`jade`** or **`parí`**: Jade kúro nínú ètò

### Example Session / Àpẹẹrẹ Ìgbà

```
🔍 Ayẹwo Gbolohun Yorùbá / Yoruba Grammar Checker
📝 Ló fáìlì grammar: ./grammar/yoruba_grammar.cfg
💡 Tẹ gbolohun láti ṣayẹwo grammar (tẹ 'iranlọ́wọ́' fun àwọn aṣe, 'q' lati jade)
💡 Enter Yoruba sentences to check grammar (type 'help' for commands, 'q' to quit)

➤ Tẹ gbolohun Yorùbá: Ọmọ náà lọ sí ilé
✅ Ó tọ́ / Valid: Sentence is grammatically correct

➤ Tẹ gbolohun Yorùbá: Lọ ọmọ sí ilé náà
❌ Kò tọ́ / Invalid: Word order error detected

➤ Tẹ gbolohun Yorùbá: iranlọ́wọ́

📖 Àwọn aṣe tí ó wà / Available commands:
  help / iranlọ́wọ́ - Han iránlọ́wọ́ yìí / Show this help
  q / jade          - Jáde kúro nínú ètò / Quit the program
  quit / parí       - Jáde kúro nínú ètò / Quit the program

➤ Tẹ gbolohun Yorùbá: jade
👋 Ó dàbọ̀! / Goodbye!
```

## Yoruba Language Support / Àtìlẹ́yìn Èdè Yorùbá

### Supported Characters / Àwọn Lẹ́tà tí a ń gbà

The checker supports all standard Yoruba characters including:

- **Basic letters**: a, b, d, e, ẹ, f, g, gb, h, i, j, k, l, m, n, o, ọ, p, r, s, ṣ, t, u, w, y
- **Tone marks**: 
  - Low tone: à, è, ẹ̀, ì, ò, ọ̀, ù (grave accent)
  - High tone: á, é, ẹ́, í, ó, ọ́, ú (acute accent)  
  - Mid tone: a, e, ẹ, i, o, ọ, u (no mark)
- **Nasalization**: ạ, ẹ̣, ị, ọ̣, ụ (dot below)

### Text Validation / Ìdánwò Ọ̀rọ̀

The application performs Yoruba-specific validation:

- Checks for proper Yoruba character patterns
- Validates diacritic usage
- Ensures text appears to be Yoruba language
- Length limits (max 1000 characters)

## Error Handling / Ìmúnibá pẹ̀lú Àṣìṣe

Comprehensive error handling with bilingual messages:

- **Missing grammar file**: Àṣìṣe + Error messages in both languages
- **Invalid Yoruba text**: Detection of non-Yoruba character patterns  
- **Input validation**: Length and format checking
- **System errors**: Graceful handling of interrupts and EOF

## Grammar File Format / Ọ̀nà Fáìlì Grammar

The application expects a context-free grammar file for Yoruba in CFG format:

```
S -> NP VP
NP -> Det N | N  
VP -> V | V NP
Det -> 'náà' | 'kan'
N -> 'ọmọ' | 'ilé' | 'ìwé'
V -> 'lọ' | 'wá' | 'ka'
```

## Cultural Considerations / Àwọn Ohun Àṣà

This tool respects Yoruba language and culture:

- Proper Yoruba greetings and farewells
- Culturally appropriate interface language
- Support for traditional Yoruba sentence structures
- Recognition of Yoruba linguistic patterns

## Technical Details / Àwọn Ẹ̀kọ́ Ìmọ̀-ẹ̀rọ

- **Unicode Support**: Full UTF-8 support for Yoruba diacritics
- **Character Encoding**: Handles all Yoruba special characters
- **Pattern Matching**: Regular expressions for Yoruba text validation
- **Bilingual Output**: All messages in both Yoruba and English
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Troubleshooting / Ìtúnṣe Àṣìṣe

### Common Issues / Àwọn Àṣìṣe Tí Ó Máa Ń Ṣẹlẹ̀

1. **Grammar file not found / Ko rí fáìlì grammar**
   - Check file path / Ṣayẹwo ọ̀nà fáìlì
   - Verify file permissions / Rí dájú àṣẹ fáìlì

2. **Yoruba characters not displaying / Àwọn lẹ́tà Yorùbá kò hàn**
   - Ensure terminal supports Unicode / Rí dájú pé terminal gbà Unicode
   - Check font supports Yoruba diacritics / Ṣayẹwo bóya font gbà àmì ohùn Yorùbá

3. **Text not recognized as Yoruba / Kò mọ ọ̀rọ̀ náà gẹ́gẹ́ bí Yorùbá**
   - Use proper Yoruba characters / Lo àwọn lẹ́tà Yorùbá tó tọ́
   - Include appropriate diacritics / Fi àmì ohùn tó yẹ sí i

## Contributing / Ìdárayá

When contributing to this project:

1. Respect both Yoruba and English language conventions
2. Test with various Yoruba text samples  
3. Ensure proper Unicode handling
4. Maintain bilingual interface consistency
5. Consider cultural sensitivity in language use

## License / Ìwé-àṣẹ

This project is part of a larger language processing toolkit. See the main project LICENSE file for details.