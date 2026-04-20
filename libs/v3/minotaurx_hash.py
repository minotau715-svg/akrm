import ctypes
import os

LIB_PATH = os.path.join(os.path.dirname(__file__), "minotaurx_native.so")

_load_error = None
_lib = None

try:
    _lib = ctypes.CDLL(LIB_PATH)
except OSError as e:
    _load_error = str(e)

if _lib is not None:
    _lib.hash_minotaurx.argtypes = [
        ctypes.POINTER(ctypes.c_ubyte),
        ctypes.POINTER(ctypes.c_ubyte),
    ]
    _lib.hash_minotaurx.restype = ctypes.c_int


def get_lib_load_status():
    return _lib is not None, _load_error


def hash_minotaurx(input_bytes):
    if len(input_bytes) != 80:
        raise ValueError("Input must be exactly 80 bytes")
    if _lib is None:
        raise RuntimeError(f"Native library not loaded: {_load_error}")

    in_buf = (ctypes.c_ubyte * 80).from_buffer_copy(input_bytes)
    out_buf = (ctypes.c_ubyte * 32)()

    rc = _lib.hash_minotaurx(in_buf, out_buf)
    return rc, bytes(out_buf)
