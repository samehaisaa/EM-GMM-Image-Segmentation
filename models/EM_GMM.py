import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
from matplotlib.patches import Ellipse

# Turn on interactive mode
plt.ion()

# Generate synthetic data (2D for visualization)
n_samples = 500
n_features = 2
n_clusters = 3
X, y_true = make_blobs(n_samples=n_samples, centers=n_clusters, clu__init__ster_std=1.5, random_state=42)

# Add random noise to the data
noise = np.random.randn(n_samples, n_features) * 10  # Adjust the scale of the noise
X_noisy = X + noise

# Initialize Gaussian Mixture Model (GMM) with sklearn
gmm = GaussianMixture(n_components=n_clusters, covariance_type='full', random_state=42, max_iter=1, warm_start=True)

# Create a plot to update during iterations
fig, ax = plt.subplots(figsize=(8, 6))

def plot_iteration(iteration, gmm, X, ax):
    ax.clear()
    ax.scatter(X[:, 0], X[:, 1], c='gray', s=30, alpha=0.6, label='Data points')
    
    # Plot the Gaussian components
    for i, (mean, cov) in enumerate(zip(gmm.means_, gmm.covariances_)):
        plot_gaussian(mean, cov, ax, label=f'Cluster {i+1}')
    
    ax.set_title(f'EM Algorithm - Iteration {iteration}')
    ax.legend()
    plt.draw()  # Make sure to redraw the plot
    plt.pause(0.5)  # Pause to allow the plot to update and visualize changes

def plot_gaussian(mean, cov, ax, label):
    """Plot an ellipse representing a 2D Gaussian."""
    # Compute the ellipse for the covariance matrix
    v, w = np.linalg.eigh(cov)
    v = 1.3 * np.sqrt(2.0) * np.sqrt(v)  # 2 standard deviations
    u = w[0] / np.linalg.norm(w[0])  # Eigenvector
    
    angle = np.arctan2(u[1], u[0])
    angle = 180.0 * angle / np.pi  # Convert to degrees
    
    # Create the ellipse
    ell = Ellipse(mean, width=v[0], height=v[1], angle=180.0 + angle, edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(ell)
    ax.scatter(mean[0], mean[1], c='red', s=100, zorder=10, label=label)

# Fit the GMM and visualize each iteration
for i in range(50):  # Set number of iterations to visualize
    gmm.fit(X_noisy)  # Use the noisy data to see more changes
    plot_iteration(i+1, gmm, X_noisy, ax)

# Keep the plot window open after iterations end
plt.ioff()  # Turn off interactive mode
plt.show()  # Display the final plot and keep it open
