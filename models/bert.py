from .base import BaseModel
from .bert_modules.bert import BERT

import torch.nn as nn


class BERTModel(BaseModel):
    def __init__(self, args):
        super().__init__(args)
        self.bert = BERT(args)
        self.out = nn.Linear(self.bert.hidden, args.bert_num_items + 1)

    @classmethod
    def code(cls):
        return 'bert'

    def forward(self, x):
        x = self.bert(x)
        return self.out(x)
    
    def set_masks(self, masks):
        """
        for mask in masks:
            print(mask)
            print(mask.data.size())
        """
        self.bert.embedding.token.set_masks((masks[0]), 'embedding_token')
        self.bert.embedding.position.pe.set_masks((masks[1]), 'embedding_position')
        self.bert.transformer_blocks[0].attention.linear_layers[0].set_masks((masks[2]), 'tr0_lin0')
        self.bert.transformer_blocks[0].attention.linear_layers[1].set_masks((masks[3]), 'tr0_lin1')
        self.bert.transformer_blocks[0].attention.linear_layers[2].set_masks((masks[4]), 'tr0_lin2')
        self.bert.transformer_blocks[0].attention.output_linear.set_masks((masks[5]), 'tr0_lin3')
        self.bert.transformer_blocks[0].feed_forward.w_1.set_masks((masks[6]), 'tr0_ff0')
        self.bert.transformer_blocks[0].feed_forward.w_2.set_masks((masks[7]), 'tr0_ff1')
        self.bert.transformer_blocks[1].attention.linear_layers[0].set_masks((masks[8]), 'tr1_lin0')
        self.bert.transformer_blocks[1].attention.linear_layers[1].set_masks((masks[9]), 'tr1_lin1')
        self.bert.transformer_blocks[1].attention.linear_layers[2].set_masks((masks[10]), 'tr1_lin2')
        self.bert.transformer_blocks[1].attention.output_linear.set_masks((masks[11]), 'tr1_lin3')
        self.bert.transformer_blocks[1].feed_forward.w_1.set_masks((masks[12]), 'tr1_ff0')
        self.bert.transformer_blocks[1].feed_forward.w_2.set_masks((masks[13]), 'tr1_ff1')