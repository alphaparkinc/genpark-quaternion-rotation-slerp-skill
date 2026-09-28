import sys
import json
import math
from client import Quaternion

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-quaternion-rotation-slerp-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "rotate_vector",
                    "description": "Rotate 3D vector using axis-angle quaternion representation",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "vector": {"type": "array", "items": {"type": "number"}},
                            "axis": {"type": "array", "items": {"type": "number"}},
                            "angle_rad": {"type": "number"}
                        },
                        "required": ["vector", "axis", "angle_rad"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "rotate_vector":
            v = args.get("vector")
            axis = args.get("axis")
            ang = args.get("angle_rad", 0.0)
            q = Quaternion.from_axis_angle(axis, ang)
            v_rot = q.rotate_vector(v)
            res = {"content": [{"type": "text", "text": json.dumps({"rotated_vector": v_rot})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
