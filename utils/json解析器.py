class 对象数组解析器:
    def __init__(self, 对象数组: list[dict]):
        """
        入参：
            对象数组：
                形状为 [{},{},...]
                每个对象均包含 "key" 属性，且保证互异
        """
        if not isinstance(对象数组, list):
            raise TypeError("参数必须是列表")
        if len(对象数组) == 0:
            # 空列表情况，设为空字典
            self.结构 = {}
            return
        if not isinstance(对象数组[0], dict):
            raise TypeError("列表元素必须是字典")

        self.结构 = {}
        for item in 对象数组:
            if "key" not in item:
                raise ValueError("每个字典必须包含 \'key\' 键")
            key = item["key"]
            if key in self.结构:
                raise ValueError("key值\'{}\'重复".format(key))
            # 复制字典并删除key键
            new_item = {k: v for k, v in item.items() if k != "key"}
            self.结构[key] = new_item

    def __len__(self):
        return len(self.结构)

    @property
    def 共通属性(self):
        """每个字典都有的属性（不包含key）"""
        if not self.结构:
            return set()
        keys_sets = [set(v.keys()) for v in self.结构.values()]
        common = set.intersection(*keys_sets) if keys_sets else set()
        return common

    @property
    def 所有属性(self):
        """所有出现过的属性（不包含key）"""
        if not self.结构:
            return set()
        all_keys = set()
        for v in self.结构.values():
            all_keys.update(v.keys())
        return all_keys

    @property
    def 非共通属性(self):
        """所有属性 - 共通属性"""
        return self.所有属性 - self.共通属性

    def 提取属性值(self, 属性名):
        """返回 { k: v[属性名] for k,v in self.结构.items() }"""
        return {k: v[属性名] for k, v in self.结构.items()}

    def __getitem__(self, key):
        """支持通过键获取对象（已删除key属性后的字典）"""
        return self.结构[key]

    def __contains__(self, key):
        return key in self.结构

    def keys(self):
        return self.结构.keys()

    def values(self):
        return self.结构.values()

    def items(self):
        return self.结构.items()