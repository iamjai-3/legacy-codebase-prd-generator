"""
File System Tools for Agentic AI.

Provides safe file system operations with working directory boundaries.
All operations are restricted to the configured working directory.
"""

from pathlib import Path


def _validate_path(working_directory: str, path: str) -> tuple[bool, Path, str]:
    """
    Validate that a path is within the working directory.

    Args:
        working_directory: The permitted working directory
        path: Path to validate (relative or absolute)

    Returns:
        Tuple of (is_valid, resolved_path, error_message)
    """
    try:
        working_dir = Path(working_directory).resolve()

        # Handle relative paths
        if not Path(path).is_absolute():
            full_path = (working_dir / path).resolve()
        else:
            full_path = Path(path).resolve()

        # Check if within working directory
        try:
            full_path.relative_to(working_dir)
            return True, full_path, ""
        except ValueError:
            return False, full_path, f"Path '{path}' is outside the permitted working directory"

    except Exception as e:
        return False, Path(), f"Invalid path: {str(e)}"


def get_files_info(working_directory: str, directory: str = ".") -> str:
    """
    List files and subdirectories in a directory with metadata.

    Returns a formatted string with file names, sizes, and whether each is a directory.

    Args:
        working_directory: The permitted working directory boundary
        directory: Directory to list (relative to working_directory)

    Returns:
        Formatted string listing directory contents
    """
    is_valid, target_dir, _ = _validate_path(working_directory, directory)

    if not is_valid:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not target_dir.exists():
        return f"Error: Directory '{directory}' does not exist"

    if not target_dir.is_dir():
        return f"Error: '{directory}' is not a directory"

    try:
        files_info = []
        for item in sorted(target_dir.iterdir()):
            try:
                # Get relative path from working directory (fallback to item.name if outside or on error)
                try:
                    rel_path = item.relative_to(Path(working_directory).resolve())
                except (ValueError, OSError):
                    rel_path = item.name

                is_dir = item.is_dir()
                file_size = item.stat().st_size if not is_dir else 0

                files_info.append(f"- {rel_path}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                files_info.append(f"- {rel_path}: Error reading file info: {e}")

        if not files_info:
            return f"Directory '{directory}' is empty"

        return "\n".join(files_info)

    except PermissionError:
        return f"Error: Permission denied accessing '{directory}'"
    except Exception as e:
        return f"Error listing files: {str(e)}"


def get_file_content(working_directory: str, filepath: str) -> str:
    """
    Read and return the contents of a file.

    Args:
        working_directory: The permitted working directory boundary
        filepath: Path to the file (relative to working_directory)

    Returns:
        File contents as string, or error message
    """
    is_valid, full_path, _ = _validate_path(working_directory, filepath)

    if not is_valid:
        return f"Error: Cannot read '{filepath}' as it is outside the permitted working directory"

    if not full_path.exists():
        return f"Error: File '{filepath}' does not exist"

    if full_path.is_dir():
        return f"Error: '{filepath}' is a directory, not a file"

    try:
        # Check file size to avoid reading huge files
        file_size = full_path.stat().st_size
        max_size = 1024 * 1024  # 1MB limit

        if file_size > max_size:
            return f"Error: File '{filepath}' is too large ({file_size} bytes). Maximum size is {max_size} bytes."

        content = full_path.read_text(encoding="utf-8")
        return content

    except UnicodeDecodeError:
        return f"Error: File '{filepath}' is not a text file or has invalid encoding"
    except PermissionError:
        return f"Error: Permission denied reading '{filepath}'"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_file(working_directory: str, filepath: str, content: str) -> str:
    """
    Write content to a file, creating it if it doesn't exist.

    Args:
        working_directory: The permitted working directory boundary
        filepath: Path to the file (relative to working_directory)
        content: Content to write to the file

    Returns:
        Success message or error message
    """
    is_valid, full_path, _ = _validate_path(working_directory, filepath)

    if not is_valid:
        return f"Error: Cannot write '{filepath}' as it is outside the permitted working directory"

    try:
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the file
        full_path.write_text(content, encoding="utf-8")

        return f"Successfully wrote {len(content)} bytes to '{filepath}'"

    except PermissionError:
        return f"Error: Permission denied writing to '{filepath}'"
    except Exception as e:
        return f"Error writing file: {str(e)}"


def find_files(
    working_directory: str,
    pattern: str,
    directory: str = ".",
    max_results: int = 50,
) -> str:
    """
    Find files matching a glob pattern within a directory.

    Args:
        working_directory: The permitted working directory boundary
        pattern: Glob pattern to match (e.g., "*.py", "**/*.java")
        directory: Directory to search in (relative to working_directory)
        max_results: Maximum number of results to return

    Returns:
        Formatted string listing matching files
    """
    is_valid, search_dir, _ = _validate_path(working_directory, directory)

    if not is_valid:
        return (
            f"Error: Cannot search '{directory}' as it is outside the permitted working directory"
        )

    if not search_dir.exists():
        return f"Error: Directory '{directory}' does not exist"

    if not search_dir.is_dir():
        return f"Error: '{directory}' is not a directory"

    try:
        matches = []
        working_path = Path(working_directory).resolve()

        # Use glob to find matching files
        for match in search_dir.glob(pattern):
            if len(matches) >= max_results:
                break

            # Validate each match is within working directory
            try:
                rel_path = match.relative_to(working_path)
                is_dir = match.is_dir()
                size = match.stat().st_size if not is_dir else 0

                matches.append(f"- {rel_path}: file_size={size} bytes, is_dir={is_dir}")
            except (ValueError, OSError):
                continue

        if not matches:
            return f"No files found matching pattern '{pattern}' in '{directory}'"

        result = f"Found {len(matches)} file(s) matching '{pattern}':\n"
        result += "\n".join(matches)

        if len(matches) >= max_results:
            result += f"\n\n(Results limited to {max_results} files)"

        return result

    except Exception as e:
        return f"Error searching files: {str(e)}"


def create_directory(working_directory: str, directory: str) -> str:
    """
    Create a directory and any necessary parent directories.

    Args:
        working_directory: The permitted working directory boundary
        directory: Directory path to create

    Returns:
        Success message or error message
    """
    is_valid, full_path, _ = _validate_path(working_directory, directory)

    if not is_valid:
        return (
            f"Error: Cannot create '{directory}' as it is outside the permitted working directory"
        )

    try:
        full_path.mkdir(parents=True, exist_ok=True)
        return f"Successfully created directory '{directory}'"

    except PermissionError:
        return f"Error: Permission denied creating '{directory}'"
    except Exception as e:
        return f"Error creating directory: {str(e)}"


def delete_file(working_directory: str, filepath: str) -> str:
    """
    Delete a file (not directories).

    Args:
        working_directory: The permitted working directory boundary
        filepath: Path to the file to delete

    Returns:
        Success message or error message
    """
    is_valid, full_path, _ = _validate_path(working_directory, filepath)

    if not is_valid:
        return f"Error: Cannot delete '{filepath}' as it is outside the permitted working directory"

    if not full_path.exists():
        return f"Error: File '{filepath}' does not exist"

    if full_path.is_dir():
        return f"Error: '{filepath}' is a directory. Use a different tool to delete directories."

    try:
        full_path.unlink()
        return f"Successfully deleted '{filepath}'"

    except PermissionError:
        return f"Error: Permission denied deleting '{filepath}'"
    except Exception as e:
        return f"Error deleting file: {str(e)}"
