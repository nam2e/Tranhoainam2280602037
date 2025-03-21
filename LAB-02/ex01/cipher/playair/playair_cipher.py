class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = set(key)  # Lưu các ký tự đã xuất hiện trong khóa
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không bao gồm "J"
        matrix = []

        # Thêm các ký tự trong khóa vào ma trận
        for letter in key:
            if letter not in matrix:
                matrix.append(letter)

        # Thêm các ký tự còn lại trong bảng chữ cái
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)

        # Chia ma trận thành 5x5
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
   
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
      
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Xử lý văn bản thành các cặp ký tự
        i = 0
        while i < len(plain_text):
            pair = plain_text[i:i + 2]
            if len(pair) == 1 or pair[0] == pair[1]:  # Nếu chỉ có 1 ký tự hoặc 2 ký tự giống nhau
                pair = pair[0] + "X"
                i += 1
            else:
                i += 2

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
    
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        # Giải mã từng cặp ký tự
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự "X" được thêm vào trong quá trình mã hóa
        final_text = ""
        i = 0
        while i < len(decrypted_text):
            if i < len(decrypted_text) - 1 and decrypted_text[i + 1] == "X" and (i + 2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i + 2]):
                final_text += decrypted_text[i]
                i += 2  # Bỏ qua ký tự "X"
            else:
                final_text += decrypted_text[i]
                i += 1

        return final_text