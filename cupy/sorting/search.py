from cupy import reduction


def argmax(a, axis=None, dtype=None, out=None, keepdims=False, allocator=None):
    """Returns the indices of the maximum along an axis.

    Args:
        a (cupy.ndarray): Array to take argmax.
        axis (int): Along which axis to find the maximum. ``a`` is flattened by
            default.
        dtype: Data type specifier.
        out (cupy.ndarray): Output array.
        keepdims (bool): If True, the axis ``axis`` is preserved as an axis of
            length one.
        allocator (function): CuPy memory allocator. The allocator of ``a`` is
            used by default.

    Returns:
        cupy.ndarray: The indices of the maximum of ``a`` along an axis.

    .. seealso:: :func:`numpy.argmax`

    """
    return reduction.argmax(a, axis=axis, dtype=dtype, out=out,
                            keepdims=keepdims, allocator=allocator)


def nanargmax(a, axis=None, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def argmin(a, axis=None, dtype=None, out=None, keepdims=False, allocator=None):
    """Returns the indices of the minimum along an axis.

    Args:
        a (cupy.ndarray): Array to take argmin.
        axis (int): Along which axis to find the minimum. ``a`` is flattened by
            default.
        dtype: Data type specifier.
        out (cupy.ndarray): Output array.
        keepdims (bool): If True, the axis ``axis`` is preserved as an axis of
            length one.
        allocator (function): CuPy memory allocator. The allocator of ``a`` is
            used by default.

    Returns:
        cupy.ndarray: The indices of the minimum of ``a`` along an axis.

    .. seealso:: :func:`numpy.argmin`

    """
    return reduction.argmin(a, axis=axis, dtype=dtype, out=out,
                            keepdims=keepdims, allocator=allocator)


def nanargmin(a, axis=None, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def argwhere(a, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def nonzero(a, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def flatnonzero(a, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def where(condition, x=None, y=None, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def searchsorted(a, v, side='left', sorter=None, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError


def extract(condition, arr, allocator=None):
    # TODO(beam2d): Implement it
    raise NotImplementedError
