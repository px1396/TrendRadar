from fastmcp import FastMCP
import httpx

# 初始化
mcp = FastMCP("TrendRadar-Cloud")

# 请替换为你自己服务器上 TrendRadar 的 API 地址
# 比如通过 ngrok 或 cloudflare tunnel 穿透出来的地址
API_URL = "http://你的服务器IP或域名/api"

@mcp.tool()
async def search_trends(keyword: str) -> str:
    """搜索热点新闻"""
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{API_URL}/search", params={"q": keyword}, timeout=30.0)
            return resp.text
        except Exception as e:
            return f"连接 TrendRadar 失败: {str(e)}"