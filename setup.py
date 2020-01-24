from setuptools import setup
setup(
    name='merge_pdf',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'mergepdf=merge_pdf:run'
        ]
    }
)
