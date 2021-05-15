import os
import shutil
import time

def main():
	path = input("Enter the folder that you want to delete from: ")
	deleted_folders_count = 0
	deleted_files_count = 0
	no_of_days = 60
	seconds = time.time()-no_of_days*24*60*60
	
	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= os.stat(root_folder).st_ctime:
				os.remove(root_folder)
				deleted_folders_count += 1
				break
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= os.stat(folder_path).st_ctime:
						os.remove(folder_path)
						deleted_folders_count += 1
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= os.stat(folder_path).st_ctime:
						os.remove(file_path)
						deleted_files_count += 1

	else: 
		if seconds >= os.stat(path):
			os.remove(path)
			deleted_files_count += 1

	print("Deleted ",deleted_files_count," files and deleted ", deleted_folders_count, "folders")

main()


