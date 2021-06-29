"""
Author: kok-s0s
Date: 2021-06-30 01:27:38
LastEditors: kok-s0s
LastEditTime: 2021-06-30 01:30:03
Description: file content
"""

from gmssl import sm3, func

if __name__ == "__main__":
    y = sm3.sm3_hash(func.bytes_to_list())
    print(y)
