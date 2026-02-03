"""
Code Analysis Tools for Agentic AI.

Provides code parsing, analysis, and semantic search capabilities
using the existing vector store infrastructure.
"""

import ast
import re
from pathlib import Path
from typing import Any

from src.vector_store.qdrant_manager import QdrantManager
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def analyze_code_structure(working_directory: str, filepath: str) -> str:
    """
    Analyze the structure of a code file.
    
    Extracts classes, methods, imports, and other structural information.
    
    Args:
        working_directory: The permitted working directory
        filepath: Path to the code file
        
    Returns:
        Formatted analysis of the code structure
    """
    from src.tools.file_tools import _validate_path
    
    is_valid, full_path, error = _validate_path(working_directory, filepath)
    
    if not is_valid:
        return f"Error: {error}"
    
    if not full_path.exists():
        return f"Error: File '{filepath}' does not exist"
    
    try:
        content = full_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"
    
    # Determine file type and parse accordingly
    ext = full_path.suffix.lower()
    
    if ext == ".py":
        return _analyze_python(content, filepath)
    elif ext == ".java":
        return _analyze_java(content, filepath)
    elif ext in (".ts", ".tsx", ".js", ".jsx"):
        return _analyze_typescript(content, filepath)
    elif ext == ".cs":
        return _analyze_csharp(content, filepath)
    else:
        return f"Unsupported file type: {ext}. Supported: .py, .java, .ts, .tsx, .js, .jsx, .cs"


def _analyze_python(content: str, filepath: str) -> str:
    """Analyze Python code structure using AST."""
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        return f"Error parsing Python file: {str(e)}"
    
    classes = []
    functions = []
    imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = [
                n.name for n in node.body 
                if isinstance(n, ast.FunctionDef) or isinstance(n, ast.AsyncFunctionDef)
            ]
            classes.append({
                "name": node.name,
                "line": node.lineno,
                "methods": methods,
            })
        elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            # Only top-level functions
            if not any(
                node in ast.walk(cls) 
                for cls in ast.walk(tree) 
                if isinstance(cls, ast.ClassDef)
            ):
                functions.append({
                    "name": node.name,
                    "line": node.lineno,
                    "args": [arg.arg for arg in node.args.args],
                })
        elif isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    
    # Build output
    lines = [f"# Code Analysis: {filepath}\n"]
    
    if imports:
        lines.append("## Imports")
        for imp in sorted(set(imports)):
            lines.append(f"  - {imp}")
        lines.append("")
    
    if classes:
        lines.append("## Classes")
        for cls in classes:
            lines.append(f"  - {cls['name']} (line {cls['line']})")
            for method in cls['methods']:
                lines.append(f"    - {method}()")
        lines.append("")
    
    if functions:
        lines.append("## Functions")
        for func in functions:
            args = ", ".join(func['args'])
            lines.append(f"  - {func['name']}({args}) (line {func['line']})")
    
    return "\n".join(lines)


def _analyze_java(content: str, filepath: str) -> str:
    """Analyze Java code structure using regex patterns."""
    lines = [f"# Code Analysis: {filepath}\n"]
    
    # Extract package
    package_match = re.search(r'package\s+([\w.]+)\s*;', content)
    if package_match:
        lines.append(f"## Package\n  - {package_match.group(1)}\n")
    
    # Extract imports
    imports = re.findall(r'import\s+([\w.]+)\s*;', content)
    if imports:
        lines.append("## Imports")
        for imp in imports[:20]:  # Limit to first 20
            lines.append(f"  - {imp}")
        if len(imports) > 20:
            lines.append(f"  - ... and {len(imports) - 20} more")
        lines.append("")
    
    # Extract classes
    class_pattern = r'(?:public|private|protected)?\s*(?:abstract|static|final)?\s*class\s+(\w+)'
    classes = re.findall(class_pattern, content)
    if classes:
        lines.append("## Classes")
        for cls in classes:
            lines.append(f"  - {cls}")
        lines.append("")
    
    # Extract methods
    method_pattern = r'(?:public|private|protected)\s+(?:static\s+)?[\w<>[\],\s]+\s+(\w+)\s*\([^)]*\)'
    methods = re.findall(method_pattern, content)
    if methods:
        lines.append("## Methods")
        for method in methods[:30]:  # Limit to first 30
            lines.append(f"  - {method}()")
        if len(methods) > 30:
            lines.append(f"  - ... and {len(methods) - 30} more")
    
    return "\n".join(lines)


def _analyze_typescript(content: str, filepath: str) -> str:
    """Analyze TypeScript/JavaScript code structure using regex patterns."""
    lines = [f"# Code Analysis: {filepath}\n"]
    
    # Extract imports
    import_pattern = r'import\s+(?:(?:\{[^}]+\}|\*\s+as\s+\w+|\w+)\s+from\s+)?[\'"]([^\'"]+)[\'"]'
    imports = re.findall(import_pattern, content)
    if imports:
        lines.append("## Imports")
        for imp in imports[:20]:
            lines.append(f"  - {imp}")
        if len(imports) > 20:
            lines.append(f"  - ... and {len(imports) - 20} more")
        lines.append("")
    
    # Extract classes
    class_pattern = r'(?:export\s+)?class\s+(\w+)'
    classes = re.findall(class_pattern, content)
    if classes:
        lines.append("## Classes")
        for cls in classes:
            lines.append(f"  - {cls}")
        lines.append("")
    
    # Extract functions
    func_pattern = r'(?:export\s+)?(?:async\s+)?function\s+(\w+)'
    functions = re.findall(func_pattern, content)
    
    # Also arrow functions with const
    arrow_pattern = r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>'
    functions.extend(re.findall(arrow_pattern, content))
    
    if functions:
        lines.append("## Functions")
        for func in functions[:30]:
            lines.append(f"  - {func}()")
        if len(functions) > 30:
            lines.append(f"  - ... and {len(functions) - 30} more")
    
    # Extract interfaces
    interface_pattern = r'(?:export\s+)?interface\s+(\w+)'
    interfaces = re.findall(interface_pattern, content)
    if interfaces:
        lines.append("\n## Interfaces")
        for iface in interfaces:
            lines.append(f"  - {iface}")
    
    return "\n".join(lines)


def _analyze_csharp(content: str, filepath: str) -> str:
    """Analyze C# code structure using regex patterns."""
    lines = [f"# Code Analysis: {filepath}\n"]
    
    # Extract namespace
    ns_match = re.search(r'namespace\s+([\w.]+)', content)
    if ns_match:
        lines.append(f"## Namespace\n  - {ns_match.group(1)}\n")
    
    # Extract using statements
    usings = re.findall(r'using\s+([\w.]+)\s*;', content)
    if usings:
        lines.append("## Using Statements")
        for u in usings[:20]:
            lines.append(f"  - {u}")
        if len(usings) > 20:
            lines.append(f"  - ... and {len(usings) - 20} more")
        lines.append("")
    
    # Extract classes
    class_pattern = r'(?:public|private|protected|internal)?\s*(?:abstract|static|sealed|partial)?\s*class\s+(\w+)'
    classes = re.findall(class_pattern, content)
    if classes:
        lines.append("## Classes")
        for cls in classes:
            lines.append(f"  - {cls}")
        lines.append("")
    
    # Extract methods
    method_pattern = r'(?:public|private|protected|internal)\s+(?:static\s+)?(?:async\s+)?[\w<>[\],\s]+\s+(\w+)\s*\([^)]*\)'
    methods = re.findall(method_pattern, content)
    if methods:
        lines.append("## Methods")
        for method in methods[:30]:
            lines.append(f"  - {method}()")
        if len(methods) > 30:
            lines.append(f"  - ... and {len(methods) - 30} more")
    
    return "\n".join(lines)


def search_codebase(form_name: str, query: str, limit: int = 10) -> str:
    """
    Search the codebase using semantic search in the vector store.
    
    Args:
        form_name: The form name to search in
        query: Natural language search query
        limit: Maximum number of results
        
    Returns:
        Formatted search results
    """
    try:
        manager = QdrantManager()
        results = manager.search(
            form_name=form_name,
            query=query,
            limit=limit,
        )
        
        if not results:
            return f"No results found for query: '{query}'"
        
        lines = [f"# Search Results for: '{query}'\n"]
        
        for i, result in enumerate(results, 1):
            lines.append(f"## Result {i} (Score: {result.score:.3f})")
            
            if result.metadata:
                if "file_path" in result.metadata:
                    lines.append(f"File: {result.metadata['file_path']}")
                if "doc_type" in result.metadata:
                    lines.append(f"Type: {result.metadata['doc_type']}")
            
            # Truncate content if too long
            content = result.content
            if len(content) > 500:
                content = content[:500] + "..."
            
            lines.append(f"\n{content}\n")
            lines.append("---")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Search error: {e}")
        return f"Error searching codebase: {str(e)}"


def get_code_context(
    form_name: str,
    query: str,
    doc_type: str | None = None,
    limit: int = 5,
) -> str:
    """
    Retrieve relevant code context from the knowledge base.
    
    Args:
        form_name: The form name to search in
        query: Natural language query describing what context is needed
        doc_type: Optional filter by document type (code, business_logic, database, etc.)
        limit: Maximum number of context chunks
        
    Returns:
        Formatted context for use in prompts
    """
    try:
        manager = QdrantManager()
        
        filter_metadata = {}
        if doc_type:
            filter_metadata["doc_type"] = doc_type
        
        results = manager.search(
            form_name=form_name,
            query=query,
            limit=limit,
            filter_metadata=filter_metadata if filter_metadata else None,
        )
        
        if not results:
            return f"No context found for: '{query}'"
        
        lines = [f"# Retrieved Context for: '{query}'\n"]
        
        for i, result in enumerate(results, 1):
            source = "unknown"
            if result.metadata:
                source = result.metadata.get("file_path", result.metadata.get("source", "unknown"))
            
            lines.append(f"[Context {i}] Source: {source}")
            lines.append(result.content)
            lines.append("")
        
        return "\n".join(lines)
        
    except Exception as e:
        logger.error(f"Context retrieval error: {e}")
        return f"Error retrieving context: {str(e)}"
