import argparse
from typing import Any
import tensorflow as tf


class EasyDict(dict):
    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value

    def __delattr__(self, name: str) -> None:
        del self[name]


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def params_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--hop",
        type=int,
        default=256,
        help="Hop size (window size = 4*hop)",
    )
    parser.add_argument(
        "--mel_bins",
        type=int,
        default=256,
        help="Mel bins in mel-spectrograms",
    )
    parser.add_argument(
        "--sr",
        type=int,
        default=44100,
        help="Sampling Rate",
    )
    parser.add_argument(
        "--small",
        type=str2bool,
        default=False,
        help="If True, use model with shorter available context, useful for small datasets",
    )
    parser.add_argument(
        "--latdepth",
        type=int,
        default=64,
        help="Depth of generated latent vectors",
    )
    parser.add_argument(
        "--coorddepth",
        type=int,
        default=64,
        help="Dimension of latent coordinate and style random vectors",
    )
    parser.add_argument(
        "--max_lat_len",
        type=int,
        default=512,
        help="Length of latent sequences: a random on-the-fly crop will be used for training",
    )
    parser.add_argument(
        "--base_channels",
        type=int,
        default=128,
        help="Base channels for generator and discriminator architectures",
    )
    parser.add_argument(
        "--shape",
        type=int,
        default=128,
        help="Length of spectrograms time axis",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=64,
        help="Generator spectrogram window (must divide shape)",
    )
    parser.add_argument(
        "--mu_rescale",
        type=float,
        default=-25.0,
        help="Spectrogram mu used to normalize",
    )
    parser.add_argument(
        "--sigma_rescale",
        type=float,
        default=75.0,
        help="Spectrogram sigma used to normalize",
    )
    parser.add_argument(
        "--files_path",
        type=str,
        default="audio_samples/",
        help="Path of compressed latent samples to decode",
    )
    parser.add_argument(
        "--save_path",
        type=str,
        default="decoded_samples/",
        help="Path where decoded audio files will be saved",
    )
    parser.add_argument(
        "--dec_path",
        type=str,
        default="checkpoints/ae",
        help="Path of pretrained decoders weights",
    )
    parser.add_argument(
        "--load_path",
        type=str,
        default="None",
        help="If not None, load models weights from this path",
    )
    parser.add_argument(
        "--base_path",
        type=str,
        default="checkpoints",
        help="Path where pretrained models are downloaded",
    )
    parser.add_argument(
        "--testing",
        type=str2bool,
        default=True,
        help="True if optimizers weight do not need to be loaded",
    )
    parser.add_argument(
        "--cpu",
        type=str2bool,
        default=False,
        help="True if you wish to use cpu",
    )
    parser.add_argument(
        "--mixed_precision",
        type=str2bool,
        default=True,
        help="True if your GPU supports mixed precision",
    )

    tmp_args = parser.parse_args()

    args.hop = tmp_args.hop
    args.mel_bins = tmp_args.mel_bins
    args.sr = tmp_args.sr
    args.small = tmp_args.small
    args.latdepth = tmp_args.latdepth
    args.coorddepth = tmp_args.coorddepth
    args.max_lat_len = tmp_args.max_lat_len
    args.base_channels = tmp_args.base_channels
    args.shape = tmp_args.shape
    args.window = tmp_args.window
    args.mu_rescale = tmp_args.mu_rescale
    args.sigma_rescale = tmp_args.sigma_rescale
    args.save_path = tmp_args.save_path
    args.files_path = tmp_args.files_path
    args.dec_path = tmp_args.dec_path
    args.load_path = tmp_args.load_path
    args.base_path = tmp_args.base_path
    args.testing = tmp_args.testing
    args.cpu = tmp_args.cpu
    args.mixed_precision = tmp_args.mixed_precision

    if args.small:
        args.latlen = 128
    else:
        args.latlen = 256
    args.coordlen = (args.latlen // 2) * 3

    print()

    args.datatype = tf.float32
    gpuls = tf.config.list_physical_devices("GPU")
    if len(gpuls) == 0 or args.cpu:
        args.cpu = True
        args.mixed_precision = False
        tf.config.set_visible_devices([], "GPU")
        print()
        print("Using CPU...")
        print()
    if args.mixed_precision:
        args.datatype = tf.float16
        print()
        print("Using GPU with mixed precision enabled...")
        print()
    if not args.mixed_precision and not args.cpu:
        print()
        print("Using GPU without mixed precision...")
        print()

    return args


def parse_args():
    args = EasyDict()
    return params_args(args)
