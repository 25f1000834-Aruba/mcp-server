import hashlib
from fastmcp import FastMCP

mcp = FastMCP("TDS Exam MCP Server")
NORMALIZED_EMAIL = "25f1000834@ds.study.iitm.ac.in"

@mcp.tool(name="solve_challenge")
def solve_challenge() -> str:
    challenge = ""
    raw_str = f"{challenge}:{NORMALIZED_EMAIL}"
    full_hash = hashlib.sha256(raw_str.encode("utf-8")).hexdigest()
    return full_hash[:16]

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=7860)
