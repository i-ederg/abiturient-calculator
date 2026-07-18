from django.shortcuts import render
import csv

def index(request):
    rows = []
    error = 0
    code = ""
    c1, c2, c3 = 1, 1, 1
    if request.method == "POST":
        code=request.POST.get("code")

        if not code:
            error = 1
            return render(request, "main/index.html", {"error": error})

        file=request.FILES.get("file")

        if not file:
            error = 2
            return render(request, "main/index.html", {"error": error})

        if not(file.name.endswith(".csv")):
            error=3
            return render(request, "main/index.html", {"error":error})


        if file:
            csv_file=file.read().decode("utf-8-sig").splitlines()
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                rows.append(row)
            for l in rows[1:]:
                error=5
                if l[7] == code:
                    break
                c1 += 1
                if l[1]=="1":
                    c2 += 1
                    if l[2]!="—":
                        c3 += 1
            if c1 == len(rows):
                error=4
                return render(request, "main/index.html", {"error": error})
    return render(request,'main/index.html', {'code':code,'c1': c1, 'c2': c2, 'c3': c3, 'error': error})

