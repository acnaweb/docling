from loguru import logger

from docling.document_converter import DocumentConverter


def main():
    logger.info("running job")

    converter = DocumentConverter()
    doc = converter.convert("https://arxiv.org/pdf/2501.17887")
    # doc.document.export_to_markdown()
    output = doc.document.export_to_dict()
    print(output)


if __name__ == "__main__":
    main()
