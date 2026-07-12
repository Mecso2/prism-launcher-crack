This repo contains patches to both the source code and a few specific version of the built binary.
The source code patch has a high chance of working with future versions as well, while the binary patches are guaranteed to only work with their respective versions.

### Source code
- Apply `source.patch` to the source code
- Build it for your platform of choice
### Binary
- Download `PrismLauncher-Windows-MSVC-Portable-{VERSION}.zip` from the official github page
- Extract it and `cd` into the directory
- Run `bin_patch_{VERSION}.py`
- Optionally delete `prismlauncher.exe`, since you will use the newly created `prismlauncher_patched.exe` instead
### Finally
- Launch it
- Add an offline profile
- Have fun
