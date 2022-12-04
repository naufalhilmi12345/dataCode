import numpy as np

class PolynomialFeatures:

    def __init__(self):
        pass

    # Source: https://stackoverflow.com/questions/58867481/polynomial-expansion-from-scratch-with-numpy-python
    def transform(self, lst, degree):
        if degree==1:
            if 1 not in lst:
                result = lst.insert(0,1)
            result = lst
            return result
        elif degree > 1:
            new_result=[]
            result = self.transform(lst, degree-1)
            new_result.extend(result)
            for item in lst:
                for p_item in result:
                    tmp = item*p_item
                    if (tmp not in result) and (tmp not in new_result):
                        new_result.append(tmp)
            return new_result
        return 0
