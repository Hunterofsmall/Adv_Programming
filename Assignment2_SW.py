import subprocess

class FileManager:
	def __init__(self, name_remote: str, name_local: str, name_cloud: str):
		#check whether the input is string:
		if not all (isinstance(arg, str) for arg in [name_remote, name_local, name_cloud]):
			raise TypeError("All inputs must be str type")

		self.name_remote = name_remote
		self.name_local = name_local
		self.name_cloud = name_cloud

	def __repr__(self):
		return (
			f"The name of the remote='{self.name_remote}', "'\n'
			f"The master local directory='{self.name_local}', "'\n'
    		f"The master cloud directory='{self.name_cloud}')"'\n'
    		)

	def convertCloudToLocal(self, filename: str):
		Cloud_path_CloudToLocal = self.name_remote + ":" + self.name_cloud + "/" + filename
		Local_path_CloudToLocal = Cloud_path_CloudToLocal.replace(self.name_remote + ":" + self.name_cloud, self.name_local)
		return Local_path_CloudToLocal

	def convertLocalToCloud(self, filename: str):
		Local_path_LocalToCloud = self.name_local + "/" + filename
		Cloud_path_LocalToCloud = Local_path_LocalToCloud.replace(self.name_local, self.name_remote + ":" + self.name_cloud)
		return Cloud_path_LocalToCloud

	def uploadData(self, filename: str):
		Local_path = self.convertCloudToLocal(filename)
		Cloud_path = self.convertLocalToCloud(filename).strip(filename)
		try:
			subprocess.run(
				["rclone", "copy", Local_path, Cloud_path],
				check = True
				)
			print(f"Successfully uploaded {filename} to {Cloud_path}")
		except subprocess.CalledProcessError as e:
			print (f"Error uploading file '{filename}'")

	def downloadData(self, filename: str):
		Local_path = self.convertCloudToLocal(filename).strip(filename)
		Cloud_path = self.convertLocalToCloud(filename)
		try:
			subprocess.run(
				["rclone", "copy", Cloud_path, Local_path],
				check = True
				)
			print(f"Successfully download {filename} to {Local_path}")
		except subprocess.CalledProcessError as e:
			print (f"Error downloading file '{filename}'")



c1 = FileManager("Dropbox_SW", "/Users/nathan/Desktop/Adv", "/Shenghan Wu/Shenghan Wu/Adv")
print(repr(c1))
#c1.downloadData("test.py")
c1.uploadData("test.py")



