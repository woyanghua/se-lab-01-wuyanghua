# before.py - 强化版带坏味道的代码（CodeQL 必扫出问题）
class OrderProcessor:
    # 过长函数 + 大量重复代码（超过10行重复）
    def process_online_order(self, items, user):
        # 订单为空校验（重复代码块1）
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        # 计算商品总价（重复代码块2）
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        print(f"计算总价：{total}")
        
        # VIP折扣（重复代码块3）
        if user["is_vip"]:
            total = total * 0.9
            print("VIP折扣已应用")
        
        # 税费计算（重复代码块4）
        tax_rate = 0.1
        tax = total * tax_rate
        final_price = total + tax
        print(f"税费：{tax}，最终价格：{final_price}")
        
        print(f"线上订单处理完成，总价：{final_price}")
        return True

    def process_offline_order(self, items, user):
        # 完全重复的代码块（和process_online_order 100%重复）
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        print(f"计算总价：{total}")
        
        if user["is_vip"]:
            total = total * 0.9
            print("VIP折扣已应用")
        
        tax_rate = 0.1
        tax = total * tax_rate
        final_price = total + tax
        print(f"税费：{tax}，最终价格：{final_price}")
        
        print(f"线下订单处理完成，总价：{final_price}")
        return True

# 多个未使用变量（强化版，CodeQL 必识别）
unused_var1 = 100
unused_var2 = "这是未使用的变量2"
unused_var3 = [1,2,3,4,5]

# 未使用的函数（新增坏味道）
def unused_function():
    print("这个函数定义了但从未被调用")

if __name__ == "__main__":
    processor = OrderProcessor()
    test_items = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
    test_user = {"is_vip": True}
    processor.process_online_order(test_items, test_user)
    processor.process_offline_order(test_items, test_user)
