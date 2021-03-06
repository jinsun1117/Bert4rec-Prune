from loggers import *
from config import STATE_DICT_KEY, OPTIMIZER_STATE_DICT_KEY
from utils import AverageMeterSet

import torch
import torch.nn as nn
import torch.optim as optim
from tensorboardX import SummaryWriter
from tqdm import tqdm

from abc import *
from pathlib import Path

from models.bert_modules.custom_layers import MaskedLinear, MaskedEmbedding

class AbstractPruner():
    def __init__(self, args, model):
        self.args = args
        self.device = args.device
        self.model = model.to(self.device)
        self.is_parallel = args.num_gpu > 1
        if self.is_parallel:
            self.model = nn.DataParallel(self.model)

    def print_mask(self, model):
        """Print only for linear layers for now"""
        for modules in model.bert.modules():
            if type(modules) in [MaskedLinear, MaskedEmbedding]:
                if type(modules.get_masks()) is str:
                    print('no mask')
                else:
                    print(modules)
                    print(modules.get_masks())
            #else:
                #print('no mask')

    def print_percentage(self, model):
        """Print only for linear layers for now"""
        for modules in model.bert.modules():
            if type(modules) in [MaskedLinear, MaskedEmbedding]:
                if type(modules.get_masks()) is str:
                    print('no mask')
                else:
                    print(modules)
                    print(100*(1-modules.get_masks().view(-1,1).sum().item()/modules.get_masks().view(-1,1).size(0)))
            #else:
                #print('no mask')
