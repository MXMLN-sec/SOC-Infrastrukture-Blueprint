#!/usr/bin/env python3

## Command Line Arguments
# NEW CUSTOMER or UPDATE CUSTOMER
# GIT CONFIG OR EXPORT CONFIG
# Customer Name
# Customer Repository URL
##


# -- Command Line Arguments
# List all Configs (rolls) to select from
# Copy the Rolls to the Customer Repository staging branch
# Create Playbook

import argparse
import tempfile
import git
import os
from datetime import date
import yaml

def preparation():
	# Open existing Blueprint Repository
	blueprint_repository = git.Repo(".")

	# Check if the Blueprint Repository is up to date
	if blueprint_repository.is_dirty(untracked_files=True):
		print("[!] The Repository is not up to date. Please use git pull to update the Repository")
		#raise SystemExit


	### Customer Details
	parser = argparse.ArgumentParser(description='Generate Ansible configuration')

	# create the parser for the "new" command
	parser.add_argument('-c', '--customer', required=True,
			help='The Name of the customer.')
	parser.add_argument('-r', '--repo', required=True,
			help='The URL of the Customer Repostiory in Bitbucket.')
	args = parser.parse_args()

	# Customer Name
	customer_name = args.customer
	
	# Customer Bitbucket Repository
	customer_repository_url = args.repo


	### Customer Repository
	temp_dir = tempfile.TemporaryDirectory()
	customer_repository_localpath = temp_dir.name + "-" + customer_name
	# Check if a direcotry with the same name already exists
	if(os.path.isdir(customer_repository_localpath)):
		print("A direcotry with the same name for the Customer Repositiry already exists: " + customer_repository_localpath)
		raise SystemExit

	# Clone the Customer Repository
	print("[+] Cloning Repository from " + customer_repository_url + " ...")
	git.Repo.clone_from(customer_repository_url, customer_repository_localpath)
	print("[+] Cloning Completed to temporary location: " + customer_repository_localpath)

	# Create a new Shovel branch with date in the name
	date_today = date.today()
	customer_branch_shovel = "Shovel_" + date_today.strftime("%Y-%m-%d")
	# Init Customer Repository
	customer_repository = git.Repo.init(customer_repository_localpath)

	### Workaround: If a repository is empty it's not possible to create a new branch
	# Check if necessary
	dir = os.listdir(customer_repository_localpath)
	if len(dir) == 0:
		print("[+] Workaround for empty Master Repository required - empty README.md file will be created")
		# Create an empty README.md file
		open(customer_repository_localpath + "/README.md", 'a').close()

		# Provide a list of files to stage
		customer_repository.index.add(['README.md'])

		# Provide a commit message
		customer_repository.index.commit('Initial commit.')
		print("[+] Workaround finised")
	### End Workaround

	# Create a Shovel branch
	customer_repository.git.branch(customer_branch_shovel)
	print("[+] Created a new Branch: " + customer_branch_shovel)

	# Checkout Shovel branch
	customer_repository.git.checkout(customer_branch_shovel)
	print("[+] Checkout to Shovel Branch " + customer_branch_shovel)



def customer_config():
	# Create Directories
	pass




def refinishing():
	# git add
	# git commit
	# git push
	# git close
	# cleanup question?
	#temp_dir.cleanup()
	pass


def main():
		preparation()
		customer_config()
		refinishing()

if __name__ == "__main__":
		main()