from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    _nama = db.Column(db.String(100), nullable=False, unique=True)
    _alamat = db.Column(db.String(150), nullable=False)

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        self._nama = value.upper()

    @property
    def alamat(self):
        return self._alamat

    @alamat.setter
    def alamat(self, value):
        self._alamat = value.upper()

    def to_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'alamat': self.alamat,
        }

class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    _judul = db.Column(db.String(100), nullable=False, unique=True)
    _genre = db.Column(db.String(50), nullable=False)
    _tahun = db.Column(db.String(4), nullable=False)

    @property
    def judul(self):
        return self._judul

    @judul.setter
    def judul(self, value):
        self._judul = value.upper()

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value.upper()

    @property
    def tahun(self):
        return self._tahun

    @tahun.setter
    def tahun(self, value):
        self._tahun = value.upper()

    def to_dict(self):
        return {
            'id': self.id,
            'judul': self.judul,
            'genre': self.genre,
            'tahun': self.tahun,
        }

class Pesan(db.Model):
    __tablename__ = 'pesan'
    pesan_id = db.Column(db.Integer, primary_key=True)
    _pesan = db.Column(db.String(300), nullable=False)
    tanggal = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def pesan(self):
        return self._pesan

    @pesan.setter
    def pesan(self, value):
        self._pesan = value.upper()

    def to_dict(self):
        return {
            'pesan_id': self.pesan_id,
            'pesan': self.pesan,
            'tanggal': self.tanggal.strftime('%Y-%m-%d %H:%M:%S'),
        }

class Bangun(db.Model):
    __tablename__ = 'bangun'
    bangun_id = db.Column(db.Integer, primary_key=True)
    _nama_bangun = db.Column(db.String(100), nullable=True)
    panjang = db.Column(db.Float, nullable=True)
    lebar = db.Column(db.Float, nullable=True)
    luas = db.Column(db.Float, nullable=True)

    @property
    def nama_bangun(self):
        return self._nama_bangun

    @nama_bangun.setter
    def nama_bangun(self, value):
        self._nama_bangun = value.upper()

    def to_dict(self):
        return {
            'bangun_id': self.bangun_id,
            'nama_bangun': self.nama_bangun,
            'panjang': self.panjang,
            'lebar': self.lebar,
            'luas': self.luas,
        }