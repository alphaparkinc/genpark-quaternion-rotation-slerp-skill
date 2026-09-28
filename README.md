# genpark-quaternion-rotation-slerp-skill

> Unit quaternion 3D orientation engine with Hamiltonian multiplication, vector rotation, and SLERP interpolation.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[3D Geometry / Camera Ray] --> B[Transform & Matrix Pipeline]
    B --> C[Intersection & Lighting Kernel]
    C --> D[Rendered Vector / Pixel Result]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`).
- **3D Graphics Algorithms**: Ray-sphere intersection, unit quaternion rotation, mesh OBJ triangulation, 4x4 perspective frustum projection, and Bézier de Casteljau curves.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-quaternion-rotation-slerp-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-quaternion-rotation-slerp-skill.git
cd genpark-quaternion-rotation-slerp-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-quaternion-rotation-slerp-skill": {
      "command": "python",
      "args": ["-m", "genpark-quaternion-rotation-slerp-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
