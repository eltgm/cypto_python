import struct
from enum import Enum

from bitarray import bitarray


class SHA1Buffer(Enum):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0


class SHA1:
    _message = None
    _buffers = {
        SHA1Buffer.A: None,
        SHA1Buffer.B: None,
        SHA1Buffer.C: None,
        SHA1Buffer.D: None,
        SHA1Buffer.E: None
    }

    @classmethod
    def hash(cls, message: str):
        cls._message = message

        preprocessed_bit_array = cls.__append_message_length(cls.__alignment(message))
        cls.__initialize_buffer()
        cls.__calculate_hash(preprocessed_bit_array)
        return cls.__get_result()

    # Выравниваем сообщение
    @classmethod
    def __alignment(cls, message: str):
        bit_array = bitarray(endian="big")
        bit_array.frombytes(message.encode("utf-8"))

        bit_array.append(1)
        while len(bit_array) % 512 != 448:
            bit_array.append(0)

        return bitarray(bit_array, endian="big")

    # добавляем к сообщению его длину
    @classmethod
    def __append_message_length(cls, message: bitarray):
        length = (len(cls._message) * 8) % (pow(2, 64))
        length_bit_array = bitarray(endian="big")
        length_bit_array.frombytes(struct.pack(">Q", length))

        result = message.copy()
        result.extend(length_bit_array)
        return result

    # инициализиурем буфер
    @classmethod
    def __initialize_buffer(cls):
        for buffer_type in cls._buffers.keys():
            cls._buffers[buffer_type] = buffer_type.value

    # проводим расчеты. Используем маску & 0xFFFFFFFF чтобы не получить переполнение int32
    @classmethod
    def __calculate_hash(cls, message: bitarray):
        rotate_left = lambda x, n: ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

        N = len(message) // 32
        X = [message[(x * 512): (x * 512) + 512] for x in range(N // 16)]

        for word in X:
            w = list(struct.unpack(">16L", word)) + [0] * 64
            for i in range(16, 80):
                w[i] = rotate_left((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

            a = cls._buffers[SHA1Buffer.A]
            b = cls._buffers[SHA1Buffer.B]
            c = cls._buffers[SHA1Buffer.C]
            d = cls._buffers[SHA1Buffer.D]
            e = cls._buffers[SHA1Buffer.E]

            for i in range(0, 80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                a, b, c, d, e = (
                    rotate_left(a, 5) + f + e + k + w[i] & 0xFFFFFFFF,
                    a,
                    rotate_left(b, 30),
                    c,
                    d,
                )

            cls._buffers[SHA1Buffer.A] = cls._buffers[SHA1Buffer.A] + a & 0xFFFFFFFF
            cls._buffers[SHA1Buffer.B] = cls._buffers[SHA1Buffer.B] + b & 0xFFFFFFFF
            cls._buffers[SHA1Buffer.C] = cls._buffers[SHA1Buffer.C] + c & 0xFFFFFFFF
            cls._buffers[SHA1Buffer.D] = cls._buffers[SHA1Buffer.D] + d & 0xFFFFFFFF
            cls._buffers[SHA1Buffer.E] = cls._buffers[SHA1Buffer.E] + e & 0xFFFFFFFF

    @classmethod
    def __get_result(cls):
        return f"{format(cls._buffers[SHA1Buffer.A], '08x')}{format(cls._buffers[SHA1Buffer.B], '08x')}{format(cls._buffers[SHA1Buffer.C], '08x')}{format(cls._buffers[SHA1Buffer.D], '08x')}{format(cls._buffers[SHA1Buffer.E], '08x')}"
