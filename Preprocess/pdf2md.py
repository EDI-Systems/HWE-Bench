import subprocess
import shutil
from pathlib import Path

import fitz  # pip install pymupdf


# ============= Configuration: Modify only here =============

# Root directory (contains 0/1/.../projectX/datasheet)
ROOT_DIR = "D:/llm/unpdf"  # TODO: Replace with your root path

MAX_PAGES = 50        # Maximum number of pages to process per PDF

# =========================================================


def get_pdf_page_count(pdf_path: Path) -> int:
    """Get the total number of pages in the PDF"""
    try:
        doc = fitz.open(pdf_path)
        n = doc.page_count
        doc.close()
        return n
    except Exception as e:
        print(f"⚠ Cannot get page count: {pdf_path}, Error: {e}")
        return 0


def process_single_pdf(pdf_path: Path, final_out_dir: Path, tmp_root: Path):
    """
    Call mineru for a single PDF, limit pages,
    keep only md files in final_out_dir, use tmp_root as a temporary directory (will be cleared).
    """
    pdf_path = pdf_path.resolve()
    stem = pdf_path.stem

    # Clear tmp_root before each processing to ensure it's clean
    if tmp_root.exists():
        shutil.rmtree(tmp_root, ignore_errors=True)
    tmp_root.mkdir(parents=True, exist_ok=True)

    total_pages = get_pdf_page_count(pdf_path)
    if total_pages == 0:
        print(f"Skipping: {pdf_path} (Page count is 0 or failed to read)")
        return

    end_page = min(MAX_PAGES - 1, total_pages - 1)
    if total_pages > MAX_PAGES:
        print(f"  ⚠ {pdf_path.name}: Total {total_pages} pages, processing only first {MAX_PAGES} pages (0~{end_page})")
    else:
        print(f"  📄 {pdf_path.name}: Total {total_pages} pages, processing all (0~{end_page})")

    cmd = [
        "mineru",
        "-p", str(pdf_path),
        "-o", str(tmp_root),
        "-m", "auto",
        "-b", "pipeline",
        "-l", "ch",
        "-f", "false",   # Disable formulas
        "-t", "true",    # Enable tables
        "-d", "cpu",
        "-s", "0",
        "-e", str(end_page),
    ]

    print("  Executing command:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Recursively find all md files under tmp_root (newer mineru writes md in subdir/auto)
    md_files = list(tmp_root.rglob("*.md"))
    if not md_files:
        print(f"   No md files found in {tmp_root} (and subdirectories)")
        return

    # Take the first md, prioritize paths containing 'auto'
    auto_mds = [p for p in md_files if "auto" in p.parts]
    candidates = auto_mds or md_files
    md_src = candidates[0]

    md_dest = final_out_dir / f"{stem}.md"

    # Avoid overwriting files with the same name
    if md_dest.exists():
        i = 1
        while True:
            candidate = final_out_dir / f"{stem}_{i}.md"
            if not candidate.exists():
                md_dest = candidate
                break
            i += 1

    shutil.move(str(md_src), str(md_dest))
    print(f"   Completed: {pdf_path.name} → {md_dest.name}")


def process_datasheet_dir(datasheet_dir: Path):
    """
    Process a single datasheet directory:
    - Find all pdfs inside
    - Output to the sibling directory output/pdf/pdf_md
    - Temporary directory: output/pdf/pdf_md/_tmp (deleted after processing)
    """
    project_dir = datasheet_dir.parent
    final_out_dir = project_dir / "output" / "pdf" / "pdf_md"
    tmp_root = final_out_dir / "_tmp"

    final_out_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(datasheet_dir.glob("*.pdf"))
    if not pdfs:
        print(f"⚠ No pdf found under {datasheet_dir}, skipping")
        return

    print(f"\n Processing datasheet: {datasheet_dir}")
    print(f"Final output directory: {final_out_dir}")
    print(f"Total {len(pdfs)} PDFs:\n")

    for pdf in pdfs:
        process_single_pdf(pdf, final_out_dir, tmp_root)

    # Delete temporary directory after processing the entire datasheet
    if tmp_root.exists():
        shutil.rmtree(tmp_root, ignore_errors=True)
        print(f"  Deleted temporary directory: {tmp_root}")


def main():
    root = Path(ROOT_DIR)
    if not root.exists() or not root.is_dir():
        print(f" ROOT_DIR does not exist or is not a directory: {root}")
        return

    # Find all directories named 'datasheet' under root
    datasheet_dirs = [p for p in root.rglob("datasheet") if p.is_dir()]
    if not datasheet_dirs:
        print(f" No 'datasheet' directory found under {root}")
        return

    print(f"Found {len(datasheet_dirs)} datasheet directories under {root}")

    for ds_dir in datasheet_dirs:
        process_datasheet_dir(ds_dir)

    print("\nAll datasheet processing completed!")


if __name__ == "__main__":
    main()
