# 咖喱牌Wav转Mp3

## 简介

这是一个简单的桌面应用程序，用于将 WAV 文件转换为 MP3 文件。该程序使用 `ffmpeg` 进行音频转换，并提供一个图形用户界面供用户选择文件和查看转换进度。

## 功能

- 选择 WAV 文件并转换为 MP3 文件
- 显示转换进度
- 使用 `ffmpeg` 进行音频转换
- 图形用户界面友好

## 安装

1. 确保已安装 Python 3.x。
2. 克隆或下载此项目到本地。
3. 在项目目录下创建并激活虚拟环境：

    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

4. 安装所需依赖：

    ```bash
    pip install -r requirements.txt
    ```

5. 下载 `ffmpeg.exe` 文件并放置在项目目录中：

    [下载链接](https://example.com/path/to/ffmpeg.exe)

6. 确保 [icon.ico](http://_vscodecontentref_/3) 文件位于项目目录中。

## 使用

1. 运行程序：

    ```bash
    python app.py
    ```

2. 在图形界面中点击“选择WAV文件”按钮，选择要转换的 WAV 文件。
3. 程序将开始转换，并显示进度条。
4. 转换完成后，将弹出提示框显示转换结果。

## 打包

1. 安装 PyInstaller：

    ```bash
    pip install pyinstaller
    ```

2. 使用以下命令打包程序：

    ```bash
    pyinstaller wav-mp3.spec
    ```

3. 打包后的可执行文件将在 [dist](http://_vscodecontentref_/4) 目录中生成。

## 注意事项

- 确保 `ffmpeg.exe` 文件在系统路径中，或者与 [app.py](http://_vscodecontentref_/5) 文件在同一目录中。
- 打包时请确保 [icon.ico](http://_vscodecontentref_/6) 文件和 `ffmpeg.exe` 文件在项目目录中。

## 许可证

MIT License