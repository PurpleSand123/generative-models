from huggingface_hub import hf_hub_download

# Download the model from the Hub
hf_hub_download(repo_id="stabilityai/sv3d", filename="sv3d_p.safetensors", local_dir="checkpoints/")