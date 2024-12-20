from model import db, Film
from sqlalchemy.exc import IntegrityError

def create_film(data):
    try:
        film = Film(
            judul=data['judul'],
            genre=data['genre'],
            tahun=data['tahun'])

        db.session.add(film)
        db.session.commit()

        return film.to_dict(), 200

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {'error': 'Film sudah ada.'}, 409

def get_films():
    film_list = Film.query.all()

    # Membuat list untuk menyimpan hasil yang akan ditampilkan
    result = []

    # Mengiterasi setiap entri mahasiswa dan menyusun dictionary untuk setiap entri
    for film in film_list:
        result.append({
            'id': film.id,
            'judul': film.judul,
            'genre': film.genre,
            'tahun': film.tahun,
        })
    
    return result

def get_film_by_genre(genre):
    film = Film.query.filter_by(_genre=genre.upper()).all()

    # Tangani kasus jika data film tidak ditemukan
    if not film:
        return {'error': 'Genre not found'}, 404
    
    # Membuat salinan data mahasiswa
    result = [
        {
            'id': film.id,
            "judul": film.judul,
            "genre": film.genre,
            "tahun" :film.tahun,
        }
        for film in film
    ]
    return result

def delete_film(id):
    film = Film.query.get(id)

    if not film:
        return {"error": "Film tidak ditemukan."}, 404

    db.session.delete(film)
    db.session.commit()
    return {"success": "Film berhasil dihapus."}, 200
