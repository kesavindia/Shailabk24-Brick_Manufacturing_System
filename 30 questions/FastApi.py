from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, query_param: str = None):
#     return {"item_id": item_id, "query_param": query_param}
# print(read_item(2))
# print(read_root())
class Solution:
    def factorial(self, N):
        result = [1]  # Initialize the result with a single digit 1

        for i in range(2, N + 1):
            self.multiply(result, i)

        # The result list now contains the digits of N!
        return result

    def multiply(self, result, num):
        carry = 0

        for i in range(len(result)):
            product = result[i] * num + carry
            result[i] = product % 10
            carry = product // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

# Example usage:
sol = Solution()
N = 5
result_digits = sol.factorial(N)
print(result_digits)
