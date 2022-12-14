#!/usr/bin/env python3

## Command Line Arguments
# NEW CUSTOMER or UPDATE CUSTOMER
# GIT CONFIG OR EXPORT CONFIG
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

def parser():
	### Customer Details
	parser = argparse.ArgumentParser(description='Generate Ansible configuration')

	# create the parser for the "new" command
	parser.add_argument('-c', '--customer', required=True,
			help='The Name of the customer.')
	parser.add_argument('-r', '--repo', required=True,
			help='The URL of the Customer Repostiory in Bitbucket.')
	args = parser.parse_args()

	# Customer Name
	global customer_name
	customer_name = args.customer
	
	# Customer Bitbucket Repository
	global customer_repository_url
	customer_repository_url = args.repo


def preparation():
	# Open existing Blueprint Repository
	blueprint_repository = git.Repo(".")

	# Check if the Blueprint Repository is up to date
	if blueprint_repository.is_dirty(untracked_files=True):
		print("[!] The Repository is not up to date. Please use git pull to update the Repository")
		#raise SystemExit

	### Customer Repository
	global temp_dir
	temp_dir = tempfile.TemporaryDirectory()
	global customer_repository_localpath
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
	global customer_branch_shovel
	customer_branch_shovel = "Shovel_" + date_today.strftime("%Y-%m-%d")
	# Init Customer Repository
	global customer_repository
	customer_repository = git.Repo.init(customer_repository_localpath)

	# ### Workaround: If a repository is empty it's not possible to create a new branch
	# # Check if necessary
	# dir = os.listdir(customer_repository_localpath)
	# if len(dir) == 0:
	# 	print("[+] Workaround for empty Master Repository required - empty README.md file will be created")
	# 	# Create an empty README.md file
	# 	open(customer_repository_localpath + "/README.md", 'a').close()

	# 	# Provide a list of files to stage
	# 	customer_repository.index.add(['README.md'])

	# 	# Provide a commit message
	# 	customer_repository.index.commit('Initial commit.')
	# 	print("[+] Workaround finised")
	# ### End Workaround

	# Create a Shovel branch
	customer_repository.git.branch(customer_branch_shovel)
	print("[+] Created a new Branch: " + customer_branch_shovel)

	# Checkout Shovel branch
	customer_repository.git.checkout(customer_branch_shovel)
	print("[+] Checkout to Shovel Branch " + customer_branch_shovel)



def customer_config():
	# Create Directories
	list = ["roles"]
	for items in list:
		path = os.path.join(customer_repository_localpath, items) 
		try:
			os.mkdir(path)
		except OSError as error:
			print(error)
		# workaround file creation: git ignores empty folders
		open(path + "/.blank", 'a').close()

	# List the configuration parameters
	index = -1
	for role in os.listdir(r'roles'):
		index += 1
		print("{}: {}".format(index,role))

	customer_roles = input("Which Roles should be deployed for " + customer_name + "? Enter the numbers from the list above and seperate with a comma: ")
	print(customer_roles)

def refinishing():
	# git add#
	print("[+] Git add all new files")
	customer_repository.git.add('--all')
	
	# git commit
	print("[+] Git commit")
	customer_repository.git.commit('-m', 'First commit after shovel script run')

	# git push
	print("[+] Git push")
	customer_repository.git.push('--set-upstream', 'origin', customer_branch_shovel)

	# git close
	# cleanup question?
	#temp_dir.cleanup()


def main():
	parser()
	preparation()
	customer_config()
	refinishing()

if __name__ == "__main__":
		main()