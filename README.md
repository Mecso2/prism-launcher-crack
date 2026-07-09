This repo contains patches to both the source code and one specific version of the built binary.
The souece code patch has a high chance of working with future versions as well, while the binary patch is guaranteed to only work with this version.

### Source code
- Apply `source.patch` to the source code
- Build it for your platform of choice
### Binary
- Download `PrismLauncher-Windows-MSVC-Portable-11.0.2.zip` from the official github page
- Extract it and `cd` into the directory
- Run `bin_patch_11.0.2.py`
- Optionally delete `prismlauncher.exe`, since you will use the newly created `prismlauncher_patched.exe` instead
### Finally
- Launch it
- Add an offline profile
- Have fun
