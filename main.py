from flask import Flask
from flask_restful import Api, Resource, reqparse , abort , fields, marshal_with
from flask_sqlalchemy import SQLAlchemy, Model

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Modelodel):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

def __repr__(self):
    return f"Video(name = {name}, views = {views},likes = {likes})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help = "Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help= "Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help= "Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help = "Name of the video is required")
video_update_args.add_argument("views", type=int, help= "Views of the video")
video_update_args.add_argument("likes", type=int, help= "Likes on the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(404, message="Could not find video with that id")
        return result 
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first
        if result:
            abort(409, message="Video id taken...")
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_put_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
        abort(404,message="Video doesn't exist, cannot update")

    if "name" in args:
        result.name = args['name']
    if "views" in args:
        result.views = args['views']
    if "likes" in args:
        result.likes = args['likes']
    
    db.session.commit()
    return result

def delete(self, video_id):
    abort_if_video_id_doesnt_exist(video_id)
    del videos[video_id]
    return '',204
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)