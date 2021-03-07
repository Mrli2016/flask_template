from app import init_app  # 从project文件夹中的__init__.py中导入create_app函数

# 记住这里的变量名app
app = init_app()

if __name__ == '__main__':
    app.run(debug=True)
