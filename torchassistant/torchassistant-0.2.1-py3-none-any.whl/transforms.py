import torch
from torchassistant.utils import pad_sequences


def reverse_onehot(y_hat, ground_true):
    return y_hat.argmax(dim=-1), ground_true


def pad_targets(y_hat, ground_true):
    filler = ground_true[0][-1]
    seqs, mask = pad_sequences(ground_true, filler)
    target = torch.LongTensor(seqs)
    return y_hat, target, mask


class DecodeText:
    def __init__(self, session):
        self.session = session

    def __call__(self, y_hat, ground_true):
        preprocessed_datasets = [ds for name, ds in self.session.datasets.items()
                                 if name.startswith("autogenerated")]
        ds = preprocessed_datasets[0]
        target_tokenizer = ds.preprocessors[-1]

        y_hat = y_hat.argmax(dim=2).tolist()
        if type(ground_true) is torch.Tensor:
            ground_true = ground_true.tolist()

        predicted_texts = []
        actual_texts = []
        for predicted_tokens, true_tokens in zip(y_hat, ground_true):
            predicted_texts.append(target_tokenizer.decode(predicted_tokens))
            actual_texts.append(target_tokenizer.decode(true_tokens))

        return predicted_texts, actual_texts
