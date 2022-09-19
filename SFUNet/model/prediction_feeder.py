#feeder for data to predict
import tensorflow as tf
import numpy as np

class PredictionFeeder(tf.keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays)."""

    def __init__(self, batch_size, img_size, features_dataset):
        self.batch_size = batch_size
        self.img_size = img_size
        self.features_dataset = features_dataset
        

    def __len__(self):
        return len(self.features_dataset) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_data = self.features_dataset[i : i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="float32")
        for j in range(len(batch_input_data)):
            img = batch_input_data[j]
            shift = (img + abs(np.min(img)))
            img = np.divide(shift, np.max(shift))
            img = np.expand_dims(img, axis=-1)
            x[j] = img
        return x