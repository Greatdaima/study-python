%load_ext autoreload
%autoreload 2

from kans import *
# create a KAN: 2D inputs, 1D output, and 5 hidden neurons. cubic spline (k=3), 5 grid intervals (grid=5).
device = torch.device('cpu')
model = KAN(width=[2,5,1], grid=5, k=3, seed=0, device=device)
# create dataset f(x,y) = exp(sin(pi*x)+y^2)
f = lambda x: torch.exp(torch.sin(torch.pi*x[:,[0]]) + x[:,[1]]**2)
dataset = create_dataset(f, n_var=2)
print('dataset['train_input'].shape, dataset['train_label'].shape')
# plot KAN at initialization
model(dataset['train_input']);
model.plot(beta=50)