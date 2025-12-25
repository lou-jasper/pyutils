from setuptools import setup, find_packages

setup(
    name="loujasper-pyutils",
    version="0.1.0",
    description="自定义通用Python工具库",
    author="loujasper",
    author_email="loujaspersayhi@gmail.com",
    packages=find_packages(),  # 自动识别所有包
    install_requires=[
        "requests>=2.31.0",
        "psutil>=5.9.0"
    ],
    python_requires=">=3.8", 
)
