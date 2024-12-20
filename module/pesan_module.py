from model import db, Pesan

def create_pesan(data):
    pesan = Pesan(
        pesan=data['pesan'])

    db.session.add(pesan)
    db.session.commit()

    # Menyusun pesan sapaan
    greeting = f"Berhasil Membuat feedback pada, {pesan.tanggal}!"

    # Mengembalikan data user beserta sapaan
    return {'message': greeting}, 200

def get_pesans():
    pesan_list = Pesan.query.all()

    # Membuat list untuk menyimpan hasil yang akan ditampilkan
    result = []

    # Mengiterasi setiap entri mahasiswa dan menyusun dictionary untuk setiap entri
    for pesan in pesan_list:
        result.append({
            'pesan_id': pesan.pesan_id,
            'pesan': pesan.pesan,
            'tanggal': pesan.tanggal
        })
    
    return result
    
def delete_pesan(pesan_id):
    pesan = Pesan.query.get(pesan_id)

    if not pesan:
        return {"error": "Feedback tidak ditemukan."}, 404

    db.session.delete(pesan)
    db.session.commit()
    return {"success": "Feedback berhasil dihapus."}, 200
