from setuptools import setup, find_packages

setup(
    name='your_package_name',  # パッケージ名
    version='0.1',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        # ここに依存ライブラリを追加
    ],
)
