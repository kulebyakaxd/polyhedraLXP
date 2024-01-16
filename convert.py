def convert_proxy_format(proxy_string):
    # Разбиваем строку по ':'
    parts = proxy_string.split(':')
    # Проверяем, что строка содержит все необходимые части
    if len(parts) == 4:
        ip, port, user, pwd = parts
        # Формируем итоговый формат
        formatted_proxy = f"{user}:{pwd}@{ip}:{port}"
        return formatted_proxy
    else:
        # В случае, если строка не соответствует ожидаемому формату
        return "Неверный формат входной строки"

# Пример использования
a=[]
with open("proxy.txt") as f:
    proxies = [r.strip() for r in f.readlines()]
with open("proxy2.txt",'w') as f:
    for proxy in proxies:
        converted_proxy = convert_proxy_format(proxy)
        f.write(converted_proxy+"\n")
