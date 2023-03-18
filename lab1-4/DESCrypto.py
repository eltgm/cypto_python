from bitarray import bitarray

IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)

E = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)

PC1 = (
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
)

PC2 = (
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)

SPIN_TABLE = (1, 2, 4, 6, 8, 10, 12, 14, 15, 17, 19, 21, 23, 25, 27, 28)

S = (
    (
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
    ),
    (
        (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
    ),
    (
        (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
    ),
    (
        (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
        (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
        (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
    ),
    (
        (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),
    ),
    (
        (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
        (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
    ),
    (
        (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
    ),
    (
        (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
        (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11),
    )
)

P = (
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
)

IP1 = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
)


class DESCrypto:
    def __init__(self):
        self.child_keys = []

    def encode(self, enter: str, key: str):
        result = ""
        blocks = self._processing_encode_input(enter)

        for block in blocks:
            irb_result = self._init_replace_block(block)
            block_result = self._iteration(irb_result, key, False)
            block_result = self._end_replace_block(block_result)
            result += str(hex(int(block_result.encode(), 2)))

        return result

    def decode(self, cipher_text: str, key: str):
        result = []
        blocks = self._processing_decode_input(cipher_text)

        for block in blocks:
            irb_result = self._init_replace_block(block)
            block_result = self._iteration(irb_result, key, True)
            block_result = self._end_replace_block(block_result)

            for i in range(0, len(block_result), 8):
                result.append(block_result[i: i + 8])

        return self._bit_decode(list(filter(lambda value: value != '00000000', result)))

    # преобразуем входящее сообщение в битовые блоки размером 64
    def _processing_encode_input(self, enter: str) -> list:
        result = []
        bit_string = self._bit_encode(enter)

        if len(bit_string) % 64 != 0:
            for i in range(64 - len(bit_string) % 64):
                bit_string += '0'
        for i in range(len(bit_string) // 64):
            result.append(bit_string[i * 64: i * 64 + 64])

        return result

    # преобразуем входящий шифр в битовый блок
    @staticmethod
    def _processing_decode_input(enter: str) -> list:
        result = []
        input_list = enter.split("0x")[1:]
        int_list = [int("0x" + i, 16) for i in input_list]

        for i in int_list:
            bin_data = str(bin(i))[2:]
            while len(bin_data) < 64:
                bin_data = '0' + bin_data
            result.append(bin_data)

        return result

    # преобразуем строку из utf-8 в строку из двоичных символов.
    # Добавляем 1 в начале, чтобы довести двоичный размер символа до 8 знаков
    # (по таблице uft-8 символы лежат в диапазоне от 1000001 до 1111010)
    @staticmethod
    def _bit_encode(s: str) -> str:
        return bitarray(
            ''.join(
                [bin(int('1' + hex(c)[2:], 16))[3:]
                 for c in s.encode('utf-8')]
            )
        ).to01()

    # переставляем символы из блока согласно таблице перестановки
    @staticmethod
    def _replace_block(block: str, replace_table: tuple) -> str:
        result = ""
        for i in replace_table:
            result += block[i - 1]

        return result

    # начальная перестановка элементов в блоке
    def _init_replace_block(self, block: str):
        return self._replace_block(block, IP)

    # преобразование каждого блока
    def _iteration(self, block: str, key: str, is_decode: bool) -> str:
        self._key_selection_replacement(key)
        for i in range(16):
            left, right = block[0: 32], block[32: 64]
            next_left = right
            f_result = self._f_function(right, is_decode, i)
            right = self._not_or(left, f_result)
            block = next_left + right

        return block[32:] + block[:32]

    # преобразование ключа в 16 блоков по 48 бит
    def _key_selection_replacement(self, key: str):
        self.child_keys = []
        for child_key56 in self._spin_key(key):
            self.child_keys.append(self._replace_block(child_key56, PC2))

    def _f_function(self, right: str, is_decode: bool, num: int):
        right = self._block_extend(right)

        if is_decode:
            sbc_result = self._s_box_compression(15 - num, right)
        else:
            sbc_result = self._s_box_compression(num, right)

        return self._p_box_replacement(sbc_result)

    # расширяем каждый блок с 32 до 48 бит
    @staticmethod
    def _block_extend(block: str) -> str:
        extended_block = ""

        for i in E:
            extended_block += block[i - 1]

        return extended_block

    # преобразование ключа в битовую строку размером 64 бита и его первоначальная перестановка
    def _key_conversion(self, key):
        key = self._bit_encode(key)

        while len(key) < 64:
            key += '0'
        first_key = key[:64]

        return self._replace_block(first_key, PC1)

    def _s_box_compression(self, num: int, block48: str) -> str:
        result_not_or = self._not_or(block48, self.child_keys[num])
        return self._s_box_replace(result_not_or)

    # битовый сдвиг одного блока ключа
    def _spin_key(self, key: str):
        kc = self._key_conversion(key)
        left, right = kc[0: 28], kc[28: 56]

        for i in range(1, 17):
            left_after_spin = left[SPIN_TABLE[i - 1]:] + left[:SPIN_TABLE[i - 1]]
            right_after_spin = right[SPIN_TABLE[i - 1]:] + right[:SPIN_TABLE[i - 1]]

            yield left_after_spin + right_after_spin

    # замена символов согласно S таблице
    @staticmethod
    def _s_box_replace(block48: str) -> str:
        result = ""

        for i in range(8):
            row_bit = (block48[i * 6] + block48[i * 6 + 5]).encode("utf-8")
            line_bit = (block48[i * 6 + 1: i * 6 + 5]).encode("utf-8")
            row = int(row_bit, 2)
            line = int(line_bit, 2)
            data = S[i][row][line]
            no_full = str(bin(data))[2:]
            while len(no_full) < 4:
                no_full = '0' + no_full
            result += no_full

        return result

    def _p_box_replacement(self, block32: str) -> str:
        return self._replace_block(block32, P)

    # конечная перестановка в блоках согласно таблице IP^-1
    def _end_replace_block(self, block: str) -> str:
        return self._replace_block(block, IP1)

    @staticmethod
    def _not_or(a: str, b: str) -> str:
        result = ""
        size = len(a) if len(a) < len(a) else len(b)
        for i in range(size):
            result += '0' if a[i] == b[i] else '1'

        return result

    @staticmethod
    def _bit_decode(s: list):
        return ''.join([chr(i) for i in [int(b, 2) for b in s]])
