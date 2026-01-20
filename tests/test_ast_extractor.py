"""
Tests for AST-based Code Extraction.
"""

import pytest

from src.extractors.code_extractor import CodeExtractor


class TestASTExtractor:
    """Tests for AST-based extraction in CodeExtractor."""

    @pytest.fixture
    def extractor(self):
        return CodeExtractor()

    def test_extract_java_ast(self, extractor):
        """Test Java AST extraction."""
        java_content = """
        package com.example;

        import java.util.List;
        import com.example.model.BaseEntity;

        public class UserService extends BaseEntity implements Service, Configurable {
            
            private UserRepository userRepository;
            public static final String CACHE_KEY = "users";
            
            public User findById(Long id) {
                return userRepository.find(id);
            }
            
            private void validate(User user) {
                // validation
            }
        }
        """

        # We need to mock _determine_file_type as it is not the focus here
        classes, methods, imports, fields, inherits, implements = (
            extractor._extract_code_structure_ast(java_content, "java")
        )

        assert "UserService" in classes
        assert "findById" in methods
        assert "validate" in methods
        assert "java.util.List" in imports
        assert "com.example.model.BaseEntity" in imports

        # New AST capabilities
        assert "userRepository" in fields
        assert "CACHE_KEY" in fields
        assert "BaseEntity" == inherits
        assert "Service" in implements
        assert "Configurable" in implements

    def test_extract_python_ast(self, extractor):
        """Test Python AST extraction."""
        python_content = """
import os
from typing import List
from .base import BaseService

class UserService(BaseService):
    def __init__(self, db):
        self.db = db
        
    def find_user(self, id: int) -> dict:
        return self.db.get(id)
        """

        classes, methods, imports, fields, inherits, implements = (
            extractor._extract_code_structure_ast(python_content, "python")
        )

        assert "UserService" in classes
        assert "find_user" in methods
        assert "__init__" in methods
        assert "os" in imports
        assert (
            "typing.List" in imports or "List" in imports
        )  # distinct implementations might vary slightly
        assert "BaseService" == inherits
        # Python doesn't have explicit interfaces in the same way, but we track inheritance

    def test_extract_sql_ast(self, extractor):
        """Test SQL AST extraction."""
        sql_content = """
        CREATE TABLE users (
            id INT PRIMARY KEY,
            username VARCHAR(50),
            email VARCHAR(100)
        );
        
        SELECT * FROM users WHERE id = 1;

        INSERT INTO audit_log (action) VALUES ('login');
        """

        # SQL should use the AST path too now
        classes, methods, imports, fields, inherits, implements = (
            extractor._extract_code_structure_ast(sql_content, "sql")
        )

        assert "users" in classes  # Tables -> Classes
        assert "audit_log" in classes
        assert "id" in fields  # Columns -> Fields
        assert "username" in fields
        assert "SELECT" in methods  # Statement Types -> Methods
        assert "INSERT" in methods
