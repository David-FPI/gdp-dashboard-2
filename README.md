# 🏠 California Housing Data Analytics Tool

Phân tích dữ liệu nhà ở bang California dựa trên bộ dữ liệu từ năm 1990, giúp trực quan hóa và rút ra các xu hướng về giá trị nhà, thu nhập, tuổi nhà và khoảng cách tới các thành phố lớn. Dữ liệu được tải từ file **California_Houses.csv**.

---

## 📚 Data Collection

Bộ dữ liệu gốc được sử dụng trong bài báo:  
Pace, R. Kelley, and Ronald Barry. *"Sparse spatial autoregressions."* Statistics & Probability Letters 33.3 (1997): 291-297.

- Bộ dữ liệu này là tài nguyên tuyệt vời để nhập môn học máy (Machine Learning) vì có độ lớn vừa phải, dễ hiểu và cần xử lý dữ liệu cơ bản.
- Dữ liệu dựa trên thống kê dân số California năm 1990 (không phải dữ liệu nhà ở hiện tại như Zillow Zestimate).
- Mỗi dòng dữ liệu tương ứng với một khu dân cư ở California.

### 📄 Các cột trong dữ liệu:

| Cột                    | Mô tả                                            |
| ---------------------- | ------------------------------------------------ |
| Median_House_Value     | Giá trị trung vị của nhà (USD)                   |
| Median_Income          | Thu nhập trung vị trong khu vực (10,000 USD)     |
| Median_Age             | Tuổi trung bình của nhà (năm)                    |
| Tot_Rooms              | Tổng số phòng                                    |
| Tot_Bedrooms           | Tổng số phòng ngủ                                |
| Population             | Tổng dân số trong khu vực                        |
| Households             | Tổng số hộ gia đình                              |
| Latitude               | Vĩ độ                                            |
| Longitude              | Kinh độ                                          |
| Distance_to_coast      | Khoảng cách tới bờ biển (mét)                    |
| Distance_to_LA         | Khoảng cách tới Los Angeles (mét)                |
| Distance_to_SanDiego   | Khoảng cách tới San Diego (mét)                  |
| Distance_to_SanJose    | Khoảng cách tới San Jose (mét)                   |
| Distance_to_SanFrancisco| Khoảng cách tới San Francisco (mét)             |

### 📊 Dữ liệu gồm:  
- 20,640 dòng và 14 cột.
- Không có giá trị null ✅
- Không có dòng trùng lặp ✅

---

## 🔍 Data Processing

1. **Xử lý giá trị null**: Không phát hiện null trong dataset.
2. **Xử lý dòng trùng lặp**: Không phát hiện dòng trùng lặp.

---

## 📈 Data Visualization

### 1. **Biểu đồ phân phối Giá trị Nhà trung vị**
- Giá trị nhà tập trung chủ yếu trong khoảng **50,000 - 200,000 USD**.
- Giá trị trung bình: **206,855 USD**  
- Giá trị trung vị: **179,700 USD**  
- Độ lệch chuẩn: **115,395 USD**  
- Dữ liệu nghiêng phải (có một số nhà giá trị rất cao > 500,000 USD).

### 2. **Biểu đồ Giá trị nhà theo Tuổi nhà**
- Đồ thị đường thể hiện mối quan hệ giữa **tuổi nhà** và **giá trị trung vị**.
- Khu vực có nhà mới (tuổi thấp) thường có giá trị cao hơn.
- Xác nhận: tuổi nhà ảnh hưởng lớn đến giá trị thị trường.

### 3. **Biểu đồ Tròn: Giá trị nhà theo khoảng cách đến thành phố**
- So sánh giá trị nhà trung vị gần:
  - **Coast**
  - **Los Angeles**
  - **San Diego**
  - **San Jose**
  - **San Francisco**
- Kết luận: các vùng gần các trung tâm đô thị lớn có giá trị cao hơn rõ rệt.

### 4. **Biểu đồ Bong bóng: Thu nhập vs Giá trị nhà (Kích thước: Dân số)**
- **Trục X**: Median Income
- **Trục Y**: Median House Value
- **Bong bóng**: Dân số khu vực
- Quan sát:
  - Có xu hướng **tương quan dương**: thu nhập cao → giá nhà cao.
  - Vùng có dân số lớn nhưng giá nhà chưa cao là tiềm năng phát triển.

### 5. **Bản đồ tương tác: Giá trị nhà theo khoảng cách**
- Sử dụng layer bản đồ:
  - **Hexagon Layer** (màu sắc)
  - **Scatterplot Layer** (kích thước)
- Giúp nhận diện vùng nào có giá trị nhà cao và xa/gần các thành phố lớn.
- Công cụ mạnh cho nhà đầu tư bất động sản và phân tích quy hoạch.

---

## 🚀 Kết luận

Công cụ **California Housing Data Analytics Tool** giúp:
- Hiểu rõ xu hướng bất động sản tại California (dựa trên dữ liệu năm 1990).
- Phân tích ảnh hưởng của **thu nhập**, **tuổi nhà** và **vị trí địa lý** tới giá trị nhà.
- Hỗ trợ các quyết định đầu tư và quy hoạch thị trường nhà đất.

---

## 📦 Yêu cầu cài đặt

```bash
pip install pandas matplotlib seaborn altair pydeck
