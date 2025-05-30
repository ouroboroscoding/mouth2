# coding=utf8
""" Mouth

Handles communication
"""

__author__		= "Chris Nasr"
__version__		= "1.0.0"
__copyright__	= "Ouroboros Coding Inc."
__email__		= "chris@ouroboroscoding.com"
__created__		= "2022-12-12"

# Python imports
from sys import argv, exit, stderr

def cli():
	"""CLI

	Called from the command line to run from the current directory

	Returns:
		uint
	"""

	# If we have no arguments
	if len(argv) == 1:

		# Run the REST server
		from mouth import rest
		return rest.run()

	# Else, if we have one argument
	elif len(argv) == 2:

		# If we are installing
		if argv[1] == 'install':
			from mouth import install
			return install.run()

		# Else, if we are explicitly stating the rest service
		elif argv[1] == 'rest':
			from mouth import rest
			return rest.run()

		# Else, if we are upgrading
		elif argv[1] == 'upgrade':
			from mouth import upgrade
			return upgrade.run()

	# Else, arguments are wrong, print and return an error
	print('Invalid arguments', file=stderr)
	return 1

# Only run if called directly
if __name__ == '__main__':
	exit(cli())