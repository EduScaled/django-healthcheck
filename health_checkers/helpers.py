
def check_service(name, plugins):
    check = [p for p in plugins if p.__class__.__name__ == name]
    if check:
        return {
                str(check[0].identifier()): "working" if check[0].status != 0 else "unavailable"
            }, 200 if check[0].status != 0 else 500
    return {}, 500