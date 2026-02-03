"""
UI Migration Agent.

Specialized agent for frontend migration from legacy Java Swing to React.
Analyzes screenshots and generates React components.
"""

from pathlib import Path

from src.core.agentic.agentic_base import AgenticAgent, AgenticConfig
from src.core.agentic.tool_registry import ToolParameter
from src.tools import code_tools, file_tools, minio_tools
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


UI_SYSTEM_PROMPT = """You are a UI migration specialist.
Your job is to migrate legacy Java Swing interfaces to modern React applications.

## Your Task
1. Analyze UI screenshots to understand the layout and components
2. Identify form fields, buttons, tables, and other UI elements
3. Generate React TypeScript components matching the legacy UI
4. Create type definitions for all data structures
5. Implement form validation matching legacy rules

## React Component Rules
1. Use functional components with hooks
2. Use TypeScript with proper typing
3. Use CSS modules or styled-components for styling
4. Implement proper form handling with controlled components
5. Add proper accessibility attributes
6. Handle loading and error states

## Example Component
```tsx
import React, { useState, useEffect } from 'react';
import { VehicleService } from '../services/vehicleService';
import { Vehicle } from '../types/Vehicle';
import styles from './VehicleList.module.css';

interface VehicleListProps {
  onVehicleSelect?: (vehicle: Vehicle) => void;
}

export const VehicleList: React.FC<VehicleListProps> = ({ onVehicleSelect }) => {
  const [vehicles, setVehicles] = useState<Vehicle[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadVehicles();
  }, []);

  const loadVehicles = async () => {
    try {
      const data = await VehicleService.getAll();
      setVehicles(data);
    } catch (err) {
      setError('Failed to load vehicles');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div className={styles.error}>{error}</div>;

  return (
    <div className={styles.container}>
      <table>
        <thead>
          <tr>
            <th>Vehicle Number</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {vehicles.map(v => (
            <tr key={v.vehicleId} onClick={() => onVehicleSelect?.(v)}>
              <td>{v.vehicleNumber}</td>
              <td>{v.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
```

Match the legacy UI as closely as possible while using modern React patterns.
"""


class UIMigrationAgent(AgenticAgent):
    """
    Specialized agent for UI migration tasks.

    Generates React components from legacy Java Swing UI
    based on screenshot analysis.
    """

    def __init__(
        self,
        form_name: str,
        output_dir: Path,
        config: AgenticConfig | None = None,
    ) -> None:
        """
        Initialize the UI migration agent.

        Args:
            form_name: Name of the form
            output_dir: Output directory for generated components
            config: Optional agent configuration
        """
        self.form_name = form_name
        self.output_dir = Path(output_dir)

        if config is None:
            config = AgenticConfig()
        config.working_directory = self.output_dir

        super().__init__(
            name="UIMigrationAgent",
            system_prompt=UI_SYSTEM_PROMPT,
            config=config,
        )

    def _register_default_tools(self) -> None:
        """Register UI-specific tools."""
        # Screenshot tools
        self.tool_registry.register(
            name="list_screenshots",
            description="List available UI screenshots.",
            parameters=[],
            function=lambda **kwargs: minio_tools.list_screenshots(self.form_name),
        )

        self.tool_registry.register(
            name="get_form_docs",
            description="Get form documentation including field descriptions.",
            parameters=[],
            function=lambda **kwargs: minio_tools.get_form_docs(self.form_name),
        )

        self.tool_registry.register(
            name="search_codebase",
            description="Search for UI-related code and validation rules.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Search query",
                    required=True,
                ),
            ],
            function=lambda **kwargs: code_tools.search_codebase(
                self.form_name,
                kwargs["query"],
            ),
        )

        self.tool_registry.register(
            name="get_code_context",
            description="Get code context for UI patterns.",
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Topic to get context for",
                    required=True,
                ),
            ],
            function=lambda **kwargs: code_tools.get_code_context(
                self.form_name,
                kwargs["query"],
            ),
        )

        # File tools
        self.tool_registry.register(
            name="write_file",
            description="Write generated component to a file.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="File path to write",
                    required=True,
                ),
                ToolParameter(
                    name="content",
                    type="string",
                    description="File content",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.write_file(
                str(self.output_dir),
                kwargs["filepath"],
                kwargs["content"],
            ),
        )

        self.tool_registry.register(
            name="get_files_info",
            description="List files in a directory.",
            parameters=[
                ToolParameter(
                    name="directory",
                    type="string",
                    description="Directory to list",
                    required=False,
                ),
            ],
            function=lambda **kwargs: file_tools.get_files_info(
                str(self.output_dir),
                kwargs.get("directory", "."),
            ),
        )

        self.tool_registry.register(
            name="get_file_content",
            description="Read a file's content.",
            parameters=[
                ToolParameter(
                    name="filepath",
                    type="string",
                    description="Path to file",
                    required=True,
                ),
            ],
            function=lambda **kwargs: file_tools.get_file_content(
                str(self.output_dir),
                kwargs["filepath"],
            ),
        )

    async def generate_components(self) -> str:
        """
        Generate React components from screenshots.

        Returns:
            Summary of generated components
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

        prompt = f"""
Generate React TypeScript components for form '{self.form_name}'.

Steps:
1. List available screenshots
2. Get form documentation to understand field requirements
3. Search for validation rules in the legacy code
4. Generate React components in frontend/components/
5. Create type definitions in frontend/types/
6. Create API service layer in frontend/services/

Make sure to:
- Match the legacy UI layout
- Implement all validation rules
- Use proper TypeScript types
- Include CSS styling
"""

        return await self.send_message(prompt)
