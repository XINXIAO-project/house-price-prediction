Start-Process powershell -ArgumentList "D:\Anaconda\python.exe -m uvicorn src.api:app --reload"
Start-Sleep -Seconds 3
Start-Process powershell -ArgumentList "D:\Anaconda\python.exe -m streamlit run app.py"