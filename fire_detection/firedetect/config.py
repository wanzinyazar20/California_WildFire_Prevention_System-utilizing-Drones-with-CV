# import the necessary packages
import os

# initialize the path to the fire and non-fire dataset directories
FIRE_PATH = os.path.sep.join(["fire_dataset",
	"Fire"])
NON_FIRE_PATH = "8_scenes"

# initialize the class labels in the dataset
CLASSES = ["Non-Fire", "Fire"]

# define the size of the training and testing split
TRAIN_SPLIT = 0.75
TEST_SPLIT = 0.25

# define the initial learning rate, batch size, and number of epochs
INIT_LR = 1e-2
BATCH_SIZE = 32
NUM_EPOCHS = 10

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["output", "fire_detection.model.h5"])

# define the path to the output learning rate finder plot and
# training history plot
LRFIND_PLOT_PATH = os.path.sep.join(["output", "lrfind_plot.png"])
TRAINING_PLOT_PATH = os.path.sep.join(["output", "training_plot.png"])

# define the path to the output directory that will store our final
# output with labels/annotations along with the number of iamges to
# sample
OUTPUT_IMAGE_PATH = os.path.sep.join(["output", "examples"])
SAMPLE_SIZE = 50
