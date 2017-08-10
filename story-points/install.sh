echo 'export PATH="$PATH:'$(pwd)'"' >> ~/.bashrc

echo '#!/usr/bin/env bash' > story
echo 'python "'$(pwd)'/__main__.py" "$@"' >> story
chmod +x story
