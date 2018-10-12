def init():
    DEVICE = torch.device('cuda')
    SCREEN_WIDTH = 600
    TARGET_UPDATE = 10
    ITERATIONS = 500
    BATCH_SIZE = 128
    GAMMA = 0.999
    EPSILON_START = 0.9
    EPSILON_END = 0.05
    EPSILON_DECAY = 200