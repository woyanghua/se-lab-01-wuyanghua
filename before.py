class OrderProcessor:
    def process_online_order(self, items, user):
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        
        if user["is_vip"]:
            total = total * 0.9
        
        tax = total * 0.1
        final_price = total + tax
        
        print(f"线上订单处理完成，总价：{final_price}")
        return True

    def process_offline_order(self, items, user):
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        
        if user["is_vip"]:
            total = total * 0.9
        
        tax = total * 0.1
        final_price = total + tax
        
        print(f"线下订单处理完成，总价：{final_price}")
        return True

unused_variable = "我是没用的变量"

if __name__ == "__main__":
    processor = OrderProcessor()
    test_items = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
    test_user = {"is_vip": True}
    processor.process_online_order(test_items, test_user)
    processor.process_offline_order(test_items, test_user)
