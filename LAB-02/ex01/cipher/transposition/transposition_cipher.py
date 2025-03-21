class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):

        encrypted_text = [''] * key

        # Lặp qua từng ký tự trong văn bản gốc
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key

        # Ghép các chuỗi cột lại thành văn bản mã hóa
        return ''.join(encrypted_text)

    def decrypt(self, text, key):

        # Tính số hàng và số ô trống
        num_rows = (len(text) + key - 1) // key  # Làm tròn lên
        num_shaded_boxes = (num_rows * key) - len(text)

        # Tạo danh sách các chuỗi tương ứng với các hàng
        plain_text = [''] * num_rows

        col = 0
        row = 0

        for symbol in text:
            plain_text[row] += symbol
            row += 1

            # Nếu đã đến cuối hàng hoặc gặp ô trống, chuyển sang cột tiếp theo
            if (row == num_rows) or (row == num_rows - 1 and col >= key - num_shaded_boxes):
                row = 0
                col += 1

        # Ghép các chuỗi hàng lại thành văn bản gốc
        return ''.join(plain_text)