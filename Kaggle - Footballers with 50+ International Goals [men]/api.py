import kagglehub

# Download latest version
path = kagglehub.dataset_download("whisperingkahuna/footballers-with-50-international-goals-men")

print("Path to dataset files:", path)
