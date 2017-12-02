import unittest

import numpy

from cupy import testing


class TestEinSumError(unittest.TestCase):

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis1(self, xp):
        xp.einsum('..', xp.zeros((2, 2, 2)))

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis2(self, xp):
        xp.einsum('...i...', xp.zeros((2, 2, 2)))

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis3(self, xp):
        xp.einsum('i...->...i...', xp.zeros((2, 2, 2)))

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis4(self, xp):
        xp.einsum('...->', xp.zeros((2, 2, 2)))

    @testing.numpy_cupy_raises()
    def test_no_arguments(self, xp):
        xp.einsum()

    @testing.numpy_cupy_raises()
    def test_one_argument(self, xp):
        xp.einsum('')

    @testing.numpy_cupy_raises()
    def test_not_string_subject(self, xp):
        xp.einsum(0, 0)

    @testing.numpy_cupy_raises()
    def test_bad_argument(self, xp):
        xp.einsum('', 0, bad_arg=0)

    @testing.numpy_cupy_raises()
    def test_too_many_operands1(self, xp):
        xp.einsum('', 0, 0)

    @testing.numpy_cupy_raises()
    def test_too_many_operands2(self, xp):
        xp.einsum('i,j', xp.array([0, 0]), xp.array([0, 0]), xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_too_few_operands1(self, xp):
        xp.einsum(',', 0)

    @testing.numpy_cupy_raises()
    def test_many_dimension1(self, xp):
        xp.einsum('i', 0)

    @testing.numpy_cupy_raises()
    def test_many_dimension2(self, xp):
        xp.einsum('ij', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_too_many_dimension3(self, xp):
        xp.einsum('ijk...->...', xp.arange(6).reshape(2, 3))

    @testing.numpy_cupy_raises()
    def test_too_few_dimension(self, xp):
        xp.einsum('i->i', xp.arange(6).reshape(2, 3))

    @testing.numpy_cupy_raises()
    def test_invalid_char1(self, xp):
        xp.einsum('i%', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_invalid_char2(self, xp):
        xp.einsum('j$', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_invalid_char3(self, xp):
        xp.einsum('i->&', xp.array([0, 0]))

    # output subscripts must appear in inumpy.t
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts1(self, xp):
        xp.einsum('i->ij', xp.array([0, 0]))

    # output subscripts may only be specified once
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts2(self, xp):
        xp.einsum('ij->jij', xp.array([[0, 0], [0, 0]]))

    # output subscripts must not incrudes comma
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts3(self, xp):
        xp.einsum('ij->i,j', xp.array([[0, 0], [0, 0]]))

    # dimensions much match when being collapsed
    @testing.numpy_cupy_raises()
    def test_invalid_diagonal1(self, xp):
        xp.einsum('ii', xp.arange(6).reshape(2, 3))

    @testing.numpy_cupy_raises()
    def test_invalid_diagonal2(self, xp):
        xp.einsum('ii->', xp.arange(6).reshape(2, 3))

    # invalid -> operator
    @testing.numpy_cupy_raises()
    def test_invalid_arrow1(self, xp):
        xp.einsum('i-i', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_invalid_arrow2(self, xp):
        xp.einsum('i>i', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_invalid_arrow3(self, xp):
        xp.einsum('i->->i', xp.array([0, 0]))

    @testing.numpy_cupy_raises()
    def test_invalid_arrow4(self, xp):
        xp.einsum('i-', xp.array([0, 0]))


@testing.parameterize(*testing.product({
    'do_opt': (True, False)
}))
@testing.with_requires('numpy>=1.12')
class TestOptimizedEinSumError(unittest.TestCase):

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis1(self, xp):
        xp.einsum('..', xp.zeros((2, 2, 2)), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis2(self, xp):
        xp.einsum('...i...', xp.zeros((2, 2, 2)), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_irregular_ellipsis3(self, xp):
        xp.einsum('i...->...i...', xp.zeros((2, 2, 2)), optimize=self.do_opt)

    # Numpy bug?
    # numpy not raises error if optimize is True.
    # @testing.numpy_cupy_raises()
    # def test_irregular_ellipsis4(self, xp):
    #     xp.einsum('...->', xp.zeros((2, 2, 2)), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_not_string_subject(self, xp):
        xp.einsum(0, 0, optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_bad_argument(self, xp):
        xp.einsum('', 0, bad_arg=0, optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_too_many_operands1(self, xp):
        xp.einsum('', 0, 0, optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_too_many_operands2(self, xp):
        xp.einsum('i,j', xp.array([0, 0]), xp.array([0, 0]), xp.array([0, 0]),
                  optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_too_few_operands1(self, xp):
        xp.einsum(',', 0, optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_many_dimension1(self, xp):
        xp.einsum('i', 0, optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_many_dimension2(self, xp):
        xp.einsum('ij', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_too_many_dimension3(self, xp):
        xp.einsum('ijk...->...', xp.arange(6).reshape(2, 3),
                  optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_too_few_dimension(self, xp):
        xp.einsum('i->i', xp.arange(6).reshape(2, 3), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_char1(self, xp):
        xp.einsum('i%', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_char2(self, xp):
        xp.einsum('j$', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_char3(self, xp):
        xp.einsum('i->&', xp.array([0, 0]), optimize=self.do_opt)

    # output subscripts must appear in inumpy.t
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts1(self, xp):
        xp.einsum('i->ij', xp.array([0, 0]), optimize=self.do_opt)

    # output subscripts may only be specified once
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts2(self, xp):
        xp.einsum('ij->jij', xp.array([[0, 0], [0, 0]]), optimize=self.do_opt)

    # output subscripts must not incrudes comma
    @testing.numpy_cupy_raises()
    def test_invalid_output_subscripts3(self, xp):
        xp.einsum('ij->i,j', xp.array([[0, 0], [0, 0]]), optimize=self.do_opt)

    # dimensions much match when being collapsed
    @testing.numpy_cupy_raises()
    def test_invalid_diagonal1(self, xp):
        xp.einsum('ii', xp.arange(6).reshape(2, 3), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_diagonal2(self, xp):
        xp.einsum('ii->', xp.arange(6).reshape(2, 3), optimize=self.do_opt)

    # invalid -> operator
    @testing.numpy_cupy_raises()
    def test_invalid_arrow1(self, xp):
        xp.einsum('i-i', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_arrow2(self, xp):
        xp.einsum('i>i', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_arrow3(self, xp):
        xp.einsum('i->->i', xp.array([0, 0]), optimize=self.do_opt)

    @testing.numpy_cupy_raises()
    def test_invalid_arrow4(self, xp):
        xp.einsum('i-', xp.array([0, 0]), optimize=self.do_opt)


@testing.parameterize(
    {'shape_a': (2, 3), 'subscripts': 'ij'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': '...'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': 'ji'},  # transpose
    {'shape_a': (3, 3), 'subscripts': 'ii->i'},  # diagonal 2d
    {'shape_a': (3, 3, 3), 'subscripts': 'jii->ij'},  # partial diagonal 3d
    {'shape_a': (3, 3, 3), 'subscripts': 'iji->ij'},  # partial diagonal 3d
    {'shape_a': (3, 3, 3), 'subscripts': '...ii->...i'},  # partial diagonal 3d
    {'shape_a': (3, 3, 3), 'subscripts': 'iii->i'},  # diagonal 3d
    {'shape_a': (2, 3, 4), 'subscripts': 'ijk->jik'},  # swap axes
    {'shape_a': (2, 3, 4), 'subscripts': 'ijk->kij'},  # swap axes
    {'shape_a': (2, 3, 4), 'subscripts': 'ijk->ikj'},  # swap axes
    {'shape_a': (2, 3, 4), 'subscripts': 'kji->ikj'},  # swap axes
    {'shape_a': (2, 3, 4), 'subscripts': 'j...i->i...j'},  # swap axes
    {'shape_a': (3,), 'subscripts': 'i->'},  # sum
    {'shape_a': (3, 3), 'subscripts': 'ii'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'ijkj->kij'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'ijij->ij'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'jiji->ij'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'ii...->...'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'i...i->...'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': '...ii->...'},  # trace
    {'shape_a': (2, 2, 2, 2), 'subscripts': 'j...i->...'},  # sum

    {'shape_a': (2, 3), 'subscripts': 'ij->ij...'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': 'ij->i...j'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': 'ij->...ij'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': 'ij...->ij'},  # do nothing
    {'shape_a': (2, 3), 'subscripts': 'i...j->ij'},  # do nothing
)
class TestEinSumUnaryOperation(unittest.TestCase):
    # Avoid overflow
    skip_dtypes = (numpy.bool_, numpy.int8, numpy.uint8)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_einsum_unary(self, xp, dtype):
        if dtype in self.skip_dtypes:
            return xp.array([])
        a = testing.shaped_arange(self.shape_a, xp, dtype)
        return xp.einsum(self.subscripts, a)


@testing.parameterize(
    # outer
    {'shape_a': (2,), 'shape_b': (3,),
     'subscripts': 'i,j'},
    # dot matvec
    {'shape_a': (2, 3), 'shape_b': (3,),
     'subscripts': 'ij,j'},
    {'shape_a': (2, 3), 'shape_b': (2,),
     'subscripts': 'ij,i'},
    # dot matmat
    {'shape_a': (2, 3), 'shape_b': (3, 4),
     'subscripts': 'ij,jk'},
    # tensordot
    {'shape_a': (3, 4, 2), 'shape_b': (4, 3, 2),
     'subscripts': 'ijk, jil -> kl'},
    {'shape_a': (3, 4, 2), 'shape_b': (4, 2, 3),
     'subscripts': 'i...,...k->ki...'},
    {'shape_a': (3, 4, 2), 'shape_b': (4, 3, 2),
     'subscripts': 'ij...,ji...->i...'},
    # trace and tensordot and diagonal
    {'shape_a': (2, 3, 2, 4), 'shape_b': (3, 2, 2),
     'subscripts': 'ijil,jkk->kj', 'skip_overflow': True},
    {'shape_a': (2, 4, 2, 3), 'shape_b': (3, 2, 4),
     'subscripts': 'i...ij,ji...->...j'},
    # broadcast
    {'shape_a': (2, 3, 4), 'shape_b': (3,),
     'subscripts': 'ij...,j...->ij...'},
    {'shape_a': (2, 3, 4), 'shape_b': (3,),
     'subscripts': 'ij...,...j->ij...'},
    {'shape_a': (2, 3, 4), 'shape_b': (3,),
     'subscripts': 'ij...,j->ij...'},
    {'shape_a': (4, 3), 'shape_b': (3, 2),
     'subscripts': 'ik...,k...->i...'},
    {'shape_a': (4, 3), 'shape_b': (3, 2),
     'subscripts': 'ik...,...kj->i...j'},
    {'shape_a': (4, 3), 'shape_b': (3, 2),
     'subscripts': '...k,kj'},
    {'shape_a': (4, 3), 'shape_b': (3, 2),
     'subscripts': 'ik,k...->i...'},
    {'shape_a': (2, 3, 4, 5), 'shape_b': (4,),
     'subscripts': 'ijkl,k'},
    {'shape_a': (2, 3, 4, 5), 'shape_b': (4,),
     'subscripts': '...kl,k'},
    {'shape_a': (2, 3, 4, 5), 'shape_b': (4,),
     'subscripts': '...kl,k...'},
    {'shape_a': (1, 1, 1, 2, 3, 2), 'shape_b': (2, 3, 2, 2),
     'subscripts': '...lmn,lmno->...o'},
)
class TestEinSumBinaryOperation(unittest.TestCase):
    skip_dtypes = (numpy.bool_, numpy.int8, numpy.uint8)
    skip_overflow = False

    @testing.for_all_dtypes_combination(['dtype_a', 'dtype_b'],
                                        no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_einsum_binary(self, xp, dtype_a, dtype_b):
        if self.skip_overflow and (dtype_a in self.skip_dtypes or
                                   dtype_b in self.skip_dtypes):
            return xp.array([])
        a = testing.shaped_arange(self.shape_a, xp, dtype_a)
        b = testing.shaped_arange(self.shape_b, xp, dtype_b)
        return xp.einsum(self.subscripts, a, b)


class TestEinSumBinaryOperationWithScalar(unittest.TestCase):
    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_scalar_1(self, xp, dtype):
        shape_a = (2,)
        a = testing.shaped_arange(shape_a, xp, dtype)
        return xp.asarray(xp.einsum(',i->', 3, a))

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_scalar_2(self, xp, dtype):
        shape_a = (2,)
        a = testing.shaped_arange(shape_a, xp, dtype)
        return xp.asarray(xp.einsum('i,->', a, 4))


@testing.parameterize(*testing.product({
    'shape_a': [(2, 3)], 'shape_b': [(3, 4)], 'shape_c': [(4, 5)],
    'subscripts': ['ij,jk,kl'], 'skip_overflow': [True],
}) + testing.product({
    'shape_a': [(2, 4)], 'shape_b': [(2, 3)], 'shape_c': [(2,)],
    'subscripts': ['ij,ik,i->ijk'], 'skip_overflow': [False],
}) + testing.product({
    'shape_a': [(2, 4)], 'shape_b': [(3, 2)], 'shape_c': [(2,)],
    'subscripts': ['ij,ki,i->jk'], 'skip_overflow': [False],
}) + testing.product({
    'shape_a': [(2, 3, 4)], 'shape_b': [(2,)], 'shape_c': [(3, 4, 2,)],
    'subscripts': ['i...,i,...i->...i'], 'skip_overflow': [True],
}))
class TestEinSumTernaryOperation(unittest.TestCase):
    skip_dtypes = (numpy.bool_, numpy.int8, numpy.uint8)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_einsum_ternary(self, xp, dtype):
        if self.skip_overflow and dtype in self.skip_dtypes:
            return xp.array([])
        a = testing.shaped_arange(self.shape_a, xp, dtype)
        b = testing.shaped_arange(self.shape_b, xp, dtype)
        c = testing.shaped_arange(self.shape_c, xp, dtype)
        return xp.einsum(self.subscripts, a, b, c).astype(numpy.float32)


@testing.parameterize(*testing.product({
    'shape_a': [(2, 3)], 'shape_b': [(3, 4)], 'shape_c': [(4, 5)],
    'subscripts': ['ij,jk,kl'], 'skip_overflow': [True],
    'optimize': [True, 'greedy']
}) + testing.product({
    'shape_a': [(2, 4)], 'shape_b': [(2, 3)], 'shape_c': [(2,)],
    'subscripts': ['ij,ik,i->ijk'], 'skip_overflow': [False],
    'optimize': [True, 'greedy']
}) + testing.product({
    'shape_a': [(2, 4)], 'shape_b': [(3, 2)], 'shape_c': [(2,)],
    'subscripts': ['ij,ki,i->jk'], 'skip_overflow': [False],
    'optimize': [True, 'greedy']
}) + testing.product({
    'shape_a': [(2, 3, 4)], 'shape_b': [(2,)], 'shape_c': [(3, 4, 2,)],
    'subscripts': ['i...,i,...i->...i'], 'skip_overflow': [True],
    'optimize': [True, 'greedy']
}))
@testing.with_requires('numpy>=1.12')
class TestEinSumTernaryOptimizedOperation(unittest.TestCase):
    skip_dtypes = (numpy.bool_, numpy.int8, numpy.uint8)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(contiguous_check=False)
    def test_einsum_ternary(self, xp, dtype):
        if self.skip_overflow and dtype in self.skip_dtypes:
            return xp.array([])
        a = testing.shaped_arange(self.shape_a, xp, dtype)
        b = testing.shaped_arange(self.shape_b, xp, dtype)
        c = testing.shaped_arange(self.shape_c, xp, dtype)
        return xp.einsum(self.subscripts, a, b, c,
                         optimize=self.optimize).astype(numpy.float32)


@testing.parameterize(
    # memory constraint
    {'subscript': 'a,b,c->abc', 'opt': ('greedy', 0)},
    {'subscript': 'acdf,jbje,gihb,hfac', 'opt': ('greedy', 0)},
    # long paths
    {'subscript': 'acdf,jbje,gihb,hfac,gfac,gifabc,hfac', 'opt': True},
    {'subscript': 'chd,bde,agbc,hiad,bdi,cgh,agdb', 'opt': True},
    # edge cases
    {'subscript': 'eb,cb,fb->cef', 'opt': True},
    {'subscript': 'dd,fb,be,cdb->cef', 'opt': True},
    {'subscript': 'bca,cdb,dbf,afc->', 'opt': True},
    {'subscript': 'dcc,fce,ea,dbf->ab', 'opt': True},
    {'subscript': 'a,ac,ab,ad,cd,bd,bc->', 'opt': True},
)
@testing.with_requires('numpy>=1.12')
class TestEinSumPath(unittest.TestCase):

    chars = 'abcdefghij'
    sizes = numpy.array([2, 3, 4, 5, 4, 3, 2, 6, 5, 4, 3])
    global_size_dict = {}
    for size, char in zip(sizes, chars):
        global_size_dict[char] = size

    def build_operands(self, string, size_dict=global_size_dict):
        # Builds views based off initial operands
        operands = [string]
        terms = string.split('->')[0].split(',')
        for term in terms:
            dims = [size_dict[x] for x in term]
            operands.append(numpy.random.rand(*dims))

        return operands

    @testing.numpy_cupy_equal()
    def test_einsum_path(self, xp):
        outer_test = self.build_operands(self.subscript)
        return xp.einsum_path(*outer_test, optimize=self.opt,
                              einsum_call=True)[1]


@testing.parameterize(
    {'shape_a': (2, 3, 4), 'shape_b': (4, 3), 'shape_c': (3, 3, 4),
     'subscript': 'a...,...b,c...->abc...'},
    {'shape_a': (2, 3, 4), 'shape_b': (3, 4), 'shape_c': (3, 3, 4),
     'subscript': 'a...,...,c...->ac...'},
    {'shape_a': (3, 3, 4), 'shape_b': (4, 3), 'shape_c': (2, 3, 4),
     'subscript': 'a...,...b,c...->abc...'},
    {'shape_a': (3, 3, 4), 'shape_b': (3, 4), 'shape_c': (2, 3, 4),
     'subscript': 'a...,...,c...->ac...'},
)
@testing.with_requires('numpy>=1.12')
class TestEinSumPathEllipsis(unittest.TestCase):

    @testing.numpy_cupy_equal()
    def test_einsum_path_ellipsis(self, xp):
        a = testing.shaped_arange(self.shape_a, xp, dtype=numpy.float32)
        b = testing.shaped_arange(self.shape_b, xp, dtype=numpy.float32)
        c = testing.shaped_arange(self.shape_c, xp, dtype=numpy.float32)
        # Check path only
        return xp.einsum_path(self.subscript, a, b, c, optimize=True,
                              einsum_call=True)[1][0][:2]
