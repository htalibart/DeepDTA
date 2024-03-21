import argparse
import os
import pathlib


def argparser():
	parser = argparse.ArgumentParser()
	# for model
	parser.add_argument(
	  '--seq_window_lengths',
	  type=int,
	  nargs='+',
	  help='Space seperated list of motif filter lengths. (ex, --window_lengths 4 8 12)'
	)
	parser.add_argument(
	  '--smi_window_lengths',
	  type=int,
	  nargs='+',
	  help='Space seperated list of motif filter lengths. (ex, --window_lengths 4 8 12)'
	)
	parser.add_argument(
	  '--num_windows',
	  type=int,
	  nargs='+',
	  help='Space seperated list of the number of motif filters corresponding to length list. (ex, --num_windows 100 200 100)'
	)
	parser.add_argument(
	  '--num_hidden',
	  type=int,
	  default=0,
	  help='Number of neurons in hidden layer.'
	)
	parser.add_argument(
	  '--num_classes',
	  type=int,
	  default=0,
	  help='Number of classes (families).'
	)
	parser.add_argument(
	  '--max_seq_len',
	  type=int,
	  default=0,
	  help='Length of input sequences.'
	)
	parser.add_argument(
	  '--max_smi_len',
	  type=int,
	  default=0,
	  help='Length of input sequences.'
	)
	# for learning
	parser.add_argument(
	  '--learning_rate',
	  type=float,
	  default=0.001,
	  help='Initial learning rate.'
	)
	parser.add_argument(
	  '--num_epoch',
	  type=int,
	  default=100,
	  help='Number of epochs to train.'
	)
	parser.add_argument(
	  '--batch_size',
	  type=int,
	  default=256,
	  help='Batch size. Must divide evenly into the dataset sizes.'
	)
	parser.add_argument(
	  '--dataset_path',
	  type=pathlib.Path,
	  required=True,
	  help='Directory for input data.'
	)
	#  parser.add_argument(
	#	   '--problem_type',
	#	   type=int,
	#	   default=1,
	#	   help='Type of the prediction problem (1-4)'
	#  )
	parser.add_argument(
	  '--binary_th',
	  type=float,
	  default=0.0,
	  help='Threshold to split data into binary classes'
	)
	parser.add_argument(
	  '--is_log',
	  type=int,
	  default=0,
	  help='use log transformation for Y'
	)
	parser.add_argument(
	  '--checkpoint_path',
	  type=pathlib.Path,
	  default=pathlib.Path('.'),
	  help='Path to write checkpoint file.'
	)
	parser.add_argument(
	  '--log_dir',
	  type=pathlib.Path,
	  default=pathlib.Path('/tmp'),
	  help='Directory for log data.'
	)
	parser.add_argument(
	  '--train_fold',
	  type=pathlib.Path,
	  required=True,
	  help='.txt with train fold split indices'
	)
	parser.add_argument(
	  '--test_fold',
	  type=pathlib.Path,
	  required=True,
	  help='.txt with test fold split indices'
	)
	
	FLAGS, unparsed = parser.parse_known_args()
	return FLAGS




def logging(msg, FLAGS):
	fpath = FLAGS.log_dir/"log.txt"
	with open( fpath, "a" ) as fw:
	fw.write("%s\n" % msg)
	#print(msg)
