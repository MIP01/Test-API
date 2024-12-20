from model import db, Bangun

def create_bangun(data):
    try:
        # Ambil data input
        panjang = data.get('panjang')
        lebar = data.get('lebar')
        nama_bangun = data.get('nama_bangun')

        # Validasi input
        if not panjang or not lebar or not nama_bangun:
            return {"error": "Semua field wajib diisi."}, 400

        # Validasi tipe data untuk panjang dan lebar
        if not isinstance(panjang, (int, float)) or not isinstance(lebar, (int, float)):
            return {"error": "Panjang dan lebar harus berupa angka."}, 400

        # Hitung luas berdasarkan jenis bangun
        if nama_bangun.upper() in ['PERSEGI', 'PERSEGI PANJANG']:
            luas = panjang * lebar
        else:
            return {"error": f"Jenis bangun '{nama_bangun}' tidak didukung untuk perhitungan."}, 400

        # Buat instance Bangun
        bangun = Bangun(
            nama_bangun=nama_bangun, 
            panjang=panjang,
            lebar=lebar,
            luas=luas
        )

        db.session.add(bangun)
        db.session.commit()

        # Kembalikan respons
        return {
            "message": f"Bangun datar '{bangun.nama_bangun}' berhasil dibuat!",
            "data": bangun.to_dict()
        }, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def get_banguns():
    bangun_list = Bangun.query.all()

    # Membuat list untuk menyimpan hasil yang akan ditampilkan
    result = []

    # Mengiterasi setiap entri mahasiswa dan menyusun dictionary untuk setiap entri
    for bangun in bangun_list:
        result.append({
            'bangun_id': bangun.bangun_id,
            'nama_bangun': bangun.nama_bangun,
            'panjang': bangun.panjang,
            'lebar': bangun.lebar,
            'luas': bangun.luas,
        })
    
    return result

def delete_bangun(bangun_id):
    bangun = Bangun.query.get(bangun_id)

    if not bangun:
        return {"error": "Bangun datar tidak ditemukan."}, 404

    db.session.delete(bangun)
    db.session.commit()
    return {"success": "Bangun datar berhasil dihapus."}, 200
