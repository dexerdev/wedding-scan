function register_reward() {
    var name = document.getElementById('name').value;
    var phone = document.getElementById('phone').value;
    var table_no = document.getElementById('table-id').value;
    var url = '/api/register_reward'
    var json = JSON.stringify({
        "name": name,
        "phone": phone,
        "table_no": table_no
    });
    fetch(url, {
        method: "POST",
        body: json,
        headers: {
            "Content-type": "application/json; charset=utf-8"
        }
    }).then(response => response.json()).then((data) => {
        if (data.success) {
            Swal.fire({
                title: data.message,
                text: "กรุณา Capture QRCode ไว้แลกหน้างาน",
                icon: "success",
                showconfirmbutton: true,
                html: `<img src="${data.data.qr_code_path.replace("app/", "/")}" alt="QR Code" style="width: 300px; height: 300px;"> <br> <span style="color: red;">กรุณา Capture QRCode ไว้แลกหน้างาน</span>`,
            }).then(function () {
                // window.location.href = "/thank";
            });
        }
        else {
            Swal.fire({
                title: data.message,
                icon: "error",
                showconfirmbutton: true,
            });
        }
    })
}