class FileChunkIterator:
    """
    按块读取文件的迭代器
    适合处理大文件，避免一次性加载到内存
    """

    def __init__(self, filepath, chunk_size=1024):
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file = None

    def __iter__(self):
        self.file = open(self.filepath, 'r', encoding='utf-8')
        return self

    def __next__(self):
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()  # 读完后关闭文件
            raise StopIteration
        return chunk

    def __del__(self):
        # 防止文件未关闭（兜底处理）
        if self.file and not self.file.closed:
            self.file.close()


# ---- 测试（先创建一个测试文件）----
import os

# 创建测试文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello World! " * 100)

print("=== 文件分块读取 ===")
chunk_reader = FileChunkIterator("test.txt", chunk_size=50)
for i, chunk in enumerate(chunk_reader):
    print(f"第{i+1}块({len(chunk)}字节): {chunk[:30]}...")

os.remove("test.txt")  # 清理测试文件