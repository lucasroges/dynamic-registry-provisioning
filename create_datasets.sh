poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=08.json -o central\;nodes=100\;unique_images=08 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=16.json -o central\;nodes=196\;unique_images=16 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=08.json -o community12p\;nodes=100\;unique_images=08 -rp community -c 3 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=16.json -o community12p\;nodes=196\;unique_images=16 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=08.json -o community25p\;nodes=100\;unique_images=08 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=16.json -o community25p\;nodes=196\;unique_images=16 -rp community -c 12 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=08.json -o p2p\;nodes=100\;unique_images=08 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=16.json -o p2p\;nodes=196\;unique_images=16 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=32.json -o central\;nodes=100\;unique_images=32 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=64.json -o central\;nodes=196\;unique_images=64 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=32.json -o community12p\;nodes=100\;unique_images=32 -rp community -c 3 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=64.json -o community12p\;nodes=196\;unique_images=64 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=32.json -o community25p\;nodes=100\;unique_images=32 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=64.json -o community25p\;nodes=196\;unique_images=64 -rp community -c 12 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;unique_images=32.json -o p2p\;nodes=100\;unique_images=32 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;unique_images=64.json -o p2p\;nodes=196\;unique_images=64 -rp p2p >> create_datasets.log
