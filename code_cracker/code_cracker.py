class CodeCracker:
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    decryption_key = '! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o'
    alphabet_no_spaces = alphabet.replace(" ", "")
    decryption_key_no_spaces = decryption_key.replace(" ", "")

    def decrypt_message(self, message) -> str:
        cracked_message = ""
        if type(message) != str:
            cracked_message = "This is not a string"
        else:
            for character in message:
                this_index = self.decryption_key_no_spaces.index(character)
                cracked_message += self.alphabet_no_spaces[this_index]

        return cracked_message

    def enrypt_message(self, message) -> str:
        encrypted_message = ""
        if type(message) != str:
            encrypted_message = "This is not a string"
        else:
            for character in message:
                this_index = self.alphabet_no_spaces.index(character)
                encrypted_message += self.decryption_key_no_spaces[this_index]

        return encrypted_message


if __name__ == "__main__":
    obj = CodeCracker()
    message_to_decrypt = '!)"'
    print("Cracked message is", obj.decrypt_message(message_to_decrypt))

    message_to_decrypt = 'no'
    print("Cracked message is", obj.decrypt_message(message_to_decrypt))

    message_to_encrypt = 'wxyz'
    print("Encrypted message is", obj.enrypt_message(message_to_encrypt))
