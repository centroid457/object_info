import pathlib
from typing import *

from PROJECT import PROJECT


# =====================================================================================================================
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
# TODO: FINISH!!! IT IS NOT WORKING!!!
class History:
    # ------------------------------------------------
    FILE_NAME: str = "HISTORY.md"
    filepath: pathlib.Path = pathlib.Path(FILE_NAME)

    # ------------------------------------------------
    SEPARATOR_PATTERN = r'(\**\n+)*## USAGE EXAMPLES'

    LINE_STARS_WRAPPER: str = "*" * 80
    LINE_STARS_FILE_SEPARATOR: str = "*" * 30
    LINE_FILE_HEADER: str = "```python"
    LINE_FILE_FOOTER: str = "```"
    LINE_SEPARATOR_FILE: str = LINE_STARS_FILE_SEPARATOR

    LINES_HEADER: List[str] = [
        "Release History",
        "===============",
        "",
    ]

    # WORK WRITE ------------------------------------------------------------------------------------------------------
    @classmethod
    def file_clear(cls) -> None:
        cls.filepath.write_text("")

    @classmethod
    def file_append_lines(cls, lines: Optional[Union[str, List[str]]] = None) -> None:
        if not lines:
            lines = ""
        if isinstance(lines, str):
            lines = [lines, ]
        with cls.filepath.open("a") as fo_append:
            for lines in lines:
                fo_append.write(f"{lines}\n")

    # GENERATE ========================================================================================================
    @classmethod
    def update(cls):
        cls.file_clear()
        cls.append_main()

    @classmethod
    def append_main(cls):
        FEATURES = [
            f"",
            f"",
            f"## Features",
        ]
        for num, feature in enumerate(PROJECT.FEATURES, start=1):
            if isinstance(feature, list):
                FEATURES.append(f"{num}. {feature[0]}:  ")
                for block in feature[1:]:
                    FEATURES.append(f"\t- {block}  ")
            else:
                FEATURES.append(f"{num}. {feature}  ")

        LINES = [
            f"",

            f"",
            f"",
            cls.LINE_STARS_WRAPPER,
            f"## License",
            f"See the [LICENSE](LICENSE) file for license rights and limitations (MIT).",

            f"",
            f"",
            f"## Release history",
            f"See the [HISTORY.md](HISTORY.md) file for release history.",

            f"",
            f"",
            f"## Installation",
            f"```commandline",
            f"pip install {PROJECT.NAME_INSTALL}",
            f"```",

            f"",
            f"",
            f"## Import",
            f"```python",
            f"from {PROJECT.NAME_IMPORT} import *",
            f"```",
        ]
        cls.file_append_lines(LINES)


# =====================================================================================================================
if __name__ == '__main__':
    History.update()


# =====================================================================================================================
