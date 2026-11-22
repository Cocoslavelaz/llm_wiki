#!/usr/bin/env python3
"""
PDF Extraction Helper for LLM Wiki
Usage:
    uv run --with pypdf python scripts/extract_pdf.py <path_to_pdf> [--output <output_markdown_or_txt>]
"""

import sys
import argparse
from pathlib import Path

def extract_pdf_text(pdf_path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        print("[Error] pypdf is not installed. Please run via uv: uv run --with pypdf python scripts/extract_pdf.py ...", file=sys.stderr)
        sys.exit(1)

    if not pdf_path.exists():
        print(f"[Error] File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    
    extracted_text = []
    extracted_text.append(f"# Extracted Content: {pdf_path.name}")
    extracted_text.append(f"Total Pages: {num_pages}\n")

    for idx, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        extracted_text.append(f"--- [Page {idx + 1}] ---")
        extracted_text.append(page_text.strip())
        extracted_text.append("\n")

    return "\n".join(extracted_text)

def main():
    parser = argparse.ArgumentParser(description="Extract clean text from PDF for LLM Wiki Ingestion.")
    parser.add_argument("pdf_path", type=Path, help="Path to the PDF file in raw/papers/")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Optional output path (defaults to stdout)")

    args = parser.parse_args()
    
    content = extract_pdf_text(args.pdf_path)
    
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(f"[Success] Extracted {len(content)} characters to {args.output}")
    else:
        print(content)

if __name__ == "__main__":
    main()
