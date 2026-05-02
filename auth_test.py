import os
from kaggle.api.kaggle_api_extended import KaggleApi

def test_auth():
    # 1. Manually set environment variables to bypass config files
    os.environ['KAGGLE_USERNAME'] = 'dirkxie37'
    os.environ['KAGGLE_KEY'] = 'KGAT_357c3538c6cbf91f3bfbb1d451c2866d'

    try:
        api = KaggleApi()
        print("Attempting to authenticate...")
        api.authenticate()
        print("✅ Authentication successful!")
        
        # 2. Try a simple API call to verify communication
        print("Testing API communication (listing datasets)...")
        datasets = api.dataset_list(search='titanic', page=1)
        
        if datasets:
            print(f"✅ Success! Found {len(datasets)} datasets.")
            print(f"Sample dataset: {datasets[0].ref}")
        else:
            print("⚠️ Authenticated, but no datasets found (check internet/proxy).")

    except Exception as e:
        print("\n❌ Authentication Failed!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        
        # Check for common SSL/Time issues
        if "SSL" in str(e):
            print("\nPossible fix: Your server's SSL certificates or clock might be out of sync.")

if __name__ == "__main__":
    test_auth()


# import os
# import sys

# # 1. SET CREDENTIALS AT THE ABSOLUTE TOP
# # This ensures any library imported later sees these immediately.
# os.environ['KAGGLE_USERNAME'] = 'dirkxie37'
# os.environ['KAGGLE_KEY'] = 'KGAT_d45c8406bacb9da18b2e30787c602a37'

# print("--- Step 1: Testing MLEBench Import ---")
# try:
#     from mlebench.data import download_and_prepare_dataset
#     print("✅ Successfully imported download_and_prepare_dataset")
# except ImportError as e:
#     print(f"❌ Import failed: {e}. Are you sure you are in the right uv venv?")
#     sys.exit(1)

# def test_mlebench_flow():
#     print("\n--- Step 2: Testing Dataset Preparation ---")
    
#     # Replace 'titanic' with the actual dataset/benchmark name you are using
#     dataset_name = "spaceship-titanic" 
    
#     try:
#         print(f"Calling download_and_prepare_dataset('{dataset_name}')...")
        
#         # Note: Depending on your mlebench version, you might need to specify 
#         # a target directory. If it tries to download to your home dir, 
#         # it might fail due to the 100% disk usage.
#         download_and_prepare_dataset(dataset_name)
        
#         print("\n✅ SUCCESS: mlebench authenticated and executed the download flow.")
        
#     except Exception as e:
#         print("\n❌ MLEBench Task Failed!")
#         print(f"Error Type: {type(e).__name__}")
#         print(f"Message: {str(e)}")
        
#         if "401" in str(e) or "Unauthorized" in str(e):
#             print("👉 This is still an Auth error. Check if KAGGLE_KEY is exactly right.")
#         elif "No space left on device" in str(e):
#             print("👉 Disk Error: Even with links, the download target might be on your full '/' partition.")

# if __name__ == "__main__":
#     test_mlebench_flow()