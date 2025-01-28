from typing import List, Optional, Union
from ..constants.enums import ContentType, TextType, MarkType, HeadingLevel
from ..exceptions.validation import RequiredFieldError, InvalidMarkError


class Text:
    """
    Represents a text element in the ADF document.

    Attributes:
        text: The actual text content
        marks: Optional list of marks to apply to the text
    """

    def __init__(self, text: str, *marks: Union[str, dict]):
        if not text:
            raise RequiredFieldError("text is required")

        self.text = text
        self.marks = marks

    def _validate_marks(self, marks: tuple) -> List[dict]:
        """
        Validates and formats the marks applied to the text.

        Args:
            marks: Tuple of marks to validate

        Returns:
            List[dict]: List of validated mark dictionaries
        """
        accepted_marks = []
        valid_marks = [mark.value for mark in MarkType]

        for mark in marks:
            if isinstance(mark, dict):
                if mark["type"] not in valid_marks:
                    raise InvalidMarkError(f"Invalid mark: {mark}")
                accepted_marks.append(mark)
            elif mark in valid_marks:
                accepted_marks.append({"type": mark})
            else:
                raise InvalidMarkError(f"Invalid mark: {mark}")

        return accepted_marks

    def _create_content(self) -> List[dict]:
        """
        Creates the content dictionary for the text element.

        Returns:
            List[dict]: The content in ADF format
        """
        return [
            {
                "type": ContentType.TEXT.value,
                "text": self.text,
                "marks": self._validate_marks(self.marks),
            }
        ]

    def heading(
        self,
        level: Union[int, HeadingLevel] = HeadingLevel.H1,
        local_id: Optional[str] = None,
    ) -> dict:
        """
        Creates a heading element.

        Args:
            level: The heading level (1-6)
            local_id: Optional local identifier

        Returns:
            dict: The heading in ADF format
        """
        if isinstance(level, HeadingLevel):
            level = level.value

        heading = {
            "type": TextType.HEADING.value,
            "attrs": {"level": level},
            "content": self._create_content(),
        }

        if local_id:
            heading["attrs"]["localId"] = local_id

        return heading

    def paragraph(self, local_id: Optional[str] = None) -> dict:
        """
        Creates a paragraph element.

        Args:
            local_id: Optional local identifier

        Returns:
            dict: The paragraph in ADF format
        """
        paragraph = {
            "type": TextType.PARAGRAPH.value,
            "content": self._create_content(),
        }

        if local_id:
            paragraph["attrs"] = {"localId": local_id}

        return paragraph

    @staticmethod
    def merge_paragraphs(*paragraphs: dict, spacing: int = 1) -> dict:
        """
        Merge multiple paragraphs to a single inline paragraph.

        Args:
            paragraphs: The paragraphs to append
            spacing: The spacing between paragraphs

        Returns:
            dict: The combined paragraph in ADF format
        """
        content = []
        for p in paragraphs:
            content.extend(p["content"])
            content.append({"type": "text", "text": " " * spacing})  # Add spacing

        # Remove the last added spacing
        if content and spacing > 0:
            content.pop()

        return {"type": "paragraph", "content": content}
