import numpy as np
import csv

class Searcher:
    def __init__(self, indexPath):
        self.indexPath = indexPath
    def search(self, queryFeatures, limit=10):
        result = {}

        with open(self.indexPath) as f:
            reader = csv.reader(f)

            for row in reader:
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)

                result[row[0]] = d

            f.close()
        results = sorted([(v, k) for (k, v) in result.items()])

        return results[:limit]
    
    def chi2_distance(self, histA, histB, eps=1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
        return d
