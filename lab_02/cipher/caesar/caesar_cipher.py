from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()  # Convert text to uppercase for consistent processing
        encrypted_text = []
        for letter in text:
            # Find the index of the letter in the alphabet
            letter_index = self.alphabet.index(letter)
            # Calculate the new index after shifting (modulo alphabet_len to wrap around)
            output_index = (letter_index + key) % alphabet_len
            # Get the encrypted letter from the alphabet
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text) # Join the list of characters to form the encrypted string

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()  # Convert text to uppercase for consistent processing
        decrypted_text = []
        for letter in text:
            # Find the index of the letter in the alphabet
            letter_index = self.alphabet.index(letter)
            # Calculate the original index after shifting back (modulo alphabet_len to wrap around)
            output_index = (letter_index - key) % alphabet_len
            # Get the decrypted letter from the alphabet
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text) # Join the list of characters to form the decrypted string
