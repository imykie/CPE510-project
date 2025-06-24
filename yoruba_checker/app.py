import sys
import os
import re
from core.validator import SentenceValidator

def main():
    grammar_file = './grammar/yoruba_grammar.cfg'
    
    if len(sys.argv) > 1:
        grammar_file = sys.argv[1]
    
    if not os.path.exists(grammar_file):
        print(f"❌ Àṣìṣe: Ko rí fáìlì grammar '{grammar_file}'.")
        print("Lílò: python app.py [grammar_file]")
        print(f"❌ Error: Grammar file '{grammar_file}' not found.")
        print("Usage: python app.py [grammar_file]")
        sys.exit(1)
    
    try:
        validator = SentenceValidator(grammar_file)
    except Exception as e:
        print(f"❌ Àṣìṣe ní ìbere validator: {e}")
        print(f"❌ Error initializing validator: {e}")
        sys.exit(1)
    
    print("🔍 Ayẹwo Gbolohun Yorùbá / Yoruba Grammar Checker")
    print(f"📝 Ló fáìlì grammar: {grammar_file}")
    print("💡 Tẹ gbolohun láti ṣayẹwo grammar (tẹ 'iranlọwọ' fun awọn aṣe, 'q' lati jade)")
    print("💡 Enter Yoruba sentences to check grammar (type 'help' for commands, 'q' to quit)")
    
    while True:
        try:
            sentence = input("\n➤ Tẹ gbolohun Yorùbá: ").strip()
            
            if not sentence:
                continue
            
            if sentence.lower() in ['q', 'quit', 'jade', 'párí']:
                print("👋 Ó dàbọ! / Goodbye!")
                break
            
            if sentence.lower() in ['help', 'iranlọwọ', 'egba']:
                print("\n📖 Àwọn aṣe tí ó wà / Available commands:")
                print("  help / iranlọwọ - Han iránlọ́wọ́ yìí / Show this help")
                print("  q / jade          - Jáde kúro nínú ètò / Quit the program")
                print("  quit / párí       - Jáde kúro nínú ètò / Quit the program")
                continue
            
            if len(sentence) > 1000:
                print("❌ Àṣìṣe: Gbolohun gigún jú (tí ó pọ jú lẹtà 1000)")
                print("❌ Error: Sentence too long (max 1000 characters)")
                continue
            
            # Basic Yoruba character validation
            if not re.search(r'[a-zà-ỹ\s.,!?;:-]', sentence.lower()):
                print("❌ Àṣìṣe: Gbolohun kò dàbí èdè Yorùbá")
                print("❌ Error: Text doesn't appear to be Yoruba")
                continue
            
            valid, message = validator.validate(sentence)
            status_yoruba = "✅ Ó tọ" if valid else "❌ Kò tọ"
            status_english = "✅ Valid" if valid else "❌ Invalid"
            print(f"{status_yoruba} / {status_english}: {message}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Ó dàbọ! / Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Ó dàbọ! / Goodbye!")
            break
        except Exception as e:
            print(f"❌ Àṣìṣe tí a kò rétì: {e}")
            print(f"❌ Unexpected error: {e}")

if __name__ == '__main__':
    main()
