class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = ''

        for letter in text.lower():
            if is_encrypt and letter in self.alphabet:
                index = self.alphabet.index(letter)
                new_index = (index + shift) % len(self.alphabet)
                result += self.alphabet[new_index]
            elif is_encrypt == False and letter in self.alphabet:
                index = self.alphabet.index(letter)
                new_index = (index - shift) % len(self.alphabet)
                result += self.alphabet[new_index]
            else:
                result += letter
        return result


cipher_master = CipherMaster()
print(
    cipher_master.process_text(
        text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
        shift=-3,
        is_encrypt=False,
    )
)


# def cipher(self, original_text, shift):
#         result = ''
#         for letter in original_text.lower():
#             if letter in self.alphabet:
#                 index = self.alphabet.index(letter)
#                 new_index = (index + shift) % len(self.alphabet)
#                 result += self.alphabet[new_index]
#             else:
#                 result += letter
#         return result

#     def decipher(self, cipher_text, shift):
#         result = ''
#         for letter in cipher_text.lower():
#             if letter in self.alphabet:
#                 index = self.alphabet.index(letter)
#                 new_index = (index - shift) % len(self.alphabet)
#                 result += self.alphabet[new_index]
#             else:
#                 result += letter
#         return result


# cipher_master = CipherMaster()
# print(
#     cipher_master.cipher(
#         original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
#         shift=2,
#     )
# )
# print(
#     cipher_master.decipher(
#         cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
#         shift=-3,
#     )
# )
