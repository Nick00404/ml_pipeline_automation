import unittest
import torch
from src.model import SimpleNN

class TestModel(unittest.TestCase):
    def test_forward(self):
        model = SimpleNN(10, 5, 2)
        x = torch.randn(10)
        output = model(x)
        self.assertEqual(output.shape[0], 2)

if __name__ == '__main__':
    unittest.main()
