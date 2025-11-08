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
            elif is_encrypt is False and letter in self.alphabet:
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
