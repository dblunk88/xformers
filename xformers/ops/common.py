import torch


def get_xformers_operator(name: str):
    def no_such_operator(*args, **kwargs):
        raise RuntimeError(
            f"No such operator xformers::{name} - did you forget to build xformers with `python setup.py develop`?"
        )

    try:
        return getattr(torch.ops.xformers, name)
    except (RuntimeError, AttributeError):
        return no_such_operator
