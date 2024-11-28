Swal.fire({
    text: "...เราทั้งสองคนรู้สึกเป็นเกียรติและดีใจอย่างยิ่ง ที่ทุกท่านมาแสดงความยินดีและมอบคำอวยพรให้เราทั้งสอง เราขอให้ทุกท่านประสบแต่ความสุขและความสำเร็จในทุก ๆ ด้านเช่นกัน...",
    imageUrl: '/static/assets/img/logo_wedding1.png', 
    imageWidth: 400,
    width: 800,
    confirmButtonColor: '#ffffff',
    confirmButtonText: '❤️',
    customClass: {
        confirmButton: 'heart-button',
        popup: 'custom-margin'
    },
    showClass: {
        popup: `
          animate__animated
          animate__fadeInUp
          animate__faster
        `
    },
    hideClass: {
        popup: `
          animate__animated
          animate__fadeOutDown
          animate__faster
        `
    },
    didOpen: () => {
        const textElement = Swal.getHtmlContainer(); // ดึงองค์ประกอบของข้อความ
        if (textElement) {
            textElement.style.color = '#ff8a8a'; // ตั้งค่าสีเป็นสีชมพู
        }
    }
});
