from websockets import serve
import asyncio

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        connected_clients.remove(websocket)

async def main():
    async with serve(handler, "0.0.0.0", 8765, ping_interval=None):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())