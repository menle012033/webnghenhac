document.addEventListener("DOMContentLoaded", function() {
    // Hàm để lấy dữ liệu từ cơ sở dữ liệu (giả sử dùng fetch API)
    function fetchData() {
        // Giả sử URL này trả về dữ liệu JSON chứa các tùy chọn
        const url = 'https://api.example.com/options';

        fetch(url)
            .then(response => response.json())
            .then(data => {
                populateSelect(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    // Hàm để thêm các tùy chọn vào select
    function populateSelect(options) {
        const selectElement = document.getElementById('styledSelect1');
        
        // Xóa các tùy chọn cũ nếu cần thiết
        // selectElement.innerHTML = '<option value="">-----------------------------------</option>';

        options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.label;
            selectElement.appendChild(optionElement);
        });
    }

    // Gọi hàm fetchData để lấy và thêm dữ liệu vào select khi trang tải xong
    fetchData();
});