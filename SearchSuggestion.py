class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        tmp_candidate = products
        for i in range(1, len(searchWord) + 1):
            tmp_ans = []
            for candidate in tmp_candidate:
                if candidate[:i] == searchWord[:i]:
                    tmp_ans.append(candidate)
            res.append(tmp_ans[:3])
            tmp_candidate = tmp_ans
        return res


