import struct
from enum import Enum
from math import (
    floor,
    sin,
)

from bitarray import bitarray


class MD5Buffer(Enum):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476


class MD5:
    _message = None
    _buffers = {
        MD5Buffer.A: None,
        MD5Buffer.B: None,
        MD5Buffer.C: None,
        MD5Buffer.D: None,
    }

    @classmethod
    def hash(cls, message: str):
        cls._message = message

        preprocessed_bit_array = cls.__append_message_length(cls.__alignment(message))
        cls.__initialize_buffer()
        cls.__calculate_hash(preprocessed_bit_array)
        return cls.__get_result()

    # Шаг 1. выравнивание потока
    @classmethod
    def __alignment(cls, message: str):
        bit_array = bitarray(endian="big")
        bit_array.frombytes(message.encode("utf-8"))

        bit_array.append(1)
        while len(bit_array) % 512 != 448:
            bit_array.append(0)

        return bitarray(bit_array, endian="big")

    # Шаг 2. добавление длины сообщения
    @classmethod
    def __append_message_length(cls, message: bitarray):
        length = (len(cls._message) * 8) % (pow(2, 64))
        length_bit_array = bitarray(endian="big")
        length_bit_array.frombytes(struct.pack("<Q", length))

        result = message.copy()
        result.extend(length_bit_array)
        return result

    # Шаг 3. Инициализация буфера
    @classmethod
    def __initialize_buffer(cls):
        for buffer_type in cls._buffers.keys():
            cls._buffers[buffer_type] = buffer_type.value

    # Шаг 4. Вычисление в цикле
    @classmethod
    def __calculate_hash(cls, message: bitarray):
        F = lambda x, y, z: (x & y) | (~x & z)
        G = lambda x, y, z: (x & z) | (y & ~z)
        H = lambda x, y, z: x ^ y ^ z
        I = lambda x, y, z: y ^ (x | ~z)

        rotate_left = lambda x, n: (x << n) | (x >> (32 - n))

        modular_add = lambda a, b: (a + b) % pow(2, 32)

        T = [floor(pow(2, 32) * abs(sin(i + 1))) for i in range(64)]

        N = len(message) // 32

        for chunk_index in range(N // 16):
            start = chunk_index * 512
            X = [message[start + (x * 32): start + (x * 32) + 32] for x in range(16)]

            X = [int.from_bytes(word.tobytes(), byteorder="little") for word in X]

            A = cls._buffers[MD5Buffer.A]
            B = cls._buffers[MD5Buffer.B]
            C = cls._buffers[MD5Buffer.C]
            D = cls._buffers[MD5Buffer.D]

            for i in range(4 * 16):
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    temp = F(B, C, D)
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    temp = G(B, C, D)
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    temp = H(B, C, D)
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    temp = I(B, C, D)

                temp = modular_add(temp, X[k])
                temp = modular_add(temp, T[i])
                temp = modular_add(temp, A)
                temp = rotate_left(temp, s[i % 4])
                temp = modular_add(temp, B)

                A = D
                D = C
                C = B
                B = temp

            cls._buffers[MD5Buffer.A] = modular_add(cls._buffers[MD5Buffer.A], A)
            cls._buffers[MD5Buffer.B] = modular_add(cls._buffers[MD5Buffer.B], B)
            cls._buffers[MD5Buffer.C] = modular_add(cls._buffers[MD5Buffer.C], C)
            cls._buffers[MD5Buffer.D] = modular_add(cls._buffers[MD5Buffer.D], D)

    # Шаг 5. Результат вычислений
    @classmethod
    def __get_result(cls):
        A = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.A]))[0]
        B = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.B]))[0]
        C = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.C]))[0]
        D = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.D]))[0]

        return f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}"
