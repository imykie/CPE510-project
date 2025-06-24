# English to Yoruba Translator

A comprehensive machine translation tool that converts English text to Yoruba with both GUI and CLI interfaces.

## Features

- **Dual Interface**: Both graphical (GUI) and command-line (CLI) modes
- **Real-time Translation**: Instant English to Yoruba translation
- **Dictionary Management**: Load, save, and customize translation dictionaries
- **Word Reordering**: Basic grammatical structure adjustment for Yoruba
- **Extensive Vocabulary**: Built-in dictionary with 50+ common words
- **Input Validation**: Text sanitization and length limits
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6+
- tkinter (for GUI mode - usually included with Python)
- Unicode support for Yoruba diacritics

## Installation

1. Ensure you have Python 3.6+ installed
2. Navigate to the `translator` directory
3. For GUI mode, ensure tkinter is available (usually pre-installed)

## Usage

### GUI Mode (Default)

```bash
python app.py
```

or explicitly:

```bash
python app.py --gui
```

### CLI Mode

```bash
python app.py --cli
```

### Custom Dictionary

```bash
python app.py custom_dictionary.json
```

### Help

```bash
python app.py --help
```

## GUI Interface

### Features

- **Clean Design**: White background with black text for optimal readability
- **Text Areas**: Scrollable input and output areas for longer texts
- **Buttons**: 
  - 🔄 **Translate**: Convert English to Yoruba
  - 🗑️ **Clear**: Clear both input and output areas
  - 📁 **Load Dict**: Load custom dictionary from JSON file
  - 💾 **Save Dict**: Save current dictionary to JSON file
- **Keyboard Shortcuts**: Ctrl+Enter to translate
- **Status Bar**: Shows dictionary size and usage instructions

### GUI Example

```
🌍 English to Yoruba Translator

Enter English text:
┌─────────────────────────────────────────────────┐
│ The boy reads books                             │
│                                                 │
└─────────────────────────────────────────────────┘

Yoruba translation:
┌─────────────────────────────────────────────────┐
│ ọmọkùnrin nàà ka àwọn ìwé                      │
│                                                 │
└─────────────────────────────────────────────────┘

[🔄 Translate] [🗑️ Clear] [📁 Load Dict] [💾 Save Dict]

📚 Dictionary contains 50 translations | Press Ctrl+Enter to translate
```

## CLI Interface

### Commands

- **Translation**: Simply type English text to get Yoruba translation
- **Dictionary Management**:
  - `add <english> = <yoruba>` - Add new translation
  - `save <filename>` - Save dictionary to file
  - `load <filename>` - Load dictionary from file
- **Help**: `help` - Show available commands
- **Exit**: `q`, `quit`, or `exit`

### CLI Example

```bash
🌍 English to Yoruba Translator (CLI Mode)
💡 Commands: 'help', 'add <english> = <yoruba>', 'save <file>', 'load <file>', 'q' to quit

➤ Enter English text: The teacher reads books
🌍 Yoruba: olùkọ́ nàà ka àwọn ìwé

➤ Enter English text: add school = ilé-ìwé
✅ Added: school → ilé-ìwé

➤ Enter English text: The boy goes to school
🌍 Yoruba: ọmọkùnrin nàà lọ sí ilé-ìwé

➤ Enter English text: save my_dictionary.json
✅ Dictionary saved to my_dictionary.json

➤ Enter English text: help

📖 Available commands:
  help                    - Show this help
  add <english> = <yoruba> - Add new translation
  save <filename>         - Save dictionary to file
  load <filename>         - Load dictionary from file
  q, quit, exit          - Exit program

➤ Enter English text: q
👋 Goodbye!
```

## Built-in Dictionary

The translator includes a comprehensive dictionary with:

### Common Words
- **Articles**: the → nàà, a/an → kan
- **Pronouns**: my → mi, your → rẹ, his/her → rẹ̀
- **People**: boy → ọmọkùnrin, girl → ọmọbìnrin, man → ọkùnrin, woman → obìnrin
- **Animals**: dog → ajá, cat → ológbò
- **Objects**: book → ìwé, chair → àga, table → tábìlì, house → ilé
- **Food**: apple → àpù, water → omi, food → oúnjẹ
- **Verbs**: go → lọ, come → wá, see → rí, eat → jẹ, read → ka, play → ṣeré
- **Adjectives**: good → dára, bad → burú, big → ńlá, small → kékeré
- **Greetings**: hello → pẹ̀lẹ́, goodbye → ó dàbọ̀
- **Responses**: yes → bẹ́ẹ̀ni, no → bẹ́ẹ̀kọ́

### Verb Forms
The dictionary includes both base forms and conjugated forms:
- read/reads → ka
- go/goes → lọ
- see/sees → rí
- eat/ate → jẹ

## Word Reordering Rules

The translator applies basic grammatical transformations:

### Determiner-Noun Reordering
English: "the boy" → Yoruba: "ọmọkùnrin nàà" (boy the)
English: "a book" → Yoruba: "ìwé kan" (book a)

### Supported Determiners
- kan (a/an)
- nàà (the)  
- mi (my)
- rẹ (your)
- rẹ̀ (his/her)

## Dictionary Management

### JSON Format

Custom dictionaries use JSON format:

```json
{
  "hello": "pẹ̀lẹ́",
  "world": "ayé",
  "computer": "kọ̀ǹpútà",
  "internet": "íńtánẹ́ẹ̀tì"
}
```

### Loading Custom Dictionaries

1. **GUI Mode**: Use the "📁 Load Dict" button
2. **CLI Mode**: Use `load filename.json` command
3. **Startup**: `python app.py custom_dict.json`

### Saving Dictionaries

1. **GUI Mode**: Use the "💾 Save Dict" button  
2. **CLI Mode**: Use `save filename.json` command

## Input Validation

### Security Features
- Input sanitization to remove potentially harmful characters
- Length limits (1000 characters for sentences, 100 words max)
- Character filtering with regex patterns

### Supported Characters
- Letters: a-z, A-Z
- Yoruba diacritics: àáảãạ, èéẻẽẹ, etc.
- Punctuation: .,!?;:-
- Whitespace and common symbols

## Error Handling

### Common Scenarios
- **GUI not available**: Automatically falls back to CLI mode
- **File operations**: Proper error messages for load/save failures
- **Invalid input**: Graceful handling of malformed text
- **Dictionary errors**: Validation of JSON format and content
- **System interrupts**: Clean exit on Ctrl+C and EOF

## Technical Details

### Architecture
- **Object-oriented design**: `EnglishYorubaTranslator` class
- **Modular interfaces**: Separate GUI and CLI implementations
- **Unicode support**: Full UTF-8 handling for Yoruba characters
- **Cross-platform**: Consistent behavior across operating systems

### Performance
- **Efficient lookup**: Dictionary-based translation with O(1) word lookup
- **Memory optimization**: Streaming text processing
- **Responsive GUI**: Non-blocking user interface

## Customization

### Adding New Words
```bash
# CLI mode
add computer = kọ̀ǹpútà
add internet = íńtánẹ́ẹ̀tì

# Or edit JSON file directly
{
  "computer": "kọ̀ǹpútà",
  "internet": "íńtánẹ́ẹ̀tì"
}
```

### Grammar Rules
To modify word reordering rules, edit the `apply_word_order_rules` method in the `EnglishYorubaTranslator` class.

## Limitations

### Current Limitations
- **Word-by-word translation**: No contextual understanding
- **Basic grammar**: Simple determiner-noun reordering only
- **Limited vocabulary**: Built-in dictionary covers common words
- **No semantic analysis**: Cannot handle idiomatic expressions

### Future Improvements
- Neural machine translation integration
- Advanced grammatical transformations
- Larger vocabulary databases
- Context-aware translation
- Pronunciation guides

## Troubleshooting

### GUI Issues
1. **tkinter not available**:
   ```bash
   # Install tkinter (Linux)
   sudo apt-get install python3-tk
   ```

2. **Yoruba characters not displaying**:
   - Ensure system supports Unicode fonts
   - Try different font settings in terminal/GUI

### CLI Issues
1. **Commands not recognized**:
   - Check command syntax: `add word = translation`
   - Ensure proper spacing around `=`

2. **File operations failing**:
   - Check file permissions
   - Verify JSON format validity
   - Use absolute file paths

### Dictionary Issues
1. **Translations not working**:
   - Verify dictionary format
   - Check for typos in word spellings
   - Ensure proper Unicode encoding

## Contributing

### Development Guidelines
1. **Code Style**: Follow existing patterns and naming conventions
2. **Testing**: Test with various English inputs and Yoruba outputs
3. **Documentation**: Update README for new features
4. **Localization**: Maintain Unicode support for Yoruba characters

### Adding Features
1. **New Grammar Rules**: Extend `apply_word_order_rules` method
2. **UI Improvements**: Enhance GUI layout and functionality  
3. **Dictionary Expansion**: Add more comprehensive word lists
4. **Language Support**: Consider other West African languages

## License

This project is part of a larger language processing toolkit. See the main project LICENSE file for details.

## Acknowledgments

- Yoruba language experts for linguistic guidance
- Unicode Consortium for character encoding standards
- Python community for tkinter and language processing tools