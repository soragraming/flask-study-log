class Registry:
    registries = []

    def __init__(self, name = 'ABC'): # 初期化時に呼び出されれるもの
        print('コンストラクタ呼び出し')
        self.name = name
        Registry.registries.append(self.name)

    def __del__(self):
        print(f"{self.name}を削除")
        Registry.registries.remove(self.name)

    def print_name(self):
        print(self.name)

a = Registry('A') # a.name = 'A'
b = Registry('B')
c = Registry()
a.print_name() # A
b.print_name() # B
c.print_name() # ABC 初期値が採用される(4行目)
print(Registry.registries)
del a # 削除時に呼び出されるものデストラクタ
print(Registry.registries)
print('プログラムが終了しました。')