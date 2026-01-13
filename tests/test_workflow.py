"""
Tests for PRD generation workflow.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.agents.base_agent import AgentContext
from src.extractors.code_extractor import CodeExtractor, CodeFile
from src.vector_store.qdrant_manager import QdrantManager


class TestCodeExtractor:
    """Tests for CodeExtractor."""
    
    def test_determine_file_type_adapter(self):
        """Test file type detection for adapters."""
        extractor = CodeExtractor()
        from pathlib import Path
        
        # Mock path and content
        file_type = extractor._determine_file_type(
            Path("UserAdapter.java"),
            "public class UserAdapter extends BaseAdapter {}"
        )
        
        assert file_type == "adapter"
    
    def test_determine_file_type_service(self):
        """Test file type detection for services."""
        extractor = CodeExtractor()
        from pathlib import Path
        
        file_type = extractor._determine_file_type(
            Path("UserService.java"),
            "public class UserService {}"
        )
        
        assert file_type == "service"
    
    def test_extract_code_structure_java(self):
        """Test Java code structure extraction."""
        extractor = CodeExtractor()
        
        java_content = """
package com.example;

import java.util.List;
import com.example.model.User;

public class UserService {
    
    public User findById(Long id) {
        return null;
    }
    
    private void validate(User user) {
        // validation
    }
}
"""
        classes, methods, imports = extractor._extract_code_structure(java_content, "java")
        
        assert "UserService" in classes
        assert "findById" in methods
        assert "java.util.List" in imports
    
    def test_get_collection_name(self):
        """Test collection name generation."""
        manager = QdrantManager()
        
        name = manager.get_collection_name("le01")
        assert "prd_agent" in name
        assert "le01" in name
    
    def test_get_collection_name_sanitization(self):
        """Test collection name sanitization."""
        manager = QdrantManager()
        
        name = manager.get_collection_name("LE-01 Form")
        assert " " not in name
        assert "-" not in name


class TestAgentContext:
    """Tests for AgentContext."""
    
    def test_context_creation(self):
        """Test agent context creation."""
        context = AgentContext(
            form_name="le01",
            form_title="LE01 Form",
            description="Test form",
        )
        
        assert context.form_name == "le01"
        assert context.form_title == "LE01 Form"
        assert context.additional_context == {}
    
    def test_context_with_additional(self):
        """Test context with additional data."""
        context = AgentContext(
            form_name="le01",
            additional_context={"project": "test"}
        )
        
        assert context.additional_context["project"] == "test"


@pytest.mark.asyncio
async def test_mock_screenshot_analysis():
    """Test screenshot analysis with mocked dependencies."""
    from src.agents.screenshot_analysis_agent import ScreenshotAnalysisAgent
    
    agent = ScreenshotAnalysisAgent()
    context = AgentContext(form_name="test_form")
    
    # Test with empty screenshots
    result = await agent.analyze(context, screenshots=[])
    
    assert not result.success
    assert "No screenshots found" in (result.error or "")


@pytest.mark.asyncio  
async def test_mock_requirements_generation():
    """Test requirements generation with mocked LLM."""
    from src.agents.requirements_generator_agent import RequirementsGeneratorAgent
    
    with patch.object(RequirementsGeneratorAgent, 'invoke_llm') as mock_llm:
        mock_llm.return_value = """[
            {
                "req_id": "FR-001",
                "title": "User Login",
                "description": "Users can log in",
                "priority": "P0",
                "category": "CRUD",
                "user_story": "As a user, I want to log in",
                "acceptance_criteria": ["Given valid credentials"],
                "dependencies": [],
                "source_references": []
            }
        ]"""
        
        agent = RequirementsGeneratorAgent()
        context = AgentContext(form_name="test_form")
        
        result = await agent.analyze(context)
        
        assert result.success
        assert result.data is not None
        assert len(result.data.functional_requirements) > 0

