from flask import Flask, render_template_string

app = Flask(__name__)

fanpages = [
    {"id": "100059340352233", "name": "Đẹp xinh"},
    {"id": "100066548179469", "name": "Nước Hoa Cao Cấp GilLe"},
    {"id": "100077441823700", "name": "Nguyễn Phương Anh"},
    {"id": "100084817671700", "name": "Sac Dep Viet"},
    {"id": "100085392258304", "name": "Bọn Không Răng"},
    {"id": "100087942131197", "name": "Người đương thời"},
    {"id": "100088563311931", "name": "Trạm Cảm Xúc"},
    {"id": "100094076577678", "name": "Nguyễn Ngọc Thảo"},
    {"id": "100094297484436", "name": "Trần Thị Lan"},
    {"id": "100094469225127", "name": "Phan Hồng"},
    {"id": "61550890906005", "name": "Đã Xa Nhau"},
    {"id": "61553564804201", "name": "Trương Hoàng Anh"},
    {"id": "61553770886341", "name": "Huyền Phan"},
    {"id": "61553941071991", "name": "Nhi Võ"},
    {"id": "61554007627595", "name": "Trần Dạ Thảo"},
    {"id": "61554174875386", "name": "Nga Trần"},
    {"id": "61554859539309", "name": "KÝ ỨC 8X9X"},
    {"id": "61558373218659", "name": "Trần Nhã Uyên"},
    {"id": "61568267111556", "name": "Bé mỡ Cà Mau"},
    {"id": "61569623338958", "name": "Phan Minh Phú"},
    {"id": "61573557481207", "name": "Trang Ốc Quế"},
    {"id": "61575152075404", "name": "Lê Thị Hằng"},
    {"id": "61575792195433", "name": "Hoàng Thị Lam"},
    {"id": "61576359155093", "name": "Radio 8"},
    {"id": "61581184464439", "name": "Hoàng Thị Mận"},
    {"id": "61583431812887", "name": "Trạm Sạc Động Lực"},
    {"id": "61584234714381", "name": "Nghỉ Việc Đổi Tên"},
    {"id": "61584681522002", "name": "Vầng Trăng Xưa"},
    {"id": "61584935280426", "name": "Trạm Năng Lương"},
    {"id": "61586861499998", "name": "Góc Truyện"},
    {"id": "61587037382008", "name": "Truyện Hay Mỗi Tối"},
    {"id": "61587206873407", "name": "Truyện Đêm Khuya"},
    {"id": "61587229648023", "name": "Chuyện Nhỏ Chuyện To"},
    {"id": "duongbaho2021", "name": "Đường Bá Hổ"},
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Fanpage Tool</title>
    <style>
        body { font-family: Arial; background: #f5f6fa; }
        h1 { text-align: center; }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 80%;
            background: white;
        }
        th, td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        th { background: #4CAF50; color: white; }
        tr:hover { background: #f1f1f1; cursor: pointer; }
    </style>

    <script>
        function openPage(id) {
            // mở facebook tab mới
            window.open("https://facebook.com/" + id, "_blank");

            // gọi API xóa
            fetch("/delete/" + id)
                .then(() => {
                    // reload lại trang
                    window.location.reload();
                });
        }
    </script>
</head>
<body>

<h1>📊 Fanpage Tool</h1>

<table>
<tr>
    <th>#</th>
    <th>Name</th>
    <th>ID</th>
</tr>

{% for page in fanpages %}
<tr onclick="openPage('{{ page.id }}')">
    <td>{{ loop.index }}</td>
    <td>{{ page.name }}</td>
    <td>{{ page.id }}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, fanpages=fanpages)

@app.route("/delete/<page_id>")
def delete(page_id):
    global fanpages
    fanpages = [p for p in fanpages if p["id"] != page_id]
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)