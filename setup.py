from setuptools import setup, Extension

PACKAGES = ["cellstates"]


USE_CYTHON = True
try:
    import numpy
    from Cython.Build import cythonize
except (ModuleNotFoundError, ImportError):
    USE_CYTHON = False

if USE_CYTHON:
    ext = ".pyx" if USE_CYTHON else ".c"

    EXTENSIONS = [
        Extension(
            "cellstates.cluster",
            ["src/cellstates/cluster" + ext],
            include_dirs=[numpy.get_include(), "."],
            extra_compile_args=["-fopenmp"],
            extra_link_args=["-fopenmp"],
            define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        ),
        Extension(
            "cellstates.chelpers",
            ["src/cellstates/chelpers" + ext],
            include_dirs=[numpy.get_include(), "."],
            extra_compile_args=["-fopenmp"],
            extra_link_args=["-fopenmp"],
            define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        ),
    ]

    EXTENSIONS = cythonize(EXTENSIONS, compiler_directives={"language_level": 3})
else:
    EXTENSIONS = []

if __name__ == "__main__":
    setup(ext_modules=EXTENSIONS)
