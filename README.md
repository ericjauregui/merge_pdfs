# merge_pdfs

Simple Python utility to merge all PDFs inside `input/` into one file at `output/merged_pdf.pdf`.

## Requirements

- Python 3.12+
- `PyPDF2`

## Usage

From the project root:

```bash
uv run python main.py
```

The script asks for the output filename at runtime:

```text
Enter output PDF filename [merged_pdf.pdf]:
```

- Press Enter to use `merged_pdf.pdf`.
- If you omit `.pdf`, it is added automatically.

## Folder structure and edge-case behavior

- If `input/` is missing, the script creates it automatically.
- If `output/` is missing, the script creates it automatically.
- If both folders are missing, both are created automatically.
- If `input/` exists but contains no `.pdf` files, the script exits safely with a helpful message.
- PDFs are merged in filename-sorted order.

Expected structure after first run:

```text
merge_pdfs/
├── input/
├── output/
│   └── merged_pdf.pdf   # created when one or more PDFs exist in input/
├── main.py
└── README.md
```

## Notes

- Place files to merge in `input/`.
- Existing `output/<chosen-name>.pdf` will be overwritten on each successful run.
