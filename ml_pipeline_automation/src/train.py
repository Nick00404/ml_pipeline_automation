import torch
from model import SimpleNN

def train():
    # Dummy training loop
    model = SimpleNN(input_size=10, hidden_size=5, num_classes=2)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    for epoch in range(5):
        # dummy input and output
        x = torch.randn(10)
        y = torch.tensor([1])
        optimizer.zero_grad()
        outputs = model(x)
        loss = ((outputs - y.float()) ** 2).mean()
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch}, Loss: {loss.item()}')

if __name__ == '__main__':
    train()
