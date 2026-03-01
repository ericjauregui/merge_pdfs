from pathlib import Path

from PyPDF2 import PdfMerger


def get_output_filename() -> str:
	default_name = "merged_pdf.pdf"
	requested_name = input(
		"Enter output PDF filename [merged_pdf.pdf]: "
	).strip()

	if not requested_name:
		return default_name

	safe_name = Path(requested_name).name
	if not safe_name.lower().endswith(".pdf"):
		safe_name = f"{safe_name}.pdf"

	if safe_name == ".pdf":
		return default_name

	return safe_name


def main() -> None:
	project_root = Path(__file__).resolve().parent

	input_dir = project_root / "input"
	output_dir = project_root / "output"

	input_dir.mkdir(parents=True, exist_ok=True)
	output_dir.mkdir(parents=True, exist_ok=True)

	pdfs = sorted(file for file in input_dir.iterdir() if file.suffix.lower() == ".pdf")

	if not pdfs:
		print(
			"No PDF files found in input/. Add one or more .pdf files and run again."
		)
		return

	print("pdfs to merge:\n", [pdf.name for pdf in pdfs])
	output_filename = get_output_filename()
	output_file = output_dir / output_filename

	merger = PdfMerger()
	try:
		for pdf in pdfs:
			merger.append(str(pdf))

		merger.write(str(output_file))
		print(f"\n{output_filename} created in output/!")
	finally:
		merger.close()


if __name__ == "__main__":
	main()