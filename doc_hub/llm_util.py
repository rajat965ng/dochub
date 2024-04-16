from backend.backend.query_utils import query


def main():
    result = query("How much Red Hat revenue increased in year 2023?")
    print(result['result'])
