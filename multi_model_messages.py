import base64
import mimetypes
from pathlib import Path
from tkinter import TclError,Tk,filedialog
from langchain.messages import HumanMessage,AIMessage
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def choose_image_file() -> Path:
    """open a local file picker when no image is passed on the command lines"""
    root=None
    try:
        root=Tk()
        root.withdraw()
        root.attributes("-topmost",True)
        filename=filedialog.askopenfilename(
            title="Choose an image",
            filetypes=[
                ("images","*.png *.jpg *.jpeg *.webp"),
                ("All files","*.*"),
            ],
        )
    except TclError as e:
        print(f"Could not open the file picker: {e}")
        filename = input("Image path: ").strip().strip('"').strip("'")
    finally:
        if root is not None:
            root.destroy()
    if not filename:
        raise SystemExit("no image selected.")

    return Path(filename).expanduser()  # expanduser() expands a home-directory shortcut such as ~ if one is present.


def image_to_data_url(image_path:Path) -> str:
    image_path=image_path.expanduser().resolve()

    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found :{image_path}")

    mime_type,_=mimetypes.guess_type(str(image_path))
    if not mime_type or not mime_type.startswith("image/"):
        raise ValueError(f"not am image file: {image_path}")

    image_b64=base64.b64encode(image_path.read_bytes()).decode("utf-8")
    
    return f"data:{mime_type};base64,{image_b64}"


def build_image_message(image_path:Path)->HumanMessage:
    return HumanMessage(
        content=[
            {"type":"text","text":"tell me what is image about"},
            {"type":"image_url","image_url":{"url":image_to_data_url(image_path)}},
        ]
    )


agent=create_agent(model="groq:qwen/qwen3.8-27b")
image_path=choose_image_file()
message=build_image_message(image_path)

response=agent.invoke(
    {
        "messages":message
    }

)


print(response["messages"][-1].content)


