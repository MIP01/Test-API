from model import db, User
from sqlalchemy.exc import IntegrityError

def create_user(data):
    try:
        user = User(
            nama=data['nama'],
            alamat=data['alamat'])

        db.session.add(user)
        db.session.commit()

        # Menyusun pesan sapaan
        greeting = f"Selamat datang, {user._nama}!"

        # Mengembalikan data user beserta sapaan
        return {'message': greeting}, 200

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {'error': 'User sudah ada.'}, 409

def get_users():
    user_list = User.query.all()

    # Membuat list untuk menyimpan hasil yang akan ditampilkan
    result = []

    # Mengiterasi setiap entri mahasiswa dan menyusun dictionary untuk setiap entri
    for user in user_list:
        result.append({
            'user_id': user.user_id,
            'nama': user.nama,
            'alamat': user.alamat
        })
    
    return result
    
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    db.session.delete(user)
    db.session.commit()
    return {"success": "User berhasil dihapus."}, 200
