# English Grammar Checker

A command-line tool for validating English sentence grammar using context-free grammar rules.

## Features

- **Grammar Validation**: Validates English sentences against predefined grammar rules
- **Error Handling**: Robust error handling for file operations and user input
- **Input Validation**: Sanitizes input and enforces length limits
- **Interactive Interface**: User-friendly prompts with help system
- **Customizable Grammar**: Support for custom grammar files
- **Graceful Exit**: Handles interrupts and EOF gracefully

## Requirements

- Python 3.6+
- `core.validator` module (SentenceValidator class)

## Installation

1. Ensure you have Python 3.6+ installed
2. Navigate to the `english_checker` directory
3. Make sure the `core` module and `grammar` directory are present

## Usage

### Basic Usage

```bash
python app.py
```

This will use the default grammar file `./grammar/english_grammar.cfg`.

### Custom Grammar File

```bash
python app.py path/to/your/grammar.cfg
```

### Interactive Commands

Once running, you can use these commands:

- **Enter text**: Type any English sentence to check its grammar
- **`help`**: Show available commands
- **`q`** or **`quit`**: Exit the program

### Example Session

```
🔍 English Grammar Checker
📝 Using grammar file: ./grammar/english_grammar.cfg
💡 Enter sentences to check grammar (type 'help' for commands, 'q' to quit)

➤ Enter sentence: The cat sits on the mat
✅ Valid: Sentence is grammatically correct

➤ Enter sentence: Cat the sits
❌ Invalid: Grammar error detected

➤ Enter sentence: help

📖 Available commands:
  help  - Show this help message
  q     - Quit the program
  quit  - Quit the program

➤ Enter sentence: q
👋 Goodbye!
```

## Error Handling

The application handles various error conditions:

- **Missing grammar file**: Clear error message with usage instructions
- **Invalid input**: Input validation with length limits (max 1000 characters)
- **Validator errors**: Graceful handling of initialization failures
- **Interrupts**: Clean exit on Ctrl+C or EOF

## Grammar File Format

The application expects a context-free grammar file in CFG format. The default file should be located at `./grammar/english_grammar.cfg`.

Example grammar rules:
```
S -> NP VP
NP -> Det N | N
VP -> V | V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'mat'
V -> 'sits' | 'runs'
```

## Technical Details

- **Input sanitization**: Removes potentially harmful characters
- **Unicode support**: Handles various text encodings
- **Memory efficient**: Streams input processing
- **Cross-platform**: Works on Windows, macOS, and Linux

## Troubleshooting

### Common Issues

1. **Grammar file not found**
   - Ensure the grammar file exists at the specified path
   - Check file permissions

2. **Validator initialization fails**
   - Verify the grammar file format is correct
   - Check for syntax errors in the grammar rules

3. **Import errors**
   - Ensure the `core` module is in the Python path
   - Verify all required dependencies are installed

### Debug Mode

For debugging issues, you can modify the error handling in `app.py` to show more detailed error messages.

## Contributing

When contributing to this project:

1. Follow the existing code style
2. Add appropriate error handling
3. Update documentation for new features
4. Test with various grammar files and input scenarios

## License

This project is part of a larger language processing toolkit. See the main project LICENSE file for details.